from csv import reader


def csv(fn):
    with open(fn, 'r', encoding='cp852') as db:
        for line in reader(db):
            print(line)
