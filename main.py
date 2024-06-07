import random
from collections import defaultdict

snidanok = {
    "plastivzi": {
        "moloko": 0.2,
        "plastivzi": 0.1
    },
    "mlynzy": {
        "muka": 0.4,
        "moloko": 0.4,
        "jajzja": 2
    },
    "omlet": {
        "jajzja": 2,
        "moloko": 0.1,
        "syr": 0.2,
        "olija": 0.1,
        "perez": 0.1
    },
    "buterbrot": {
        "hlib": 0.2,
        "kovbasa": 0.3,
        "syr": 0.3,
        "maslo": 0.1
    }
}

perscha_strava = {
    "borsch": {
        "mjaso": 0.4,
        "kartoplia": 0.4,
        "morkva": 0.1,
        "zybulia": 0.1,
        "buriak": 0.1,
        "salo": 0.1,
        "perez": 0.1
    },
    "sup": {
        "mjaso": 0.4,
        "kartoplia": 0.4,
        "morkva": 0.1,
        "zybulia": 0.1,
        "gretschka": 0.1
    },
    "okroschka": {
        "mjaso": 0.3,
        "kartoplia": 0.3,
        "ogirky": 0.3,
        "zelenj": 0.2,
        "jajzja": 3,
        "smetana": 0.3
    },
    "uha": {
        "ryba": 0.4,
        "kartoplia": 0.2,
        "morkva": 0.1,
        "zybulia": 0.1,
        "spezij": 0.05
    }
}

golovna_strava = {
    "pasta_bolonjez": {
        "salo": 0.1,
        "spagetti": 0.5,
        "parmezan": 0.1,
        "olija": 0.1
    },
    "plov": {
        "mjaso": 0.4,
        "rys": 0.4,
        "morkva": 0.3,
        "zybulia": 0.3,
        "olija": 0.1
    },
    "ragu ovotscheve": {
        "mjaso": 0.3,
        "kartoplja": 0.2,
        "morkva": 0.2,
        "zybulia": 0.2,
        "olija": 0.1,
        "pomidory": 0.3
    },
    "schnizel": {
        "mjaso": 0.4,
        "kartoplja": 0.2,
        "moloko": 0.2,
        "jajzja": 2,
        "panirovka": 0.2,
        "olija": 0.3
    }
}

mama = ["salo", "perez"]
to_delete = set()

for key, value in snidanok.items():
    for sub_key in value.keys():
        if sub_key in mama:
            to_delete.add(key)

for key, value in perscha_strava.items():
    for sub_key in value.keys():
        if sub_key in mama:
            to_delete.add(key)

for key, value in golovna_strava.items():
    for sub_key in value.keys():
        if sub_key in mama:
            to_delete.add(key)

for strava in to_delete:
    if strava in snidanok:
        del snidanok[strava]
    if strava in perscha_strava:
        del perscha_strava[strava]
    if strava in golovna_strava:
        del golovna_strava[strava]

print(f"Ne gotuvaty {to_delete}")

def choose_unique_dishes(snidanok, perscha_strava, golovna_strava, days=3):
    if len(snidanok) < days or len(perscha_strava) < days or len(golovna_strava) < days:
        raise ValueError("Недостаточно блюд в одной из категорий для выбора уникальных блюд на все дни")

    snidanok_list = list(snidanok.keys())
    perscha_strava_list = list(perscha_strava.keys())
    golovna_strava_list = list(golovna_strava.keys())

    chosen_dishes = {}

    for day in range(1, days + 1):
        random.shuffle(snidanok_list)
        random.shuffle(perscha_strava_list)
        random.shuffle(golovna_strava_list)

        chosen_dishes[f"Denj {day}"] = {
            "snidanok": snidanok_list.pop(),
            "perscha_strava": perscha_strava_list.pop(),
            "golovna_strava": golovna_strava_list.pop()
        }

    return chosen_dishes

def calculate_ingredients(chosen_dishes, snidanok, perscha_strava, golovna_strava):
    total_ingredients = defaultdict(float)

    for day, meals in chosen_dishes.items():
        for meal_type, meal in meals.items():
            if meal_type == "snidanok":
                ingredients = snidanok[meal]
            elif meal_type == "perscha_strava":
                ingredients = perscha_strava[meal]
            elif meal_type == "golovna_strava":
                ingredients = golovna_strava[meal]

            for ingredient, amount in ingredients.items():
                total_ingredients[ingredient] += amount

    return total_ingredients



chosen_dishes = choose_unique_dishes(snidanok, perscha_strava, golovna_strava, days=3)


total_ingredients = calculate_ingredients(chosen_dishes, snidanok, perscha_strava, golovna_strava)

print("\n Menju na try dni:")

for day, meals in chosen_dishes.items():

    print(
        f" {day}: Snidanok - {meals['snidanok']}, Perscha strava - {meals['perscha_strava']}, Golovna strava) - {meals['golovna_strava']}")

print("\n Lyst zakupivli:")
for ingredient, amount in total_ingredients.items():
    print(f"{ingredient}: {amount} кг")
