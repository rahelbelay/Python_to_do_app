# keep tracking to do using a list
todo_list = []

def print_todo():
    for todo in todo_list:
        print(todo)

# i need a way add todo's
def add_todo(todo):
    todo_list.append(todo)
# print empty to do list
# print_todo()
# add to do by calling the function
# add_todo("feed the cat")
# print_todo()

# I need to delet todo's
def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print("😟sorry,we cound't find that.")
delete_todo(0)
print_todo()
delete_todo(0)
print_todo()

# I need to print todo's

# show the user the menu

def main():
    menu = """
The BestTodo App Ever
=====================
0. Quit
1. print the todos
2. add the todo
3. Complete a todo
"""
is_running =True
while is_running:
    print(menu)
    choice = input("Choose one:")
    if choice == "0":
        is_running =False
        print("Thank you for using the to do app")
    elif choice == "1":
        print_todo()
    elif choice == "2":
        # prompt them what they want
        new_todo = input("what do you need to do?")
    elif choice == "3":
        index_to_complete = int(input("complete which to do?"))
        delete_todo(index_to_complete)
    else:
        print("please enter a number for your choice.")
main()


