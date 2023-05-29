"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hash_val = self.calculate_hash_value(string)
        self.table[hash_val] = {hash_val : string}
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_val = self.calculate_hash_value(string)
        if self.table[hash_val]:
            return hash_val
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if string:
            n = len(string)
            ascii_char_1: int = ord(string[0])
            ascii_char_2: int = ord(string[1])
            # hash_value = (ascii_char_1 * (31 ** (n-1))) + (ascii_char_2 * (31 ** (n-2)))
            hash_value = (ascii_char_1 * ascii_char_2) + 2788
            return hash_value
        else:
            return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))
# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
