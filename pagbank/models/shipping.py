from pydantic import BaseModel, Field
from pagbank.models.enum import CountryTypeEnun


class Address(BaseModel):
    street: str = Field(min_length=1, max_length=60, description="Address Street.")
    number: str = Field(min_length=1, max_length=20, description="Address Number.")
    complement: str | None = Field(
        min_length=1, max_length=40, description="Complement Address."
    )
    locality: str = Field(
        min_length=1, max_length=40, description="Neighborhood of the address."
    )
    city: str = Field(min_length=1, max_length=90, description="Address city.")
    region: str = Field(min_length=1, max_length=50, description="Nome do Estado")
    region_code: str = Field(min_length=2, max_length=2, description="Sigla do Estado")
    country: str = Field(
        min_length=1,
        max_length=3,
        default=CountryTypeEnun.BRA,
        description="Address country",
    )
    postal_code: str = Field(
        min_length=8, max_length=8, default="BR", description="Address zip code."
    )


class Shipping(BaseModel):
    address: Address  # = Field(description="Contains order delivery address information.")
