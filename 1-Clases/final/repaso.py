# String 
print("Hola mundo") 

# Integers 
print(5)
print(0)
print(-5)
print(1e5) # python soparta notación cienctifica

# complex
print(1+1j)

# float 
print(5.0)
print(0.0) 

# boolean
print(True)
print(False)

# Casting
int(5.0)

# variables 
soyUnaMentira = True
print(soyUnaMentira)

valorBase = 0
valorBase = valorBase + 3
print(valorBase)

# funciones 
def funcionSum2Num(a, b):
    print(a+b)

def funcionRes2Num(a,b):
    return b-a
    
funcionSum2Num(5, 5)
res =  funcionRes2Num(5, 5)
print(res)

# Listas 
a = []
a = list()
b = [5,0,3.4,8+4j,True,"texto",0]

b.append("último texto")
print(b)
b.pop()
print(type(b[5]))
b[0] = "STring"

b.reverse()
print(b)
print(help(b.reverse))

# Tuplas 
a = ()
b = (4,3,10)
print(b.count(3))
print(dir(b))
print("Traer el tercer elemento de b con b[2]: %d " % b[2])

# Diccionarios 
a =  {"5":"home", "gato":"cat", "azul":"blue"}

print(a["hogar"])
print(a)
print(type(a))



