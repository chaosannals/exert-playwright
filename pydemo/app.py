import asyncio
import re
import sys
from loguru import logger
from playwright.async_api import async_playwright, ProxySettings, TimeoutError

@logger.catch
async def main():
    '''
    
    '''
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(
                headless=False,
                proxy=ProxySettings(
                    server="socks://127.0.0.1:1080",
                ),
            )
            page = await browser.new_page(
                locale='zh-CN',
                screen={
                    'width': 800,
                    'height': 600,
                },
                storage_state='auth.json'
            )
            await page.goto('https://github.com/chaosannals?tab=repositories')
            while True:
                #await page.wait_for_url(re.compile(r'https?://.*?github.com'))
                try:
                    async with page.expect_navigation() as r:
                        print(await r.value)
                except TimeoutError as e:
                    print(e)
    except KeyboardInterrupt as e:
        print('close.')



if __name__ == '__main__':
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
    asyncio.run(main())