new_list = input()
new_2 = new_list.split(" ")
new_list_2 = [int(x) for x in new_2]
mod_list = [x + 1 for x in new_list_2]
print(mod_list)