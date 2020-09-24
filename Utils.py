# This is a module
# A module/ file contain all of the related function or classes which will be reusable
# if no need for the declaration of attribute(s), self can be directly use for calculation
class Formula:
    def square(self):
        return self * self

    def absolute(self):
        return abs(self)

    def max(self):
        max = self[0]
        for digit in self:
            if max <= digit:
                max = digit
        return max

    def min(self):
        min = self[0]
        for digit in self:
            if min >= digit:
                min = digit
        return min


def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45
