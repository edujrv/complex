import math

class Complejo:
    def __init__(self, real, imaginario):
        """
        Inicializa un objeto Complejo con los valores de la parte real e imaginaria.

        Parámetros:
            real (float): El valor de la parte real del número complejo.
            imaginario (float): El valor de la parte imaginaria del número complejo.
        """
        self.real = self.convertir_numero(real)
        self.imaginario = self.convertir_numero(imaginario)

    def operacion(self, other, lambda_function):
        """
        Funcion de orden superior que realiza una operación entre dos números complejos.

        Parámetros:
            other (Complejo): El otro número complejo con el que se realizará la operación.
            lambda_function (function): La función lambda que define la operación a realizar.

        Retorna:
            Complejo: El resultado de la operación como un nuevo número complejo.
        """
        return Complejo(*lambda_function(self, other))
    
    
    # Establece los atributos con los que voy a matchear cuando use pattern matching.
    __match_args__ = ("real", "imaginario")

    def __add__(self, other):
        """
        Suma dos números complejos o un número complejo con un entero o flotante.

        Parámetros:
        - other: El número complejo, entero o flotante a sumar.

        Retorna:
        - El resultado de la suma.

        Lanza:
        - TypeError: Si se intenta sumar un complejo con un tipo diferente a complejo, entero o flotante.
        """
        match other:
            case Complejo(_, _):
                return self.operacion(other, lambda x, y: (x.real + y.real, x.imaginario + y.imaginario))
            case int(_):
                return self.operacion(other, lambda x, y: (x.real + y, x.imaginario))
            case float(_):
                return self.operacion(other, lambda x, y: (x.real + y, x.imaginario))
            case _:
                raise TypeError("No se puede sumar un complejo con un tipo diferente a complejo, int o float")
            

    def __sub__(self, other):
        """
        Resta el complejo actual con otro complejo, un entero o un flotante.

        Parámetros:
            other (Complejo, int, float): El número o complejo a restar.

        Retorna:
            Complejo: El resultado de la resta.

        Lanza:
            TypeError: Si se intenta restar un complejo con un tipo diferente a complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return self.operacion(other, lambda x, y: (x.real - y.real, x.imaginario - y.imaginario))
            case int(_):
                return self.operacion(other, lambda x, y: (x.real - y, x.imaginario))
            case float(_):
                return self.operacion(other, lambda x, y: (x.real - y, x.imaginario))
            case _:
                raise TypeError("No se puede restar un complejo con un tipo diferente a complejo, int o float")


    def __mul__(self, other):
        """
        Realiza la multiplicación de dos números complejos.

        Parámetros:
            other: El número complejo o escalar con el que se va a multiplicar.

        Retorna:
            El resultado de la multiplicación.

        Lanza:
            TypeError: Si se intenta multiplicar un complejo con un tipo diferente a complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return self.operacion(other, lambda x, y: ((x.real * y.real) - (x.imaginario * y.imaginario), (x.real * y.imaginario) + (x.imaginario * y.real)))
            case int(_):
                return self.operacion(other, lambda x, y: ((x.real * y) - (x.imaginario * 0), (x.real * 0) + (x.imaginario * y)))
            case float(_):
                return self.operacion(other, lambda x, y: ((x.real * y) - (x.imaginario * 0), (x.real * 0) + (x.imaginario * y)))
            case _:
                raise TypeError("No se puede multiplicar un complejo con un tipo diferente a complejo, int o float")
            
    
    def __truediv__(self, other):
        """
        Realiza la división de dos números complejos.

        Parámetros:
            other: El número complejo o escalar con el que se va a dividir.

        Retorna:
            El resultado de la división.

        Lanza:
            TypeError: Si se intenta dividir un número complejo con un tipo diferente a complejo, int o float.
        """
        
        match other:
            case Complejo(_, _):
                return self.operacion(other, lambda x, y: (((x.real * y.real) + (x.imaginario * y.imaginario)) / ((y.real ** 2) + (y.imaginario ** 2)), ((x.imaginario * y.real) - (x.real * y.imaginario)) / ((y.real ** 2) + (y.imaginario ** 2))))
            case int(_):
                return self.operacion(other, lambda x, y: (x.real / y, x.imaginario / y))
            case float(_):
                return self.operacion(other, lambda x, y: (x.real / y, x.imaginario / y))
            case _:
                raise TypeError("No se puede dividir un complejo con un tipo diferente a complejo, int o float")
            
    def __pow__(self, n):
        """
        Calcula la potencia de un número complejo elevado a la potencia n.

        Parámetros:
        - n: La potencia a la que se desea elevar el número complejo.

        Retorna:
        El resultado de elevar el número complejo a la potencia n.
        """
        r = abs(self)
        theta = math.atan(self.imaginario / self.real)

        return self.operacion(n, lambda x, y: (round( math.pow(r, y) * math.cos(y * theta), 2), round(math.pow(r, y) * math.sin(y * theta), 2)))

    def __neg__(self):
        """
        Devuelve el negativo del número complejo.

        Retorna:
            Complejo: El negativo del número complejo.
        """
        return Complejo(-self.real, -self.imaginario)
    
    # actua como Modulo
    def __abs__(self):
        """
        Devuelve el valor absoluto del número complejo.

        Retorna:
            float: El valor absoluto del número complejo.
        """
        return (self.real ** 2 + self.imaginario ** 2) ** (1/2)

    def __str__(self):
        """
        Devuelve una representación en cadena del número complejo.

        Si el componente imaginario es negativo, se muestra en formato "real - abs(imaginario)i".
        Si el componente imaginario es positivo o cero, se muestra en formato "real + imaginarioi".

        Retorna:
            str: Representación en cadena del número complejo.
        """
        if self.imaginario < 0:
            return f"{self.real} - {abs(self.imaginario)}i"
        else:
            return f"{self.real} + {self.imaginario}i"

    def __hash__(self):
        """
        Calcula el valor hash del objeto Complejo.

        Retorna:
            int: El valor hash del objeto Complejo.
        """
        return hash((self.real, self.imaginario))
    
    def __repr__(self):
        """
        Devuelve una representación en cadena del número complejo.
        Si el componente imaginario es negativo, se muestra en formato "real - abs(imaginario)i".
        Si el componente imaginario es positivo o cero, se muestra en formato "real + imaginarioi".
        """
        if self.imaginario < 0:
            return f"{self.real} - {abs(self.imaginario)}i"
        else:
            return f"{self.real} + {self.imaginario}i"
    
    def __dict__(self):
        """
        Devuelve un diccionario con las propiedades del número complejo.
        
        Retorna:
            dict: Un diccionario con las propiedades del número complejo.
                Las claves son "real" y "imaginario".
        """
        return {"real": self.real, "imaginario": self.imaginario}
    
    

    def __eq__(self, other):
        """
        Compara si dos números complejos son iguales.

        Parámetros:
            other: El número complejo o el valor numérico a comparar.

        Retorna:
            bool: True si los números complejos son iguales, False en caso contrario.

        Lanza:
            TypeError: Si se intenta comparar un número complejo con un tipo diferente a complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return (self.real == other.real and self.imaginario == other.imaginario)
            case int(_):
                return (self.real == other.real and self.imaginario == 0)
            case float(_):
                return (self.real == other.real and self.imaginario == 0)
            case _:
                raise TypeError("No se puede comparar un complejo con un tipo diferente a complejo, int o float")
            
    def __gt__(self, other):
        """
        Compara si el número complejo actual es mayor que otro número complejo, entero o flotante.

        Parámetros:
            other (Complejo, int, float): El número complejo, entero o flotante a comparar.

        Retorna:
            bool: True si el número complejo actual es mayor que el otro número, False en caso contrario.

        Lanza:
            TypeError: Si se intenta comparar un número complejo con un tipo diferente a complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return (self.real, self.imaginario) > (other.real, other.imaginario)                    
            case int(_):
                return self > Complejo(other, 0)
            case float(_):
                return self > Complejo(other, 0)
            case _:
                raise TypeError("No se puede comparar un complejo con un tipo diferente a complejo, int o float")
    
    def __lt__(self, other):
        """
        Compara si el complejo actual es menor que otro objeto.

        Parámetros:
            other: El objeto con el que se compara.

        Retorna:
            True si el complejo actual es menor que el otro objeto, False de lo contrario.

        Lanza:
            TypeError: Si el objeto con el que se compara no es de tipo complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return (self.real, self.imaginario) < (other.real, other.imaginario)                    
            case int(_):
                return self < Complejo(other, 0)
            case float(_):
                return self < Complejo(other, 0)
            case _:
                raise TypeError("No se puede comparar un complejo con un tipo diferente a complejo, int o float")
            
    def __ge__(self, other):
        """
        Compara si el complejo actual es mayor o igual que otro valor.

        Parámetros:
            other: El valor a comparar con el complejo actual.

        Retorna:
            True si el complejo actual es mayor o igual que el valor dado, False en caso contrario.

        Lanza:
            TypeError: Si se intenta comparar un complejo con un tipo diferente a complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return self > other or self == other
            case int(_):
                return self > Complejo(other, 0) or self == Complejo(other, 0)
            case float(_):
                return self > Complejo(other, 0) or self == Complejo(other, 0)
            case _:
                raise TypeError("No se puede comparar un complejo con un tipo diferente a complejo, int o float")
    
    def __le__(self, other):
        """
        Compara si el complejo actual es menor o igual que otro valor.

        Parámetros:
            other: El valor con el que se compara el complejo actual.

        Retorna:
            bool: True si el complejo actual es menor o igual que el valor dado, False en caso contrario.

        Lanza:
            TypeError: Si se intenta comparar un complejo con un tipo diferente a complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return self < other or self == other
            case int(_):
                return self < Complejo(other, 0) or self == Complejo(other, 0)
            case float(_):
                return self < Complejo(other, 0) or self == Complejo(other, 0)
            case _:
                raise TypeError("No se puede comparar un complejo con un tipo diferente a complejo, int o float")
    
    def __ne__(self, other):
        """
        Compara si el complejo actual es diferente al otro valor.

        Parámetros:
            other: El valor a comparar con el complejo actual.

        Retorna:
            True si el complejo actual es diferente a `other`, False en caso contrario.

        Lanza:
            TypeError: Si `other` no es de tipo Complejo, int o float.
        """
        return not self == other

        # match other:
        #     case Complejo(_, _):
        #         return not self == other
        #     case int(_):
        #         return not self == Complejo(other, 0)
        #     case float(_):
        #         return not self == Complejo(other, 0)
        #     case _:
        #         raise TypeError("No se puede comparar un complejo con un tipo diferente a complejo, int o float")
    
    def __radd__(self, other):
        """
        Realiza la suma inversa entre un número complejo y otro objeto.

        Este método permite la suma de un objeto Complejo con otro objeto, 
        donde el objeto Complejo es el segundo operando.

        Parámetros:
        - other: El otro objeto que se va a sumar con el objeto Complejo.

        Retorna:
        - El resultado de la suma entre el objeto Complejo y el otro objeto.

        Ejemplo:
        c1 = Complejo(2, 3)
        c2 = 5
        resultado = c2 + c1  # Llama a __radd__ de c1
        print(resultado)  # Salida: (7+3i)
        """
        return self + other
    
    def __rsub__(self, other):
        """
        Realiza la resta inversa entre un número complejo y otro objeto.

        Este método permite la resta de un objeto Complejo con otro objeto, 
        donde el objeto Complejo es el segundo operando.

        Parámetros:
            other: El objeto con el que se va a realizar la resta.

        Retorna:
            Un nuevo objeto Complejo que representa la resta entre el número complejo y el otro objeto.

        Lanza:
            TypeError: Si el otro objeto no es de tipo Complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return self.operacion(other, lambda x, y: (y.real - x.real, y.imaginario - x.imaginario))
            case int(_):
                return self.operacion(other, lambda x, y: (y - x.real, -x.imaginario))
            case float(_):
                return self.operacion(other, lambda x, y: (y - x.real, -x.imaginario))
            case _:
                raise TypeError("No se puede restar un complejo con un tipo diferente a complejo, int o float")
    
    def __rmul__(self, other):
        """
        Realiza la multiplicacion inversa entre un número complejo y otro objeto.

        Este método permite la multiplicacion de un objeto Complejo con otro objeto, 
        donde el objeto Complejo es el segundo operando.

        Parámetros:
        other (Complejo): El número complejo con el que se va a multiplicar.

        Retorna:
        Complejo: El resultado de la multiplicación.
        """
        return self * other
    
    def __rtruediv__(self, other):
        """
        Realiza la división inversa entre un número complejo y otro objeto.

        Este método permite la division de un objeto Complejo con otro objeto, 
        donde el objeto Complejo es el segundo operando.

        Parámetros:
            other: El objeto con el que se realizará la división.

        Retorna:
            El resultado de la división inversa.

        Lanza:
            TypeError: Si se intenta dividir un número complejo con un tipo de objeto diferente a complejo, int o float.
        """
        match other:
            case Complejo(_, _):
                return self.operacion(other, lambda x, y: (((y.real * x.real) + (y.imaginario * x.imaginario)) / ((x.real ** 2) + (x.imaginario ** 2)), ((y.imaginario * x.real) - (y.real * x.imaginario)) / ((x.real ** 2) + (x.imaginario ** 2))))
            case int(_):
                return self.operacion(other, lambda x, y: (((y * x.real) + (0 * x.imaginario)) / ((x.real ** 2) + (x.imaginario ** 2)), ((0 * x.real) - (y * x.imaginario)) / ((x.real ** 2) + (x.imaginario ** 2))))
            case float(_):
                return self.operacion(other, lambda x, y: (((y * x.real) + (0 * x.imaginario)) / ((x.real ** 2) + (x.imaginario ** 2)), ((0 * x.real) - (y * x.imaginario)) / ((x.real ** 2) + (x.imaginario ** 2))))
            case _:
                raise TypeError("No se puede dividir un complejo con un tipo diferente a complejo, int o float")
    

    def conjugado(self):
        """
        Devuelve el conjugado del número complejo.

        Retorna:
            Complejo: El número complejo conjugado.
        """
        return Complejo(self.real, -self.imaginario)
    
    def fase(self):
        """
        Calcula la fase del número complejo.

        Retorna el ángulo en radianes entre el número complejo y el eje real positivo.

        Retorna:
            float: El ángulo en radianes.
        """
        return math.atan(self.imaginario / self.real)
    
    def inverso(self):
        """
        Calcula el inverso del número complejo.

        Retorna:
            float: El inverso del número complejo.
        """
        return self.conjugado() / (self.real ** 2 + self.imaginario ** 2)
    

    # si la cantidad de - es 2, entonces ambos numeros son negativos
    # si la cantidad de - es 1 y hay un +, entonces el primer numero es negativo
    # si la cantidad de - es 1 y no hay un +, entonces el segundo numero es negativo
    # si la cantidad de - es 0, entonces ambos numeros son positivos
    @classmethod
    def from_string(cls, string):
        """
        Crea una instancia de la clase Complejo a partir de una cadena de texto.

        Parámetros:
            string (str): La cadena de texto que representa el número complejo.

        Retorna:
            Complejo: Una instancia de la clase Complejo.

        Lanza:
            None
        """
        string = string.replace(' ', '')
        cantidad_de_menos = string.count('-')
        if string.find('i') != -1:
            match cantidad_de_menos:
                case 2:
                    string = string.split('-')
                    img = string[2].replace('i', '')
                    img = -1 if img == '' else -float(img)
                    return cls(-float(string[1]), img)
                case 1:
                    if string.find('+') != -1:
                        string = string.split('+')
                        img = string[1].replace('i', '')
                        img = 1 if img == '' else float(img)
                        return cls(float(string[0]), img)
                    else:
                        string = string.split('-')
                        img = string[1].replace('i', '')
                        img = -1 if img == '' else -float(img)
                        if string[0] == '':
                            return cls(0, img)
                        else:
                            return cls(float(string[0]), img)
                case 0:
                    if string.find('+') != -1:
                        string = string.split('+')
                        if len(string) == 2:
                            img = string[1].replace('i', '')
                            img = 1 if img == '' else float(img)
                            return cls(float(string[0]), img)
                        else:
                            img = string[0].replace('i', '')
                            img = 1 if img == '' else float(img)
                            return cls(0, img)
                    else:
                        img = string.replace('i', '')
                        img = 1 if img == '' else float(img)
                        return cls(0, img)
        else:
            return cls(float(string), 0)
        
    def convertir_numero(self, valor):
        """
        Metodo auxiliar para convertir un valor en entero si es un float con parte decimal cero,
        de lo contrario devuelve el valor original.
        
        Parámetros:
            valor (int or float): El valor a convertir.
        
        Retorna:
            int or float: El valor convertido o el valor original.
        
        Lanza:
            None
        """
        if isinstance(valor, int):
            # Si el valor ya es un entero, devolverlo como está
            return valor
        elif isinstance(valor, float):
            # Si el valor es un float y su parte decimal es cero, convertir a entero
            if valor.is_integer():
                return int(valor)
            else:
                # Si la parte decimal no es cero, devolver el float original
                return valor
        else:
            # Si el valor no es ni int ni float, imprimir un mensaje de error o manejarlo según sea necesario
            print("Error: El valor no es ni int ni float")