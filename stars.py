def draw_stars(arr):
    stars = ""
    for value in arr:
        if isinstance(value, int):
            stars += value * "*"
            print stars
            stars = ""
        if isinstance(value, str):
            stars += len(value) * (value[0]).lower()
            print stars
            stars = ""

draw_stars([4,'Tom',1, 'Michael', 5, 7, 'Jimmy Smith'])