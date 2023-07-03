#after submitted itt, i discovered that exists isdigit() so it could be easier

def validate_pin(pin):
    #if the length is not 4 or 6, false
    digit = ["0","1","2","3","4","5","6","7","8","9"]
    if len(pin)!=4 and len(pin)!=6:
        return False
    #if is not a digit, false
    for x in list(pin):
        if x not in digit:
            return False
            break
    return True