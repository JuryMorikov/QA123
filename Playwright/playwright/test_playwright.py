import re
from playwright.sync_api import Page, expect


def test_login_page(page: Page):
    page.goto('https://demo.opencart.com/admin/')
    page.fill('input#input-username', 'demo')
    page.wait_for_timeout(10000)