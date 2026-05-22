# Software FJ - Sistema de Gestión de Reservas


## Funcionalidades

- Registro de clientes.
- Reserva de salas de juntas.
- Alquiler de equipos tecnológicos.
- Contratación de asesorías especializadas.
- Cálculo automático de costos según el servicio solicitado.
- Validación de datos de entrada.
- Manejo de errores mediante excepciones personalizadas.
- Registro de eventos y errores en archivo de logs.
- Simulación de múltiples operaciones de reserva.

---

## Tecnologías Utilizadas

- Python 3
- Librería logging
- Programación Orientada a Objetos (POO)
- Clases Abstractas (ABC)

---

## Estructura del Sistema

### Clase Cliente

Representa la información de los clientes del sistema.

Características:

- Encapsulación mediante atributos privados:
  - `__id`
  - `__nombre`

Método principal:

- `obtener_detalles()`

---

### Clase Servicio

Clase abstracta que define el comportamiento general de todos los servicios.

Método abstracto:

```python
calcular_costo()
```

Las siguientes clases heredan de Servicio:

- ReservaSala
- AlquilerEquipo
- AsesoriaEspecializada

---

### ReservaSala

Permite calcular el costo de una reserva de sala según las horas solicitadas.

Validaciones:

- Las horas deben ser mayores a cero.

---

### AlquilerEquipo

Permite calcular el costo de alquiler de equipos tecnológicos.

Características:

- Soporta descuentos opcionales.
- Valida que los días de alquiler sean mayores a cero.

---

### AsesoriaEspecializada

Calcula el costo de asesorías especializadas aplicando un recargo del 15%.

---

### Clase Reserva

Integra la información del cliente y del servicio.

Funciones:

- Procesar reservas.
- Registrar eventos exitosos.
- Gestionar errores.
- Mantener la continuidad del sistema ante fallos.

---

## Conceptos de Programación Orientada a Objetos Implementados

### Encapsulación

Implementada en la clase Cliente mediante atributos privados.

```python
self.__id
self.__nombre
```

---

### Abstracción

Implementada mediante las clases abstractas:

- EntidadBase
- Servicio

---

### Herencia

Las clases:

- ReservaSala
- AlquilerEquipo
- AsesoriaEspecializada

heredan de la clase Servicio.

---

### Polimorfismo

Cada servicio implementa su propia versión del método:

```python
calcular_costo()
```

permitiendo diferentes comportamientos según el tipo de servicio.

---

## Manejo de Excepciones

El sistema utiliza excepciones personalizadas para controlar errores de negocio.

### Excepciones implementadas

```python
SoftwareFJError
ReservaInvalidaError
```

Ejemplos:

- Horas negativas en una reserva.
- Días de alquiler iguales o menores a cero.

---

## Registro de Eventos (Logs)

Se utiliza la librería logging para registrar:

- Reservas exitosas.
- Errores de validación.
- Errores inesperados.

Archivo generado:

```text
sistema_errores.log
```

---

## Simulación de Operaciones

El sistema ejecuta 10 operaciones de prueba que incluyen:

- Casos exitosos.
- Casos con errores controlados.
- Validación del funcionamiento de las excepciones.
- Continuidad operativa del sistema.

---

## Ejecución del Proyecto

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python sistemaSoftwareFJ.py
```

---

## Resultados Esperados

Durante la ejecución se mostrarán:

- Reservas exitosas.
- Alertas por datos inválidos.
- Mensajes de finalización de procesos.
- Registro automático de eventos en el archivo de logs.

---

## Autor

Ana Paola Ramírez Fernandez 

Proyecto académico desarrollado en Python que implementa los principios de la Programación Orientada a Objetos, el manejo de excepciones y el registro de eventos, con el propósito de gestionar reservas de manera eficiente, segura y organizada.
