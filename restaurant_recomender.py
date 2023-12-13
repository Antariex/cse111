from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes

# List of restaurant options
restaurants = [
    {
        "name": "Lo de Charly",
        "type": "Barbecue 🥩🥓",
        "price_range": "Moderate",
        "payment_methods": ["Cash", "Credit Card", "Debit Card"],
        "delivery_time_minutes": 40,
        "opening_hour": 0,
        "closing_hour": 24,
        "neighborhood": "Villa Ortuzar",
        "address": "Av. Álvarez Thomas 2101, CABA",
    },
    {
        "name": "La Mezzeta",
        "type": "Pizza 🍕🥟",
        "price_range": "Affordable",
        "payment_methods": ["Cash", "Credit Card", "Debit Card"],
        "delivery_time_minutes": 25,
        "opening_hour": 11,
        "closing_hour": 24,
        "neighborhood": "Villa Ortuzar",
        "address": "Av. Álvarez Thomas 1321, CABA",
    },
    {
        "name": "La Conga",
        "type": "Peruvian and Latin Food 🍗🐟",
        "price_range": "Moderate",
        "payment_methods": ["Cash", "Credit Card", "Debit Card"],
        "delivery_time_minutes": 50,
        "opening_hour": 12,
        "closing_hour": 24,
        "neighborhood": "Balvanera",
        "address": "La Rioja 39, CABA",
    },
    {
        "name": "El Antojo",
        "type": "Argentine homestyle food 🥩🍟",
        "price_range": "Expensive",
        "payment_methods": ["Cash", "Debit Card"],
        "delivery_time_minutes": 40,
        "opening_hour": 12,
        "closing_hour": 23,
        "neighborhood": "Villa del Parque",
        "address": "Tinogasta 3174, CABA",
    },
    {
        "name": "Mostaza",
        "type": "Fast Food 🍔🍟",
        "price_range": "Moderate",
        "payment_methods": ["Cash", "Debit Card", "Credit Card"],
        "delivery_time_minutes": 30,
        "opening_hour": 8,
        "closing_hour": 24,
        "neighborhood": "Palermo",
        "address": "Av. Santa Fe 3253, CABA",
    },
    {
        "name": "Sigue la Vaca",
        "type": "Barbecue and Buffet 🥩🍗",
        "price_range": "Expensive",
        "payment_methods": ["Cash", "Debit Card", "Credit Card"],
        "delivery_time_minutes": "Not available",
        "opening_hour": 12,
        "closing_hour": 24,
        "neighborhood": "Puerto Madero",
        "address": "Av. Alicia Moreau de Justo 1714, CABA",
    },
    {
        "name": "Shawarma Al-Arabe",
        "type": "Arabian Food 🥙🥗",
        "price_range": "Moderate",
        "payment_methods": ["Cash", "Debit Card"],
        "delivery_time_minutes": 25,
        "opening_hour": 12,
        "closing_hour": 24,
        "neighborhood": "Recoleta",
        "address": "Rodríguez Peña 1579, CABA",
    },
]


# Function to get filtered restaurants based on food type
def get_filtered_restaurants(selected_food_type):
    if not selected_food_type:
        return restaurants
    return [
        restaurant
        for restaurant in restaurants
        if restaurant.get("type", "") == selected_food_type
    ]


# Function to handle choice combobox change event
def on_choice_combobox_change(event):
    choice = choice_combobox.get()
    if choice == "Delivery":
        delivery_time_max = int(entry_delivery_time.get())
        selected_food_type = food_type_combobox.get()
        selected_price_range = price_range_combobox.get()
        filtered_restaurants = get_filtered_restaurants(selected_food_type)
        show_result(filtered_restaurants)
    elif choice == "Dine In":
        pass


# Function to show the result in a messagebox
def show_result(filtered_restaurants):
    if not filtered_restaurants:
        result = "No restaurants available at the moment."
    else:
        result = f'We found {len(filtered_restaurants)} restaurants, the first one is {filtered_restaurants[0]["name"]}.'
    messagebox.showinfo("Restaurant Recommender", result)


# Function to show recommendations based on user choices
def show_recommendations():
    selected_food_type = food_type_combobox.get()
    filtered_restaurants = get_filtered_restaurants(selected_food_type)

    # Sort restaurants by delivery time and get the top recommendation
    sorted_restaurants = sorted(
        filtered_restaurants, key=lambda x: x["delivery_time_minutes"]
    )
    top_recommendations = sorted_restaurants[:1]

    # Display the recommendations
    if not top_recommendations:
        result = "No similar recommendations to what you are looking for."
    else:
        recommendations = "\n".join(
            [
                f"\n {restaurant['name']} \n \n Type of food: {restaurant['type']} \n Payment methods: {restaurant['payment_methods']} \n "
                f"Opening hour: {restaurant['opening_hour']} A.M. \n Closing hour: {restaurant['closing_hour']} P.M. \n "
                f"Address: {restaurant['address']}"
                for restaurant in top_recommendations
            ]
        )
        result = f"Our recommended:\n{recommendations}"

    messagebox.showinfo("Restaurant Recommender", result)


# Create the main window
root = tk.Tk()
root.title("Restaurant Recommender")

# Change the theme using ThemedStyle
style = ThemedStyle(root)
style.set_theme("equilux")

# Change the background color of the entire window
root.configure(bg="#373737")

# Add a label to the window
label = tk.Label(
    root,
    text="Welcome to the Restaurant Recommender!",
    font=("Sans Serif", 14, "bold"),
    bg="#373737",
    fg="white",
)
label.pack(pady=16)

# Frame for user choice
choice_frame = tk.Frame(root, bg="#373737")
choice_frame.pack(pady=16)

# Label and entry for delivery time
label_delivery_time = tk.Label(
    choice_frame,
    text="Delivery Time (minutes):",
    font=("Sans Serif", 12),
    bg="#373737",
    fg="white",
)
label_delivery_time.grid(row=0, column=0)
entry_delivery_time = tk.Entry(choice_frame, width=5, font=("Sans Serif", 12))
entry_delivery_time.grid(row=0, column=1)

# Label and combobox for user choice
label_choice = tk.Label(
    choice_frame, text="Choose:", font=("Sans Serif", 12), bg="#373737", fg="white"
)
label_choice.grid(row=1, column=0)
choices = ["Delivery 🏍️", "Dine In 🍽️"]
choice_combobox = ttk.Combobox(choice_frame, values=choices, font=("Sans Serif", 12))
choice_combobox.set(choices[0])
choice_combobox.grid(row=1, column=1, pady=16)
choice_combobox.bind("<<ComboboxSelected>>", on_choice_combobox_change)

# Label and combobox for food type
label_food_type = tk.Label(
    choice_frame, text="Food Type:", font=("Sans Serif", 12), bg="#373737", fg="white"
)
label_food_type.grid(row=2, column=0)
food_types = set(restaurant["type"] for restaurant in restaurants)
default_food_type = (
    food_types.pop() if food_types else ""
)
food_type_combobox = ttk.Combobox(
    choice_frame, values=list(food_types), font=("Sans Serif", 12)
)
food_type_combobox.set(default_food_type)
food_type_combobox.grid(row=2, column=1, pady=16)

# Label and combobox for neighborhood
label_neighborhood = tk.Label(
    choice_frame,
    text="Neighborhood:",
    font=("Sans Serif", 12),
    bg="#373737",
    fg="white",
)
label_neighborhood.grid(row=3, column=0)
neighborhoods = set(restaurant["neighborhood"] for restaurant in restaurants)
neighborhood_combobox = ttk.Combobox(
    choice_frame, values=list(neighborhoods), font=("Sans Serif", 12)
)
neighborhood_combobox.set(
    neighborhoods.pop() if neighborhoods else ""
)
neighborhood_combobox.grid(row=3, column=1, pady=16)

# Label and combobox for price range
label_price_range = tk.Label(
    choice_frame, text="Price Range:", font=("Sans Serif", 12), bg="#373737", fg="white"
)
label_price_range.grid(row=4, column=0)
price_ranges = set(restaurant["price_range"] for restaurant in restaurants)
price_range_combobox = ttk.Combobox(
    choice_frame, values=list(price_ranges), font=("Sans Serif", 12)
)
price_range_combobox.set(
    price_ranges.pop() if price_ranges else ""
)
price_range_combobox.grid(row=4, column=1, pady=16)

# Button to show recommendations
show_recommendations_button = ttk.Button(
    root, text="Show Me the Recommendation", command=show_recommendations
)
show_recommendations_button.pack(pady=10)


# Start the Tkinter event loop
root.mainloop()
