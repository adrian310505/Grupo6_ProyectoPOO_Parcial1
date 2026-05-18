# Grupo6_ProyectoPOO_Parcial1
# 🏨 Sistema de Gestión de Servicios de Hotel
### Proyecto Primer Parcial — Programación Orientada a Objetos | Grupo 6

---

## 📋 Descripción

Sistema desarrollado en Python que gestiona los servicios de un hotel.
Permite registrar huéspedes, crear reservas de habitaciones y servicios adicionales,
calcular costos y generar reportes completos aplicando los principios de POO.

---

## 🗂️ Estructura del repositorio

```
ProyectoPOO_Parcial1/
│── servicio_hotel.py        ← Superclase base
│── reserva_habitacion.py    ← Clase hija: Reserva de habitación
│── servicio_adicional.py    ← Clase hija: Servicio adicional
│── huesped.py               ← Clase adicional: Huésped
│── gestor_hotel.py          ← Clase adicional: Gestor con métodos polimórficos
│── main.py                  ← Programa principal
└── README.md
```

---

## 📐 Diagrama de clases

```
ServicioHotel  (superclase)
├── codigo          : str   (privado, @property)
├── descripcion     : str   (privado, @property)
├── precio_base     : float (privado, @property)
├── calcular_costo()         ← método polimórfico 1
└── mostrar_info()           ← método polimórfico 2

        ┌──────────────────────────┐
        │                          │
ReservaHabitacion          ServicioAdicional
├── numero_noches              ├── cantidad
├── tipo_habitacion            ├── tipo_servicio
├── calcular_costo()           ├── urgente
└── mostrar_info()             ├── calcular_costo()
                               └── mostrar_info()

Huesped
├── id_huesped
├── nombre
├── telefono
└── email

GestorHotel
├── registrar_huesped()
├── agregar_servicio()
├── calcular_costo()    ← polimórfico 1 (recorre lista heterogénea)
├── mostrar_info()      ← polimórfico 2 (recorre lista heterogénea)
└── generar_reporte_completo()
```

---

## ✅ Requisitos de POO cumplidos

| Requisito | Detalle |
|---|---|
| **5 clases** | `ServicioHotel`, `ReservaHabitacion`, `ServicioAdicional`, `Huesped`, `GestorHotel` |
| **Encapsulamiento** | Todos los atributos son privados (`_attr`), acceso con `@property` y `@setter` con validaciones |
| **Herencia** | `ReservaHabitacion` y `ServicioAdicional` heredan de `ServicioHotel` |
| **Polimorfismo** | `calcular_costo()` y `mostrar_info()` operan sobre lista heterogénea sin `isinstance` |
| **`__str__()`** | Implementado en todas las clases |

---

## 💡 Reglas de negocio implementadas

**ReservaHabitacion:**
- Costo = noches × precio por noche
- Si la estadía es ≥ 7 noches → 10 % de descuento automático
- Tipos válidos: `simple`, `doble`, `suite`

**ServicioAdicional:**
- Costo = cantidad × precio por unidad
- Si es urgente → recargo del 20 %
- Tipos válidos: `spa`, `lavanderia`, `room_service`, `transporte`, `tours`, `otro`

---

## ▶️ Instrucciones para ejecutar

1. Clonar el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd ProyectoPOO_Parcial1
   ```
2. Ejecutar el programa (requiere Python 3.10+):
   ```bash
   python main.py
   ```
3. No se necesitan librerías externas.

---

## 📸 Evidencias de ejecución

Captura de pantalla de la ejecución del programa en PyCharm.
Se puede verificar la consola con la salida completa del sistema, incluyendo el total facturado de **$2969.00**, la fecha y hora del sistema visibles en la barra inferior (**17/05/2026 — 20:29**).

[📸 Ver captura de ejecución](https://drive.google.com/file/d/1Hj4h-cgs7mXTsmPk1fu7c8vAta28NP-e/view?usp=drivesdk)

---

## 🎬 Video explicativo

🔗 [Ver video explicativo aquí](https://drive.google.com/file/d/1vCSGdARQrBkKbH1xhqFEBdCe3oPxU1QH/view?usp=drivesdk)

> El video explica las clases creadas, herencia, encapsulamiento, polimorfismo y ejecución final del sistema.

---

## 👥 Integrantes

- Luna Henry
- Sánchez Adrian
- Merchán Evelyn
- Veintimilla Alejandra
- Rodríguez Nayeli
