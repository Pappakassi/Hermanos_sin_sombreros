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
        count = 0
        for _ in self.arr:
            count += 1

        print("Length of the list:", count)

        #make a new array that is one size bigger
        self.new_arr = [0] * (self.size+1)

        #copy elements from the old array into the new one
        for i in range(1,(count+1)):
            self.new_arr[i] = self.arr[i-1]

        #append the new element at the end
        self.new_arr[0] = value

        #print statements after appending
        print(f"PREPEND original array: {self.arr}")
        print(f"PREPEND new array: {self.new_arr}")
        
        return self.new_arr

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        """inserts a value at the given index"""
        # Check if the index is valid
        if index < -1 or index > len(self.arr)+1:
            raise IndexOutOfBounds()
        #It should be possible to add to the front and back of the list, and anywhere in between
        else:
            self.arr[index] = value

        return self.arr
    
    def insert_into_list(self, value, index):
        """TEST function : this function is based on the teachers demo,
            this method doesn't care about indexout of bounds
            it pushes the last value out of the list"""
        i = len(self.arr) - 1 #ef listinn er 4 stök, þá byrjum við með stak nr.3
        while i > index: #förum ekki lengra til vinstri en index'ið sem var sett inn
            self.arr[i] = self.arr[i-1] #stak nr. 4 fær gildið á staki nr.3
            #við erum að færa allt til hægri með því að 
            #gefa staki á ákveðnu indexi, gildið á stakinu sem var á undan
            i -=1 #svo lækkum við i'ið þar til það nær indexinum
        #þegar þessi lúppa er búin að rönna þá rönnar þetta hérna að neðan
        self.arr[index] = value

        return self.arr

    #Time complexity: O(1) - constant time
    def append(self, value):
        """Copies the contents of the old array into a new one.
        Adds a new item to the new array after the last item"""
        
        #make a new array that is one size bigger
        self.new_arr = [0] * (self.size+1)

        #copy elements from the old array into the new one
        for i in range(len(self.new_arr)-1):
            self.new_arr[i] = self.arr[i]

        #append the new element at the end
        self.new_arr[len(self.new_arr)-1] = value

        #print statements after appending
        print(f"original array: {self.arr}")
        print(f"new array: {self.new_arr}")
        
        return self.new_arr
    
    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # Sets the value at a specific location to a specific value
        # Overwrites the current value there
        # If the index is not within the current list, raise IndexOutOfBounds()
        # Initialize a counter
        length = 0

        # Use a while loop to count elements
        while True:
            try:
                _ = self.arr[length]
                length += 1
            except IndexError:
                break
        
        if length > index: #förum ekki lengra til vinstri en index'ið sem var sett inn
            self.arr[index] = value
        else:
            raise IndexOutOfBounds()
        
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

        if length > index: #förum ekki lengra til vinstri en index'ið sem var sett inn
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
        double_size = 2 * self.size
        self.new_array = [0] * double_size
        
        return self.new_array

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

    # arr_lis = ArrayList(3)
    # print(arr_lis)
    # arr_lis.insert(2,0)
    # print(arr_lis)
    
    # new_list = ArrayList(3)

    # new_list.insert_into_list(2,1)
    # print(new_list)

    arr_lis = ArrayList(3)
    arr_lis.insert(1,0)
    arr_lis.insert(2,1)
    arr_lis.insert(3,2)
    arr_lis.append(9)
    arr_lis.prepend(6)
    arr_lis.set_at(8,1)
    print(f"set at: {arr_lis}")

    value = arr_lis.get_at(1)
    print(f"This is the value: {value}")

    smalue = arr_lis.get_last()
    print(f"This is the value: {smalue}")