class InvalidAge(Exception):
    pass
age=-18
try:
    if(age<0):
        raise InvalidAge("Age should be positive")
except InvalidAge as e:
    age=0
    print(e)
else:
    print("Age Validated")
finally:
    print("Data Updated")