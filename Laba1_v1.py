

class Transport:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def printinfo(self):
        print("Transport" , self.name, self.type)


class Iterulka:
    def iterTrans(self):
        listtype = ["Bibika", "Bibika", "Samoletik", "Korablik", "Podlodochka"]
        listname = ["Malenkaya", "Bolshaya", "Gruzovoy", "Plavuchiy", "Kurskdgsdvsdvsdvsdvsdvsdvsdvsdvsdvsdvsdvsdvsdvsdvdsvdsvsdvsdvsdvsdvsdvsdvsdvsdvsdvs"]
        for i in range(0, 4):
            trans = Transport(listname[i], listtype[i])
            trans.printinfo()


def main():
    iterator = Iterulka()
    iterator.iterTrans()


print("Pokazivau vseh")
if __name__ == "__main__":
    main()
