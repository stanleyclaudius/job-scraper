from bs4 import BeautifulSoup
import requests


def string_to_url(string):
    string = string.strip().replace(' ', '%20')
    return string


def scrap_indeed_website(position, location):
    url = f'https://id.indeed.com/lowongan-kerja?q={string_to_url(position)}&l={string_to_url(location)}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.findAll('div', class_='job_seen_beacon')

    if len(jobs) != 0:
        for job in jobs:
            job_content = job.find('table', class_='jobCard_mainContent big6_visualChanges')
            job_link = 'https://id.indeed.com' + job_content.h2.a['href']
            job_id = job_content.h2.a['data-jk']
            job_title = job_content.h2.a.span.text
            company_info = job_content.find('div', class_='heading6 company_location tapItem-gutter companyInfo')
            company_name = company_info.span.text
            company_location = company_info.div.text
            job_salary_content = job_content.find('div', class_='heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly')
            try:
                job_salary = job_salary_content.find('div', class_='salary-snippet-container').div.text
            except:
                job_salary = 'No salary data found'

            try:
                job_type = job_salary_content.findAll('div', class_='metadata')

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


if __name__ == '__main__':
    print("Search Job Via Indeed Indonesia")
    position = input('Job Position: ')
    location = input('Location: ')
    scrap_indeed_website(position, location)