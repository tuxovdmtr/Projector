# complexity of your algorithm - O(rounds * cats)

rounds = int(input("Input rounds: "))
cats = int(input("Input number of cats: "))


rounds = int(input("Input rounds: "))
cats = int(input("Input number of cats: "))


def get_cats_with_hats(rounds: int, cats: int):
    cats_list = [True] * cats
    cats_with_hats = []
    while rounds > 0:
        for round in range(2, rounds + 1):
            for cat in range(round, len(cats_list)+1):
                if cat % round == 0:
                    cats_list[cat-1] = not cats_list[cat-1]
            else:
                rounds -= 1
        break             
    for cat_pos, status in enumerate(cats_list):
        if status == True:
            cats_with_hats.append(cat_pos + 1)
    return cats_with_hats

print(f"Cats with hats: {get_cats_with_hats(rounds, cats)}")
