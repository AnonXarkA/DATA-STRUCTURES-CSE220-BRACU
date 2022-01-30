# task 2


vowels = ["A", "E", "I", "O", "U"]
consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L",
              "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]


class Hashstring:
    def __init__(self, str):
        self.str = str

    def string_get(self):
        return self.str

    def string_key(self):
        val = 0
        n = 0
        for x in self.str:
            if x in consonants:
                val = val + 1
            if x not in consonants and x not in vowels:
                n += int(x)
        s_key = ((val * 24) + n)
        return s_key


class Hashtable:
    def __init__(self, size=9):
        self.size = size
        self.list = [0] * size

    def function(self, string_key):
        return string_key % self.size

    def add(self, s):
        val = s.string_key()
        position = self.function(val)
        for y in range(1, self.size):
            if self.list[position] == 0:
                self.list[position] = s.string_get()
                break
            else:
                position = (val+y) % self.size

    def print(self):
        for y in range(self.size):
            print(self.list[y])


hash_table = Hashtable()
list = ["X9ZAR2JD6F7", "ZJO9V49NDOU", "G94F5SMC2DG", "KD9LNX46TT2",
        "WN2NY54F22D", "YVRFKVUOH6Y", "NJ89I7DN7V8", "5W8UWJSDCJH", "5YLHRBO79CT"]
for x in list:
    v = Hashstring(x)
    hash_table.add(v)
hash_table.print()
