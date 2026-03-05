# Open the file 'demo.txt' and read it
try :
    f = open("demo.txt", "r")
    print(f)
except FileNotFoundError as error :
    print(f"It seems like {error}")

