# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderStatus(str, enum.Enum):
    """
    The status of the Order
    """

    PENDING = "pending"
    UNFULFILLED = "unfulfilled"
    FULFILLED = "fulfilled"
    DISPUTED = "disputed"
    DISPUTE_LOST = "dispute-lost"
    REFUNDED = "refunded"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        unfulfilled: typing.Callable[[], T_Result],
        fulfilled: typing.Callable[[], T_Result],
        disputed: typing.Callable[[], T_Result],
        dispute_lost: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderStatus.PENDING:
            return pending()
        if self is OrderStatus.UNFULFILLED:
            return unfulfilled()
        if self is OrderStatus.FULFILLED:
            return fulfilled()
        if self is OrderStatus.DISPUTED:
            return disputed()
        if self is OrderStatus.DISPUTE_LOST:
            return dispute_lost()
        if self is OrderStatus.REFUNDED:
            return refunded()
