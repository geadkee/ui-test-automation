from pathlib import Path
from uuid import uuid4
import warnings
import pytest
import pytest_html
import os

def pytest_addoption(parser):
    parser.addoption("--PASSWORD", action="store", default=None, help="Test login password; overrides TEST_PASSWORD.")


@pytest.fixture(scope="session")
def password(pytestconfig):
    value = pytestconfig.getoption("PASSWORD") or os.getenv("TEST_PASSWORD")
    if not value:
        raise pytest.UsageError("Pass --PASSWORD=... or set TEST_PASSWORD before running authenticated tests.")
    return value


def pytest_html_report_title(report):
    report.title = "UI Test Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # Capture while the page is still available, before fixture teardown.
    if not report.failed or report.when not in ("setup", "call"):
        return
    page = item.funcargs.get("page")
    htmlpath = item.config.getoption("htmlpath", default=None)
    if page is None or not htmlpath:
        return

    report_dir = Path(htmlpath).expanduser().resolve().parent
    relative_path = Path("assets") / f"failure-{uuid4().hex}.png"
    try:
        (report_dir / "assets").mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(report_dir / relative_path), full_page=True)
    except Exception as error:
        warnings.warn(f"Could not capture failure screenshot: {error}", stacklevel=2)
        return

    extras = list(getattr(report, "extras", []))
    extras.append(pytest_html.extras.png(relative_path.as_posix(), name="Failure screenshot"))
    report.extras = extras
