from DataStructures import single_linked_list as sll

def new_stack():
    newstack = {
        "first":None,
        "last":None,
        "size":0,
    }
    return newstack

def push(stack, element):
    sll.add_first(stack, element)
    return stack    

def pop(stack, element):
    sll.remove_first(stack, element)
    return stack

def is_empty(stack):
    return sll.is_empty(stack)

def top(stack):
    return sll.first_element(stack)

def size(stack):
    return sll.size(stack)