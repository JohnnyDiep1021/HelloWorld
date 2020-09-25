# Utils is now an object
import Utils
# Can directly use the class or function without need the object
from Utils import Formula, lbs_to_kg, kg_to_lbs

# Directly import the function
from Package.Calculation import CalFunction

number = [2, 3, 5, 6, 9, 1, 2, 5, 6]
print(Formula.square(2))
print(Formula.min(number))
print(Utils.Formula.max(number))
print(lbs_to_kg(150))
print(kg_to_lbs(70))

print(CalFunction.calc_total(30, 30))
print(CalFunction.calc_average(30, 30))
# Ctrl / will be a shortcut for comment
