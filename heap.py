class heap:
    def __init__(self):
        self.items = []

    def swap(self,index1,index2):
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp
        
    def heappush(self,x):
        self.items.append(x)
        #self.print()
        self._shiftdown(self.size()-1)

    def heappop(self,index):
        temp = self.items[index]
        self.items[index] = self.items[self.size()-1]
        self.items.pop(self.size()-1)
        self._shiftup(index)
        self._shiftdown(self.size()-1)
        return temp

    def _shiftdown(self,n):
        index = n
        while(index != 0 and self.items[index//2] > self.items[index]):
            self.swap(index//2,index)
            index = index // 2
            self.print2()

    def _shiftup(self,n):
        index = n
        while(1):
          try:  
            if(self.items[index*2+1] < self.items[index*2+2]):
                
                    self.swap(index*2+1,index)
                    index = index *2+1
            else:
                    self.swap(index*2+2,index)
                    index = index *2+2   
            self.print2()    
          except IndexError:
            break       

    def size(self):
        return len(self.items)

    def print(self):
            print(self.items)

    def print2(self):
            count = 0
            print(" ")
            print("start")
            print(" ")
            for i in range(self.size()):
                if(count == i):
                    print(self.items[i])
                    print(" ")
                    count *= 2
                    count += 2
                else:
                    print(str(self.items[i])+" ", end="")
                    if(i % 2 == 0):
                        print(" ",end="")
            print(" ")
            print(" ")
            print("end")
                

test = heap()
test.heappush(3)
test.heappush(2)
test.heappush(1)
test.heappush(4)
test.heappush(6)
test.heappush(8)
test.heappush(6)
test.heappush(9)
test.heappush(10)
test.heappush(5)
test.print2()