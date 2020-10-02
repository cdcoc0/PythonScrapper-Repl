import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)

  #모든 html요소 가져오기
  #print(indeed_result.text)

  #html로부터 정보 추출하기(페이지 정보)
  #beautiful soup lib
  #quick start
  #soup = data extractor
  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class" : "pagination"})

  #pagination에서 찾은 요소의 list
  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
  #span태그 안의 문자열만 갖고와
  #pages.append(link.find("span").string)
  #print(page.find("span"))

  #맨 마지막 요소를 제외하고 가져오기
  #pages = pages[:-1]

  #마지막 페이지 가져오기
  max_page = pages[-1]
  
  return max_page


#페이지 수만큼 request 사용
#range: 배열 만들어줌
def extract_indeed_jobs(last_page):
  jobs = []
  #for page in range(last_page):
  result = requests.get(f"{URL}&start={0 * LIMIT}")
  #html에서 데이터 추출(job)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
  for r in results:
    title = r.find("h2", {"class": "title"}).find("a")["title"]
    print(title)
  
  return jobs