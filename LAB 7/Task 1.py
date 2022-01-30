# task 1

def max_val(list):
    val = list[0]
    for i in list:
        if val < abs(i):
            val = abs(i)
    return val


class keyIndex:
    def __init__(self, k):
        self.k = k

    def key_indx(self):
        global maxv
        maxv = max_val(self.k)
        self.temp = [0] * ((max_val(self.k)*2)+1)

        for i in self.k:
            if 0 == self.temp[maxv + i]:
                self.temp[maxv + i] = 1
            else:
                self.temp[maxv+i] = self.temp[maxv+i]+1

    def printlist(self):
        print(self.temp)

    def search(self, key):
        k1 = int(key)
        if 0 > k1+maxv or k1+maxv >= len(self.temp):
            print(False)
        else:
            print(True)

    def sorted(self):
        indx = 0
        for x in range(0, len(self.temp)):
            if len(self.k) <= indx:
                print(self.k)
                break
            if 1 <= self.temp[x]:
                for y in range(0, self.temp[x]):
                    self.k[indx] = x - maxv
                    indx = indx + 1


list = [-4, 7, 3, 4, 2, -9, -7]
key_indx = keyIndex(list)
key_indx.key_indx()
key_indx.printlist()
key_indx.search(3)
key_indx.sorted()
