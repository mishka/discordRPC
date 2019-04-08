from time import sleep
from selenium import webdriver
from pypresence import Presence
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

client_id = ''  
RPC = Presence(client_id, pipe=0)
RPC.connect() 

chrome_options = Options()
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = { 'browser':'ALL' }
chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(chrome_options = chrome_options, desired_capabilities = dc)

with open("./youtube.js", "r") as x:
    js = x.read()
    x.close()

while True:
    try:
        driver.execute_script(js)
        logdriver = driver.get_log('browser')
        RPC.update(large_image = 'youtube', large_text = 'Youtube', details = driver.title[:-10], state = logdriver[-1]['message'][20:-1])
        sleep(15)
    except Exception as e:
        print(str(e))
        sleep(10)
        continue
