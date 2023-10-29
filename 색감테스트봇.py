from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def start_game():
    driver = webdriver.Chrome()
    driver.get('https://humantest.me/service/color')
    driver.implicitly_wait(10)
    start_button = driver.find_element(By.XPATH, '//div[@id="absolute_color_control"]/span')
    start_button.click()
    try:
        while True:
            # 정답 색상 (answer_color(1)을 갖는 요소)을 클릭
            correct_color = driver.find_element(By.XPATH, '//span[@onclick="answer_color(1)"]')
            correct_color.click()
            time.sleep(0.06)
    except KeyboardInterrupt:
        print("게임을 중단합니다.")
    finally:
        driver.close()

if __name__ == "__main__":
    start_game()
