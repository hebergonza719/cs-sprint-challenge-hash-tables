def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    
    for x in range(length):
        weight = weights[x]
        if weight in hash_table:
            print(weight)
            value = hash_table[weight]
            return (x, value)
        diff = limit - weight
        hash_table[diff] = x

    return None

weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))