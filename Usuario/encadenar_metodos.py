# declarar una clase y darle el nombre Usuario
class Usuario:
    # declarando un atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self , name, email_address):
    # los asignamos en consecuencia
        self.name = name
        self.email = email_address
    # el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
        # agregando el método de depósito
    def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self
    def hacer_retiro(self, amount): 
        self.balance_cuenta-=amount
        return self
    def mostrar_balance_usuario(self):
        print("Usuario: ",self.name,", Balance: $",self.balance_cuenta)
    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)


guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
caro = Usuario("Carolina Miranda","caro@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python
print(caro.name)

guido.hacer_deposito(100).hacer_deposito(200).hacer_deposito(700)
monty.hacer_deposito(900).hacer_deposito(500)
caro.hacer_deposito(1000)
print("Balance Guido: ",guido.balance_cuenta)	# salida: 300
print("Balance Monty: ",monty.balance_cuenta)	# salida: 550
print("Balance Caro: ",caro.balance_cuenta)	# salida: 1000
x=100
y=10
z=450
sum=y+x
sum2=x+y+z
guido.hacer_retiro(x)
monty.hacer_retiro(y).hacer_retiro(x)
caro.hacer_retiro(x).hacer_retiro(y).hacer_retiro(z)

print("Nuevo Balance Guido (-$",x,"): ",guido.balance_cuenta)	# salida: 200
print("Nuevo Balance Monty (-$",sum,"): ",monty.balance_cuenta)	# salida: 540
print("Nuevo Balance Caro (-$",sum2,"): ",caro.balance_cuenta)	# salida: 550

guido.mostrar_balance_usuario()
monty.mostrar_balance_usuario()
caro.mostrar_balance_usuario()
tx=400
guido.transfer_dinero(caro,tx)
print("Nuevos balances, por transferencia de Guido por $",tx," a Carolina----->")
guido.mostrar_balance_usuario()
caro.mostrar_balance_usuario()