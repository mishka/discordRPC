from time import time, sleep
from selenium import webdriver
from pypresence import Presence
from selenium.webdriver.chrome.options import Options

client_id = ''  
RPC = Presence(client_id, pipe=0)
RPC.connect() 

chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(chrome_options = chrome_options)
song = []

while(True):
    try:
        song_name = driver.title[:-10]
        song.append(song_name)
        lenght = driver.execute_script("return document.getElementById('movie_player').getDuration()")
        t = time()
        RPC.update(large_image = 'youtube', large_text = 'Youtube', details = song_name, start = t, end = t + lenght)

        print('Current status: ' + song_name)

        while song[0] == driver.title[:-10]:
            continue
        else:
            del song[:]
            pass
    except:
        sleep(10)
