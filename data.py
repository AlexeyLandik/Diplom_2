class Data:

    RESPONSE_KEYS_FOR_SUCCESS_REGISTRATION_AND_LOGIN = ('success' and 'true' and 'user' and 'email' and 'name' and 'accessToken' and 'refreshToken')
    RESPONSE_FOR_REGISTRATION_EXISTING_USER = '{"success":false,"message":"User already exists"}'
    RESPONSE_FOR_USER_WITHOUT_EMAIL = '{"success":false,"message":"Email, password and name are required fields"}'
    RESPONSE_FOR_LOGIN_USER_WITH_INCORRECT_EMAIL = '{"success":false,"message":"email or password are incorrect"}'
    CHANGED_USER_DATA = {"email": "changed_email@mail1.ru", "password": "changed_password", "name": "changed_name"}
    RESPONSE_AFTER_SUCCESS_CHANGED_LOGINED_USER_DATA = ('{"success":true,"user":{"email":"changed_email@mail1.ru",'
                                                        '"name":"changed_name"}}')
    RESPONSE_AFTER_NOT_SUCCESS_CHANGED_NOT_LOGINED_USER_DATA = '{"success":false,"message":"You should be authorised"}'
    EXIST_EMAIL = 'changed_email@mail.ru'
    RESPONSE_AFTER_NOT_SUCCESS_CHANGED_USER_DATA_EXIST_EMAIL = ('{"success":false,"message":"User with such email '
                                                                'already exists"}')
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6c"]}
    NOT_VALID_INGREDIENTS = {"ingredients": ["not_valid_ingredient"]}
    EMPTY_INGREDIENTS = {"ingredients": []}
    RESPONSE_CREATE_ORDER_WITHOUT_INGREDIENTS = '{"success":false,"message":"Ingredient ids must be provided"}'
    RESPONSE_GET_ORDERS_BY_NOT_AUTH_USER = '{"success":false,"message":"You should be authorised"}'
