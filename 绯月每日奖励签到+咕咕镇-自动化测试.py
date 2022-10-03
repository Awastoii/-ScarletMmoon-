from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def mian():
    web = Edge()
    web.get("https://9shenmi.com/register.php")
    time.sleep(1)

    username = input('请输入您的账号')
    password = input('请输入您的密码')

    web.find_element(By.NAME, "pwuser").send_keys(username)
    web.find_element(By.NAME, "pwpwd").send_keys(password, Keys.ENTER)

    time.sleep(2)
    try:
        web.find_element(By.XPATH, '//*[@id="pdUserName"]').click()
        work1 = web.find_element(By.ID, 'pdUserName')
        ActionChains(web).move_to_element(work1).perform()  # perform执行
        web.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[2]/ul/li[4]/a').click()
        time.sleep(1)
        web.find_element(By.XPATH, '//*[@id="alldiv"]/div[3]/div[2]/div[1]/div[3]/table/tbody/tr/td/div[6]/a').click()
    except:
        print("今天已经领取过奖励了")

    time.sleep(3)
    web.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/ul/li[1]/a').click()
    web.find_element(By.XPATH, '/html/body/div[2]/div[3]/table[1]/tbody/tr/td[1]/a').click()

    time.sleep(3)

    web.switch_to.window(web.window_handles[-1])
    web.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/button[4]').click()
    time.sleep(2)
    try:
        web.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/button[2]').click()
        time.sleep(0.5)
        web.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/button').click()
    except:
        print("今天已经领取过了")
    # web.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/button[3]').click()  #暂定，此段代码和下一段代码为进入海滩收获页面并清空今日装备
    # web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/button').click()
    time.sleep(1)
    web.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/button').click()
    time.sleep(1)

    num = 0
    num2 = 0

    try:
        while num != 10:
            web.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div/div[2]/button[2]').click()
            time.sleep(1)
            num += 1
    except:
        print("今日体力不足")

    try:
        while num2 != 5:
            web.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/div/div/div/div[2]/button[1]').click()
            time.sleep(0.5)
            web.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/button').click()
            time.sleep(0.5)
            num2 += 1
    except:
        print("今日体力不足")

    web.quit()
    print("已完成！")

#def task():
#     while True:
#         task_time = time.strftime("%H:%M:%S")
#         time.sleep(0.7)
#         print("\r当前系统时间为",task_time,end="")
#
#         if task_time == "12:00:00":
#             ScarletMoon_auto()
#             break
#         if task_time == "12:00:01":
#             guguzhen_auto()
#             break

if __name__ == '__main__':
    mian()


