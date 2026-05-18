# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# main.py
# Programa principal del Sistema de Gestión de Servicios de Hotel.
# Demuestra el funcionamiento completo del sistema:
#   1. Creación de objetos de las clases hijas.
#   2. Almacenamiento en lista de la superclase (ServicioHotel).
#   3. Ejecución de métodos heredados y métodos propios.
#   4. Ejecución de los dos métodos polimórficos obligatorios.
#   5. Impresión con __str__() de cada objeto.
#   6. Demostración de validaciones del encapsulamiento.
# ─────────────────────────────────────────────────────────────────

from reserva_habitacion import ReservaHabitacion
from servicio_adicional import ServicioAdicional
from huesped import Huesped
from gestor_hotel import GestorHotel


def separador(titulo=""):
    """Función auxiliar para imprimir separadores visuales en consola."""
    linea = "=" * 50
    if titulo:
        print(f"\n{linea}")
        print(f"  {titulo.upper()}")
        print(linea)
    else:
        print(linea)


def main():
    """Función principal que ejecuta toda la demostración del sistema."""

    separador("Sistema de Gestión de Servicios de Hotel")

    # ── 1. Crear el gestor del hotel ──────────────────────────────
    # GestorHotel centraliza el manejo de huéspedes y servicios
    gestor = GestorHotel("Hotel Paraíso")

    # ── 2. Crear objetos Huesped y registrarlos ───────────────────
    # Cada Huesped aplica encapsulamiento con @property y @setter
    separador("Registro de huéspedes")

    h1 = Huesped("H001", "Ana Torres",       "0991234567", "ana.torres@email.com")
    h2 = Huesped("H002", "Carlos Vera",      "0987654321", "carlos.vera@email.com")
    h3 = Huesped("H003", "María López",      "0976543210", "maria.lopez@email.com")

    gestor.registrar_huesped(h1)
    gestor.registrar_huesped(h2)
    gestor.registrar_huesped(h3)

    # ── 3. Crear objetos de las clases hijas ──────────────────────
    # ReservaHabitacion y ServicioAdicional heredan de ServicioHotel
    separador("Creación de servicios")

    # ReservaHabitacion — 3 noches, sin descuento
    r1 = ReservaHabitacion(
        codigo="RES001",
        descripcion="Habitación simple para Ana Torres",
        precio_por_noche=85.00,
        numero_noches=3,          # int() se aplica en el setter
        tipo_habitacion="simple"
    )

    # ReservaHabitacion — 8 noches, con descuento del 10% (>= 7 noches)
    r2 = ReservaHabitacion(
        codigo="RES002",
        descripcion="Suite para Carlos Vera",
        precio_por_noche=250.00,
        numero_noches=8,          # supera el umbral → descuento aplicado
        tipo_habitacion="suite"
    )

    # ReservaHabitacion — 5 noches, sin descuento
    r3 = ReservaHabitacion(
        codigo="RES003",
        descripcion="Habitación doble para María López",
        precio_por_noche=130.00,
        numero_noches=5,
        tipo_habitacion="doble"
    )

    # ServicioAdicional — spa, 2 sesiones, servicio estándar
    s1 = ServicioAdicional(
        codigo="SVC001",
        descripcion="Sesión de spa relajante",
        precio_por_unidad=60.00,
        cantidad=2,
        tipo_servicio="spa",
        urgente=False             # sin recargo
    )

    # ServicioAdicional — lavandería urgente, recargo del 20%
    s2 = ServicioAdicional(
        codigo="SVC002",
        descripcion="Servicio de lavandería urgente",
        precio_por_unidad=15.00,
        cantidad=3,
        tipo_servicio="lavanderia",
        urgente=True              # recargo del 20% aplicado
    )

    # ServicioAdicional — room service, 4 pedidos, estándar
    s3 = ServicioAdicional(
        codigo="SVC003",
        descripcion="Room service desayuno ejecutivo",
        precio_por_unidad=22.50,
        cantidad=4,
        tipo_servicio="room_service",
        urgente=False
    )

    # ── 4. Guardar en lista de la superclase ServicioHotel ────────
    # POLIMORFISMO: la lista acepta objetos de distintas clases hijas
    # porque todas heredan de ServicioHotel
    servicios = [r1, r2, r3, s1, s2, s3]

    # Registrar cada servicio en el gestor
    for sv in servicios:
        gestor.agregar_servicio(sv)

    # ── 5. Imprimir objetos con __str__() ─────────────────────────
    # Cada clase tiene su propio __str__() que devuelve info compacta
    separador("Representación __str__() de cada objeto")
    for sv in servicios:
        print(sv)   # llama a __str__() del objeto correspondiente

    # ── 6. Uso de métodos heredados y propios ─────────────────────
    # Métodos propios de ReservaHabitacion (no están en la superclase)
    separador("Métodos propios: ReservaHabitacion")
    print(f"  {r1.codigo} — Noches: {r1.numero_noches} | Tipo: {r1.tipo_habitacion}")
    print(f"  {r2.codigo} — Noches: {r2.numero_noches} | Tipo: {r2.tipo_habitacion}")

    # Métodos propios de ServicioAdicional
    separador("Métodos propios: ServicioAdicional")
    print(f"  {s1.codigo} — Tipo: {s1.tipo_servicio} | Urgente: {s1.urgente}")
    print(f"  {s2.codigo} — Tipo: {s2.tipo_servicio} | Urgente: {s2.urgente}")

    # ── 7. Métodos polimórficos obligatorios ──────────────────────

    # POLIMÓRFICO 1: calcular_costo()
    # El gestor recorre la lista y llama calcular_costo() en cada objeto
    # sin saber si es ReservaHabitacion o ServicioAdicional
    separador("POLIMORFISMO 1 — calcular_costo()")
    total_general = gestor.calcular_costo(servicios)

    # POLIMÓRFICO 2: mostrar_info()
    # El gestor recorre la lista y llama mostrar_info() en cada objeto
    # sin saber su tipo concreto — cada uno imprime su propia info
    separador("POLIMORFISMO 2 — mostrar_info()")
    gestor.mostrar_info(servicios)

    # ── 8. Reporte completo de huéspedes ──────────────────────────
    separador("Reporte de huéspedes registrados")
    gestor.listar_huespedes()

    # ── 9. Demostración de validaciones del encapsulamiento ───────
    # Se intenta crear objetos con datos inválidos para demostrar
    # que los @setter capturan el error antes de asignar el valor
    separador("Demostración de validaciones (@setter)")

    pruebas = [
        ("Precio negativo en ReservaHabitacion",
         lambda: ReservaHabitacion("X", "Test", -100, 2, "simple")),
        ("Cero noches en ReservaHabitacion",
         lambda: ReservaHabitacion("X", "Test", 100, 0, "simple")),
        ("Tipo habitación inválido",
         lambda: ReservaHabitacion("X", "Test", 100, 2, "presidencial")),
        ("Código vacío en ServicioAdicional",
         lambda: ServicioAdicional("", "Test", 50, 1, "spa")),
        ("Email inválido en Huésped",
         lambda: Huesped("H99", "Test", "0000", "correo_sin_arroba")),
    ]

    for descripcion, prueba in pruebas:
        try:
            prueba()
            print(f"  ✘ [{descripcion}]: No se lanzó error (inesperado).")
        except ValueError as e:
            # El @setter capturó el error correctamente
            print(f"  ✔ [{descripcion}]: Error capturado → {e}")

    # ── 10. Resumen final ─────────────────────────────────────────
    separador("FIN DEL PROGRAMA")
    print(f"\n  Total facturado al hotel: ${total_general:.2f}")
    print()


# Punto de entrada del programa
if __name__ == "__main__":
    main()
