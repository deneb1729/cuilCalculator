cuil_multiplicators = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]


def generator(dni_number: int, gener: str):

    extended_dni = "0" + str(dni_number) if (len(str(dni_number)) < 8) else str(dni_number)
    precuil = "20" + extended_dni if gener == "M" else "27" + extended_dni

    accumulator = 0
    for e, d in zip(cuil_multiplicators, precuil):
        accumulator += e * int(d)

    rest = accumulator % 11
    if rest == 0:
        return precuil + "0"
    elif rest == 1:
        if gener == "M":
            return "23" + precuil[2:] + "9"
        if gener == "F":
            return "23" + precuil[2:] + "4"

    return precuil + str(11 - rest)
