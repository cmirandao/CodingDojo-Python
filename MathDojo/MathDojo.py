
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        newvalor=self.result #recibe y guarda el resultado de la operacion anterior
        #dependiendo si la tupla nums esta vacia o no realiza la suma
        if nums:
            self.result=sum(nums,num) #suma los valores entregados por parametro
            self.result+=newvalor #suma el valor guardado de la operacion anterior al resultado
        else:
            self.result=num+newvalor
        return self

    '''El metodo restar, resta los valores entregados por parametro
    y luego ese valor lo resta al resultado.
    Nota: En la plataforma de codingdojo indicaba que el resultado
    para x = md.add(2).add(2,5,1).restar(3,2).result era 5, pero no me parecia logico
    sumar los valores si el metodo se llama restar.'''
    def restar(self, num, *nums):
        newval=self.result #recibe y guarda el resultado de la operacion anterior
        #dependiendo si la tupla nums esta vacia o no realiza la resta
        if nums:
            for i in range(len(nums)):
                self.result=num-nums[i-1] #resta los valores entregados por parametro
                #resta el valor guardado de la operacion anterior al resultado
                self.result=newval-self.result
        else:
            self.result=newval-num
        return self
# crear una instancia:
md = MathDojo()
cm = MathDojo()
jk = MathDojo()
x = md.add(2).add(2,5,1).restar(3,2).add(6).result
y = cm.add(9,1).restar(3,7).result
z = jk.add(100,3,6,2).add(9,5).restar(45,2).restar(60).result
print("x: ",x)
print("y: ",y)
print("z: ",z)

