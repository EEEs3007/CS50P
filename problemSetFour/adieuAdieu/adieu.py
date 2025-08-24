import inflect
p = inflect.engine()

Name_lst = []

while True:
    try:
    # input
    # strip the input,
    # put all the names into a list
        Name = input("Name: ").strip()
        Name_lst.append(Name)
  
    except EOFError:
        print("\n")
        break

# print the list in one line, with the commands as a separator
print("Adieu, adieu, to", p.join(Name_lst))
