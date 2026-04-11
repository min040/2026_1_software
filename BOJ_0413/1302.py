n = int(input())
books = {}

for _ in range(n):
    name = input()
    books[name] = books.get(name, 0) + 1

max_cnt = max(books.values())

candidates = [k for k in books if books[k] == max_cnt]
print(sorted(candidates)[0])