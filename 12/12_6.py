# БСБО-05-19 Савранский Сергей

msg = input("Message >> ").upper()
transform_letters = {
    "A": [
        " *** ",
        "*   *",
        "*****",
        "*   *",
        "*   *",
    ],

    "B": [
        "**** ",
        "*   *",
        "**** ",
        "*   *",
        "**** ",
    ],

    "C": [
        " *** ",
        "*   *",
        "*    ",
        "*   *",
        " *** ",
    ]
}

for i in range(5):
    for ch in msg:
        print(f"{transform_letters[ch][i]}  ", end='')
    print()
