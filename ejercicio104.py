# Exercise 104
"""
The following dictionary:
stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
save to stocks.json using the json package. Set the indent to 4.
File stocks.json after saving:
{
    "PLW": [
        "Playway",
        350
    ],
    "BBT": [
        "Boombit",
        22
    ]
}
"""
import json


stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json', 'w', encoding='utf-8') as file:
    json.dump(stocks, file, indent=4)
