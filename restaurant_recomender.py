from datetime import datetime

restaurants = [
    {
        'name': 'Silver Rice Sushi 🍣',
        'priceBracket': '2',
        'deliveryTimeMinutes': 40,
        'openHour': '12',
        'closeHour': '23',
        'distance': '5',
    },
    {
        'name': 'Nikko\'s Rotisserie Chicken 🍗',
        'priceBracket': '1',
        'deliveryTimeMinutes': 20,
        'openHour': '12',
        'closeHour': '21',
        'distance': '8',
    },
    {
        'name': 'Aita Trattoria 🍝',
        'priceBracket': '3',
        'deliveryTimeMinutes': 60,
        'openHour': '18',
        'closeHour': '22',
        'distance': '1',
    },
    {
        'name': 'Lula Bagel 🥯',
        'priceBracket': '1',
        'deliveryTimeMinutes': 20,
        'openHour': '0',
        'closeHour': '12',
        'distance': '2',
    },
    {
        'name': 'Golden Chopstick 🥢',
        'priceBracket': '1',
        'deliveryTimeMinutes': 20,
        'openHour': '15',
        'closeHour': '23',
        'distance': '12',
    },
]

hour = datetime.now().hour
dollar_signs = '$$'
delivery_time_max = int(input('Enter an expected delivery time from 10 to 90 minutes: '))
max_distance = int(input('Enter a distance between the restaurant and your location: '))
result = ''

price_bracket = len(dollar_signs)

filtered_restaurants = [restaurant for restaurant in restaurants if
                        int(restaurant['priceBracket'].count('$')) <= price_bracket
                        and int(restaurant['deliveryTimeMinutes']) <= delivery_time_max
                        and int(restaurant['distance']) <= max_distance
                        and int(restaurant['openHour']) <= hour <= int(restaurant['closeHour'])]

if not filtered_restaurants:
    result = 'There are no restaurants available right now.'
else:
    result = f'We found {len(filtered_restaurants)} restaurants, the first is {filtered_restaurants[0]["name"]}.'

print(result)