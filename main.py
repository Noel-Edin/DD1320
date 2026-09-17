from bintreeFile import Bintree
from linkedQFile import LinkedQ

class HittadLösning(Exception):
    pass

class ParentNode():
    #Klass för att kunna skriva ut vägen från start till slut, sparar ordet och pekaren till dess förälder
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

def writechain(node):
    #Skriver ut kedjan av ord, går tillbaka till startordet och skriver ut lösningen sist
    if node is not None:
        writechain(node.parent)
        print(node.word)

svenska = Bintree()
gamla = Bintree()

with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        svenska.put(ordet)

def makechildren(nod, slutord, q):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    startord = nod.word

    for i in range(len(startord)):
        for bokstav in alfabet:
            nytt_ord = startord[:i] + bokstav + startord[i+1:]
            if nytt_ord in svenska and nytt_ord not in gamla:
                gamla.put(nytt_ord)
                barn_nod = ParentNode(nytt_ord, parent = nod)

                if nytt_ord == slutord:
                    writechain(barn_nod)
                    raise HittadLösning
                q.enqueue(barn_nod)

if __name__ == "__main__":
    start = input("Startord: ")
    slut = input("Slutord: ")

    q = LinkedQ()
    start_nod = ParentNode(start)
    q.enqueue(start_nod)
    gamla.put(start)

    try:
        while not q.isEmpty():
            akutell_nod = q.dequeue()
            makechildren(akutell_nod, slut, q)

        #Om kön töms och loopen slutade saknades det lösning
        print("Det fanns ingen väg till", slut)

    except HittadLösning:
        pass
