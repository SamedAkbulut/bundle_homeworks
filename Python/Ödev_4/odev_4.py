import time
class Yonetmenler:
    def __init__(self, Name, Movie, Year, YearOfDeath, Quote, Award):
        self.Name = Name
        self.Movie = Movie
        self.Year = Year
        self.YearOfDeath = YearOfDeath
        self.Quote = Quote
        self.Award = Award 
        if self.YearOfDeath == "-":
            self.YearOfDeath="Still Alive"
        print(self.intro())
        self.doYouLike()

    def intro(self):
        a="Director's ; \nName :{} \nMovie :{}\nRelease year of the movie :{}\nAward :{}\nYear of Death :{}\nQuote:{}".format(self.Name, self.Movie,self.Year, self.Award, self.YearOfDeath, self.dQuote())
        return a
    def dQuote(self):
        if self.Quote== "-":
            return("Sorry, s/he doesn't have a quote")
        else:
            return(self.Quote)
            
    def doYouLike(self):
        b=str(input("Do you like this director ? (y or n)\n"))
        if b== "y":
            print("Good for you\n")
        elif b== "n":
            print("Pity for you\n")
        time.sleep(1)
movie1= Yonetmenler("Alfred Hitchcock", "Psycho", 1964, 1980,"There is no terror in the bang, only the anticipation of it.", "Golden Globe-Best Supporting Actress")
movie2= Yonetmenler("Stanley Kubrick", "A Clockwock Orange", 1971, 1999, "If it can be written, or thought, it can be filmed", "Venice Film Festival-Pasinetti")               
movie3= Yonetmenler("Katia Lund", "City of God", 2002, "-" , "-", "Academy Award-Best Director")
movie4= Yonetmenler("Christopher Nolan", "Dark Knight", 2008, "-", "n", "Academy Award-Best Supporting Actor")
movie5= Yonetmenler("Nuri Bilge Ceylan", "Kış Uykusu", 2014, "-", "-", "Cannes Film Festival- Palme d'Or")
movie6= Yonetmenler("Frank Derebont", "Shawshank Redemption", 1994, "-", "-", "-")
                    
