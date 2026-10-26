# UI Test Automation
UI test automation using Python + Playwright + pytest for [SauceDemo](https://www.saucedemo.com)

Bonus: Testing UI against API too

## Setup

Requires an installed Python 3.11+. From the repository root, create
and activate a virtual environment to keep project dependencies separate from
your global Python installation:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

On macOS/Linux, activate with `source .venv/bin/activate` instead.
Run tests in the same activated terminal. Use `deactivate` when finished.

## Run tests

Replace `PASSWORD` with the SauceDemo password:

```powershell
# Run all tests with the browser visible
pytest --headed --PASSWORD="PASSWORD" -rp

# Run only the happy flow purchase test. 
pytest tests/test_2_users_make_purchases.py --headed --PASSWORD="PASSWORD" -rp
```
Tips:  Add `-s` to show test logs. Use `--headed` during manual run to view activity in browser

The repo already have the secret set `TEST_PASSWORD`, and will be used once the pipeline runs

## Configuration

`pytest.ini` automatically loads the base URL from `config.json`.
To use another configuration, add `--variables other-config.json`.

## Structure

```text
pages/         Page objects, selectors, user actions, assertions
tests/         Test cases: Login, Purchase, API/UI comparison tests
test_data/     Product data + valid/invalid credentail
utils/         Helper logs
conftest.py    Password fixture and report hooks
config.json    Where we'll keep the environment variables, can be differentiate liek `sit.json` or `uat.json`
```

## Reports in Html

- Open `reports/report.html` after running tests.
- Failure screenshots are under `reports/assets/` when a browser page is available. Share the entire `reports/` folder

