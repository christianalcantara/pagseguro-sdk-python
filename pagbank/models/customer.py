from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, constr

from pagbank.models.enum import PhoneTypeEnum


class Phone(BaseModel):
    country: int = Field(
        default=55,
        ge=1,
        le=99,
        description="Código do país do telefone (ex.: 55 para Brasil)",
    )
    area: int = Field(
        ge=1, le=99, description="Código de área do telefone (ex.: 11 para São Paulo)"
    )
    number: str = Field(
        min_length=8,
        max_length=9,
        description="Número de telefone sem o código de área",
    )
    type: PhoneTypeEnum = PhoneTypeEnum.MOBILE


class Customer(BaseModel):
    nome: constr(min_length=1, max_length=30) = Field(description="Nome do cliente")
    email: EmailStr = Field(description="E-mail do cliente")
    tax_id: constr(min_length=11, max_length=14) = Field(
        alias="cpf_cnpj", description="CPF ou CNPJ do cliente"
    )
    phone: List[Phone] = Field(
        alias="phones",
        description="Lista de telefones do cliente",
    )


if __name__ == "__main__":
    # Exemplo de uso:
    customer = Customer(
        nome="João Silva",
        email="joao.silva@example.com",
        cpf_cnpj="12345678901",
        phones=[Phone(area_code=11, number="987654321")],
    )
    print(customer.model_dump())
