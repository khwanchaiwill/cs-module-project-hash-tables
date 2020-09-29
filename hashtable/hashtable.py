class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here

        # initialize capacity
        self.capacity = capacity
        # the buckets is empty array * capacity 
        self.buckets = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # return the len of the buckets list to hold the hash table data the number of slot in main list
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        
        return (self.buckets + 1) % self.capacity 

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # initailize the hashing string
        my_hash = str(key).encode()

        # initailize the sum to be the default as 0
        total = 0
        for byte in my_hash:
            # sum the total of string integer 
            total += byte
            # limit the total to 32 bits 
            total &= 0xFFFFFFFF
        # return the total that will modulo with the len( of hashing table ## slot later)
        return total
  

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # compute index of key
        index = self.hash_index(key)
        # initialize hash table to check base case
        # node = self.buckets[index]
        self.buckets[index] = value

       
       # if the bucket is empty: 
        # if node == None:
        #     # bucket hash table is store the added given key to hash table, and return until it hit the limit
        #     self.buckets[index] = HashTableEntry(key, value)

        #     return 
        # # prev = node
        # # check while node (bucket is not empty) and the node.key is not = the given key: then
        # while node is not None and node.key != key:
        #     prev = node
        #     node = node.next
        # if node is  None:

        #     prev.next = HashTableEntry(key, value)
        # else:
        #     node.value = value
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # node = self.buckets[index]
        self.buckets[index] = None
        # prev = None

        # if node.key == key:
        #     self.buckets[index] = node.next
        #     return
        # while node is not None and node.key != key:
        #     prev= node
        #     node = node.next

        # if node is None:
        #     return None
        # else:
        #     # self.size -= 1
        #     result = node.value

        #     if prev is None:
        #         node = None
        #     else:
        #         prev.next = prev.next.next

        #     return result
       
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value
  


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_capacity = self.capacity





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
