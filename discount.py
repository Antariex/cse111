import datetime

def get_day_of_week():
    # Obtener el día de la semana actual del sistema operativo
    today = datetime.datetime.now().strftime("%A")
    return today

def calculate_discount(subtotal, day_of_week):
    # Verificar si hoy es martes o miércoles y el subtotal es de al menos $50
    if (day_of_week == "Tuesday" or day_of_week == "Wednesday") and subtotal >= 50:
        discount = subtotal * 0.10
        return round(discount)
    else:
        return 0

def main():
    day_of_week = get_day_of_week()
    subtotal = float(input("Por favor, introduce el subtotal: $"))

    discount = calculate_discount(subtotal, day_of_week)
    sales_tax = 0.06
    total_amount_due = subtotal - discount
    total_with_taxes = total_amount_due + sales_tax 

    if discount > 0:
        print(f"Descuento aplicado: %{discount:.2f}")

    print(f"Monto de impuestos: ${sales_tax:.2f}")
    print(f"Total: ${total_with_taxes:.2f}")

if __name__ == "__main__":
    main()
