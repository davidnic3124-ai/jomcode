def valid_capacity(value):
     if type(value) is not int or not 1 <= value  <= 100:
        raise ValueError("Capacity must be an interger from 1 to 100")
     return value
print(valid_capacity(11))
