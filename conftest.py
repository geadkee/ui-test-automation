from pathlib import Path
from uuid import uuid4
import warnings

import pytest
import pytest_html


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


# import os
# from pathlib import Path
# import runpy

# import pytest
# def pytest_addoption(parser):
#     group = parser.getgroup("ui-tests")
#     group.addoption(
#         "--variables", default="config.py", metavar="PATH",
#         help="Python configuration file defining get_app_config().",
#     )
#     group.addoption(
#         "--password", default=None,
#         help="Login password; defaults to TEST_PASSWORD from the environment.",
#     )


# @pytest.fixture(scope="session")
# def variables(pytestconfig):
#     path = Path(pytestconfig.getoption("variables"))
#     if not path.is_absolute():
#         path = pytestconfig.rootpath / path
#     if not path.is_file():
#         raise pytest.UsageError(f"Configuration file does not exist: {path}")
#     namespace = runpy.run_path(str(path))
#     get_config = namespace.get("get_app_config")
#     if not callable(get_config):
#         raise pytest.UsageError(f"{path} must define get_app_config().")
#     config = get_config()
#     if not isinstance(config, dict) or not config.get("base_url"):
#         raise pytest.UsageError("get_app_config() must return a dict with base_url.")
#     return config


# @pytest.fixture(scope="session")
# def password(pytestconfig):
#     value = pytestconfig.getoption("password") or os.getenv("TEST_PASSWORD")
#     if not value:
#         raise pytest.UsageError("Pass --password or set TEST_PASSWORD before running login tests.")
#     return value


# @pytest.fixture(scope="session")
# def app_config(variables):
#     return variables


# @pytest.fixture(scope="session")
# def valid_user(password):
#     username = os.getenv("TEST_USERNAME")
#     if not username:
#         raise pytest.UsageError(
#             "Set TEST_USERNAME before running authenticated tests."
#         )
#     return {"username": username, "password": password}


