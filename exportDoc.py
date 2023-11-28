import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

cService = webdriver.ChromeService(executable_path=r"D:\develop-source\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=cService)


# 获取配置对象 => 什么样的浏览器就选择什么浏览器配置
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# 获取driver对象, 并将配置好的option传入进去
driver = webdriver.Chrome(options=option, service=cService)

def main():
    driver.get("https://note.youdao.com/signIn/index.html")
    time.sleep(3)  # 智能等待30秒
    # print(driver.page_source)
    # 找到输入框，这里需要自行在F12的Elements中找输入框的位置，然后在这里写入
    driver.switch_to.frame(0)
    time.sleep(1)

    print(driver.page_source)

    user_input = driver.find_element(by=By.CLASS_NAME, value='dlemail')
    pw_input = driver.find_element(by=By.CLASS_NAME, value='dlpwd')
    # pw_input = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
    login_btn = driver.find_element(by=By.ID, value='dologin')
    time.sleep(1)

    # 输入用户名和密码，点击登录
    user_input.send_keys('') # 邮箱
    pw_input.send_keys('')  # 密码
    time.sleep(1)
    login_btn.click()
    time.sleep(1)


if __name__ == '__main__':
    main()
