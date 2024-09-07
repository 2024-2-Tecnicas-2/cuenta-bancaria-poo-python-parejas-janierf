import cuenta_bancaria


if __name__ == '__main__':
   def main():
    cuenta = cuenta_bancaria("Juan Perez", "123456789", 1000)

   
    print(f"Titular de la cuenta: {cuenta.getTitular()}")
    print(f"Número de cuenta: {cuenta.getNumeroCuenta()}")
    print(f"Saldo inicial: {cuenta.getSaldo()}")

    cuenta.ingresar(500)
    print(f"Saldo después de ingresar: {cuenta.getSaldo()}")

    
    cuenta.retirar(300)
    print(f"Saldo después de retirar: {cuenta.getSaldo()}")

   
    print(f"Saldo con interés: {cuenta.calcularInteres()}")

   
    cuenta.setTipoInteres(3)
    print(f"Nuevo saldo con interés: {cuenta.calcularInteres()}")

if __name__ == "__main__":
    main()