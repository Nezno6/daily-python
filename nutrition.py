def get_calories(fruit: str):
    fruit_calories = {
"apple": 130,
"banana": 105,
"grapes": 52,
"orange": 80,
"strawberry": 50,
"grapefruit": 60,
"apple": 130,
"banana": 105,
"grapes": 52,
"orange": 80,
"strawberry": 50,
"grapefruit": 60
}
    ask = fruit.lower().strip()
    if fruit_calories.__contains__(ask):
        return fruit_calories[ask]