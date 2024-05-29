#!/usr/bin/env python3
# Author ID:ykudo

# Place my_list below this comment (before the function definitions)

my_list = [ 1, 2, 3, 4, 5 ]


def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    my_list.append(my_list[-1] + 1)
    return my_list

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
   # my_list.remove(1)
   # my_list.remove(5)
   # my_list.remove(6)

    for new in items_to_remove:
        my_list.remove(new)

    return my_list

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)
