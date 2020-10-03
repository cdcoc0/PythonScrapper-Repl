import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = pages[-3].get_text(strip=True)
  return int(last_page)


def extract_job(html):
  title = html.find("h2", {"class": "fs-body3"}).find("a")["title"]
  company, location = html.find("h3", {"class": "fs-body1"}).find_all("span", recursive=False)
  #recursive=false: don't go deeper
  #unpack values
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html['data-jobid']
  return {'title': title, 'company': company, 'location': location, 'link': f"https://stackoverflow.com/jobs?id={job_id}&q=python"}



def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping so page {page + 1}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for r in results:
      job = extract_job(r)
      jobs.append(job)
      #print(r["data-jobid"])
  return jobs


def get_jobs():
  last_page = get_last_pages()
  jobs = extract_jobs(last_page)
  return []