def allThreeTheSame(loc1, loc2, loc3):
    res = {}
    for key1, value1 in loc1.items():
        for key2, value2 in loc2.items():
            for key3, value3 in loc3.items():
                if key1 == key2 == key3:
                    res.update({key1: value1})

    uniqueKeys = set(res.keys())
    res = {key: res[key] for key in uniqueKeys}

    print("Tree types in all three locations are: ", end="")
    for key, value in res.items():
        print(value, end=", ")
    print()


def uniqueInTwo(loc, loc1):
    toDel = []
    res = loc.copy()

    for key1, value1 in res.items():
        for key2, value2 in loc1.items():
            if key1 == key2:
                toDel.append(key1)

    for _ in toDel:
        res.pop(_)
    return res


def uniqueInLocation(loc, loc1, loc2):
    return uniqueInTwo(uniqueInTwo(loc, loc1), loc2)


def printUnique(loc_a, loc_b, loc_c):
    print("Unique in location A: ", end="")
    for key, values in uniqueInLocation(loc_a, loc_b, loc_c).items():
        print(values, end=", ")
    print()

    print("Unique in location B: ", end="")
    for key, values in uniqueInLocation(loc_b, loc_a, loc_c).items():
        print(values, end=", ")
    print()

    print("Unique in location C: ", end="")
    for key, values in uniqueInLocation(loc_c, loc_b, loc_a).items():
        print(values, end=", ")
    print()


def uniqueInCOnly(loc_a, loc_b, loc_c):
    res = loc_c.copy()
    toDel = []
    for _ in res:
        if _ in loc_a:
            toDel.append(_)

    for _ in toDel:
        res.pop(_)

    toDel = []

    for _ in res:
        if _ in loc_b:
            toDel.append(_)

    for _ in toDel:
        res.pop(_)

    print("Tree types that are not on A and B but are in C (same as task2...): ", end="")

    for key, value in res.items():
        print(value, end=", ")


def main():
    location_a = {"Dąb szypułkowy": "Quercus robur", "Buk zwyczajny": "Fagus sylvatica",
                  "Świerk pospolity": "Picea abies", "Sosna zwyczajna": "Pinus sylvestris",
                  "Brzoza brodawkowata": "Betula pendula", "Grab pospolity": "Carpinus betulus",
                  "Jodła pospolita": "Abies alba", "Klon jawor": "Acer pseudoplatanus",
                  "Jesion wyniosły": "Fraxinus excelsior", "Modrzew europejsk": "Larix decidua"}

    location_b = {"Dąb czerwony": "Quercus rubra", "Klon cukrowy": "Acer saccharum",
                  "Sosna żółta": "Pinus ponderosa", "Świerk biały": "Picea glauca",
                  "Czereśnia wirginijska": "Prunus virginiana", "Jodła balsamiczna": "Abies balsamea",
                  "Buk amerykański": "Fagus grandifolia", "Topola osika": "Populus tremuloides",
                  "Dąb biały": "Quercus alba", "Hemlok wschodn": "Tsuga canadensis"}
    location_c = {"Cedr himalajski": "Cedrus deodara", "Sosna himalajska": "Pinus wallichiana",
                  "Dąb skalny": "Quercus petraea", "Klon wielkolistny": "Acer macrophyllum",
                  "Świerk syberyjski": "Picea obovata", "Buk wschodni": "Fagus orientalis",
                  "Brzoza papierowa": "Betula papyrifera", "Jodła koreańska": "Abies koreana",
                  "Ginkgo": "Ginkgo biloba", "Magnolia": "Magnolia spp."}

    loc_a = {key.split(" ")[0]: value for key, value in location_a.items()}
    loc_b = {key.split(" ")[0]: value for key, value in location_b.items()}
    loc_c = {key.split(" ")[0]: value for key, value in location_c.items()}

    print("\n======== Task1 ========")
    allThreeTheSame(loc_a, loc_b, loc_c)

    print("\n======== Task2 ========")
    printUnique(loc_a, loc_b, loc_c)

    print("\n======== Task3 ========")
    uniqueInCOnly(loc_a, loc_b, loc_c)


if __name__ == "__main__":
    main()
