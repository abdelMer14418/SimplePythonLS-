import os


def list_files():
    # Obtenir la liste des fichiers et répertoires
    # dans le répertoire actuel
    files = os.listdir()

    # Afficher chaque fichier ou répertoire
    for file in files:
        print(file)


class Lister:
    def __init__(self):
        pass

    def list_files(self):
        # Obtenir la liste des fichiers et répertoires
        # dans le répertoire actuel
        files = os.listdir()

        # Afficher chaque fichier ou répertoire
        for file in files:
            print(file)


if __name__ == "__main__":
    list_files()



print("Rachid est passé par là")


#New Line
