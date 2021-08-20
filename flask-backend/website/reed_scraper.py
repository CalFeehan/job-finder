import requests
from bs4 import BeautifulSoup
import re


def extract(job_title: str, location: str) -> object:
    """Extract from web page"""
    url = f'https://www.reed.co.uk/jobs/{job_title}-jobs-in-{location}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup: object) -> list:
    jobs = []
    """Gathers required info from soup"""
    divs = soup.find_all('article', class_='job-result')
    for item in divs:

        title = item.find(
            'h3', class_='title').text.strip().replace('\n', ' ')

        company = item.find(
            'a', class_='gtmJobListingPostedBy').text.strip().replace('\n', ' ')

        job_location = item.find(
            'li', class_='location').text.strip().replace('/n', ' ')
        if '\r' in job_location:
            temp = job_location.split('\r')
            job_location = temp[0]
            del temp

        # salary not always available
        try:
            salary = item.find(
                'li', class_='salary').text.strip().replace('\n', ' ')
            # convert hour to yearly salary, need to add in comma
            if 'hour' in salary:
                match = re.findall("[0-9.]", salary)
                if match:
                    salary = ''
                    for x in match:
                        salary = salary + x
                    salary = float(salary)
                    salary = str(int(salary * 37.5 * 52))
                else:
                    salary = ''
        except:
            salary = ''

        summary = item.find(
            'div', class_='description').text.strip().replace('\n', ' ')
        if '...' in summary:
            temp = summary.split('...')
            summary = temp[0]
            summary += '...'
            del temp

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary,
            'location': job_location
            # add closing date
        }

        jobs.append(job)

    return jobs


def get_reed_jobs(job_title: str, location: str) -> list:
    reed_jobs = []
    c = extract(job_title, location)
    reed_jobs += transform(c)
    return reed_jobs
