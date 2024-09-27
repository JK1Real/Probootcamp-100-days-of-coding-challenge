from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
from time import sleep

#Keep chrome browser open after program finishes

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chromeoptions)
url="https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

driver.get(url)
sleep(30)
data = driver.find_element(By.TAG_NAME, "table")
list_head =data.find_elements(By.TAG_NAME,"th")

heads = [head.text for head in list_head]
head = heads.copy()
print(heads)
print(head)
heads[0]=[]
heads[1]=[]
heads[2]=[]
heads[3]=[]
heads[4]=[]
heads[5]=[]


def run(i):

    url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}"
    driver.get(url)
    sleep(30)
    tbody=driver.find_element(By.TAG_NAME,value="tbody")

    tr_list = tbody.find_elements(By.TAG_NAME,value="tr")
    print(len(tr_list))
    for tr_row in tr_list:
        td_list = tr_row.find_elements(By.TAG_NAME,value="td")
        print(len(td_list))
        heads[0].append(td_list[0].text)
        heads[1].append(td_list[1].text)
        heads[2].append(td_list[2].text)
        heads[3].append(td_list[3].text)
        heads[4].append(td_list[4].text)
        heads[5].append(td_list[5].text)
    print(heads[0])


for i in range(1,33):
    try:
        run(i)
    except:
        pass

data = {
            head[0]: heads[0],
            head[1]: heads[1],
            head[2]: heads[2],
            head[3]: heads[3],
            head[4]: heads[4],
            head[5]: heads[5],
}
d = pd.DataFrame(data)
d.to_csv("college_salary_report.csv",index=False)