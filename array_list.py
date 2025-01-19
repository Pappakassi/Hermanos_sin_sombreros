import functions

class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    "Raised when an array is empty"
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * self.size

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        """Returns a string representation of the ArrayList"""

        #Returns a string with all items from the array
        #Have a comma and a space between them
        # but no brackets ([ ]) around them
        return f"ArrayList: {', '.join(map(str, self.arr))}"
    

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        """Add a new value add index 0 and move all other values to the right"""

        #This might be cheating, but since we cannot use the len() function,
        #maybe this is ok ?
        #count = 0
        #for _ in self.arr:
    
        length = self.count_items(self.arr)
        print("Length of the list:", length)
        pre_value = self.insert(value, 0)
        print(f"prevuale : {pre_value}")
        #make a new array that is one size bigger
        #self.new_arr = [0] * (self.size+1)

        #copy elements from the old array into the new one
        #for i in range(1,(length+1)):
        #    self.new_arr[i] = self.arr[i-1]

        #append the new element at the end
        #self.new_arr[0] = value

        #print statements after appending
        #print(f"PREPEND original array: {self.arr}")
        #print(f"PREPEND new array: {self.new_arr}")
        
        #return self.new_arr

    
    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        """TEST function : this function is based on the teachers demo,
            this method doesn't care about indexout of bounds
            it pushes the last value out of the list"""
        
        #error checking
        if index < -1 or index > self.count_items(self.arr)+1:
            raise IndexOutOfBounds()
        else:
            length = self.count_items(self.arr)
            i = length - 1
            while i > index:
                self.arr[i] = self.arr[i-1]
                i -=1
            self.arr[index] = value

            return self.arr

    #Time complexity: O(1) - constant time
    def append(self, value):
        """Our append method"""
        length = self.count_items(self.arr)
        print("Length of the list:", length)
        pre_value = self.insert(value, (length-1))
        print(f"some stuff here : {pre_value}")
    
    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # Sets the value at a specific location to a specific value
        # Overwrites the current value there
        # If the index is not within the current list, raise IndexOutOfBounds()
        # Initialize a counter
        length = self.count_items(self.arr)
        
        if length > index: #förum ekki lengra til vinstri en index'ið sem var sett inn
            self.arr[index] = value
        else:
            raise IndexOutOfBounds("Index out of bounds!")
        
        return self.arr

    #Time complexity: O(1) - constant time
    def get_first(self):
        if not self.arr:
            raise Empty("The container is empty!")
        else:
            return self.arr[0]
            
    def count_items(self, array):
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

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        #Returns the value at a specific location in the list
        #If the index is not within the current list, raise IndexOutOfBounds()
        
        length = self.count_items(self.arr)

        if not self.arr:
            raise Empty("List is empty!")
        elif length > index: 
            return self.arr[index]
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        length = self.count_items(self.arr)

        if not self.arr:
            raise Empty("The container is empty!")
        else:
            return self.arr[length-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        #Re-allocates memory for a larger array and populates it with the original array’s items
        #Rule of Thumb: Double the Size
        length = self.count_items(self.arr)

        double_size = 2 * length
        new_array = [0] * double_size

        print(f"new array: {new_array}")

        i = 0

        while self.arr[i] <= (length-1):
            #while the length of the array is the old length, it keeps on adding elements
            #we are using the get_at() method and the append() to put the new value
            self.new_array = self.append((self.arr)[i])
            i += 1

        #here we have to copy the elements of the old array into the new one

        
        return new_array

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    print("-------------------")
    new_list = ArrayList(3)
    print(new_list)
    new_list.append(2)
    print(new_list)
    
    new_list.set_at(8,2)
    print(f"changed list : {new_list}")
    new_list.set_at(3,0)
    print(f"changed list : {new_list}")

    new_list.resize()
    print(new_list)
