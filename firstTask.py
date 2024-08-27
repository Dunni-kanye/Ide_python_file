def find_values_in_tuple(tuple2):
    list_value = tuple2[1]
    tuple_value = tuple2[2]
    value = [20, 25]
    result = []
    for target in value:
        if target in list_value:
            result.append((list_value.index(target),target))
        elif target in tuple_value:
            result.append((tuple_value.index(target), target))
            return tuple(result)
tuple2 = ("orange",[10,20,30],(5,15,25))
print(find_values_in_tuple(tuple2))
