class student:
    def __init__(sel,name,age):
        sel.name = name
        sel.age = age
        sel.la = sel.lap()

    def show(sel):
        print(sel.name , sel.age)
        sel.la.show()


    class lap:

        def __init__(sel):
            sel.brand='hp'
            sel.cpu='i5'
        
        def show(sel):
            print(sel.brand,sel.cpu)





s1 = student('sree',3) 
s1.show()
