# for run and tests

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
    # print(f"cook_book = {cook_book}")

    # Задача 2
    def get_shop_list_by_dishes(dishes, person_count):
        """Создает список покупок для блюд по количесву персон"""
        new_cook = {}
        for dish in dishes:
            if dish in cook_book:
                for ingredient in cook_book[dish]:
                    ingredient["quantity"] *= person_count
                    new_cook[ingredient["ingredient_name"]] = ingredient
        meal_dict = {}
        for value in new_cook.values():
            name = value["ingredient_name"]
            del value["ingredient_name"]
            meal_dict[name] = value
        return meal_dict

    print(get_shop_list_by_dishes(["Омлет", "Утка по-пекински"], 2))
