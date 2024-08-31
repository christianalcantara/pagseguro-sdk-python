from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=64, description="Name of the item.")
    quantity: int = Field(ge=1, le=99999, default=1, description='Quantity referring to the item.')
    unit_amount: float = Field(description='Unit amount of the item.')

    # @field_serializer("unit_amount", when_used="always")
    # def serialize_total(unit_amount: float):
    #     return int(unit_amount * 100)
