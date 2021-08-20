import requests
from bs4 import BeautifulSoup
import re


def extract(page: int, job_title: str, location: str) -> object:
    """Extract from web page"""
    url = f'https://uk.indeed.com/jobs?q={job_title}&l={location}&start={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup: object) -> list:
    jobs = []
    """Gathers required info from soup"""
    divs = soup.find_all('div', class_='job_seen_beacon')
    for item in divs:

        # sometimes first span is 'new'. This gets span containing title, as class_ is dynamic for title
        titles = item.find_all('span')
        for x in titles:
            if x.text.strip().replace('\n', ' ') != 'new':
                title = x.text.strip().replace('\n', ' ')
                break

        company = item.find(
            'span', class_='companyName').text.strip().replace('\n', ' ')

        job_location = item.find(
            'div', class_='companyLocation').text.strip().replace('/n', ' ')

        # salary not always available
        try:
            salary = item.find(
                'span', class_='salary-snippet').text.strip().replace('\n', ' ')
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
            'div', class_='job-snippet').text.strip().replace('\n', ' ')

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


def get_pages(soup: object) -> int:
    """Find number of pages availble on specific search"""
    try:
        pages = str(soup.find_all('ul', class_='pagination-list')[0])
    except Exception as e:
        print(e)
        print('No jobs matching this description.')
        return False
    if 'aria-label="next"' in pages or 'aria-label="5"' in pages:
        return 50
    elif 'aria-label="4"' in pages:
        return 40
    elif 'aria-label="3"' in pages:
        return 30
    elif 'aria-label="2"' in pages:
        return 20
    return 10


def get_indeed_jobs(job_title: str, location: str) -> list:
    indeed_jobs = []

    """
    USE THIS WHEN IMPLEMENTING MULTIPLE PAGES.

    pages = get_pages(extract(0, job_title, location))

    if pages:
        # loops through each page scraping content
        for i in range(0, pages, 10):
            c = extract(i, job_title, location)
            indeed_jobs += transform(c)
    return indeed_jobs
    """
    c = extract(10, job_title, location)
    indeed_jobs += transform(c)
    return indeed_jobs
