def list_to_cubed_dict(numbers):
    return {number:number**3 for number in numbers}

numbers = [1,2,3,4,5]
output_dict = list_to_cubed_dict(numbers)
print(output_dict)

