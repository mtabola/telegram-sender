from telethon import TelegramClient
import asyncio
import time
import datetime
import yaml
import nest_asyncio
nest_asyncio.apply()

file = open('config.yaml', 'r')
config = yaml.safe_load(file)
file.close()


async def func():
    while True:
        tn = datetime.datetime.now().strftime('%H:%M')
        if tn == '10:21':
            await client.send_file(config['chat_id'], 'target.jpg')
            print('Sented')
            print('Next sending throw', str(datetime.timedelta(seconds=86000)))
            time.sleep(86000)
            

        time.sleep(30)

# connection
with TelegramClient('session', config['api_id'], config['api_hash']) as client:
    client.loop.run_until_complete(func())