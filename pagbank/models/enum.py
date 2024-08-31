from enum import Enum


class BaseEnun(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)


class PhoneTypeEnum(str, BaseEnun):
    MOBILE = "MOBILE"
    BUSSINES = "BUSSINES"
    HOME = "HOME"


class PaymentMethodTypeEnun(str, BaseEnun):
    CREDIT_CARD = "CREDIT_CARD"
    BOLETO = "BOLETO"
    PIX = "PIX"


class CurrencyTypeEnun(str, BaseEnun):
    BRL = "BRL"


class CountryTypeEnun(str, BaseEnun):
    BRA = "BRA"
