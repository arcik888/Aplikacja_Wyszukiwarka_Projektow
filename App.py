# -*- coding: utf-8 -*-

choice = ""
while choice.lower() != "exit":

    choice = input("""
        Wybierz co chcesz zrobić:
        - Utwórz nowy projekt [N]: 
        - Akceptuj projekt [A]:
        - Uwolnij projekt do produkcji [R]: 
        - Zmień rewizję [I]:
        - Wyszukaj projekt [F]: 
        lub 'exit' aby zakończyć.
        """)

    if choice.lower() == "n":
        import new_project
    elif choice.lower() == "a":
        import update_approve
    elif choice.lower() == "r":
        import update_release
    elif choice.lower() == "i":
        import change_rev
    elif choice.lower() == "f":
        import searching
        search = searching.Search()
        search
        