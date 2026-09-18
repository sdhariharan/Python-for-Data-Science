from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

print(PaymentStatus.PENDING.name)
print(PaymentStatus.PENDING.value)