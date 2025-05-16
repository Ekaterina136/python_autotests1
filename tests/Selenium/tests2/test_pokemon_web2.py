# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# каждый тест должен начинаться с test_
def test_positive_login_wiki():
    """
    Test case POC-1
    """
	# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    chrome_options.add_argument("--disable-search-engine-choice-screen") # отключаем выбор движка для поиска
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"

	# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
	# определяем адрес страницы для теста и переходим на неё
    url = "https://pokemonbattle.ru/"
    driver.get(url=url)

	# ищем по селектору инпут "Email", кликаем по нему и вводим значение email
    email = WebDriverWait(driver, timeout=10, poll_frequency=2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class*="k_form_control"] [id="k_email"]')))
    email.click()
    email.send_keys('ea136@bk.ru')
    # email.send_keys('user@mail.com') # введи тут email своего тестового аккаунта на prod окружении

	# ищем по селектору инпут "Password", кликаем по нему и вводим значение пароля
    password = driver.find_element(by=By.CSS_SELECTOR, value='[class*="k_form_control"] [id="k_password"]')
    password.click()
    password.send_keys('89053169052qA.') # введи тут пароль своего тестового аккаунта на prod окружении

	# ищем по селектору кнопку "Войти" и кликаем по ней
    enter = driver.find_element(by=By.CSS_SELECTOR, value='[class*="k_form_send_auth"]')
    enter.click()

    # ждем успешного входа и обновления страницы
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.url_to_be(url))

	# ищем элемент на странице, который содержит ID тренера
    trainer_id = WebDriverWait(driver, timeout=10, poll_frequency=2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="header_card_trainer_id_num"]')))

	# сравниваем полученный ID из кода теста с ID вашего тестового тренера
    assert trainer_id.text == '28915', 'Unexpected ID trainer' # введи тут ID своего тренера