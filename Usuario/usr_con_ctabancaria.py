class Usuario:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.cuenta1 = CuentaBancaria(tasa_int=0.02, balance=0)
        self.cuenta2 = CuentaAhorro(tasa_int=0.05, balance=0)
    def hacer_deposito(self, amount):
        self.cuenta.balance = self.cuenta.balance + amount
        return self
    def hacer_retiro(self, amount): 
        self.cuenta.balance = self.cuenta.balance - amount
        return self
    def mostrar_balance_usuario(self):
        print("Usuario: ",self.name,", Balance Cta Bancaria: $",self.cuenta1.balance)
        print("Usuario: ",self.name,", Balance Cta Ahorro: $",self.cuenta2.balance)
        return self
    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        return self

class CuentaBancaria:
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, tasa_int,balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    def deposito(self, amount):
        self.balance+=amount
        return self
    def retiro(self, amount):
        self.balance-=amount
        return self
    def mostrar_info_cuenta(self):
        print("Cta Bancaria: $",self.balance)
        return self
    def generar_interes(self):
        self.balance=self.balance+self.balance*self.tasa_int
        return self

class CuentaAhorro:
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, tasa_int,balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaAhorro.todas_las_cuentas.append(self)
    def deposito(self, amount):
        self.balance+=amount
        return self
    def retiro(self, amount):
        self.balance-=amount
        return self
    def mostrar_info_cuenta(self):
        print("Cta Ahorro: $",self.balance)
        return self
    def generar_interes(self):
        self.balance=self.balance+self.balance*self.tasa_int
        return self

guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
caro = Usuario("Carolina Miranda","caro@python.com")

caro.cuenta1.deposito(1000).generar_interes()
caro.cuenta2.deposito(200).deposito(500).generar_interes()
guido.cuenta1.deposito(1000).deposito(500).retiro(80).generar_interes()
guido.cuenta2.deposito(10000).deposito(400).retiro(3770)

caro.mostrar_balance_usuario()
guido.mostrar_balance_usuario()