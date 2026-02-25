from typing import Protocol, runtime_checkable

from .models import PaymentResult, RefundResult


@runtime_checkable
class PaymentGatewayProtocol(Protocol):
    """Contrato mínimo para cualquier pasarela de pago."""

    def charge(self, amount: float, currency: str, reference: str) -> PaymentResult:
        ...

    def refund(self, transaction_id: str, amount: float) -> RefundResult:
        ...

    def get_status(self, transaction_id: str) -> str:
        ...
