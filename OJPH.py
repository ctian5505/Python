from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import  By
import pandas as pd
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.onlinejobs.ph/")

#Search Job
work = "data analyst"

#Locate the job search area
job_search_area = driver.find_element(By.XPATH, '//form[@action = "/jobseekers/jobsearch"]')

#type job
search_bar = job_search_area.find_element(By.XPATH, '//input[@name = "jobkeyword"]')
search_bar.send_keys(work)

#Click Search
search_button =  job_search_area.find_element(By.CSS_SELECTOR, '.btn.btn.btn-primary.btn-rounded.text-uppercase.fs-16.fw-700')
search_button.click()




####Scraping Time
job_title = []
employment_type= []
employer = []
posted_date = []
job_salary = []
job_tags = []
job_description = []
job_link = []


job_area = driver.find_elements(By.CSS_SELECTOR, '.jobpost-cat-box.latest-job-post.card-hover-default')

for job in job_area:
    job_title.append(job.find_element(By.CSS_SELECTOR, ".fs-16.fw-700").text.strip())
    employment_type.append(job.find_element(By.CSS_SELECTOR, '.mt-md-0').text.strip())
    employer.append(job.find_element(By.CSS_SELECTOR, '.fs-13.mb-0').text.strip().split("•")[0].strip())
    posted_date.append(job.find_element(By.CSS_SELECTOR, '.fs-13.mb-0').text.strip().split("•")[1].strip())
    job_salary.append(job.find_element(By.XPATH, './/dd[@class="col"]').text.strip())
    job_tag_element = job.find_elements(By.CSS_SELECTOR, '.job-tag a.badge')
    job_tags.append(", ".join([badge.text for badge in job_tag_element]))
    job_description = job.find_element(By.XPATH, './/div[@class="desc fs-14 d-none d-sm-block"]').text.strip()
    element = job.find_element(By.XPATH, '//a[contains(@href, "/jobseekers/job/")]')
    job_link.append(element.get_attribute("href"))



df = pd.DataFrame({"job_title" : job_title,
                   "employment_type" : employment_type,
                   "employer" : employer,
                   "posted_date" : posted_date,
                   "job_salary" : job_salary,
                   "job_tags" : job_tags,
                   "job_description" : job_description,
                   "job_link" : job_link })

df.to_csv("OLPH2.0.csv", index=False)

print("Done")


# the problem is the description is same same
