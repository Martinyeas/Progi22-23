from hires_film_alap import Film

def main():
    film1 = Film()
    film2 = Film()
    film3 = Film()

    film1.name = input("Adja meg az első film címét: ")
    film1.length = input("Adja meg az első film hosszát: ")
    film1.nationality = input("Adja meg az első film nemzetiségét (angol/amerikai): ")

    film2.name = input("Adja meg a második film címét: ")
    film2.length = input("Adja meg a második film hosszát: ")
    film2.nationality = input("Adja meg a második film nemzetiségét (angol/amerikai): ")

    film3.name = input("Adja meg a harmadik film címét: ")
    film3.length = input("Adja meg a harmadik film hosszát: ")
    film3.nationality = input("Adja meg a harmadik film nemzetiségét (angol/amerikai): ")

    print(film1.prefix() + film1.name + " - " + film1.length)
    print(film2.prefix() + film2.name + " - " + film2.length)
    print(film3.prefix() + film3.name + " - " + film3.length)

if __name__ == '__main__':
    main()
