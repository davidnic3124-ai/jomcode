def remaining(capacity: int, registered: int) -> int:
    return capacity - registered

print(remaining(100, 75)) # Output: 25
print(remaining.__annotations__)

