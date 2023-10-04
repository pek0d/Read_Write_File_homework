# Задача № 2

# чтение файла для последующего парсинга по относительному пути
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
    # print(f"cook_book = {cook_book}")

    def get_shop_list_by_dishes(dishes, person_count):
        """Создает список покупок для блюд по количеству
        персон из перечня рецептов"""
        # инициализация "внутреннего" словаря с единицами измерения и кол-вом
        new_cook = {}
        # распаковка списка блюд
        for dish in dishes:
            # если блюдо есть в словаре, то добавляем единицы измерения
            if dish in cook_book:
                # распаковка списка ингредиентов
                for ingredient in cook_book[dish]:
                    # умножение кол-ва персон на единицу измерения
                    ingredient["quantity"] *= person_count
                    # добавление ингредиента в словарь по ключу имени ингред.
                    new_cook[ingredient["ingredient_name"]] = ingredient
            # если блюдо нет в словаре, то выводим сообщение
            else:
                print(f"Такого блюда как {dish} нет в перечне рецептов.")
        # создание выходного 'внешнего' словаря с блюдами
        meal_dict = {}
        # распаковка по значению "внутреннего" словаря
        for value in new_cook.values():
            # присвоение наменования ингредиента по ключу продукта
            name = value["ingredient_name"]
            # удаление ключа с продуктом из "внутреннего" словаря
            del value["ingredient_name"]
            # добавление (имени) продукта во "внешний" словарь
            meal_dict[name] = value
        # возвращение "внешнего" словаря
        return meal_dict

    # Вывод результата в stdout
    print(get_shop_list_by_dishes(["Омлет", "Утка по-пекински"], 2))
