from payment_protocol_demo import (
    BankGateway,
    FakeGateway,
    PaymentGatewayProtocol,
    PaymentService,
)


def main() -> None:
    fake_gateway = FakeGateway()
    payment_service_fake = PaymentService(fake_gateway)

    print("\n=== DEMO con FakeGateway ===")
    payment_1 = payment_service_fake.process_order_payment(
        order_id="A1001", total_amount=499.90, currency="MXN"
    )
    print(payment_1)

    status_1 = payment_service_fake.check_payment_status(payment_1.transaction_id)
    print("Status:", status_1)

    refund_1 = payment_service_fake.refund_order_payment(payment_1.transaction_id, 100.00)
    print(refund_1)

    bank_gateway = BankGateway(bank_name="Banco Demo MX")
    payment_service_bank = PaymentService(bank_gateway)

    print("\n=== DEMO con BankGateway ===")
    payment_2 = payment_service_bank.process_order_payment(
        order_id="B2001", total_amount=850.00, currency="MXN"
    )
    print(payment_2)

    if payment_2.success:
        status_2 = payment_service_bank.check_payment_status(payment_2.transaction_id)
        print("Status:", status_2)

        refund_2 = payment_service_bank.refund_order_payment(payment_2.transaction_id, 200.00)
        print(refund_2)

        status_2_after = payment_service_bank.check_payment_status(payment_2.transaction_id)
        print("Status después de reembolso:", status_2_after)

    payment_3 = payment_service_bank.process_order_payment(
        order_id="B2002", total_amount=15000.00, currency="MXN"
    )
    print(payment_3)

    print("\n=== Verificación estructural (Protocol) ===")
    print("FakeGateway cumple protocolo:", isinstance(fake_gateway, PaymentGatewayProtocol))
    print("BankGateway cumple protocolo:", isinstance(bank_gateway, PaymentGatewayProtocol))


if __name__ == "__main__":
    main()
