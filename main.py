import sys
from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

def get_tennis_test():
    cService = webdriver.ChromeService(executable_path='/Users/f.shamardanov/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service = cService)
    driver.get("https://zabota-tatar.ru/ru/golden-years/courses")

    # Выбираем Направления
    element = driver.find_element(by=By.XPATH, value="/html/body/main/section/div/div[3]/div[1]/div[1]/div/button")
    element.click()
    sleep(1)

    # Выбираем Спорт
    element = driver.find_element(by=By.XPATH, value="/html/body/main/section/div/div[3]/div[1]/div[1]/div/div/ul/li[2]/button/p")
    element.click()
    sleep(1)

    # Выбираем Теннис
    element = driver.find_element(by=By.XPATH, value="/html/body/main/section/div/div[3]/div[1]/div[1]/div/div/ul/div[1]/ul/li[4]/label")
    element.click()
    sleep(1)

    elements = driver.find_elements(By.CLASS_NAME, "general-activity-card_activity_card__title___xOk_")

    for element in elements:
        if "еннис" not in element.accessible_name:
            raise "not valid filter result"
        print(element.text)
    driver.close()


def get_monday_test():
    cService = webdriver.ChromeService(executable_path='/Users/f.shamardanov/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service = cService)
    driver.get("https://zabota-tatar.ru/ru/golden-years/courses")

    # Выбираем День
    element = driver.find_element(by=By.XPATH, value="/html/body/main/section/div/div[3]/div[1]/div[2]/div/button")
    element.click()
    sleep(1)

    # Выбираем понедельник
    element = driver.find_element(by=By.XPATH, value="/html/body/main/section/div/div[3]/div[1]/div[2]/div/div/ul/li[1]")
    element.click()
    sleep(2)

    elements = driver.find_elements(By.CLASS_NAME, "schedule-list_wrapper__Xb7Va")

    for element in elements:
        if "Пн" not in element.text:
            raise "not valid filter result"
        print(element.text)
    driver.close()

def check_reset_filter_test():
    cService = webdriver.ChromeService(
        executable_path='/Users/f.shamardanov/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=cService)
    driver.get("https://zabota-tatar.ru/ru/golden-years/courses")
    sleep(1)

    element = driver.find_element(by=By.CLASS_NAME,
                                  value="general-activity-list_activity_list__amount__avMso")
    sleep(1)
    all_res = element.text

    # Выбираем День
    element = driver.find_element(by=By.XPATH,
                                  value="/html/body/main/section/div/div[3]/div[1]/div[2]/div/button")
    element.click()
    sleep(1)

    # Выбираем понедельник
    element = driver.find_element(by=By.XPATH,
                                  value="/html/body/main/section/div/div[3]/div[1]/div[2]/div/div/ul/li[1]")
    element.click()
    sleep(2)

    element = driver.find_element(by=By.CLASS_NAME,
                                  value="general-activity-list_activity_list__amount__avMso")
    sleep(1)
    if all_res == element.text:
        print("firstly", all_res, "after", element.text)
        raise "filter not work"

    element = driver.find_element(by=By.CLASS_NAME,
                                  value="active-filters_activity_filters__selected_filter__jkD7r")
    element.click()
    sleep(1)

    element = driver.find_element(by=By.CLASS_NAME,
                                  value="general-activity-list_activity_list__amount__avMso")
    sleep(1)

    if all_res != element.text:
        print("firstly", all_res, "after", element.text)
        raise "reset filter not work"


def check_only_by_appointment_test():
    cService = webdriver.ChromeService(
        executable_path='/Users/f.shamardanov/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=cService)
    driver.get("https://zabota-tatar.ru/ru/golden-years/courses")

    # Выбираем Запись на занятие
    element = driver.find_element(by=By.XPATH, value="/html/body/main/section/div/div[3]/div[1]/div[4]/div/button")
    element.click()
    sleep(1)

    # Выбираем По записи
    element = driver.find_element(by=By.XPATH,
                                  value="/html/body/main/section/div/div[3]/div[1]/div[4]/div/div/ul/li[1]")
    element.click()
    sleep(2)

    elements = driver.find_elements(By.CLASS_NAME, "general-activity-card_activity_card__appointment_type__7M8Mv")

    for element in elements:
        if element.text != "По записи":
            raise "not valid filter result"
    driver.close()

def location_test():
    cService = webdriver.ChromeService(
        executable_path='/Users/f.shamardanov/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=cService)
    driver.get("https://zabota-tatar.ru/ru/golden-years/courses")

    # Выбираем Весь Татарстан
    element = driver.find_element(by=By.XPATH, value="/html/body/main/section/div/div[3]/div[2]/button")
    element.click()
    sleep(1)

    # Выбираем Азнакаевский район
    element = driver.find_element(by=By.XPATH, value='//*[@id="modal-root"]/div/div/div[2]/div/ul/li[3]/button')
    element.click()
    sleep(1)

    # Выбираем г. Азнакаево
    element = driver.find_element(by=By.XPATH, value='//*[@id="modal-root"]/div[2]/div/div[2]/div/ul/li[2]')
    element.click()
    sleep(1)

    # Нажимаем выбрать
    element = driver.find_element(by=By.XPATH, value='//*[@id="modal-root"]/div[2]/div/div[2]/div/div/button[1]')
    element.click()
    sleep(2)

    elements = driver.find_elements(By.CLASS_NAME, "general-activity-card_activity_card__address_wrapper__JEb3N")
    for element in elements:
        if not "Азнакаево" in element.text:
            raise "not valid filter result"
    driver.close()

def run_tests() -> int:
    get_tennis_test()
    get_monday_test()
    check_reset_filter_test()
    check_only_by_appointment_test()
    location_test()

    return 0

if __name__ == '__main__':
    sys.exit(run_tests())