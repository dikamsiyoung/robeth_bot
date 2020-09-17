from IPython import get_ipython

### To use this script, fill in the following information.
# Use your own values from my.telegram.org
api_id = 'api_id from my.telegram.org'
api_hash = 'api_hash from my.telegram.org'  

# Bot Information
bot_name = 'ETH_Ads_uk_bot'
view_ad_command  = '/viewads'
view_ad_button_number = 0   # Usually the first button

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
reply[view_ad_button_number].message

### For ETH Ads Bot
async def send_message():
    time.sleep(35)
    await client.connect()
    await client.send_message(bot_name, view_ad_command)
    print('Done!')
    
### Start
while True:
    await send_message()
    
