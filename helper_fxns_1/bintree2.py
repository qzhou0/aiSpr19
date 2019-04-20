#! /usr/bin/python
import sys

def main():
    print('hey')
    
    Process(sys.argv[1],sys.argv[2])


class Node:
    def __init__(self, data):
        self.value = data
        self.smaller = None
        self.larger = None
        
    def __str__(self):
        return str(self.value)

class BinTree:
    def __init__(self, A = None):
        # A is an optional argument containing a list of values to be inserted into the binary tree just after cosntruction
        self.root = None
        self.size= 0
        if A:
            [self.insert(x) for x in A]
            
    def insert(self, V):
        # inserts a new value 
        newNode = Node(V)
        
        if self.size==0:
            self.root = newNode
            self.size+=1
        else:
            flying = self.root
            dragged = flying

            while flying:
                
                if V < flying.value:
                    dragged = flying
                    flying = flying.smaller
                    
                elif V>flying.value: 
                    dragged = flying
                    flying = flying.larger
                else:
                    return
            if V < dragged.value:
                dragged.smaller = newNode
            else: 
                dragged.larger = newNode
            self.size+=1
        
    def has(self, V):
        # returns True if V is in the list, else False
        flying = self.root
        
        while flying:
            if V==flying.value:
                return True
            elif V<flying.value:
                flying=flying.smaller
            else:
                flying = flying.larger
                return False
            
    def has_depth(self, V):
        # returns True if V is in the list, else False
        flying = self.root
        d = 1
        while flying:
            
            if V==flying.value:
                return d
            elif V<flying.value:
                flying=flying.smaller
                
            else:
                flying = flying.larger
            d+=1
            
        return d-1
        
    def get_ordered_list(self):
        # returns a list of all values in ordered sequence
        if self.size == 0:
            return []
        return self.get_ordered_listH(self.root)

    def get_ordered_listH(self,rt):
        # returns a list of all values in ordered sequence of rt, assumes rt != None
        #print("here for entry %s" % rt.value)
        if not rt.smaller:# smaller = None
            lout = [rt.value]
        else:
            lout = self.get_ordered_listH(rt.smaller)
            lout.append(rt.value)
            
        if not rt.larger:
            return lout
        lout+=self.get_ordered_listH(rt.larger)#is there a way to do this more efficiently?
        return lout
       
    def clear(self):
        # clears the list of all nodes
        self.clearR(self.root)
        self.root = None
        self.size = 0
        
    def clearR(self,treeNode):
        #does not take care of node itself
        if treeNode.smaller:
            self.clearR(treeNode.smaller)
            treeNode.smaller = None
        if treeNode.larger:
            self.clearR(treeNode.larger)   
            treeNode.larger = None
            
        #print('all null beneath %s' % treeNode.value)
        
def Process(infile, outfile):
    try:
        f=open(infile, 'r')#U deprecated
        lines=f.read().split('\n')
        f.close()
        #^^^ read infile ^^^
    
        #bintree of ints from line 1
        sints = lines[0].split(',')
        ints=[int(i) for i in sints]
        print(ints)
        BT = BinTree(ints)
        print(BT.get_ordered_list())
        
        targets = lines[1].split(',')
        print(targets)
        depths=[BT.has_depth(int(i)) for i in targets]
        Sdepths=[str(d) for d in depths]
        print(depths)
        
        f=open(outfile,'w')
        f.write(','.join(Sdepths)+'\n')
        f.close()

        print ("size:",BT.size)
        print ("average:", sum(depths)/len(depths))

    except:
        print('no file found')
    

main()
      
    
