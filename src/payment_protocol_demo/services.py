from .models import PaymentResult, RefundResult
from .protocols import PaymentGatewayProtocol


class PaymentService:
    """Lógica de negocio desacoplada del proveedor de pago."""

    def __init__(self, gateway: PaymentGatewayProtocol):
        self.gateway = gateway

    def process_order_payment(
        self, order_id: str, total_amount: float, currency: str = "MXN"
    ) -> PaymentResult:
        reference = f"order:{order_id}"
        result = self.gateway.charge(total_amount, currency, reference)

        if result.success:
            print(f"[INFO] Pago exitoso para order {order_id}. TX={result.transaction_id}")
        else:
            print(
                f"[WARN] Pago fallido/pendiente para order {order_id}. "
                f"Status={result.status}"
            )
        return result

    def refund_order_payment(self, transaction_id: str, amount: float) -> RefundResult:
        result = self.gateway.refund(transaction_id, amount)
        if result.success:
            print(f"[INFO] Reembolso exitoso. RF={result.refund_id}")
        else:
            print(f"[WARN] Reembolso rechazado. Status={result.status}")
        return result

    def check_payment_status(self, transaction_id: str) -> str:
        return self.gateway.get_status(transaction_id)
