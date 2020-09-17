from IPython import get_ipython

### To use this script, fill in the following information.
# Use your own values from my.telegram.org
api_id = 12345678
api_hash = 'api_hash from my.telegram.org'  

# Bot Information
bot_name = 'BitcoinClick_bot'
view_ad_command  = '/visit'
view_ad_button_number = 0   # Usually the first button

# Browser Information
OS_LIST = ['win32', 'linux64', 'mac64']   #available options from Google
os_version = OS_LIST[0]    #Set OS version from OS_LIST
chrome_version = '85.0.4183.87'    #Set Chrome Version

### Setting up Telethon
_ = get_ipython().getoutput('pip3 install telethon')
from telethon import TelegramClient
from telethon.sessions import StringSession

client = TelegramClient(StringSession(), api_id, api_hash)
await client.start()
await client.connect()

# Test message send and receive
_ = await client.connect()
_ = await client.send_message('me', 'Launching robEth')
_ = await client.connect()
test_message = await client.get_messages('me', 1)
test_message[0].message

### Initiate first communication with bot
_ = await client.connect()
_ = await client.send_message(bot_name, '/start')
_ = await client.connect()
reply = await client.get_messages(bot_name, 1)
reply[0].message
    
### Send command
async def send_command():
    await client.connect()
    await client.send_message(bot_name, view_ad_command)
    print('Command Sent')

### Get messages
async def get_message_url():
    await client.connect()
    message = await client.get_messages(bot_name, 3)
    if message[0] == message[2]:
        print('URL: False')
        return False
    url = message[0].reply_markup.rows[0].buttons[button_number].url
    print('Url: ' + url)
    return url

### Delay
import time
def wait(n):
    time.sleep(n)

### Open browser in background (No captcha)
_ = get_ipython().getoutput('pip install mechanize')

import mechanize
import http.cookiejar as cookielib   #cookielib was renamed to cookiejar but I like the old name

# Browser
browser = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

# Browser options
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Set User-Agent
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Open Browser in backgrounf option
def open_browser(url_link):
    r = browser.open(url_link)
    r.read()
    wait(30)
    r.close()

### Open Browser in foreground (Captcha Ads)
# Download Chrome Webdriver
import wget

url = 'https://chromedriver.storage.googleapis.com/' + chrome_version + '/chromedriver_' + os_version + '.zip'
filename = 'chromedriver_'+os_version+'.zip'
filename = wget.download(url, filename)

from zipfile import ZipFile

zip = ZipFile(filename)
zip.extractall()

_ = get_ipython().getoutput('pip3 install selenium')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException, WebDriverException

def check_browser_window(driver):
    return driver.window_handles == []

# Open browser in foreground function
def manual_ad(url):
    try:
        driver = webdriver.Chrome()
        driver.wait = WebDriverWait(driver, float('inf'))
        driver.get(url)
        driver.wait.until(check_browser_window)
        print('User Closed')
        driver.quit()
        return
    except (WebDriverException):
        print('User Closed')
        driver.quit()
        return

### Main Loop
async def run_loop():
    wait(5)
    await send_command()
    wait(5)
    url = await get_message_url()
    print(url)
    if url == False:
        manual_ad(url)
    else:
        open_browser(url)
        
### Start
while True:
    run_loop()
