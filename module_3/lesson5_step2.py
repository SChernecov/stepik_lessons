# вызвать аллерт
alert('Hello!');

# принять аллерт
alert = browser.switch_to.alert
alert.accept()

# получить текст из алерта
alert = browser.switch_to.alert
alert_text = alert.text

# принять аллерт
confirm = browser.switch_to.alert
confirm.accept()

# отклонить аллерт
confirm.dismiss()

# подтвердить аллерт с полем ввода
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()