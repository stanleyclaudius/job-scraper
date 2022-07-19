from helper.URLConverter import string_to_url
from bs4 import BeautifulSoup
import requests


def scrap_indeed_website(position, location):
    url = f'https://id.indeed.com/lowongan-kerja?q={string_to_url(position)}&l={string_to_url(location)}'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'lxml')
    jobs = soup.findAll('div', class_='job_seen_beacon')

    if len(jobs) != 0:
        for job in jobs:
            job_container = job.find('table', class_='jobCard_mainContent big6_visualChanges')
            job_detail = job_container.find('div', class_='heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly')
            company_info = job_container.find('div', class_='heading6 company_location tapItem-gutter companyInfo')

            job_link = 'https://id.indeed.com' + job_container.h2.a['href']
            job_title = job_container.h2.a.span.text
            company_name = company_info.span.text
            company_location = company_info.div.text

            try:
                job_salary = job_detail.find('div', class_='salary-snippet-container').div.text
            except:
                job_salary = 'No salary data found'

            try:
                job_type = job_detail.findAll('div', class_='metadata')

                for i in range(len(job_type)):
                    if i == len(job_type) - 1:
                        job_type = job_type[i].div.text
            except:
                job_type = 'No job type data found'

            print(f'Company Name: {company_name}')
            print(f'Company Location: {company_location}')
            print(f'Job Title: {job_title}')
            print(f'Job Detail: {job_link}')
            print(f'Job Salary: {job_salary}')
            print(f'Job Type: {job_type}')
            print()
    else:
        print('Please make sure the position and location keyword is correct.')
