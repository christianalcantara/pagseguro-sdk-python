from typing import List

from models.item import Item
from models.order import Order
from pagbank.models.charge import (
    PaymentMethod,
    Card,
    Holder,
    Boleto,
    BHolder,
    Charge,
    Amount,
)
from pagbank.models.customer import Customer, Phone
from pagbank.models.shipping import Address, Shipping
from pagbank.models.enum import PaymentMethodTypeEnun, CurrencyTypeEnun

phone_mock = Phone(country=55, area=11, number="999999999")

customer_mock = Customer(
    nome="Jose da Silva",
    email="email@test.com",
    cpf_cnpj="12345678909",
    phones=[phone_mock],
)

address_mock = Address(
    street="Avenida Brigadeiro Faria Lima",
    number="1384",
    complement="apto 12",
    locality="Pinheiros",
    city="São Paulo",
    region="SP",
    region_code="SP",
    postal_code="01452002",
)

shipping_mock = Shipping(address=address_mock)

payment_method_cc = PaymentMethod(
    type=PaymentMethodTypeEnun.CREDIT_CARD,
    installments=1,
    capture=False,
    card=Card(
        number="4111111111111111",
        exp_month=12,
        exp_year=2026,
        security_code="123",
        brand="visa",
        holder=Holder(
            name="Christian Douglas",
            cpf_cnpj="18695874524"
        ),
        store=False,
    ),
)

payment_method_bl = PaymentMethod(
    type=PaymentMethodTypeEnun.BOLETO,
    boleto=Boleto(
        holder=BHolder(
            name="Jose da Silva",
            email="email@test.com",
            cpf_cnpj="12345678909",
            address=address_mock,
        )
    ),
)

item_1_mock: Item = Item(name="item 01", quantity=1, unit_amount=8.53)
item_2_mock: Item = Item(name="item 02", quantity=2, unit_amount=6.20)
items_list: List[Item] = [item_1_mock, item_2_mock]

charges_mock = Charge(
    description="Pagamento teste",
    amount=Amount(value=6.50, currency=CurrencyTypeEnun.BRL),
    payment_method=payment_method_bl,
)

order_mock = Order(
    customer=customer_mock,
    items=items_list,
    shipping=shipping_mock,
    payment_method=list(charges_mock)
)

if __name__ == "__main__":
    from pprint import pprint
    print("*" * 100, "\nPHONE")
    print(phone_mock)
    print("*" * 100, "\nCUSTOMER")
    print(customer_mock)
    print("*" * 100, "\nADDRESS")
    print(address_mock)
    print("*" * 100, "\nSHIPPING")
    print(shipping_mock)
    print("*" * 100, "\nPAYMENT C")
    print(payment_method_cc)
    print("*" * 100, "\nPAYMENT B")
    print(payment_method_bl)
    print("*" * 100, "\nITEMS")
    print(item_1_mock)
    print("*" * 100, "\nCHARGES")
    print(charges_mock)
    pprint(order_mock.json())
