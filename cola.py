class cola: ##definimos la clase que manejara la cola
    ##constructor de la clase cola
    def __init__(self):
        self.cola=[]
        self.size= 0
        ##este metodo evalua si el arreglo esta vacio
    def vacio (self):
        return len(self.cola) ==0
        """esta sentencia funciona como un true o false, si la cola es igual a cero
        sera true si la cola es diferente de cero nos dira false"""

      ##este metodo nos permite agregar datos a nuestra cola
    def agregar(self, dato):
        self.cola +=[dato]
        """nos permite agregar un dato nuevo 
        al final de la cola"""
        self.size +=1
        """"funciona como un contador por que le añade un 
        espacio nuevo a la cola donde ira insertado el nuevo dato"""

    ##metodo para eliminar elementos de la cola
    ##con est metodo eliminaremos siempre el primer dato de la cola (FIFO)
    def eliminar(self):
      if self.vacio():
          print("La cola esta Vacia")
      else:
          self.cola = [self.cola[i] for i in range(1, self.size)]
          self.size -= 1

    """esta condicional evalua que si la cola esta vacia nos avisara pero
    si la cola tiene un elemento evalua cual es ese elemento que ocupa la primera 
    posicion y lo saca de la cola sobre escribiendo la cola desde la posicion 1 hasta la 
     ultima posicion""" ##recordemos que los indicies empiezan con el numero cero.

    ## metodo para mostrar la cola
    def mostrar (self):
        valor1= self.size -1 ##este metodo nos ayuda a recorrer la cola desde la posicion cero

        ##este while nos ayuda a recorrer la cola.
        while valor1 > -1:
            print(f"[{valor1}] => {self.cola[valor1]}")
            valor1 -=1

                  ##Menu de opciones
"""este es el menu por medio del cual podemos realizar las acciones de agregar, mostrar o eliminar elementos de una lista
los elementos de la lista deben agregarse uno a uno y pueden ser elementos de cualquier tipo"""
try:
    if __name__ == "__main__":
        opcion = 0
        cola = cola()
        while opcion != 6:
            print(
                "--- Colas ---\n 1. Agregar dato\n 2. Eliminar dato\n 3. ¿Está vacía la cola?\n 4. Mostrar cola\n 5. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                cola.agregar(dato)
            elif opcion == 2:
                cola.eliminar()
            elif opcion == 3:
                print("SI" if cola.vacio() else "NO")
            elif opcion == 4:
                cola.mostrar()

            elif opcion == 5:
                print("\n--- Sesión culminada ---")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)



