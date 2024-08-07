from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

def get_exd_detail(url, driver):
    data = dict()
    driver.get(url)

    # 電話
    telephome_element = driver.find_element(By.CLASS_NAME, 'info-tel')
    if telephome_element:
        data['telephone'] = telephome_element.text


    # email
    email_element = driver.find_element(By.CLASS_NAME, 'info-mail')
    if email_element:
        data['email'] = telephome_element.text

    #website
    website_elements = driver.find_elements(By.CLASS_NAME, 'boder-icon')
    if website_elements: # 確定有東西
        for website_element in website_elements:
            # 利用 element.get_attribute("屬性名稱") 取得資訊
            href = website_element.get_attribute('href')
            if href:
                for social_media_name in ['facebook','twitter','linkedin','website']:
                    if social_media_name in href:
                        data[social_media_name] = href
                else:
                    data['website'] = href

    # Description
    desc_element = driver.find_element(By.CLASS_NAME, 'ex-foreword')
    if desc_element: # 確定有東西
        data['description'] = desc_element.text
    return data



if __name__ == '__main__':
    text_driver = webdriver.Firefox()
    exd_url = "https://cybersec.ithome.com.tw/2024/exhibition-page/2109"
    exd_data = get_exd_detail(
        url = exd_url,
        driver = text_driver
    )
    print(exd_data)
    text_driver.close()