# Função de boas-vindas / Welcome function
def welcome():
    print('''
Welcome to Register''')


welcome()

# Função dos dados pedidos & informados / Data function
def register():

    r1: str = str(input("Hello, what is your name? "))
    r2: int = int(input("And, how old are you? "))
    r3: int = int(input("What is your birth date? "))
    r4: str = str(input("Where are you from? "))

# Final da função, pós recebimento de dados / End of function, after receiving data
    print('''Your data was completed, thanks!''')
    print(r1)
    print(r2)
    print(r3)
    print(r4)


register()
