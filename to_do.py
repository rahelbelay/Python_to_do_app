# Keep track of todos using a list.
todo_list = []

# I need to print my todos.
def print_todos():
    if len(todo_list) == 0:
        print("You have nothing to do!")
    else:
        for count, todo in enumerate(todo_list):
            print(f"{count}: {todo}")

# I need a way to add todos.
def add_todo(todo):
    # We receive a todo, which is a string
    todo_list.append(todo)

# print the empty todo list
# print_todos()
# # add a todo by calling our function
# add_todo("feed the cat")
# # print the todo list again, making sure our todo got added
# print_todos()

# I need to be able to delete todos.
def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print("💩Sorry, we couldn't find that one.💩")

# delete_todo(0)
# print_todos()
# delete_todo(0)
# print_todos()


# Show user the main menu.
def main():
    menu = """
The Best Todo App Evar
======================
0. Quit
1. Print the Todos
2. Add a Todo
3. Complete a Todo
"""
    is_running = True
    while is_running:
        print(menu)
        choice = input("Choose one: ")
        if choice == "0":
            is_running = False
            print("Thank you for using the todo app")
        elif choice == "1":
            print_todos()
        elif choice == "2":
            # Prompt them for what they want to do
            new_todo = input("What do you need to do? ")
            add_todo(new_todo)
        elif choice == "3":
            index_to_complete = int(input("Complete which todo? "))
            delete_todo(index_to_complete)
        else:
            print("Please enter a number for your choice.")


main()   