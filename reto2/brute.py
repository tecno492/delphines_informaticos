import string
from itertools import product
from time import time, sleep


def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
        # else:
        # print(''.join(p))
    sleep(0.25)

    return False


def bruteforce(password, min_nchar=1, max_nchar=8):
    print('Digits + ASCII lower / upper + punctuation')
    all_char = string.digits  # + string.ascii_letters + string.punctuation
    print(all_char)

    for le in range(min_nchar, max_nchar + 1):
        print("\t..%d char" % le)
        generator = product(all_char, repeat=int(le))

        p = product_loop(password, generator)

        if p is not False:
            return p


# EXAMPLE
start = time()
bruteforce('9999999999', 4, max_nchar=10)
end = time()
print('Total time: %.5f seconds' % (end - start))
