#!C:/python36/python

def glue(x,length,str):
    """ glues the string of digits together """
    if length == 0:
        if str.find("_") < 0:
            print(str)
        return
    for i in x:
        glue(x,length-1,str+i)


x = "19"
y = sorted(x)
for i in range(1,len(y)):
# very bad form
    if   y[i] == y[i-1] and y[i-1] != "_":
        y[i] = "_"
    elif y[i-1] == "_" and y[i] == y[i-2]:
        y[i] = "_"
    elif y[i-2] == "_" and y[i] == y[i-3]:
        y[i] = "_"
        

glue(y,5,"")
