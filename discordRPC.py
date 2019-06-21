from time import time, sleep
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
song = []

while(True):
    try:
        song_name = driver.title[:-10]
        song.append(song_name)
        lenght = driver.execute_script("return document.getElementById('movie_player').getDuration()")
        t = time()
        RPC.update(large_image = 'youtube', large_text = 'Youtube', details = song_name, start = t, end = t + lenght)
        #sleep(int(str(lenght).split('.')[0]))

        print('Current status: ' + song_name)

        while song[0] == driver.title[:-10]:
            continue
        else:
            del song[:]
            pass
    except:
        sleep(10)
