letter = input("Pelse enter the first letter: ")
begin = input("Please enter the list of words: ")
begin_2 = begin.split()
final = [x for x in begin_2 if x.lower().startswith(letter)]
print(final)