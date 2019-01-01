
class GetNumberMagic:
    cards = [
        {1, 2, 3, 4, 5, 6, 7, 8},
        {1, 2, 3, 4, 9, 10, 11, 12},
        {1, 2, 5, 6, 9, 10, 13, 14},
        {1, 3, 5, 7, 9, 11, 13, 15}
    ]

    def getNumber(self, answer):
        result = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

        for i in range(len(answer)):
            result = result & self.cards[i] if answer[i] is "Y" else result - self.cards[i]

        return result

print(GetNumberMagic().getNumber("YNYY"))
print(GetNumberMagic().getNumber("YNNN"))
print(GetNumberMagic().getNumber("NNNN"))
print(GetNumberMagic().getNumber("YYYY"))
print(GetNumberMagic().getNumber("NYNY"))

