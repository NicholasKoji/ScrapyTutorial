import json

def parse():
    yield from list(range(10))

if __name__ == '__main__':
    d = parse()
    for a in d:
        print(a)