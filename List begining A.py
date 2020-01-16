begin = input()
begin_2 = begin.split()
final = [x for x in begin_2 if x.lower().startswith('a')]
print(final)