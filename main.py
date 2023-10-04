# Задача 1


def my_cookbook():
    """Возвращает словарь с рецептами берущихся из файла recipes.txt"""

    with open("recipes.txt", encoding="utf-8") as file:
        cook_book = {}
        for line in file.read().split("\n\n"):
            meal_name, *ingredients = line.split("\n")
            cook_lst = []
            for ingredient in ingredients[1:]:
                ingredient_name, quantity, measure = ingredient.split(" | ")
                cook_lst.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )
            cook_book[meal_name] = cook_lst
        del cook_book["Фахитос"]
        return cook_book


# Задача 2


def get_shop_list_by_dishes(dishes, person_count):
    """Создает список покупок для блюд по количесву персон"""
    for dish in dishes:
        print(dish)
