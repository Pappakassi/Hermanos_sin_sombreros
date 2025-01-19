def insert(self, value, index):
        """inserts a value at the given index"""
        # Check if the index is valid
        if index < -1 or index > self.count_items(self.arr)+1:
            raise IndexOutOfBounds()
        #It should be possible to add to the front and back of the list, and anywhere in between
        else:
            self.arr[index] = value

        return self.arr