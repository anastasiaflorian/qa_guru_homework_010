import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def configure_browser():
    browser.config.window_width = 1920
    browser.config.window_heigth = 1080
    browser.config.base_url = "https://demoqa.com"

    yield

    browser.quit()