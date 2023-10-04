# Задача 1
def parse_recipes():
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


print(parse_recipes())
