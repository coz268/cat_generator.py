import random

PREFIXES = ["Мур", "Барс", "Вась", "Рыж", "Матр"]
SUFFIXES = ["зик", "ик", "ька", "ок", "ун"]

cat_name = random.choice(PREFIXES) + random.choice(SUFFIXES)
print(cat_name)
