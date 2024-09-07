class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.__titular = titular
        self.__numeroCuenta = numeroCuenta
        self.__saldo = saldo
        self.__tipoInteres = 1.5

    def getTitular(self):
        return self.__titular

    def setTitular(self, titular):
        self.__titular = titular

    def getNumeroCuenta(self):
        return self.__numeroCuenta

    def getSaldo(self):
        return self.__saldo

   
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad no válida para ingresar.")

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("No se puede retirar más de lo que hay en la cuenta.")
        elif cantidad > 0:
            self.__saldo -= cantidad
        else:
            print("Cantidad no válida para retirar.")

    def calcularInteres(self):
        return self.__saldo * (1 + self.__tipoInteres / 100)

    def setTipoInteres(self, tipoInteres):
        if 0 <= tipoInteres <= 10:
            self.__tipoInteres = tipoInteres
        else:
            print("El tipo de interés debe estar entre 0% y 10%.")