#Task1#
def check_divisibility(num, divisor):
    if not (isinstance(num, int) and isinstance(divisor, int)):
        print("The input must be a interger")
        return none
    if num % divisor == 0:
        return True
    else:
        return False

  #Task2#
  check_divisibility(10,2)
True
check_divisibility(7,3)
False
