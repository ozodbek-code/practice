''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("======= DEFINE (parametr) vs CALL (argument) =======")


# DEFINE - parametr
def greet(a):
    print(f"How do you do, {a}")


# CALL - argument
result1 = greet("Rio")
print("result1:", result1)


def greeting(b):
    print("greeting is executed")
    return f"hi {b}"


result2 = greeting("Justin")
print("result2:", result2)


print("======= Keyword & default arguments ======")


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old"


result3 = give_greet("Justin", 20)
print("result3:", result3)

result3 = give_greet("Martin")
print("result3:", result3)