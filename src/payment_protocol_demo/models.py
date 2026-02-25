from dataclasses import dataclass


@dataclass
class PaymentResult:
    success: bool
    transaction_id: str
    status: str
    message: str


@dataclass
class RefundResult:
    success: bool
    refund_id: str
    status: str
    message: str
