# env.py
# Centralized environment/test data configuration for Playwright MCP + Python
 
# Base URL for automation
BASE_URL = "https://www.demoblaze.com/index.html"
 
# User accounts used in automation scripts
USERS = {
    "logged_in_user": {
        "username": "mcppoc",
        "password": "123456"
    }
}
 
# Product inventory for Add to Cart test cases
PRODUCTS = {
    "SKU-ADD-001": {
        "name": "Samsung galaxy s6",
        "unit_price": 360
    },
    "SKU-GUEST-001": {
        "name": "Nokia lumia 1520",
        "unit_price": 820
    },
    "SKU-OPT-001": {
        "name": "HTC One M9",
        "required_option": "Color"
    },
    "SKU-QTY-001": {
        "name": "Sony vaio i5",
        "unit_price": 790
    },
    "SKU-REMOVE-001": {
        "name": "Dell i7 8gb",
        "unit_price": 700
    },
    "SKU-OOS-001": {
        "name": "Iphone 6 32gb",
        "stock": "out_of_stock",
        "unit_price": 650
    },
    "SKU-SR-001": {
        "search_query": "headphones",
        "name": "Bose Soundlink",
        "unit_price": 299
    },
    "SKU-VAR-001": {
        "name": "Macbook Pro",
        "required_option": "Storage"
    },
    "SKU-MAX-001": {
        "name": "Canon EOS",
        "maximum_quantity": 10,
        "unit_price": 300
    },
    "SKU-PERSIST-001": {
        "name": "Apple monitor",
        "quantity": 2,
        "unit_price": 180
    },
    "SKU-DEC-001": {
        "name": "LG TV",
        "unit_price": 19.95
    }
}
 
# Framework-wide constants
TIMEOUTS = {
    "DEFAULT": 5000,
    "LONG": 15000,
    "SHORT": 2000
}
 
# Paths for storing automation artifacts
PATHS = {
    "PAGE_OBJECT_DIR": "aitesting/page_objects/",
    "GENERATED_TEST_DIR": "aitesting/tests/",
    "LOGS_DIR": "aitesting/logs/",
    "SCREENSHOTS_DIR": "aitesting/logs/screenshots/"
}
 