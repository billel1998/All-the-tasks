def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

def test_recur_factorial():
    a = 23
    b = 4
    status = true
    b = recur_factorial(b)
    if a !=b:
        status = false
    assert status, "your method is wrong"