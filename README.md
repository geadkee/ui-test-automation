# UI test automation

Python, Playwright, and pytest tests for https://www.saucedemo.com.

## Structure

- `pages/`: page objects, uppercase selector constants, and reusable UI actions.
- `tests/`: login, cart, and checkout test cases.
- `test_data/`: non-secret scenario data and expected results.
- `conftest.py`: shared pytest fixtures, credential loading, and login setup.
- `config.py`: application configuration via `BASE_URL`.
- `pytest.ini`: test discovery, failure screenshots, and HTML report settings.
- `.github/workflows/ui-tests.yml`: CI execution and result uploads.
- `reports/` and `artifacts/`: generated results, ignored by Git.

## Setup

Use Python 3.11 or newer. From the repository root:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Set `TEST_USERNAME` and `TEST_PASSWORD` in your execution environment before
running authenticated tests. Passwords are not stored in test data. For a local
PowerShell session, you can enter the password without placing it in history:

```powershell
$env:TEST_USERNAME = Read-Host "Test username"
$credential = Get-Credential -UserName $env:TEST_USERNAME -Message "Test credentials"
$env:TEST_PASSWORD = $credential.GetNetworkCredential().Password
```

`BASE_URL` is optional and defaults to `https://www.saucedemo.com`.
Environment variables are loaded directly; `.env` files are not auto-loaded.

## Execution

```CLI
python -m pytest --headed
python -m pytest tests/test_1_users_access_control.py
```

The suite produces `reports/report.html`, with the generated stylesheet at
`reports/assets/style.css` and failure screenshots at `reports/assets/failure-*.png`.
Expand a failed test in the report to view its screenshot. Share or download the
whole `reports/` folder so the stylesheet and screenshots remain available.
The screenshot hook captures setup or test failures when a `page` fixture is
available; it cannot capture failures before a page exists or after it closes.
For extra styling, keep your CSS in a source file (for example,
`report_styles/custom.css`) and run `python -m pytest --css=report_styles/custom.css`.
Do not edit the generated `reports/assets/style.css`, which is rebuilt on each run.

## CI

Configure repository Actions secrets named `TEST_USERNAME` and `TEST_PASSWORD`.
The workflow installs Chromium, runs the suite, and uploads results even after
failures. Fork pull requests do not receive repository secrets, so authenticated
tests require a trusted run with those secrets available.

## Assumptions

- Credentials belong to a working SauceDemo user with purchase access.
- The selected product is Sauce Labs Backpack at $29.99.
- Expected messages are in English.
- Tests use Chromium by default; no fixed sleeps or random product selection.
- API validation is an optional assessment extension and is not implemented.
