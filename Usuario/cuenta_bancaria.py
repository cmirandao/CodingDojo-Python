class CuentaBancaria:
# atributo de clase
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
        print("Balance: $",self.balance)
        return self
    def generar_interes(self):
        self.balance=self.balance*self.tasa_int
        return self
    @classmethod
    def imprimir_todas_cuentas(cls):
        cont=0
        for cuenta in cls.todas_las_cuentas:
            cont+=1
            print(f"La cuenta {cont} tiene un balance de ${cuenta.balance}")

cta1 = CuentaBancaria(0.15, 1000)
cta2 = CuentaBancaria(0.09, 2000)
print("<--- MOSTRAR EL BALANCE INDIVIDUAL --->")
cta1.deposito(100).deposito(500).deposito(50).retiro(700).generar_interes().mostrar_info_cuenta()
cta2.deposito(500).deposito(40).retiro(20).retiro(200).retiro(170).retiro(900).generar_interes().mostrar_info_cuenta()
print("<--- MOSTRAR TODOS LOS BALANCES --->")
cta1.imprimir_todas_cuentas()