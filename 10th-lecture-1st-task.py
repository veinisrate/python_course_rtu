# Definējiet klasi Song
# Klases construktora vajag būt trīs papildu 3 parametriem(self un vēl 3!)
# title pēc noklusējuma tukša string
# author pēc noklusējuma tukšs string
# lyrics pēc noklusējuma tukšs tuple
# konstruktors saglabātu šos trīs parametrus
# un papildu izdrukātu uz ekrāna "New Song made" - (pamēģiniet arī izdrukāt šeit author un title!)
# Uzrakstiet metodi sing kas izdrukā dziesmu pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Uzrakstiet metodi yell kas izdrukā dziesmu ar lieliem burtiem pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Bonuss: uztaisiet lai sing un yell varam izsaukt vairākas reizes (ķēdejot)
# Bonuss: uztaisiet papildu parametru max_lines, kas izdrukā tikai noteiktu rindiņu skaitu gan sing gan yell. Labāk taisiet ar kādu default vērtību piem. -1 , pie kuras tad izdrukā visas rindas.
# Par ķēdēšano bija šeit: https://www.das.lv/platforma/mod/page/view.php?id=690
# Izveidojiet vairākas dziesmas ar dziesmu tekstiem
# Piemērs:
# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# ziemelmeita.sing(1).yell()
# Rezultāts uz ekrāna:
# Ziemeļmeita - Jumprava
# Gāju meklēt ziemeļmeitu
# Ziemeļmeita - Jumprava
# GĀJU MEKLĒT ZIEMEĻMEITU
# GARU, TĀLU CEĻU VEICU
# Tie kas jūtas komfortabli, uztaisiet Rap klasi kas manto no Song
# Papildu metode break_it ar diviem noklusētiem parametriem max_lines un drop vienādu ar "yeah", kura līdzīga sing, bet pievienot drop aiz katra vārda...
# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# zrap.break_it(1, "yah")
# Ziemeļmeita - Jumprava
# Gāju YAH meklēt YAH ziemeļmeitu YAH

class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song made: {self.title} by {self.author}: \n{self.lyrics}")

    def sing(self, max_lines=-1):
        if self.title != "":
            print(f"Song name: {self.title}")
        if self.author != "":
            print(f"Author: {self.author}")
        print("----")
        for num, line in enumerate(self.lyrics, 1):
            if num <= max_lines or max_lines==-1:
                print(f"{num}: {line}")
            else:
                break
        print("\n")
        return self

    def yell(self, max_lines=-1):
        if self.title != "":
            print(f"Song name: {self.title}")
        if self.author != "":
            print(f"Author: {self.author}")
        print("----")
        for num, line in enumerate(self.lyrics, 1):
            if num <= max_lines or max_lines==-1:
                print(f"{num}: {line.upper()}")
            else:
                break
        print("\n")
        return self


mySong = Song("My heart will go on", "Celine Dion",
              ("You my heart", "You my soul", "Why so long"))
print("\n")
mySong.sing(2).yell(1)

ziemelmeita = Song(lyrics=["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
print("\n")
ziemelmeita.sing(2).yell()

class Rap(Song):
    def __init__(self, title="", author="", lyrics=()):
        super().__init__(title, author, lyrics)
    
    def break_it(self, max_lines=-1, drop="YAH"):
        if self.title != "":
            print(f"Song name: {self.title}")
        if self.author != "":
            print(f"Author: {self.author}")
        print("----")
        for num, line in enumerate(self.lyrics, 1):
            if num <= max_lines or max_lines==-1:
                words_list = line.split()
                for words in words_list:
                    print(f"{words} {drop}", end=" ")
                print("")
            else:
                break
        print("\n")
        return self

my_rap = Rap("My heart will go on", "Celine Dion",
              ("You my heart", "You my soul", "Why so long"))

my_rap.break_it(1)