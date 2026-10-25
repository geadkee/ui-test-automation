"""Non-secret scenario data. Valid credentials come from the environment."""

INVALID_LOGIN_CASES = [
    {
        "id": "unknown-user",
        "username": "invalid_user",
        "password": "deliberately_invalid_password",
        "expected_error": (
            "Epic sadface: Username and password do not match any user in this service"
        ),
    },
    {
        "id": "missing-username",
        "username": "",
        "password": "deliberately_invalid_password",
        "expected_error": "Epic sadface: Username is required",
    },
    {
        "id": "missing-password",
        "username": "invalid_user",
        "password": "",
        "expected_error": "Epic sadface: Password is required",
    },
]

PRODUCTS = {
    "sauce-labs-backpack": {
        "name": "Sauce Labs Backpack",
        "description": "Streamlined backpack with protective storage for a laptop and tablet.",
        "price": "29.99",
        "image_src": "https://www.saucedemo.com/assets/sauce-backpack-1200x1500-CjRW-Djj.jpg",
    },
    "sauce-labs-bike-light": {
        "name": "Sauce Labs Bike Light",
        "description": "Water-resistant red bicycle light with three modes and an included AAA battery.",
        "price": "9.99",
        "image_src": "https://www.saucedemo.com/assets/bike-light-1200x1500-DxcZRFOA.jpg",
    },
    "sauce-labs-bolt-t-shirt": {
        "name": "Sauce Labs Bolt T-Shirt",
        "description": "Gray cotton American Apparel shirt featuring a red lightning bolt.",
        "price": "15.99",
        "image_src": "https://www.saucedemo.com/assets/bolt-shirt-1200x1500-mR0ldpVS.jpg",
    },
    "sauce-labs-fleece-jacket": {
        "name": "Sauce Labs Fleece Jacket",
        "description": "Medium-weight fleece with a quarter-length zipper, suitable for outdoor and office wear.",
        "price": "49.99",
        "image_src": "https://www.saucedemo.com/assets/sauce-pullover-1200x1500-BfbI-PSd.jpg",
    },
    "sauce-labs-onesie": {
        "name": "Sauce Labs Onesie",
        "description": "Infant bodysuit with reinforced snap fasteners and durable stitched edges.",
        "price": "7.99",
        "image_src": "https://www.saucedemo.com/assets/red-onesie-1200x1500-BrSuq0ic.jpg",
    },
    "test.allthethings()-t-shirt-(red)": {
        "name": "Test.allTheThings() T-Shirt (Red)",
        "description": "Soft cotton red shirt with an automation-testing theme.",
        "price": "15.99",
        "image_src": "https://www.saucedemo.com/assets/red-tatt-1200x1500-E-qp6aYf.jpg",
    },
}

CHECKOUT_CUSTOMER = {
    "first_name": "Test",
    "last_name": "Customer",
    "postal_code": "VLT1234",
}

ORDER_SUCCESS_MESSAGE = "Thank you for your order!"
