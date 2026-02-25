# payment-protocol-demo

Demo básico en Python para entender `Protocol` con una analogía de sistema de pagos.

## Qué incluye

- `PaymentGatewayProtocol` (contrato)
- `FakeGateway` (simulador)
- `BankGateway` (gateway bancario simplificado)
- `PaymentService` (lógica de negocio desacoplada)
- tests básicos con `pytest`

## Estructura

```text
payment-protocol-demo/
├─ main.py
├─ README.md
├─ requirements-dev.txt
├─ src/
│  └─ payment_protocol_demo/
│     ├─ __init__.py
│     ├─ models.py
│     ├─ protocols.py
│     ├─ gateways.py
│     └─ services.py
└─ tests/
   └─ test_payment_service.py
```

## Cómo correrlo (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements-dev.txt
$env:PYTHONPATH = "src"
python main.py
```

## Cómo correrlo (macOS / Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements-dev.txt
export PYTHONPATH=src
python main.py
```

## Correr tests

```bash
PYTHONPATH=src pytest -q
```

## Subir a GitHub

```bash
git init
git add .
git commit -m "feat: add payment protocol demo"
git branch -M main
git remote add origin <TU_REPO_URL>
git push -u origin main
```

## Idea principal

`PaymentService` no depende de una clase concreta (Stripe/PayPal/Banco), sino del **comportamiento** definido en `PaymentGatewayProtocol`.
