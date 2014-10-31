from datetime import date
#import json
#import csv
#import matplotlib


class Game():

    def __init__(self, frames=None, dt=None):
        self.frames = frames
        self.date = dt or date.today()

    def score(self):
        return self.partial_scores()[-1]

    def valid_frames(self):
        return (
            all([isinstance(v, int) for f in self.frames for v in f]) and
            all(
                [
                    len(self.frames) == 10,
                    len(self.frames[0]) in [2, 3],
                    all([len(f) == 2 for f in self.frames[:-1]]),
                    all(
                        [
                            (v >= 0 and v <= 10)
                            for f in self.frames for v in f
                        ]
                    ),
                    all(
                        [
                            (sum(f) >= 0 and sum(f) <= 10)
                            for f in self.frames[:-1]
                        ]
                    ),
                    not (
                        len(self.frames[-1]) == 3 and
                        sum(self.frames[-1][:-1]) == 0 and
                        self.frames[-1][2] != 0
                    ),
                ]
            )
        )

    def partial_scores(self):
        partialScores = [0] * 10
        total = 0
        if not self.valid_frames():
            return partialScores
        for i, f in enumerate(self.frames):
            total += sum(f)
            if i < 9:
                if sum(f) == 10 and f[0] != 10:
                    total += self.frames[i + 1][0]
                elif f[0] == 10:
                    if self.frames[i + 1][0] != 10:
                        total += sum(self.frames[i + 1])
                    else:
                        if i < 8:
                            total += sum(
                                [
                                    self.frames[i + 1][0],
                                    self.frames[i + 2][0]
                                ]
                            )
                        else:
                            total += sum(self.frames[i + 1][:2])
            partialScores[i] = total
        partialScores[9] = total
        return partialScores

    def distribution(self):
        dist = {
            '-': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '/': 0,
            'X': 0,
        }
        if not self.valid_frames():
            return dist
        for i, f in enumerate(self.frames):
            if i < 9:
                if sum(f) == 10:
                    if f[0] == 10:
                        dist['X'] += 1
                    elif f[1] == 10:
                        dist['/'] += 1
                        dist['-'] += 1
                    else:
                        dist['/'] += 1
                        dist[str(f[0])] += 1
                else:
                    for v in f:
                        if v == 0:
                            dist['-'] += 1
                        else:
                            dist[str(v)] += 1
            else:
                if sum(f[:2]) < 10:
                    for v in f[:2]:
                        if v == 0:
                            dist['-'] += 1
                        else:
                            dist[str(v)] += 1
                else:
                    pass
        return dist

    def from_json(self):
        pass

    def to_json(self):
        pass

    def plot_partial_scores(self):
        pass

    def plot_distribution(self):
        pass
