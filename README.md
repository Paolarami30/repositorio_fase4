Descripción

Software FJ es un sistema desarrollado en Python que permite gestionar reservas de salas, alquiler de equipos tecnológicos y contratación de asesorías especializadas.

El proyecto está enfocado en la aplicación de Programación Orientada a Objetos (POO), manejo de excepciones personalizadas y registro de eventos mediante logs.

Funcionalidades
Registro de clientes.
Reserva de salas de juntas.
Alquiler de equipos tecnológicos.
Contratación de asesorías especializadas.
Cálculo automático de costos según el servicio.
Validación de datos de entrada.
Manejo de errores con excepciones personalizadas.
Registro de eventos y errores en archivo de logs.
Simulación de múltiples operaciones de reserva.
Tecnologías utilizadas
Python 3
Librería logging
Programación Orientada a Objetos (POO)
Clases Abstractas (ABC)
Estructura del sistema
Clase Cliente

Representa la información de los clientes.

Atributos privados:

__id
__nombre

Método principal:

obtener_detalles()
Clase abstracta Servicio

Define el comportamiento base de los servicios.

Método abstracto:

calcular_costo()
Tipos de servicios

ReservaSala:

Calcula el costo según horas de uso.
Validación: horas mayores a cero.

AlquilerEquipo:

Calcula costo por días de alquiler.
Permite descuentos opcionales.
Validación: días mayores a cero.

AsesoriaEspecializada:

Aplica recargo del 15 por ciento sobre el costo base.
Clase Reserva

Integra cliente y servicio.

Funciones:

Procesar reservas.
Registrar eventos exitosos.
Manejar errores.
Mantener continuidad del sistema.
Conceptos de Programación Orientada a Objetos

Encapsulación:

Uso de atributos privados en Cliente (__id, __nombre)

Abstracción:

Clases abstractas EntidadBase y Servicio

Herencia:

ReservaSala
AlquilerEquipo
AsesoriaEspecializada

Polimorfismo:

Cada servicio implementa calcular_costo de forma diferente
Manejo de excepciones

Excepciones personalizadas:

SoftwareFJError
ReservaInvalidaError

Ejemplos:

Horas negativas
Días de alquiler inválidos
Registro de eventos

Se utiliza logging para registrar:

Reservas exitosas
Errores de validación
Errores inesperados

Archivo generado:

sistema_errores.log
Simulación del sistema

El sistema ejecuta 10 operaciones de prueba:

Casos exitosos
Casos con errores controlados
Validación de excepciones
Continuidad del sistema
Ejecución del proyecto
Clonar el repositorio
git clone <URL-del-repositorio>
Entrar a la carpeta
cd nombre-del-proyecto
Ejecutar el programa
python sistemaSoftwareFJ.py
Resultados esperados
Reservas exitosas
Mensajes de error controlados
Alertas por datos inválidos
Registro automático en logs
Autor

Ana Paola Ramírez Fernández
Proyecto desarrollado en Python para demostrar la aplicación de Programación Orientada a Objetos, manejo de excepciones y registro de eventos en un sistema de gestión de reservas.
