class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team:str, games:int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = goals + assists

    def pisteet(self):
        return self.points

    def stats(self):
        return {'name': self.name, 'nationality': self.nationality, 'assists':self.assists, 'goals':self.goals, 'penalties':self.penalties, 'team':self.team, 'games':self.games, 'points':self.points}
    
    def __str__(self):
        return f"{self.name:20}{self.team:4}{self.goals:3} +{self.assists:3} ={self.points:>3}"

