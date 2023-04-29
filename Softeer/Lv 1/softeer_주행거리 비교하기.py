A, B = map(int, input().split())

def compare(A, B):
    if(A>B):
        print("A")
    elif(A<B):
        print("B")
    else:
        print("same")
    
compare(A, B)