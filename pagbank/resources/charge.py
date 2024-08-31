from core.pb_base import PBBase
from pagbank.models.order import Order


class Charge(PBBase):
    """
    Create Charge

    [Click here for more info](https://documenter.getpostman.com/view/10863174/TVetc6HV#ad9e0eb9-4e47-4d9e-8a0a-ed4a88cb456c)  # pylint: disable=line-too-long
    """

    def create(self, order_object: Order, request_options=None):
        # if not isinstance(order_object, (Order, dict)):
        #     raise ValueError(f"order_object must be an instance of Order: {type(order_object)}")
        return self._post(
            uri="/charges",
            data=order_object,
            request_options=request_options,
        )
