from robot.api.deco import keyword
import asyncio
from pyppeteer import launch

@keyword
def capture_full_page_screenshot(url, save_path, chrome_path=None, keep_open=False):
    async def screenshot():
        browser = None
        try:
            # Launch the browser with a custom executablePath if provided
            browser = await launch(
                headless=not keep_open,
                executablePath=chrome_path
            )
            page = await browser.newPage()
            await page.goto(url, {'waitUntil': 'networkidle2'})
            await page.screenshot({'path': save_path, 'fullPage': True})

            if keep_open:
                print("Browser is open. Press Enter to close it.")
                input()  # Wait for user input before closing
        finally:
            if browser:
                await browser.close()
    asyncio.run(screenshot())