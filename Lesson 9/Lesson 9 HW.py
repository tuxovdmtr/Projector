# complexity of your algorithm - O(rounds * cats)

rounds = int(input("Input rounds: "))
cats = int(input("Input number of cats: "))


def get_cats_with_hats(rounds: int, cats: int):
    cats_list = ["Cat"] * cats
    hat_on = False
    cats_with_hats = []
    while rounds > 0:
        for round in range(1, rounds+1):
            for cat in range(round, len(cats_list)+1):
                if cat / round == cat:
                    cats_list[cat-1] = "Hat On"
                    hat_on = True
                    continue
                if cat % round == 0 and cats_list[cat-1] == "Hat Off":
                    cats_list[cat-1] = "Hat On"
                    hat_on = True
                elif cat % round == 0 and cats_list[cat-1] == "Hat On":
                    cats_list[cat-1] = "Hat Off"
                    hat_on = False
            else:
                rounds -= 1
        break             
    for cat_pos, status in enumerate(cats_list):
        if status == "Hat On":
            cats_with_hats.append(cat_pos+1)
    return cats_with_hats

print(f"Cats with hats: {get_cats_with_hats(rounds, cats)}")
