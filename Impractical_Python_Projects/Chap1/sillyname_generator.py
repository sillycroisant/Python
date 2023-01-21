"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psychi 'Sidekcik Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n")

    first = ('Baby Oil','Bad News','Big Burps','Bill Neenie-Weenie')
    last = ('ApppleYard','Bigmeat','Bloominshine','Boogerbottom','Breadslovetrout')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        print("\n")
        print("{} {}".format(first_name,last_name),file=sys.stderr)
        print("\n")
        
        try_again = input("\nTry again? (Press enter else n to quit)\n")
        if try_again.lower() == "n":
            break
        
    input("\nPress entert to exit.")
    
if __name__ == "__main__":
    main()