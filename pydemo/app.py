import asyncio
import multiprocessing
import re
import threading
import sys
from time import sleep
from typing import final
from loguru import logger
from playwright.async_api import async_playwright, ProxySettings, TimeoutError, APIRequestContext, Playwright

async def api_get(playwright: Playwright, url='https://github.com/chaosannals?tab=stars'):
    '''
    '''
    request_ctx = await playwright.request.new_context(
        proxy=ProxySettings(
            server="socks://127.0.0.1:1080",
        ),
    )
    
    r = await request_ctx.get(url)
    logger.info(await r.body())

@logger.catch
async def main():
    '''
    
    '''
    # browser = None
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(
                headless=False,
                proxy=ProxySettings(
                    server="socks://127.0.0.1:1080",
                ),
            )
            context = await browser.new_context(
                locale='zh-CN',
                screen={
                    'width': 800,
                    'height': 600,
                },
                storage_state='auth.json',
            )
            # page = await browser.new_page(
            #     locale='zh-CN',
            #     screen={
            #         'width': 800,
            #         'height': 600,
            #     },
            #     storage_state='auth.json'
            # )
            page = await context.new_page()
            await page.goto('https://github.com/chaosannals?tab=repositories')

            await api_get(playwright, 'https://github.com/dashboard-feed?page=2')

            while True:
                #await page.wait_for_url(re.compile(r'https?://.*?github.com'))
                try:
                    async with page.expect_navigation() as r:
                        #print(await r.value)
                        pass
                except TimeoutError as e:
                    #print(e)
                    pass
    except KeyboardInterrupt as e:
        #print('close.')
        pass
    # finally:
    #     if browser != None:
    #         await browser.close()

# def process_main():
#     asyncio.run(main())

def thread_main():
    try:
        asyncio.run(main())
    except:
        pass


if __name__ == '__main__':
    # process = multiprocessing.Process(
    #     target=process_main,
    #     args=[]
    # )
    try:
        logger.remove()
        logger.add(
            sink=sys.stdout,
            level='INFO'
        )
        logger.add(
            'runtime/logs/{time:YYYY-MM-DD}.log',
            level='TRACE',
            # rotation='00:00',
            rotation='2000 KB',
            retention='7 days',
            encoding='utf8'
        )
        #asyncio.run(main())

        thread = threading.Thread(target=lambda: asyncio.run(main()))
        thread.daemon = True
        thread.start()
        thread.join()

        # process.start()
        # while True:
        #     sleep(0.01)
    except KeyboardInterrupt as e:
        print('close.')
    except RuntimeError as e:
        print('exit.')
    finally:
        # process.terminate()
        pass