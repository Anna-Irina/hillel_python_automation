# https://docs.python.org/3/glossary.html#term-generator

n = 3
some_list = list(range(n))
print(some_list)

n = 50_000_000
some_list2 = list(range(n))
# # system monitor
# print(sum(some_list2))

# print(1)
# (itm for itm in range(n))
print(sum(itm for itm in range(n)))


# len vs generators
# g[1]
#
def gen(m):
    for num in range(m):
        # return num
        yield num
    yield m
    yield m + 1
    yield m + 2


g1 = gen(3)

# for val in g1:
#     print(val)

print(type(g1))
print(next(g1))
print(next(g1))
print(next(g1))


# print(next(g1))   # StopIteration Error


def prn_tree(rows):
    for i in range(1, rows + 1):
        yield f"{'*' * i:^{rows * 4}}"


g2 = prn_tree(15)
print(g2)
# print(list(g2))
print(*list(g2), sep='\n')


# read file by chunks
def read_in_chunks(fh, chunk_size):
    """Lazy function (generator) to read a file piece by piece."""
    i = 0
    while True:
        data = fh.read(chunk_size)
        if not data:
            break
        yield data
        i += 1
        print(f'Chunk #{i}')


with open('../../Lesson_11/big_file.txt') as big_fh:
    for i, _ in enumerate(read_in_chunks(big_fh, 1024), start=1):
        pass


########fh.close


def multi_yield():
    yield "First yield"
    yield "Second yield"
    yield "Third yield"
    yield "Fourth yield"


# Using the generator
my_generator = multi_yield()

print(next(my_generator))  # Prints "First yield"
print(next(my_generator))  # Prints "Second yield"
print(next(my_generator))  # Prints "Third yield"
print(next(my_generator))  # Prints "Fourth yield"
