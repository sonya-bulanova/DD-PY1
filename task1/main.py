# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_ = [{'bin': bin(val),
          'dec': val,
          'hex': hex(val),
          'oct': oct(val)
          } for val in range(16)]
pprint(list_)