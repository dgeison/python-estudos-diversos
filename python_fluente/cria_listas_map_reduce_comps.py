import timeit

symbols = "$¢£¥€¤"

# List comprehension
def list_comp():
    return [ord(s) for s in symbols if ord(s) > 127]

# Map + filter
def map_filter():
    return list(filter(lambda c: c > 127, map(ord, symbols)))

# Medir tempos (1 milhão de execuções)
time_comp = timeit.timeit(list_comp, number=1_000_000)
time_map = timeit.timeit(map_filter, number=1_000_000)

print(f"List comprehension: {time_comp:.4f}s")
print(f"Map + Filter: {time_map:.4f}s")
print(f"Diferença: {abs(time_comp - time_map):.4f}s")



# Separador visual entre os exemplos
print('\n' + '-' * 40 + '\n')

import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')