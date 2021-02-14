from selenium import webdriver

browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")

# для аллерта с кавычками:
# browser.execute_script("document.title='Script executing';")

# несколько аллертов
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
