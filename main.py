#웹 사이트 이동
#페이지 수 계산
#각 페이지에 접근
#import urlb

from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_page)