from decimal import Decimal

def count_up(start, stop, step):
    while start < stop:
        yield start
        start += Decimal(str(step))

for num in count_up(Decimal('1.2'), Decimal("2.01"), Decimal('0.01')):
    print(num)
if __name__ == "__main__":
    count_up()