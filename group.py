def groups_of_3(old_list:list[int]) -> list[list[int]]:
    new_list = []
    for i in range(0,len(old_list),3):
        new_list.append(old_list[i:i+3])
    return new_list

    



