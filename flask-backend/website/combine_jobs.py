from .indeed_scraper import get_indeed_jobs
from .reed_scraper import get_reed_jobs


def get_combined_jobs(job_title: str, location: str) -> list:
    indeed_list = get_indeed_jobs(job_title, location)
    reed_list = get_reed_jobs(job_title, location)

    temp_list = []
    combined_list = []

    for job in indeed_list:
        temp_list.append((job['title'], job['company']))

    combined_list += indeed_list

    #duplicates = 0
    for job in reed_list:
        if (job['title'], job['company']) in temp_list:
            #duplicates += 1
            #print('duplicates: ', duplicates)
            continue
        combined_list.append(job)

    #print('indeed: ', len(indeed_list))
    #print('reed: ', len(reed_list))
    #print('combined: ', len(combined_list))
    return combined_list
