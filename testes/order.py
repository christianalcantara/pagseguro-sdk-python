from testes.mock import order_mock
from pagbank import SDK
import os

TOKEN = os.environ['PB_TOKEN']
print(">>>", TOKEN)
sdk = SDK(access_token=TOKEN)


def credit_card_order():
    print(order_mock.dict())
    return sdk.charge().create(order_object=order_mock.json())


if __name__ == '__main__':
    o = credit_card_order()
    print(o)