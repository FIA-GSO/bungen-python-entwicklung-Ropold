# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int,int,int]:
    """
        Computes the r2d2 population for the given step amount
    :param steps: amount of steps to compute the population (e.g.: 5)
    :return: tuple of childs adults and old r2d2
    """
    junge, erwachsene, alt = 60, 5, 3
    for _ in range(steps - 1):
        neue_junge = (erwachsene * 4) + (alt * 2)
        neue_erwachsene = junge // 2
        neue_alt = erwachsene // 3
        print(f"Vorher  -> Junge: {junge}, Erwachsene: {erwachsene}, Alte: {alt}")
        print(f"Nachher -> Junge: {neue_junge}, Erwachsene: {neue_erwachsene}, Alte: {neue_alt}")
        junge, erwachsene, alt = neue_junge, neue_erwachsene, neue_alt
    return (junge, erwachsene, alt)


def r2d2_population_list(steps: int) -> list[tuple[int, int, int]]:
    junge, erwachsene, alt = 60, 5, 3

    history: list[tuple[int, int, int]] = []
    history.append((junge, erwachsene, alt))

    for i in range(steps - 1):
        neue_junge = (erwachsene * 4) + (alt * 2)
        neue_erwachsene = junge // 2
        neue_alt = erwachsene // 3

        junge, erwachsene, alt = neue_junge, neue_erwachsene, neue_alt
        history.append((junge, erwachsene, alt))

    return history

print(r2d2_population_list(10))



#---------------------Aufgabe 2 Quantitativer Angebotsvergleich------------------------------
#IMPLEMENT YOUR SOLUTION FOR THE Quantitativer Angebotsvergleich HERE


#---------------------Aufgabe 3 Streichholz------------------------------
def streich_holz_spiel(streichhoelzer: int = 31):
    print(f"\n=== Streichholzspiel (Nim-Spiel) ===")
    print(f"Streichhölzer zu Beginn: {streichhoelzer}")
    print("Wer das letzte Streichholz nehmen muss, verliert!")
    print("Pro Zug: mindestens 1, höchstens 6 Streichhölzer.\n")

    streichhoelzer -= 2
    print(f"Computer nimmt 2 Streichhölzer. Noch übrig: {streichhoelzer}")

    while streichhoelzer > 1:
        max_take = min(6, streichhoelzer)
        while True:
            try:
                mensch_nimmt = int(input(f"\nDein Zug (1–{max_take}, noch {streichhoelzer} übrig): "))
                if 1 <= mensch_nimmt <= max_take:
                    break
                print(f"Bitte eine Zahl zwischen 1 und {max_take} eingeben.")
            except ValueError:
                print("Bitte eine ganze Zahl eingeben.")

        streichhoelzer -= mensch_nimmt
        print(f"Du nimmst {mensch_nimmt}. Noch übrig: {streichhoelzer}")

        if streichhoelzer > 0:
            computer_nimmt = 7 - mensch_nimmt
            streichhoelzer -= computer_nimmt
            print(f"Computer nimmt {computer_nimmt}. Noch übrig: {streichhoelzer}")

    print("\nNur noch 1 Streichholz übrig – du musst es nehmen. Du verlierst!")


#---------------------Aufgabe 4 Heron ------------------------------------
def heron_verfahren(area : float, threshold:float) -> float:
    """
        computes the square root using the heron method
    :param area: size of the area e.g.25
    :param threshold: threshold for the heron method e.g. 0.01
    :return:the square root of the given area according to the heron method
    """

    return 0


#---------------------Aufgabe 5 Quersumme------------------------------
#IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!


#---------------MANAGEMENT----------------------
#-------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    # print(f"""
    #     # R2D2 Population after 5 steps is:
    #     # Young: {compute_r2d2_population(5)[0]}
    #     # Adults: {compute_r2d2_population(5)[1]}
    #     # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    # TO BE IMPLEMENTED
    
    # Aufgabe 3
    # streich_holz_spiel()

    # Aufgabe 4
    #print (f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 5
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
