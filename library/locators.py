
class Locators:

    # Гиперссылка "Вернуться на сайт boxberry"
    Back_to_boxberry = "//div[@class='ct']/a[@class='rr1']"
    # Текст блока "Войти в личный кабинет"
    Block_Login = "//form/div/div[@class='t1']"
    # Текст "Телефон"
    Telephone = "//i[@class='input-label-phone']"
    # Поле "Логин" (Телефон) и Пароль
    Login = "//div[@class='form1']/div[2]/span/div/input"
    Password = "//div[@class='form1']/div[3]/span/input"
    # Кнопка "Войти"
    Sign_in = "//div[@class='form1']/div[6]/input"

    # Тексты: 'Пароль' и 'Напомнить'
    Password_Text = "//div[@class='form1']/div[3]/i"
    Remind = "//div[@class='form1']/div[3]/a"
    # Гиперссылка "Регистрация"
    Registration = "//div[@class='form1']/div[6]/a"
    # Иконки ВК, ОК для входа через соц. сети
    VK = "//div[@class='social']/a[1]"
    OK = "//div[@class='social']/a[2]"

    # Ссылки ВК, ОК для входа через соц. сети
    VK_href = 'https://oauth.vk.com/authorize?client_id=5584202&redirect_uri=https://lkp-predprod.lkp-task.boxberry.ru/auth/vkontakte/&response_type=code'
    OK_href = 'https://connect.ok.ru/oauth/authorize?client_id=1247894784&scope=VALUABLE_ACCESS&redirect_uri=https://lkp-predprod.lkp-task.boxberry.ru/auth/odnoklassniki/&response_type=code'
