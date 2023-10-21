#!/usr/bin/env python3


class CraftedList:
    def __init__(self, *args):
        self.__elements = list(args)
        self.__current_length = self.length()

    def __str__(self):
        return str(self.__elements)

    def __len__(self):
        return self.__current_length

    def __iter__(self):
        for element in self.__elements:
            yield element

    def length(self):
        cnt = 0
        for _ in self.__elements:
            cnt += 1
        return cnt

    def append(self, el):
        self.__current_length += 1
        self.__elements = [item for item in self.__elements] + [None]
        self.__elements[self.__current_length - 1] = el

    def clear(self):
        self.__elements = []
        self.__current_length = self.length()

    def copy(self):
        copied_ls = CraftedList(*self.__elements)
        return copied_ls

    def count(self, el):
        if el not in self.__elements:
            return 0
        cnt = 0
        for element in self.__elements:
            if el == element:
                cnt += 1
        return cnt

    def extend(self, el):
        try:
            iter(el)
            self.__elements = self.__elements + el
        except TypeError:
            self.append(el)

    def index(self, el):
        for i, element in enumerate(self.__elements):
            if el == element:
                return i

    def insert(self, ind, el):
        if ind >= self.__current_length:
            self.append(el)
        else:
            tmp = self.__elements[:ind]
            tmp.append(el)
            self.__elements = tmp[:ind + 1] + self.__elements[ind:]

    def pop(self, ind=None):
        if ind is None:
            tmp = self.__elements[-1]
            self.__elements = self.__elements[:-1]
        else:
            tmp = self.__elements[ind]
            self.__elements = self.__elements[:ind] + self.__elements[ind + 1:]
        return tmp

    def remove(self, el):
        for i, e in enumerate(self.__elements):
            if el == e:
                self.__elements = self.__elements[:i] + self.__elements[i+1:]
                break

    def reverse(self):
        self.__elements =  self.__elements[::-1]

    def sort(self, key = None, reverse = False):
        self.__elements =  sorted(self.__elements, key=key, reverse=reverse)


def main():
    ml = CraftedList("aaa", "bbbb", "aaaaa", "bb", "b", "aaaaaa")
    print(ml)
    ml.sort(key=len, reverse=True)
    print(ml)


if __name__ == "__main__":
    main()
