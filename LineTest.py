from Line import Line
li = Line((1.0,2.0),(-1.0,3.0),'red')
li.show()
print(f"length = {li.length() : .5f}")
li = Line((-1.0,3.0))
li.show()