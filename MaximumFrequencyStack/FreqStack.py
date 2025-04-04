from collections import defaultdict

class FreqStack:
    def __init__(self):
        self._stacks_by_frequency = defaultdict(list)
        self._frequency_of_vals = dict()
        self._max_frequency = 0

    def push(self, val: int) -> None:
        if val not in self._frequency_of_vals:
            self._frequency_of_vals[val] = 1
        else:
            self._frequency_of_vals[val] += 1

        self._max_frequency = max(self._max_frequency, self._frequency_of_vals[val])
        self._stacks_by_frequency[self._frequency_of_vals[val]].append(val)

    def pop(self) -> int:
        res = self._stacks_by_frequency[self._max_frequency][-1]
        self._stacks_by_frequency[self._max_frequency].pop()

        self._frequency_of_vals[res] -= 1

        while self._max_frequency and not self._stacks_by_frequency[self._max_frequency]:
            self._max_frequency -= 1

        return res
