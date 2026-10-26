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
        "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
        "price": "29.99",
        "image_src": "https://www.saucedemo.com/assets/sauce-backpack-1200x1500-CjRW-Djj.jpg",
    },
    "sauce-labs-bike-light": {
        "name": "Sauce Labs Bike Light",
        "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
        "price": "9.99",
        "image_src": "https://www.saucedemo.com/assets/bike-light-1200x1500-DxcZRFOA.jpg",
    },
    "sauce-labs-bolt-t-shirt": {
        "name": "Sauce Labs Bolt T-Shirt",
        "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
        "price": "15.99",
        "image_src": "https://www.saucedemo.com/assets/bolt-shirt-1200x1500-mR0ldpVS.jpg",
    },
    "sauce-labs-fleece-jacket": {
        "name": "Sauce Labs Fleece Jacket",
        "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
        "price": "49.99",
        "image_src": "https://www.saucedemo.com/assets/sauce-pullover-1200x1500-BfbI-PSd.jpg",
    },
    "sauce-labs-onesie": {
        "name": "Sauce Labs Onesie",
        "description": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
        "price": "7.99",
        "image_src": "https://www.saucedemo.com/assets/red-onesie-1200x1500-BrSuq0ic.jpg",
    },
    "test.allthethings()-t-shirt-(red)": {
        "name": "Test.allTheThings() T-Shirt (Red)",
        "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.",
        "price": "15.99",
        "image_src": "https://www.saucedemo.com/assets/red-tatt-1200x1500-E-qp6aYf.jpg",
    },
}

CHECKOUT_DETAILS = {
    "first_name": "UI Test",
    "last_name": "Customer",
    "postcode": "56000",
}

ORDER_SUCCESS_MESSAGE = "Thank you for your order!"
