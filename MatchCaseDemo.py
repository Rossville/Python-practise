# This program compares from which does the characters of harry potter belongs to.

def MatchCaseDemo(name: str)->str:
    # it accepts string as an argument and return string as an argument as well
    house:str = ""
    match name:
        case "Harry" | "Hermione" | "Ron" :
            house = "Gryffindor"
        case "Draco":
            house = "Slytherin"
        case _:
            house = f"{name} does not belong to Gryffindor or Slytherin"
    return house

def main():
    name = input("Enter the name of the character ")
    print(MatchCaseDemo(name))

main()
