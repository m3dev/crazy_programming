from functools import reduce
from unicodedata import numeric
print(reduce(lambda map,numeric:numeric*map,map(numeric,'5000兆')))
