from pytest import approx
import pytest
from restaurant_recomender import (
    get_filtered_restaurants,
    on_choice_combobox_change,
    show_result,
    show_recommendations,
)

# Sample data for testing
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
]

def test_get_filtered_restaurants():
    result = get_filtered_restaurants(restaurants)
    assert result == restaurants

    result = get_filtered_restaurants("Pizza 🍕🥟", restaurants)
    expected_result = [restaurants[4]]
    assert result == expected_result

def test_on_choice_combobox_change():
    entry_delivery_time = "30"
    choice_combobox = "Delivery 🏍️"
    food_type_combobox = "Pizza 🍕🥟"
    price_range_combobox = "Moderate"
    result = on_choice_combobox_change(
        entry_delivery_time, choice_combobox, food_type_combobox, price_range_combobox
    )

    choice_combobox = "Dine In 🍽️"
    result = on_choice_combobox_change(
        entry_delivery_time, choice_combobox, food_type_combobox, price_range_combobox
    )

def test_show_result():
    result = show_result([], restaurants)
    assert result == "No restaurants available at the moment."

    result = show_result([restaurants[0]], restaurants)
    expected_result = 'We found 1 restaurants, the first one is Lo de Charly.'
    assert result == expected_result

def test_show_recommendations():
    result = show_recommendations([], restaurants)
    assert result == "No similar recommendations to what you are looking for."

if __name__ == '__main__':
    pytest.main()
