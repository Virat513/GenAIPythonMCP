LOGIN_USERS = {
    "valid": {"username": "standard_user", "password": "secret_sauce"},
    "invalid_username": {"username": "invalid_user", "password": "secret_sauce"},
    "invalid_password": {"username": "standard_user", "password": "wrong_pass"},
    "locked_out": {"username": "locked_out_user", "password": "secret_sauce"},
    "empty": {"username": "", "password": ""},
    "min_length": {"username": "a", "password": "b"},
    "max_length": {"username": "a"*50, "password": "b"*50},
    "sql_injection": {"username": "' OR '1'='1", "password": "' OR '1'='1"}
}