import uuid

from .models import PaymentResult, RefundResult


class FakeGateway:
    """Simulador local para pruebas."""

    def charge(self, amount: float, currency: str, reference: str) -> PaymentResult:
        tx_id = f"fake_tx_{uuid.uuid4().hex[:8]}"
        if amount <= 0:
            return PaymentResult(
                success=False,
                transaction_id=tx_id,
                status="rejected",
                message="El monto debe ser mayor a 0",
            )

        return PaymentResult(
            success=True,
            transaction_id=tx_id,
            status="approved",
            message=f"Pago simulado aprobado por {amount:.2f} {currency} (ref: {reference})",
        )

    def refund(self, transaction_id: str, amount: float) -> RefundResult:
        refund_id = f"fake_rf_{uuid.uuid4().hex[:8]}"
        if amount <= 0:
            return RefundResult(
                success=False,
                refund_id=refund_id,
                status="rejected",
                message="Monto de reembolso inválido",
            )

        return RefundResult(
            success=True,
            refund_id=refund_id,
            status="refunded",
            message=f"Reembolso simulado de {amount:.2f} aplicado a {transaction_id}",
        )

    def get_status(self, transaction_id: str) -> str:
        return "approved"


class BankGateway:
    """Gateway bancario simplificado (simulado)."""

    def __init__(self, bank_name: str):
        self.bank_name = bank_name
        self._transactions: dict[str, str] = {}

    def charge(self, amount: float, currency: str, reference: str) -> PaymentResult:
        tx_id = f"bank_tx_{uuid.uuid4().hex[:8]}"

        if currency not in {"MXN", "USD"}:
            self._transactions[tx_id] = "rejected"
            return PaymentResult(
                success=False,
                transaction_id=tx_id,
                status="rejected",
                message=f"Moneda no soportada por {self.bank_name}",
            )

        if amount > 10000:
            self._transactions[tx_id] = "pending_review"
            return PaymentResult(
                success=False,
                transaction_id=tx_id,
                status="pending_review",
                message="Pago enviado a revisión por monto alto",
            )

        self._transactions[tx_id] = "approved"
        return PaymentResult(
            success=True,
            transaction_id=tx_id,
            status="approved",
            message=f"Pago aprobado por {self.bank_name} (ref: {reference})",
        )

    def refund(self, transaction_id: str, amount: float) -> RefundResult:
        refund_id = f"bank_rf_{uuid.uuid4().hex[:8]}"
        current_status = self._transactions.get(transaction_id)

        if current_status != "approved":
            return RefundResult(
                success=False,
                refund_id=refund_id,
                status="rejected",
                message="Solo se puede reembolsar una transacción aprobada",
            )

        if amount <= 0:
            return RefundResult(
                success=False,
                refund_id=refund_id,
                status="rejected",
                message="Monto de reembolso inválido",
            )

        self._transactions[transaction_id] = "refunded"
        return RefundResult(
            success=True,
            refund_id=refund_id,
            status="refunded",
            message=f"Reembolso aprobado por {self.bank_name}",
        )

    def get_status(self, transaction_id: str) -> str:
        return self._transactions.get(transaction_id, "not_found")
