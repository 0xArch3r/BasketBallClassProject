class player:

    def __init__(self, name,guardians, experience, height):
        self._name = name
        self._guardians = guardians
        self._experience = experience
        self._height = height.split()[0]

    def name(self):
        return self._name

    def guardians(self):
        return self._guardians

    def experience(self):
        return self._experience == "YES"

    def height(self):
        return self._height

class team:

    def __init__(self, name):
        self._name = name
        self._players = []

    def name(self):
        return self._name

    def list_players(self):
        return [plyr for plyr in self._players]

    def add_player(self, plyr):
        self._players.append(plyr)

    def get_total_players(self):
        return f"Total Players: {str(len(self._players))}"

    def get_exp_players(self):
        return f'Total Experienced Players: {len([1 for _ in self._players if _.experience()])}'

    def get_inexp_players(self):
        return f'Total Inexperienced Players: {len([1 for _ in self._players if not _.experience()])}'

    def get_avg_height(self):
        return f'Average Height: {sum([int(plyr.height()) for plyr in self._players])/len(self._players):.2f}'

    def get_stats(self):
        def bprint():
            print("+"+"-"*60+"+")

        def eprint():
            print("|"+" "*60+"|")

        def vprint(string):
            print(f"|  {string}"+" "*(58 - len(string))+"|")

        bprint()
        print("|"+" "*((60 - len(self._name))//2)+self._name+" "*((60 - len(self._name))//2)+"|")
        bprint()
        eprint()
        vprint(self.get_total_players())
        vprint(self.get_exp_players())
        vprint(self.get_inexp_players())
        vprint(self.get_avg_height())
        eprint()
        bprint()
        vprint("Roster:")
        eprint()
        for p in self._players:
            vprint(f"Name: {p.name()}")
            vprint(f"Guardians: {p.guardians()}")
            vprint(f"Height: {p.height()}")
            vprint(f"Experienced: {p.experience()}")
            eprint()
        bprint()



