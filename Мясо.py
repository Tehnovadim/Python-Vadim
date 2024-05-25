def print_header_footer():
    print('~' * 50)

def get_dish_details():
    dish_name = input("Введіть назву страви, рецепт якої вам подобається: ").strip()
    recipe = input("Введіть рецепт зазначеної страви: ").strip()
    return dish_name, recipe

def format_dish_name(dish_name):
    formatted_name = dish_name.strip().upper()
    return f"{'*' * 10}{formatted_name}{'*' * 10}"

def format_recipe(recipe):
    formatted_recipe = recipe.strip().lower()
    return f"{formatted_recipe} 😊"

def count_word_occurrences(text, word):
    words = text.lower().split()
    return words.count(word.lower())

def main():
    print_header_footer()
    
    dish_name, recipe = get_dish_details()
    
    formatted_dish_name = format_dish_name(dish_name)
    formatted_recipe = format_recipe(recipe)
    
    print(formatted_dish_name)
    print(formatted_recipe)
    
    meat_count = count_word_occurrences(recipe, "мясо")
    print(f"Кількість слів 'мясо' в рецепті: {meat_count}")
    
    print_header_footer()

if __name__ == "__main__":
    main()
