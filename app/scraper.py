import asyncio
from collections import namedtuple
from playwright.async_api import async_playwright

CaseData = namedtuple("CaseData", ["parties", "filing_date", "next_hearing", "latest_order_url"])

async def fetch_case_data_async(case_type, case_number, filing_year):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://services.ecourts.gov.in/ecourtindia_v6/")

        await page.click("text=District Court")
        await page.select_option("#sess_state_code", label="Haryana")
        await page.wait_for_selector("#sess_dist_code:enabled")
        await page.select_option("#sess_dist_code", label="Faridabad")
        await page.click("input[type=submit][value='Proceed']")

        await page.wait_for_selector("text=Case Status")
        await page.click("text=Case Status")

        await page.select_option("select[name='case_type']", label=case_type)
        await page.fill("input[name='case_number']", case_number)
        await page.fill("input[name='case_year']", filing_year)

        await page.click("input[type=submit][value='Submit']")
        await page.wait_for_timeout(5000)

        parties = await page.text_content("xpath=//td[contains(text(),'Petitioner')]/following-sibling::td")
        filing_date = await page.text_content("xpath=//td[contains(text(),'Filing')]/following-sibling::td")
        next_hearing = await page.text_content("xpath=//td[contains(text(),'Next Hearing')]/following-sibling::td")
        order_link = await page.get_attribute("xpath=//a[contains(text(),'PDF')]", "href")

        await browser.close()

        return CaseData(
            parties=parties.strip() if parties else "N/A",
            filing_date=filing_date.strip() if filing_date else "N/A",
            next_hearing=next_hearing.strip() if next_hearing else "N/A",
            latest_order_url=order_link if order_link else "#"
        )

def fetch_case_data(case_type, case_number, filing_year):
    return asyncio.run(fetch_case_data_async(case_type, case_number, filing_year))
