import time
import requests
from library.Pages import PagesHelper
from library.locators import Locators

# Выполнить переход https://lkp-predprod.lkp-task.boxberry.ru/auth/

def test_status_code():
    url = "https://lkp-predprod.lkp-task.boxberry.ru/auth/"
    response = requests.get(url)
    assert response.status_code == 200

def test_check_page(browser):
    # открываем браузер
    main_page = PagesHelper(browser)
    # Мдем на сайт "https://lkp-predprod.lkp-task.boxberry.ru/auth/"
    main_page.go_to_site()

    # Ищем локтор (class-'Logo')
    main_page.wait_object_by_CLASS("logo")
    # Ищем локтор (class-'rr1') и текст ('Вернуться на сайт boxberry')
    main_page.wait_object_and_name_by_XPATH(Locators.Back_to_boxberry, 'Вернуться на сайт boxberry')
    # Ищем форму (class-'form1') блок "Войти в личный кабинет"
    main_page.wait_object_by_CLASS("form1")

    # Ищем текст (class-'t1') "Войти в личный кабинет"
    main_page.wait_object_and_name_by_XPATH(Locators.Block_Login, 'Войти в личный кабинет')

    # Ищем Поле: телефон (class-'it')
    main_page.wait_object_by_CLASS("it")

    # Ищем текст: телефон и пароль
    main_page.wait_object_and_name_by_XPATH(Locators.Telephone, 'Телефон')
    main_page.wait_object_and_name_by_XPATH(Locators.Password_Text, 'Пароль')

    # Ищем поля: телефон и Пароль
    Login = main_page.wait_object_by_XPATH(Locators.Login)
    Password = main_page.wait_object_by_XPATH(Locators.Password)

    # Ищем гиперссылку: 'Напомнить'
    main_page.wait_object_and_name_by_XPATH(Locators.Remind, 'Напомнить')

    # Ищем чекбокс reCAPTCHA (class-'it j1 recaptcha-block')
    Captcha = main_page.wait_object_by_CLASS("recaptcha-block")

    # Ищем гиперссылку "Регистрация"
    main_page.wait_object_and_name_by_XPATH(Locators.Registration, 'Регистрация')

    # Ищем кнопку "Войти"
    Button = main_page.wait_object_by_XPATH(Locators.Sign_in)
    value_button = Button.get_attribute('value')
    assert value_button == 'Войти', f'Button Value is invalid [Войти] != [{value_button}]'

    # Ищем иконки ВК, ОК для входа через соц. сети
    vk = main_page.wait_object_by_XPATH(Locators.VK)
    vk_href = vk.get_attribute('href')
    assert vk_href == Locators.VK_href, f'VK href is invalid {vk_href}'

    ok = main_page.wait_object_by_XPATH(Locators.OK)
    ok_href_ = ok.get_attribute('href')
    assert ok_href_ == Locators.OK_href,f'OK href is invalid {ok_href_}'

    # Вводим Логин Login 79257860365
    main_page.send_keys(Login, '79257860365')

    # Вводим Пароль Password Ikjnkg12.
    main_page.send_keys(Password, 'Ikjnkg12')

    # Ставим капчу Captcha
    main_page.click_the_element(Captcha)
    time.sleep(3)

    # Нажимаем войти button
    main_page.click_the_element(Button)
    time.sleep(8)


