def say_hi():
    print("Hello, my name is DIMMENTODD")

def make_protected_callback(password, callback):
        return lambda input_password: callback if input_password==password else print("no")

protected= make_protected_callback("22", say_hi())
protected("222")