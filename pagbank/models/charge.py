from datetime import date, timedelta
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field, HttpUrl, EmailStr, constr

from pagbank.models.enum import CurrencyTypeEnun, PaymentMethodTypeEnun
from pagbank.models.shipping import Address


class Holder(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=30,
        description="Name of the holder of the Credit Card, Debit Card and Brand Token.",
    )
    tax_id: constr(min_length=11, max_length=14) = Field(
        alias="cpf_cnpj",
        description="Document number (CPF or CPNJ) of the holder of the Credit Card, Debit Card and Brand Token.",
    )


class BHolder(Holder):
    email: EmailStr
    address: Address


class Boleto(BaseModel):
    due_date: date = date.today() + timedelta(days=2)
    holder: BHolder


class Card(BaseModel):
    number: str = Field(
        min_length=14, max_length=19, description="Credit or Debit Card Number."
    )
    exp_month: int = Field(
        description="Credit Card, Debit Card or Brand Token expiration month."
    )
    exp_year: int = Field(
        description="Expiration year of the Credit Card, Debit Card or Brand Token."
    )
    security_code: str = Field(
        min_length=3,
        max_length=4,
        description="Credit Card, Debit Card or Brand Token Security Code.",
    )
    store: bool = False
    brand: str = Field(min_length=2, max_length=20, description="Card banner. Ex: Visa")
    holder: Holder = Field(
        default=None,
        description="Contains the information of the holder of the Credit Card, Debit Card and Brand Token.",
    )


class PaymentMethod(BaseModel):
    type: PaymentMethodTypeEnun
    installments: int = None
    capture: bool = None
    soft_descriptor: str = None
    card: Card = None
    boleto: Boleto = None


class Amount(BaseModel):
    value: float = Field(
        description="Amount to be charged in cents. Only positive integers."
    )
    currency: CurrencyTypeEnun = Field(
        default=CurrencyTypeEnun.BRL,
        description="Three-letter ISO currency code, in upper case. For now,"
        " only the Brazilian Real (“BRL”) is supported.",
    )

    # @field_serializer("value", when_used="always")
    # def serialize_total(value: float):
    #     return int(value * 100)


class Charge(BaseModel):
    reference_id: str = Field(
        min_length=1,
        max_length=64,
        default_factory=lambda: uuid4().hex,
        description="Unique identifier assigned to the charge.",
    )
    description: str = Field(
        min_length=1, max_length=64, description="Billing description."
    )
    amount: Amount
    payment_method: PaymentMethod = None
    notification_urls: List[HttpUrl] = [
        # "https://localhost:8000/checkout/pagseguro-receive-notification/"
    ]
