from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.stacks_by_frequency = defaultdict(list)
        self.frequency_of_vals = dict()
        self.max_frequency = 0

    def push(self, val: int) -> None:
        if val not in self.frequency_of_vals:
            self.frequency_of_vals[val] = 1
        else:
            self.frequency_of_vals[val] += 1

        self.max_frequency = max(self.max_frequency, self.frequency_of_vals[val])
        self.stacks_by_frequency[self.frequency_of_vals[val]].append(val)

    def pop(self) -> int:
        res = self.stacks_by_frequency[self.max_frequency][-1]
        self.stacks_by_frequency[self.max_frequency].pop()

        self.frequency_of_vals[res] -= 1

        while self.max_frequency and not self.stacks_by_frequency[self.max_frequency]:
            self.max_frequency -= 1

        return res
