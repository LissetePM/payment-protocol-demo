from payment_protocol_demo import FakeGateway, PaymentService


def test_fake_gateway_payment_success():
    service = PaymentService(FakeGateway())
    result = service.process_order_payment("T100", 100.0, "MXN")
    assert result.success is True
    assert result.status == "approved"


def test_fake_gateway_payment_invalid_amount():
    service = PaymentService(FakeGateway())
    result = service.process_order_payment("T101", 0.0, "MXN")
    assert result.success is False
    assert result.status == "rejected"
