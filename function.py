''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("======= DEFINE (parametr) vs CALL (argument)======")
# build in fuction > print() type()
# Function - reusable block of code ! Malum bir mantiqni bajarib beruvchi blok kod
# instead of block {} in JAVA, PYTHON uses indentation!

#DEFINE - parametr
def greet(a):
    print(f"How do you do , {a}")

    def greeting(b):
        print("greeting is executed")
        return f"hi {b}"

    # CALL - argument
    result1 = greet("Rio")
    print("result1", result1)

    result2 = greeting("Justin")
    print("result2:", result2)
