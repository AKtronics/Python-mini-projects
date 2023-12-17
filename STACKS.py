# A stack is a linear data structure that stores items in a Last In First Out way.
#In stack, elements are added at one end and an element is deleted from that end only. 
#The insert and delete operations are called push and pop operations.

#In this stack we will generally have five options:
#Push --> for inserting item in the stack above the previous item.
#Pop --> For deletion of the topmost item in the stack.
#Peek --> For showing the topmost item in the stack.
#Dispaly --> For showing the whole stack in order.
#Exit --> To exit the function


# STACK IMPLEMENTATION

def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False
    
def Push(stk,item):
     stk.append(item)
     top = len(stk) - 1
     
def Pop(stk):
    if isEmpty(stk):
        return("Underflow")
    
        #Underflow means stack is empty and you can not remove an item from an empty stack
    else:
        item =stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return item    
    
def Peek(stk):
    if isEmpty(stk):
        return("Underflow")
    else:
        top = len(stk) - 1
        return stk[top]
    
def Display(stk):
    if isEmpty(stk):
        print("Stack empty")
        #@Aktronics ;)
    else:
        top = len(stk) - 1
        print(stk[top]," <-- top")
        for a in range(top-1,-1,-1):
            print(stk[a])
