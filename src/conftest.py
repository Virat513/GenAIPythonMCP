import os
import pytest
from playwright.sync_api import sync_playwright

# ----------------------------------
# Execution configuration
# ----------------------------------
# Controlled via environment variables
#
# BROWSER  = chromium | firefox | webkit
# HEADLESS = true | false
# ----------------------------------

BROWSER = os.getenv("BROWSER", "chromium").lower()
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


@pytest.fixture(scope="function")
def playwright():
    """Start Playwright for each test (parallel-safe)."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright):
    """Launch browser per test."""
    if BROWSER == "chromium":
        browser = playwright.chromium.launch(headless=HEADLESS)
    elif BROWSER == "firefox":
        browser = playwright.firefox.launch(headless=HEADLESS)
    elif BROWSER == "webkit":
        browser = playwright.webkit.launch(headless=HEADLESS)
    else:
        raise ValueError(
            "Invalid BROWSER value. Use chromium, firefox, or webkit."
        )

    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    """Create isolated browser context."""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    """Provide a fresh page to the test."""
    page = context.new_page()
    yield page
    page.close()
