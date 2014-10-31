#import json
#import csv


class Series():

    def __init__(self, games=None):
        self.games = games or []

    def from_json(self):
        pass

    def to_json(self):
        pass

    def from_csv(self):
        pass

    def to_csv(self):
        pass

    def avg_score(self):
        scores = [g.score() for g in self.games]
        return float(sum(scores)) / len(scores)

    def avg_distribution(self):
        pass

    def distribution(self):
        pass
