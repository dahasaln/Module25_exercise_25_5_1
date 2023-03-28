from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

try:
    # Переходим на страницу авторизации
    driver.get("https://petfriends.skillfactory.ru/login")
    driver.maximize_window()

    # Вводим email
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'email').send_keys('catdog@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID,'pass').send_keys('7777777')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/button').click()
     #нажимаем Мои питоцы
    driver.find_element(By.XPATH,'//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.save_screenshot("4.png")

    images = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-img-top')))
    names = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-title')))
    descriptions = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-text')))

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', 'Image not found'
        assert names[i].text != '', 'Name not found'
        assert descriptions[i].text != '', 'Description not found'
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

