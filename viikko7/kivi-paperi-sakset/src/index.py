from pelitehdas import Pelitehdas


def main():
    while True:
        pelit = Pelitehdas()
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = pelit.pelaaja_vs_pelaaja()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = pelit.pelaaja_vs_tekoaly()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = pelit.pelaaja_vs_parempi_tekoaly()
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()