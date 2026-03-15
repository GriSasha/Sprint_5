test_chrome_registration.py и test_firefox_registration.py проверяют: 
    1) Успешную регистрацию: поле «Имя» не пустое; в поле Email введён email в формате логин@домен; в поле пароль - пароль из 7 символов.
    2) Ошибку для некорректного пароля: поле «Имя» не пустое; в поле Email введён email в формате логин@домен; в поле пароль - пароль из 4 символов.

test_chrome_login_to_account.py и test_firefox_login_to_account.py проверяют возможность входа в аккаунт:
    1) по кнопке «Войти в аккаунт» на главной,
    2) через кнопку «Личный кабинет»,
    3)через кнопку в форме регистрации,
    4)через кнопку в форме восстановления пароля.

test_chrome_click_on_personal_account_moves_to_personal_account.py и test_firefox_click_on_personal_account_moves_to_personal_account.py проверяют переход в личный кабинет по клику на кнопку «Личный кабинет».

test_chrome_moving_from_personal_account_to_constructor.py и test_firefox_moving_from_personal_account_to_constructor.py проверяют переход по клику на кнопку «Конструктор» и на логотип Stellar Burgers.

test_chrome_click_on_button_logout_moves_from_account.py и test_firefox_click_on_button_logout_moves_from_account.py проверяют выход по кнопке «Выйти» в личном кабинете.

test_chrome_moving_through_sections_in_constructor.py и test_firefox_moving_through_sections_in_constructor.py проверяют, что работают переходы к разделам: «Булки», «Соусы», «Начинки».

