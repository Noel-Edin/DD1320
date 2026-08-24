import csv

class Kdrama:

    def __init__(self, kdrama):
        self.name = kdrama[0]
        self.rating = float(kdrama[1])
        self.actors = kdrama[2]
        self.viewership = float(kdrama[3])
        self.genre = kdrama [4]
        self.director = kdrama [5]
        self.writer = kdrama [6]
        self.year = int(kdrama[7])
        self.episodes = int(kdrama[8])
        self.network = kdrama [9]

    def __str__(self):
        return f"{self.name} ({self.year}) - Genre: {self.genre}, Rating: {self.rating}"

    def __lt__ (self,other):
        return self.rating < other.rating

    def get_genre(self):
        return self.genre

    def generate_popularity(self):
        return self.rating * self.viewership

def read_file_to_list(filename):
    kdramalist = []
    with open(filename, mode="r") as kdramafile:
        csvfile = csv.reader(kdramafile,delimiter = ",")
        next (csvfile)
        for line in csvfile:
           if len(line) == 10:
               newkdrama = Kdrama(line)
               kdramalist.append(newkdrama)
    return kdramalist

def search_by_genre(kdramalist, search):
    found_kdrama = []
    for kdrama in kdramalist:
        if search in kdrama.genre:
            found_kdrama.append(kdrama)
    return found_kdrama
        

def main():
    print("\n")
    kdramalist = read_file_to_list("kdrama.csv")
    kdrama1 = kdramalist[0]
    kdrama2 = kdramalist[1]
    #__str__
    print(kdrama1, "\n")
    print(kdrama2, "\n") 
    #__lt__
    if kdrama1 < kdrama2:
        print(f"{kdrama2.name} har högre rating {kdrama1.name}\n")
    else:
        print(f"{kdrama1.name} har högre eller samma rating som {kdrama2.name} \n")
    #genre
    print(f"Genren för {kdrama1.name} är: {kdrama1.get_genre()}\n")
    print(f"Genren för {kdrama2.name} är: {kdrama2.get_genre()}\n")
    #popularity
    print(f"Populariteten för {kdrama1.name}: {kdrama1.generate_popularity()}\n")
    print(f"Populariteten för {kdrama2.name}: {kdrama2.generate_popularity()}\n")

    match_genre = input (f"Vilken genre söker du? ")
    found_kdrama = search_by_genre(kdramalist, match_genre)
    if found_kdrama:
        print(f"Hittade följande serier: ")
        for kdrama in found_kdrama:
            print(f"- {kdrama.name}")
    else:
        print("Hittade inga serier med den genren")
main()
