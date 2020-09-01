import pyautogui as auto
import time

user=''
pdw=''

searchBar = (205,52)
print("***********Welcome to the instagram automation developed by Kjwebguru***********")
time.sleep(2.5)

#Open Chrome using Window Search
print('opening google chrome...')
searchCenter = auto.locateCenterOnScreen('assets/winsearch.png')
auto.moveTo(searchCenter, duration=0.3)
auto.click(searchCenter)
auto.write('chrome', interval=0.2)
chromeCenter = auto.locateCenterOnScreen('assets/chrome.png')
auto.moveTo(chromeCenter, duration=0.3)
auto.click(chromeCenter)
time.sleep(5) #To Do: Add a check if browser is open

#Open Instagram
print('opening instagram...')
auto.moveTo(searchBar, duration=0.3)
auto.click(searchBar)
auto.write('https://instagram.com', interval=0.2)
auto.press('enter')
time.sleep(5) #To Do: Check if site is open

#Open Profile
print('opening profile...')
userBar = auto.locateCenterOnScreen('assets/username.png')
auto.moveTo(userBar, duration=0.3)
auto.click(userBar)
auto.write(user, interval=0.2)
passBar = auto.locateCenterOnScreen('assets/password.png')
auto.moveTo(userBar, duration=0.1)
auto.click(passBar)
auto.write(pdw, interval=0.2)
loginBtn = auto.locateCenterOnScreen('assets/login.png')
auto.moveTo(loginBtn, duration=0.1)
auto.click(loginBtn)






