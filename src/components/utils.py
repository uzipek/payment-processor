# utils.py

class Logger:
    def __init__(self, name, level='INFO'):
        self.name = name
        self.level = level
        self.handled_levels = {
            'DEBUG': 10,
            'INFO': 20,
            'WARNING': 30,
            'ERROR': 40,
            'CRITICAL': 50
        }

    def debug(self, message):
        if self.handled_levels[self.level] >= self.handled_levels['DEBUG']:
            print(f"[{self.name}] DEBUG: {message}")

    def info(self, message):
        if self.handled_levels[self.level] >= self.handled_levels['INFO']:
            print(f"[{self.name}] INFO: {message}")

    def warning(self, message):
        if self.handled_levels[self.level] >= self.handled_levels['WARNING']:
            print(f"[{self.name}] WARNING: {message}")

    def error(self, message):
        if self.handled_levels[self.level] >= self.handled_levels['ERROR']:
            print(f"[{self.name}] ERROR: {message}")

    def critical(self, message):
        if self.handled_levels[self.level] >= self.handled_levels['CRITICAL']:
            print(f"[{self.name}] CRITICAL: {message}")


class PaymentProcessor:
    def __init__(self, logger):
        self.logger = logger

    def process_payment(self, amount, currency):
        self.logger.info("Processing payment...")
        # Simulate payment processing
        # Actual payment processing logic should be implemented here
        self.logger.info("Payment processed successfully")


def load_config():
    import json
    with open('config.json') as file:
        return json.load(file)


def validate_payment_request(data):
    if 'amount' not in data or 'currency' not in data:
        raise ValueError("Invalid payment request")
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        raise ValueError("Invalid amount")
    if data['currency'] not in ['USD', 'EUR', 'GBP']:
        raise ValueError("Invalid currency")
    return True