with open("Reviews.csv", 'r') as r, open('text.csv', 'w') as t:
    for i, line in enumerate(r):
        print(i)
        if i == 0:
            continue
        t.write(','.join(line.split(',')[9:]))