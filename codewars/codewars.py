

def fold_array(array, runs):
    for i in range(runs):
        x = int((len(array)-1)/2)
        if len(array)%2 !=0:
            b = array[:x]
        b = array[:x+1]
        c = array[x+1:]
        c.reverse()
        array = [b[i] + c[i] for i in range(len(b))]
        if len(array) %2 != 0:
            array.append(array[x])
        return array



def digital_root(n):
    x = True
    while x:
        n = sum(list(map(int,str(n))))
        if len(str(n)) == 1:
            x = False

    return n