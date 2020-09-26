from csv import reader
from datetime import date


def csv(fn):
    with open(fn, 'r', encoding='cp852') as db:
        for line in reader(db, delimiter=';'):
            if not line[0] == 'ID':
                yield {
                    'meeting': date(*map(int, line[1].split('-'))),
                    'next_meeting': date(*map(int, line[19].replace('.', '-').split('-'))) if line[19] else None,
                    'notes': line[18],
                    'offer': {
                        'details': line[12],
                        'equipment': line[13],
                        'price': float(line[14]) if line[14] else None,
                        'method': line[15],
                        'status': line[16],
                        'rating': line[17],
                    },
                    'customer': {
                        'first_name': line[2],
                        'last_name': line[3],
                        'phone': line[9],
                        'address': {
                            'street': line[5],
                            'number': line[6],
                            'code': line[7],
                            'post': line[8],
                            'commune': line[10],
                            'county': line[11],
                            'city': line[4]
                        }
                    }
                }
