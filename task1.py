# Задача № 1


def parse_recipes():
    """Возвращает словарь с рецептами
    берущихся из файла перечня recipes.txt"""
    with open("recipes.txt", encoding="utf-8") as file:
        # инициализация результирующего словаря
        cook_book = {}
        for line in file.read().split("\n\n"):
            # звездочка для распаковки переменной до конца строки
            meal_name, *ingredients = line.split("\n")
            # создание списка для блюд
            cook_lst = []
            # распаковка списка для формирования ключей итогового словаря
            for ingredient in ingredients[1:]:
                # дробление ингредиента на имя, кол-во и единицу по разделителю
                ingredient_name, quantity, measure = ingredient.split(" | ")
                # наполнение списка ключами и значениями по-ингредиентно
                cook_lst.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )
            # добавление блюда в словарь
            cook_book[meal_name] = cook_lst
        # удаление из словаря блюда "Фахитос"
        del cook_book["Фахитос"]
    return cook_book


# Вызов функции и вывод результата в stdout
print(parse_recipes())
