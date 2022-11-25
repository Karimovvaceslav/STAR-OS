import time
import start

while True:
    a = input("")
    if ("shutdown") == a:
        break
    if ("calc") == a:
        print("loading...")
        time.sleep(2)
        f = ("Enter first number: ")
        s = ("Enter second number: ")
        o = ("Enter operation: ")
        f = float(input(f))
        o = input(o)
        s = float(input(s))
        if o == '+':
            print(f + s)
        elif o == '-':
            print(f - s)
        elif o == '/':
            print(f / s)
        elif o == '*':
            print(f * s)
    if ("help") == a:
        print("Commands:")
        print("calc - open calculator")
        print("shutdown - turn off you computer")
        print("ver - information of this OS")
    if ("ver") == a:
        print("         $          ")
        print("        $ $         ")
        print("       $   $        ")
        print("$$$$$$$     $$$$$$$$")
        print(" $                $ ")
        print("  $              $  ")
        print(" $       $$       $ ")
        print("$      $    $      $")
        print("$     $      $     $")
        print("$    $        $    $")
        print("$$$$$          $$$$$")
        print("S  T  A  R      O  S")
        print("v1.0")
        print("beta version")
    