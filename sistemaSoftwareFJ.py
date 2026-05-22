import logging
from abc import ABC, abstractmethod

# 1. CONFIGURACIÓN DE LOGS (Criterio de Evaluación: Registro de eventos)
logging.basicConfig(
    filename='sistema_errores.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 2. EXCEPCIONES PERSONALIZADAS (Criterio: Manejo robusto de errores)
class SoftwareFJError(Exception):
    """Clase base para errores del sistema."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se dispara cuando los datos de la reserva no son lógicos."""
    pass

# 3. CLASES BASE Y ENCAPSULAMIENTO
class EntidadBase(ABC):
    @abstractmethod
    def obtener_detalles(self):
        pass

class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre):
        self.__id = id_cliente  # Encapsulación (Atributo privado)
        self.__nombre = nombre
        
    def obtener_detalles(self):
        return f"Cliente: {self.__nombre} (ID: {self.__id})"

# 4. ABSTRACCIÓN Y HERENCIA (Clase Servicio y sus derivados)
class Servicio(ABC):
    def __init__(self, nombre_servicio, precio_base):
        self.nombre = nombre_servicio
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0: raise ReservaInvalidaError("Horas deben ser mayores a 0")
        return self.precio_base * horas

class AlquilerEquipo(Servicio):
    # Polimorfismo y Sobrecarga simulada con parámetros opcionales
    def calcular_costo(self, dias, descuento=0):
        if dias <= 0: raise ReservaInvalidaError("Días inválidos para alquiler")
        return (self.precio_base * dias) - descuento

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        # Aplica un recargo por especialidad (Polimorfismo)
        return (self.precio_base * horas) * 1.15

# 5. CLASE RESERVA (Integra todo)
class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.cantidad)
            mensaje = f"Reserva Exitosa: {self.cliente.obtener_detalles()} - {self.servicio.nombre} - Total: ${costo}"
            print(mensaje)
            logging.info(mensaje)
        except ReservaInvalidaError as e:
            # Manejo de excepciones personalizado y encadenamiento
            error_msg = f"Error en Reserva: {str(e)}"
            print(f"ALERTA: {error_msg}")
            logging.error(error_msg)
            raise SoftwareFJError("Fallo en el procesamiento de reserva") from e
        except Exception as e:
            logging.critical(f"Error inesperado: {str(e)}")
        finally:
            print("Finalizando operación de reserva...")

# 6. SIMULACIÓN DE 10 OPERACIONES (Criterio de Evaluación)
def ejecutar_simulaciones():
    print("--- INICIANDO SISTEMA DE GESTIÓN SOFTWARE FJ ---\n")
    
    # Datos de prueba
    c1 = Cliente("101", "Juan Perez")
    c2 = Cliente("102", "Maria Lopez")
    
    s1 = ReservaSala("Sala de Juntas", 50000)
    s2 = AlquilerEquipo("Portátil Core i7", 30000)
    s3 = AsesoriaEspecializada("Consultoría IT", 100000)

    operaciones = [
        (c1, s1, 3),   # 1. Válido
        (c2, s2, 2),   # 2. Válido
        (c1, s3, 5),   # 3. Válido
        (c2, s1, -1),  # 4. INVÁLIDO (Horas negativas)
        (c1, s2, 0),   # 5. INVÁLIDO (Días cero)
        (c2, s3, 10),  # 6. Válido
        (c1, s1, 2),   # 7. Válido
        (c2, s2, 4),   # 8. Válido
        (c1, s3, 1),   # 9. Válido
        (c2, s1, 0)    # 10. INVÁLIDO
    ]

    for i, (cli, serv, cant) in enumerate(operaciones, 1):
        print(f"\nOperación #{i}:")
        try:
            res = Reserva(cli, serv, cant)
            res.procesar()
        except SoftwareFJError:
            print("El sistema detectó un error pero sigue funcionando.")
        else:
            print("Operación completada sin errores técnicos.")

if __name__ == "__main__":
    ejecutar_simulaciones()