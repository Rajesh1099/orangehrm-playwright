import os
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "videos/",
        "viewport": {
            "width": 1366,
            "height": 768
        },
        "record_video_size": {
            "width": 1366,
            "height": 768
        }
    }


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():

    # Create folders for test artifacts
    os.makedirs("reports", exist_ok=True)
    os.makedirs("videos", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)

    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Capture screenshot when test fails
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            page.screenshot(path=f"screenshots/{item.name}.png",full_page=True)

