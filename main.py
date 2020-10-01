#웹 사이트 이동
#페이지 수 계산
#각 페이지에 접근
#import urlb

import requests

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

#모든 html요소 가져오기
print(indeed_result.text)

#html로부터 정보 추출하기(페이지 정보)
#beautiful soup lib