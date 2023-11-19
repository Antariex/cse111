import csv
from datetime import datetime

def read_dictionary(filename, key_column_index=0):
    compound_dict = {}
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            product_number = row[0]
            product_name = row[1]
            product_price = row[2]
            compound_dict[product_number] = (product_number, product_name, product_price)
    return compound_dict

def main():
    
    try:
        products_dict = read_dictionary("products.csv")

        with open("request.csv", 'rt') as request_file:
            reader = csv.reader(request_file)
            next(reader)

            ordered_items = []
            total_quantity = 0
            subtotal_due = 0.0

            for row_list in reader:
                product_number = row_list[0]
                quantity = int(row_list[1])

                if product_number in products_dict:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])

                    ordered_items.append((product_name, quantity, product_price))
                    total_quantity += quantity
                    subtotal_due += quantity * product_price

                else:
                    print(f"Product with number {product_number} not found in the dictionary.\n")

        sales_tax_rate = 0.06
        sales_tax_amount = subtotal_due * sales_tax_rate
        total_amount_due = subtotal_due + sales_tax_amount

        print("Inkom Emporium\n")
        for item in ordered_items:
            print(f"{item[0]}, {item[1]}, {item[2]}")
        print("\nNumber of Items:", total_quantity)
        print(f"Subtotal: {subtotal_due:.2f}")
        print(f"Sales Tax: {sales_tax_amount:.2f}")
        print(f"Total: {total_amount_due: .2f}")
        print("\nThank you for shopping at the Inkom Emporium.")
        current_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        print(current_datetime)
        print("\nWe value your feedback! Please take a moment to complete an online survey at: www.inkomemporium.com/survey")
        
    except FileNotFoundError:
        print("Error: missing file. One or more files not found.")
    except KeyError as e:
        print(f"Error: Key {e} not found in the dictionary.")

if __name__ == "__main__":
    main()