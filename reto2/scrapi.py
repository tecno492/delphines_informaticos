import string
from itertools import product
from selenium import webdriver
from time import sleep


def product_loop(generator, driver):
    for p in generator:

        sleep(1)
        passs = ''.join(p)
        print(passs)
        driver.find_element('xpath', '//*[@id="solution"]').clear()
        sleep(0.05)
        driver.find_element('xpath', '//*[@id="solution"]').send_keys(passs)
        driver.find_element('xpath', '//*[@id="Send"]').click()
        try:
            driver.find_element('xpath', '//*[@id="statusResponseFail"]').click()
            return False
        except:
            return passs

    return False


url = 'https://cdstechchallenges.com'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

user = "delfines"
passw = "delfines999"

all_char = string.ascii_letters[:26].upper()
print(all_char)

sleep(3)
driver.find_element('xpath', '//*[@id="username"]').send_keys(user)
driver.find_element('xpath', '//*[@id="password"]').send_keys(passw + "\n")
sleep(3)
driver.find_element('xpath', '//*[@id="Reto 2: Sun_2"]').click()
sleep(2)
driver.find_element('xpath', '//*[@id="solution"]').send_keys('a')
sleep(0.2)
driver.find_element('xpath', '//*[@id="Send"]').click()

incorrect = True

for le in range(4, 8 + 1):
    stri = product(all_char, repeat=int(le))
    for p in stri:

        passs = ''.join(p)
        #print(passs)
        driver.find_element('xpath', '//*[@id="solution"]').clear()
        driver.find_element('xpath', '//*[@id="solution"]').send_keys(passs)

        driver.find_element('xpath', '//*[@id="Send"]').click()
        sleep(0.3)
        try:
            if driver.find_element('xpath', '//*[@id="statusResponseFail"]').text != "Respuesta incorrecta":
                incorrect = False
                print(passs)

        except:
            print(passs)


input()
driver.quit()
