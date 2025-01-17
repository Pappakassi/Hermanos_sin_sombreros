class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
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

        #return f"ArrayList: {self.arr}"
        return f"ArrayList: {', '.join(map(str, self.arr))}"
    

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

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
        """TEST : this function is based on the teachers demo,
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
        #Copy the contents of the old array into the new one, one element at a time.
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        pass

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

    arr_lis = ArrayList(3)
    print(arr_lis)
    arr_lis.insert(2,0)
    print(arr_lis)
    
    new_list = ArrayList(3)

    new_list.insert_into_list(2,1)
    print(new_list)