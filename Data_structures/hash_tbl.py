
class hashTbl:

    def __init__(self,size):
        self.slots = [None] * size
        self.data = [None] * size
        self.size = size
    
    def put(self,key,value):
        
        # get a hash_value to decide a spot
        hash_value = self.hashFunc(key,self.size)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        
        else:
            next_slot = self.rehash(key,self.size)

            print(next_slot)

            while(self.slots[next_slot] != None and self.slots[next_slot] != key ):
                next_slot = self.rehash(next_slot,self.size)
            

            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = value
            
            else:
                self.data[next_slot] = value


    def get(self,key):

        hash_value = self.hashFunc(key,self.size)

        if self.slots[hash_value] == key:
            return self.data[key]
        
        else:
            next_slot = self.rehash(key,self.size)

            while(self.slots[next_slot] != None and self.slots[next_slot] != key):
                next_slot = self.rehash(next_slot,len(self.slots))

            if self.slots[next_slot] == key:
                return self.data[next_slot]
        




    def hashFunc(self,key,size):
        return key%size
    

    def rehash(self,key,size):
        return (key % size)+1

    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,value):
        self.put(key,value)


h = hashTbl(8)

#h.put(1,'One')

#h.put(9,'Three')

h[1] = 'One'

h[2] = 'Two'

h[9] = 'Three'


print(h.get(9))