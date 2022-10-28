from time import sleep
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

def New_Window():
    global driver
    a = ActionChains(driver)
    elemento = driver.find_element(By.XPATH, '//*[@id="nav-header-menu"]/div/label/a/span/span[2]')
    a.move_to_element(elemento).perform()
    elemento = driver.find_element(By.CSS_SELECTOR,'a[data-id="news"]')
    a.move_to_element(elemento).click(elemento).perform()
    novidades = driver.find_elements(By.CSS_SELECTOR, 'div.andes-card__content')
    resultBlackFriday = list(filter(lambda x: "A BLACK FRIDAY tá ON na Central de Promoções." in x.text, novidades))
    print(resultBlackFriday)
    setinha = resultBlackFriday[0].find_element(By.CSS_SELECTOR, 'div.sc-news-notice-expander')
    classSetinha = driver.execute_script('return arguments[0].firstChild.className', setinha)
    first_tab_handle = driver.current_window_handle
    if(classSetinha == 'sc-news-notice-expand-icon sc-ui-chevron--down'):
        a.key_down(Keys.CONTROL).click(setinha).key_up(Keys.CONTROL).perform()
    resultBlackFriday[0].find_element(By.CSS_SELECTOR,'a').click()
    sleep(5)
    if driver.current_window_handle == first_tab_handle:
        driver.switch_to.window(driver.window_handles[1])
    # Inicia Filtro
    filterB = driver.find_element(By.CSS_SELECTOR, '#filter_trigger')
    filterB.click()
    a.move_to_element(filterB).click(filterB).perform()
    sleep(2)
    chkE = driver.find_element(By.CSS_SELECTOR, 'body > div.andes-modal__portal > div > div > div.andes-modal__scroll > div.andes-modal__content > div > div:nth-child(3) > div.sc-list-filter-group__items.sc-list-filter-group__items-line > div:nth-child(3) > label')
    chkE.click()
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div[3]/button[1]').click()
    sleep(5)
    botoesParticipar = driver.find_elements(By.CSS_SELECTOR, 'button[text="Participar"]')
    botaosPart = driver.find_elements(By.CSS_SELECTOR, '.label-container__text')
    for botao in botaosPart:
        botao.click()
        
    botoesParticipar = driver.find_elements(By.CSS_SELECTOR, 'button[text="Participar"]')
    for x in range(len(botoesParticipar)):
        try:
            el = driver.find_element(By.CSS_SELECTOR, 'button[text="Participar"]')
            a.move_to_element(el).click(el).perform()
            sleep(2)
            el2 = driver.find_element(By.CSS_SELECTOR, 'div.andes-modal__actions > button.andes-button.andes-button--large.andes-button--loud')
            a.move_to_element(el2).click(el2).perform()
            sleep(5)
        except:
            print('Erro ao tentar participar de campanha')
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    canvas.pack()
    
HEIGHT = 300
WIDTH = 500

ws = tk.Tk()
ws.title("Python Guides")
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(ws, text="Click Aqui após efetuar login", bg='White', fg='Black',
                              command=lambda: New_Window())

button.pack()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.mercadolivre.com.br/')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="nav-header-menu"]/a[2]').click()
ws.mainloop()