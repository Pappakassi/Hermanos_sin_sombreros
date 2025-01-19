


def count_items(array):
    # Initialize a counter
    length = 0

    # Use a while loop to count elements
    while True:
        try:
            _ = array[length]
            length += 1
        except IndexError:
            break
        
    return length