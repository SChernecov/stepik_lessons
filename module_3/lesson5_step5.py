# Для переключения на новую вкладку указываем, на какую вкладку мы хотим перейти
browser.switch_to.window(window_name)

# выбираем новую вкладку
new_window = browser.window_handles[1]

# запоминаем имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
first_window = browser.window_handles[0]