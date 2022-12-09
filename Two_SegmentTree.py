#Ternary

def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return list(map(int,input().split()))
def LIIS(): return list(map(int,input().split()))
    
class Two_SegmentTree():

    def __init__(self,init_sequence,identify,operator):
        self.n=len(init_sequence)
        self.tree=[identify]*(self.n*2)
        self.op=operator
        self.ide=identify

        for i, x in enumerate(init_sequence, self.n):
            self.tree[i] = x
            
        for i in range(self.n)[::-1]:
            self.tree[i]=operator(self.tree[i<<1],self.tree[i<<1|1])

    def update(self,index,value):
        index+=self.n
        self.tree[index]=value
        while index>1:
            index>>=1
            self.tree[index]=self.op(self.tree[index<<1],self.tree[index<<1|1])
            

    def query(self,left,right):
        left+=self.n
        right+=self.n
        left_value,right_value=self.ide,self.ide

        while left<right:
            if left&1:
                left_value=self.op(left_value,self.tree[left])
                left+=1

            if right&1:
                right-=1
                right_value=self.op(self.tree[right],right_value)
            
            left>>=1
            right>>=1
        
        return self.op(left_value,right_value)


