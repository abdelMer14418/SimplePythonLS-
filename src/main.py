import os


def list_files():
    
    files = os.listdir()

    for file in files:
        print(file)


class Lister:
    def __init__(self):
        pass

    def list_files(self):
       
        files = os.listdir()

        for file in files:
            print(file)


if __name__ == "__main__":
    list_files()
