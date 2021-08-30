user_choice = -1

tasks = []
tasks.append("Wynieść śmieci")
tasks.append("Powiesić pranie")

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "[" +str(task_index) + "]")

def add_task():
    task = input("Co jest do zrobienia? ")
    tasks.append(task)
    print("Zadanie zostało dodane")

while user_choice != 5:
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        add_task()


        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zapisz zmiany do pliku")
        print("5. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()