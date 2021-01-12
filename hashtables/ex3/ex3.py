def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []

    for i in arrays:
        for number in i:
            if number not in hash_table:
                hash_table[number] = 1
            else:
                hash_table[number] += 1
        
    for key, value in hash_table.items():
        if value == len(arrays):
            result.append(key)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
