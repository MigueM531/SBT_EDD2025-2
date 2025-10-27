# SBT_EDD2025-2

# Sistema de asignación de quirófanos para cirugías de emergencia

---

## Restricciones Técnicas

Únicamente se pueden utilizar la clase de árboles binarios que fue construida en clase, que es un nodo con enlace a hijo izquierdo y derecho.  
**No utilizar la clase base que utiliza una lista.**

El uso de otra clase base afectará la nota en **–2 unidades**.  
**No se permite documentación sobre el código, de ningún tipo.**

Para esta práctica, **está prohibido el uso de estructuras auxiliares** como listas, pilas u otros contenedores preconstruidos.  
**Excepción:** colas si se va a utilizar para recorrido *level order*, únicamente en este caso y debe ser con la clase base de colas construida en clase.

La implementación debe trabajar únicamente sobre nodos enlazados, utilizando punteros a hijos para todas las operaciones, y opcionalmente al padre.

Presentar la práctica sobre otra colección no cumple con lo solicitado, por lo que la nota será **0**.

La práctica debe cumplir con la totalidad de los puntos solicitados; cada punto que no se presente disminuirá la nota en **1 punto**.

El entregable de la práctica debe estar de modo tal que, con la ejecución del código, se ejecute de forma autónoma cada uno de los puntos.  
No cumplir con este punto afectará la nota en **–2 unidades.**

---

## Descripción

Diseñar e implementar un sistema que administre la asignación de quirófanos para pacientes que requieren cirugía de emergencia en un hospital.

Cada paciente tiene un nivel de emergencia asociado (**1 a 5**, donde **1 = máxima prioridad**).  
El sistema debe atender primero a los pacientes más urgentes y, en caso de empate en el nivel de emergencia, respetar el orden de llegada.

---

## Requerimientos

El sistema debe implementar un **Heap binario mínimo** utilizando nodos enlazados con los atributos:

- `valor`
- `hijo_izquierdo`
- `hijo_derecho`
- `padre` *(este último solo si se requiere para facilitar operaciones)*

---

### Cada paciente tendrá:

- **id único** (entero o string)  
- **nombre o codigo_paciente** (string)  
- **nivel_emergencia** (entero 1..5, donde 1 = máxima prioridad)  
- **timestamp_llegada** o **orden_llegada** (enteros crecientes o marca de tiempo) — se usará para desempatar  

---

### Implementar las siguientes operaciones

#### 1. Registrar paciente
- Inserta un nuevo paciente en el heap respetando la prioridad por `nivel_emergencia` y luego por `orden_llegada`.
- Después de una inserción se debe garantizar que la raíz siempre sea el paciente con menor nivel de emergencia y, en caso de empate, el de llegada más temprana.

#### 2. Consultar siguiente paciente para quirófano
- Devuelve (sin extraer) el paciente con mayor prioridad (raíz del heap).

#### 3. Programar (realizar) cirugía — sacar siguiente
- Extrae la raíz del heap (paciente con mayor prioridad) y reestructura el heap correctamente, manteniendo las prioridades.
- Después de una eliminación se debe garantizar que la raíz siempre sea el paciente con menor nivel de emergencia y, en caso de empate, el de llegada más temprana.

#### 4. Ver lista general de pacientes en espera
- Debe permitir visualizar todos los pacientes actualmente almacenados en el heap, mostrando:
  - `id`
  - `nombre`
  - `nivel_emergencia`
  - `orden_llegada`
- El orden de presentación debe ser el orden interno del heap.

#### 5. Ver lista de pacientes por nivel de emergencia
- Dado un `nivel_emergencia` (1..5), devuelve todos los pacientes con ese nivel.

---

## Entrega y sustentación

- La fecha de entrega y sustentación es:
  - **30 de octubre** durante clase (*grupo martes y jueves*), o  
  - **31 de octubre** durante clase (*grupo miércoles y viernes*).

> **TODOS SIN EXCEPCIÓN DEBEN ASISTIR ESTE DÍA.**
> Si no asisten, la nota de la sustentación será **0 (de 4 puntos posibles).**

La práctica debe ser enviada a más tardar el **29 o 30 de octubre** (dependiendo del grupo).

Se pueden hacer **solos o en parejas**, teniendo en cuenta que la sustentación será **práctica y oral, e individual**.

---

## Detalle de las notas

- **Implementación:** 20%  
- **Sustentación práctica:** 40%  
  - Se realizará de **6:00 a 6:40 a.m.** el día de entrega.  
- **Sustentación oral:** 40%  
  - A partir de las **6:40 a.m.**, ese día se indicará el orden de sustentación.

---

Tener en cuenta las **restricciones de la práctica** que pueden afectar la nota.

---

### Resumen de secciones

- **Descripción**  
- **Requerimientos**  
- **Entrega y sustentación**
