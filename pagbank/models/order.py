from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field

from pagbank.models.charge import Charge
from pagbank.models.shipping import Shipping
from pagbank.models.customer import Customer
from pagbank.models.item import Item


class Order(BaseModel):
    id: str = Field(min_length=41, max_length=41, default_factory=lambda: uuid4().hex)
    reference_id: str = Field(
        min_length=1,
        max_length=200,
        default_factory=lambda: uuid4().hex,
        description="Unique identifier assigned to the charge.",
    )
    customer: Customer
    items: List[Item] = []
    shipping: Shipping
    payment_method: Charge
