#Ternary
class ternary_int(int):
    def __init__(self,value):
        self.value=value

    def __lshift__(self, other):
        self.value=self.value*pow(3,other)

    def __rshift__(self, other):
        self.value=self.value//pow(3,other)
    
class SegmentTree():

    def __init__(self,N,init_sequence,identify,operator):
        self.n=N
        self.tree=[identify]*((self.n*3-1)//2+1)
        self.op=operator
        self.ide=identify

        for i, x in enumerate(init_sequence, (self.n+1)//2):
            self.tree[i] = x
            
        for i in range(1,(self.n+1)//2)[::-1]:
            self.tree[i]=operator(self.tree[i*3-1],operator(self.tree[i*3],self.tree[i*3+1]))

    def update(self,index,value):
        index=(self.n+1)//2+index
        self.tree[index]=value
        while index>1:
            index=(index+1)//3
            self.tree[index]=self.op(self.tree[index*3-1],self.op(self.tree[index*3],self.tree[index*3+1]))
            

    def query(self,left,right):
        left+=(self.n+1)//2
        right+=(self.n+1)//2
        left_value,right_value=self.ide,self.ide

        while left<right-1:
            if left%3==0:
                left_value=self.op(left_value,self.op(self.tree[left],self.tree[left+1]))
                left+=2
            elif left%3==1:
                left_value=self.op(left_value,self.tree[left])
                left+=1
            

            if right%3==1:
                right-=2
                right_value=self.op(self.op(self.tree[right],self.tree[right+1]),right_value)
            elif right%3==0:
                right-=1
                right_value=self.op(self.tree[right],right_value)
            
            left=(left+1)//3
            right=(right+1)//3
        if left==right-1:
            return self.op(left_value,self.op(self.tree[left],right_value))
        else:
            return self.op(left_value,right_value)
