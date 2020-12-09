import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    url = f'https://ca.indeed.com/jobs?q=developer&l=Edmonton,+AB&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_= 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_= 'company').text.strip()
        try:
            salary = item.find('span', class_='salaryText').text.strip().replace('\n,' '')
        except:
            salary = ''
        summary = item.find('div', class_='summary').text.strip()
      
        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return

joblist = [] 

for i in range(0,40,10): 
    print(f'Getting Page, {i}')
    c = extract(0)
    transform(c)
df = pd.DataFrame(joblist)
df.to_csv('jobs.csv')
