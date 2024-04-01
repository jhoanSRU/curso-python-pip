def missing_number():
    og = [6,1,2,8,3,4,7,10,5]
    nl = []
    for i in range(len(og)):
        nl.append(min(og))
        og.remove(min(og))
      

    return (nl)

def sorting():
    org =[6,1,2,8,3,4,7,10,5]
   
    for i in range(len(org)):
        for j in range(len(org)-1-i):
            if org[j] > org[j+1] :
                org[j],org[j+1] = org[j+1], org[j]
            
    return(org)

def no_duplicate():
    nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

orden = list(sorting())
print(orden)