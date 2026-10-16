import math        
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        raise NotImplementedError(f"subclasses should implement in this method")
    def perimeter(self):
        raise NotImplementedError(f"subclasses should implement in this method")
    def display_name(self):
        return f"The geometric name is {self.name}"
class Rectangle(Shape):
    def __init__(self, name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def diagonal(self):
        return math.sqrt(self.length**2+self.width**2)
    
    def aspect_ratio(self):
        return self.length/self.width
    def compare_area(self,other):
        
        if self.area()>other.area():
            return f"Rectangle A  {self.name} is bigger than  Rectangle B {other.name} "
        elif self.area()<other.area():
            return f"Rectangle A {self.name} is smaller than Rectangle B {other.name} "
        else:
            return f"Rectangle A {self.name} and Rectangle B {other.name} are equal"
    def compare_perimeter(self,other):
        if self.perimeter()>other.perimeter():
           return f"The perimeter A {self.name} is bigger than perimeter B {other.name}"
        elif self.perimeter()<other.perimeter():
            return f"The perimeter  A {self.name}  is smaller than perimeter B{other.name}"
        else:
            return f"The perimeter A{self.name}  and perimeter B {other.name} are equal"
    def compare_length(self,other):
        if self.length>other.length:
           return f"Rectangle A {self.name} longer than Rectangle B {other.name}"
        elif self.length<other.length:
            return f"Rectangle A {self.name} shorter than Rectangle B {other.name}"
        else:
            return f"The length of Rectangle A {self.name} and length of Rectangle B{other.name} is Equal"
    def compare_width(self,other):
        if self.width>other.width:
            return f"Width of Rectangle A {self.name} is bigger than width Rectangle b {other.name}"
        elif self.width<other.width:
            return f"Width of Rectangle A {self.name} is Smaller than width of Rectangle B"
        else:
            return(f"The width of rectangle A {self.name} is Equal with width of rectangle B {other.name} ")
    def is_square(self):
        if self.length==self.width:
            return f"{self.name} is square"
        else:
            return("The length and the width are not equal the form is not square")
    def __str__(self):
        return f"{self.name}: length= {self.length} ,width= {self.width}"
    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Length: {self.length}\n"
            f"Width: {self.width}\n"
            f"Area: {self.area()}\n"
            f"Perimeter : {self.perimeter()}\n"
            f"Diagonal: {self.diagonal():.2f}\n"
            f""
        )      
class Square(Shape):
    def __init__(self, name,side_length):
        super().__init__(name)
        self.side_length=side_length
    def area(self):
        return self.side_length**2
    def perimeter(self):
        return self.side_length*4
    def diagonal(self):
        return self.side_length*math.sqrt(2)
    def compare_area(self,other):
        if self.area()>other.area():
            return f"Square {self.name} Bigger than Square {other.name}"
        elif self.area()<other.area():
            return f"Square {self.name} Smaller than Square {other.name}"
        else:
            return f"Squares are equal"
    def __str__(self):
        return f"Name: {self.name} Length side :{self.side_length}"
    def display_info(self):
        return(
            f"Name: {self.name}\n"
            f"-------------------\n"
            f"Length Side: {self.side_length}\n"
            f"Area: {self.area()}\n"
            f"Perimeter: {self.perimeter()}\n"
            f"Diagonal: {self.diagonal():.2f}\n"
        )
class Triangle(Shape):
    def __init__(self, name,side_a,side_b,side_c):
        super().__init__(name)
        self.side_a=side_a
        self.side_b=side_b
        self.side_c=side_c
    def perimeter(self):
        return self.side_a+self.side_b+self.side_c
    def area(self):
        if not self.is_valid():
            return "Invalid Triangle"
        s=(self.side_a+self.side_b+self.side_c)/2
        return math.sqrt(s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c))
    def calculate_angle(self):
        angle_a=math.acos(
            (self.side_b**2+self.side_c**2-self.side_a**2)/
            (2*self.side_b*self.side_c)
        )
        angle_b=math.acos(
            (self.side_a**2+self.side_c**2-self.side_b**2)/
            (2*self.side_a*self.side_c)
        )
        angle_c=math.acos(
            (self.side_a**2+self.side_b**2-self.side_c**2)/
            (2*self.side_b*self.side_a)
        )
        return math.degrees(angle_a), math.degrees(angle_b),math.degrees(angle_c)
    def calculate_hypotenuse(self):
        a=self.side_a
        b=self.side_b
        hypotenuse=math.sqrt(a**2+b**2)
        return hypotenuse
    def calculate_missing_leg(self):
        c=self.side_c
        b=self.side_b
        side=math.sqrt(c**2-b**2)
        return side
    def distance_between_points(self,x1,y1,x2,y2):
        point=math.sqrt((x2-x1)**2+(y2-y1)**2)
        return point
    def midpoint(self,x1,y1,x2,y2):
        d=((x1+x2)/2,(y1+y2)/2)
        return d
    def centroid(self,x1,y1,x2,y2,x3,y3):
        center=((x1+x2+x3)/3,(y1+y2+y3)/3)
        return center
    def is_valid(self):
        return(
            self.side_a+self.side_b>self.side_c and
            self.side_a+self.side_c>self.side_b and
            self.side_b+self.side_c>self.side_a
        )
    def triangle_type(self):
        if self.side_a==self.side_b==self.side_c:
            return "Equilateral Triangle"
        elif self.side_a==self.side_b or self.side_a==self.side_c or self.side_b==self.side_c:
            return "Isosceles Triangle"  
        else:
            return"scalene triangle"
    def display_info(self):
        angle_a,angle_b,angle_c=self.calculate_angle()
        return(
            f"Name :{self.name}\n"
            f"{'-'*15}\n"
            f"Side (A):{self.side_a}\n"
            f"Side (B) : {self.side_b}\n"
            f"Side (C) : {self.side_c}\n"
            f"{'-'*15}\n"
            f"Triangle Perimeter: {self.perimeter()}\n"
            f"Triangle Area : {self.area():.2f}\n"
            f"Triangle calculate angles (A),(B),(C) :\n"
            f"A: {angle_a :.2f}, B: {angle_b:.2f}, C: {angle_c :.2f}\n"
            f"Calculate Hypotenuse : {self.calculate_hypotenuse():.2f}\n"
            f"Calculate missing leg : {self.calculate_missing_leg():.2f}\n"
           
        )
class Circle(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def circumference(self):
        return 2*math.pi*self.radius
    def diameter_cal(self):
        return 2*self.radius
    def radius_cal(self,diametre):
        return diametre/2
    def arc_length(self,o):
        return o/360*2*math.pi*self.radius
    def sector_area(self,o):
        return o/360*math.pi*self.radius**2
    def distance_from_center(self,x,h,y,k):
        return math.sqrt((x-h)**2+(y-k)**2 )
    def point_position(self,x,h,y,k):
        distance=self.distance_from_center(x,h,y,k)
        if distance<self.radius:
            return "The point is inside The circle"
        elif distance>self.radius:
            return "The point is outside The circle"
        else:
            return"The point is on The circle"
    def display_info(self):
        return(
            f"Name: {self.name}\n"
            f"Area: {self.area():.2f}\n"
            f"circumference: {self.circumference():.2f}\n"
            f"Diameter: {self.diameter_cal():.2f}\n"
            f"Radius: {self.radius:.2f}\n"
            
        )
class Cube(Shape):
    def __init__(self, name,side_length):
        super().__init__(name)
        self.side_length=side_length
    def area(self):
        return self.side_length**2
    def total_surface_area(self):
        return 6*self.side_length**2
    def volume(self):
        return self.side_length**3
    def face_diagonal(self):
        return self.side_length*math.sqrt(2)
    def space_diagonal(self):
        return self.side_length*math.sqrt(3)
    def total_edge_length(self):
        return 12*self.side_length
    def display_info(self):
        return(
            f"Name: {self.name}\n"
            f"Area: {self.area():.2f}\n"
            f"Total surface area {self.total_surface_area():.2f}\n"
            f"Volume {self.volume():.2f}\n"
            f"Face Diagonal : {self.face_diagonal():.2f}\n"
            f"Space Diagonal : {self.space_diagonal():.2f}\n"
            f"Total edge length {self.total_edge_length():.2f}"
        )
class Cylinder(Shape):
    def __init__(self,name,radius,height):
        super().__init__(name)
        self.radius=radius
        self.height=height
    def calculate_base_area(self):
        return math.pi*self.radius**2
    def calculate_base_circumference(self):
        return 2*math.pi*self.radius
    def calculate_volume(self):
        return math.pi*(self.radius**2*self.height)
    def calculate_diameter(self):
        return 2*self.radius
    def calculate_lateral_surface_area(self):
        return 2*math.pi*(self.radius*self.height)
    def calculate_total_surface_area(self):
        return 2*math.pi*(self.radius*self.height)+2*math.pi*(self.radius**2)
    def display_info(self):
        return(
            f"Name: {self.name}\n"
            f"Base area : {self.calculate_base_area():.2f}\n"
            f"Base circumference :{self.calculate_base_circumference():.2f}\n"
            f'Volume : {self.calculate_volume():.2f}\n'
            f"Diameter: {self.calculate_diameter():.2f}\n"
            f"Lateral Surface Area: {self.calculate_lateral_surface_area():.2f}\n"
            f"Total Surface Area: {self.calculate_total_surface_area():.2f}"

        )
class Sphere(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius=radius
    def diameter(self):
        return 2*self.radius
    def surface_area(self):
        return 4* math.pi*self.radius**2
    def volume(self):
        return 4/3*(math.pi*self.radius**3)
    def display_info(self):
        return(
            f"Name: {self.name}\n"
            f"Diameter : {self.diameter():.2f}\n"
            f"Surface area: {self.surface_area():.2f}\n"
            f"Volume: {self.volume():.2f}\n"
        )
spheres=[]
cylinders=[]
cubes=[]
circles=[]       
shaps=[]
rectangles=[]
squares=[]
triangles=[]
while True:
    print("Welcome to Shapes Application")
    print("-"*30)
    print("Our shapes")
    print("-"*30)
    print("1-Rectangle")
    print("2-Square")
    print("3-Triangle")
    print("4-Cube")
    print("5-Cylinder")
    print("6-Circle")
    print("7-Sphere")
    print("8-Exit")
    print("-"*30)
    try:
        choice=int(input("Enter a number of shape to start :"))
        if choice <1 or choice>8:
            print("Invalid number!! enter a number in range 1 and 8")
    except ValueError:
        print("You should enter a number to start")
        continue
    if choice==1:
        while True:
            print("Rectangle Menu :")
            print("-"*20)
            print("1-Add rectangle")
            print("2-Display rectangles")
            print("3-Remove rectangle")
            print("4-Edit rectangle")
            print("5-Compare rectangles")
            print("6-Operation")
            print("7-Back")
            try:
                rectangle_choice=int(input("Enter a number btween 1 and 7 : "))
                if rectangle_choice <1 or rectangle_choice>7:
                    print("Invalid Choice: Enter a number in range 1 and 7")
                    continue
            except ValueError:
                print("You should enter a number to start ")
                continue
            if rectangle_choice==1:
                print("Follow all step to add new rectangle ")
                try:
                    rectangle_name=input("Enter a rectangle name :")
                    rectangle_length=int(input("Enter rectangle length :"))
                    rectangle_width=int(input("Enter rectangle width :"))
                except ValueError:
                    print("You should Enter at last one letter for name and number for length and width")
                    continue
                new_rectangle=Rectangle(rectangle_name,rectangle_length,rectangle_width)
                rectangles.append(new_rectangle)
                print("Rectangle added")
            elif rectangle_choice==2:
                print("Rectangles List :")
                print("-"*25)
                if not rectangles:
                    print("There are not any rectangle")
                else:
                    for rectangle in rectangles:
                        print(rectangle.display_info())
                        print("-"*25)
            elif rectangle_choice==3:
                print("Follow steps to delete A rectangle")
                delete_rectangle=input("Enter the name of rectangle you want to delete :")
                for rectangle in rectangles:
                    if rectangle.name.lower().strip()==delete_rectangle.lower().strip():
                        rectangles.remove(rectangle)
                        print("Delete Done")
                        break
                else:
                    print("Please enter a name exists in rectangles list to delete")
            elif rectangle_choice==4:
                print("follow all steps tp edit a rectangle")
                rectangle_to_edit=input("Enter rectangle name to edit :")
                found_rectangle=None
                for rectangle in rectangles:
                    if rectangle.name.lower().strip()==rectangle_to_edit.lower().strip():
                        found_rectangle=rectangle
                        break
                if found_rectangle is None:
                    print(f"Rectangle {rectangle_to_edit} is not exists")
                    continue
                print(f"Rectangle {found_rectangle}")
                while True:
                    print("what do you want to edit ")
                    print("1-Edit name")
                    print("2-Edit length")
                    print("3-Edit width")
                    print("4-Edit all")
                    print("5-Back")
                    try:
                        edit=int(input("Enter a number of your choice to start :"))
                        if edit<1 or edit>5:
                            print("Invalide choice: Enter a number in range 1 and 5")
                            continue
                    except ValueError:
                        print("you should enter a number to start")
                        continue
                    if edit==1:
                        new_name=input("Enter new name:")
                        found_rectangle.name=new_name
                        print("Rectangle name edited")
                        continue
                    elif edit==2:
                        try:
                            new_length=int(input("Enter new length:"))
                            found_rectangle.length=new_length
                            print("length edited")
                            continue
                        except ValueError:
                            print("Invalid Value: Length should be a number")
                            continue
                    elif edit==3:
                        try:
                            new_width=int(input("Enter a new width: "))
                            found_rectangle.width=new_width
                            print("width Edited")
                            continue
                        except ValueError:
                            print("Invalid Value: Width should be a number")
                    elif edit==4:
                        print("complete all steps to edit name,length,width")
                        try:
                            new_name=input("Enter a rectangle new name :")
                            new_length=int(input("Enter a rectangle new length:"))
                            new_width=int(input("Enter a rectangle new width:"))
                            found_rectangle.name=new_name
                            found_rectangle.length=new_length
                            found_rectangle.width=new_width
                            print("Rectangle name,length,width Edited")
                            continue
                        except ValueError:
                            print("Invalid Value:You should enter number in length,width")
                            continue
                    elif edit==5:
                        print("You press exist")
                        break
            elif rectangle_choice==5:
                print("follow all steps to  compare two rectangles :")
                rectangle_a=input("Enter rectangle A name :")
                found_rectangle_a=None
                for rectangle in rectangles:
                    if rectangle.name.lower().strip()==rectangle_a.lower().strip():
                        found_rectangle_a=rectangle
                        break
                if found_rectangle_a is None:
                    print(f"Rectangle {rectangle_a} not found") 
                print(f"Rectangle {found_rectangle_a} found")
                rectangle_b=input("Enter Rectangle B name :") 
                found_rectangle_b=None
                for rectangle in rectangles:
                    if rectangle.name.lower().strip()==rectangle_b.lower().strip():
                        found_rectangle_b=rectangle
                        break
                if found_rectangle_b is None:
                    print(f"Rectangle {rectangle_b} not found")
                print(f"Rectangle {found_rectangle_b}found")
                while True:
                    print("choice what do you want to compare:")
                    print("-"*25)
                    print("1-compare area")
                    print("2-compare perimeter")
                    print("3-compare length")
                    print("4-compare width")
                    print("5-Exist")
                    try:
                        choice=int(input("Enter number operation :"))
                        if choice<1 or choice>5:
                            print("Please enter a number between 1 and 5")
                            continue
                    except ValueError:
                        print("Invalid value: You should enter a number ")
                        continue
                    if choice == 1:
                        print(found_rectangle_a.compare_area(found_rectangle_b))
                        continue
                    elif choice==2:
                        print(found_rectangle_a.compare_perimeter(found_rectangle_b))
                        continue
                    elif choice==3:
                        print(found_rectangle_a.compare_length(found_rectangle_b))
                        continue
                    elif choice==4:
                        print(found_rectangle_a.compare_width(found_rectangle_b))
                        continue
                    else:
                        print("you print exist")
                    break
            elif rectangle_choice==6:
                print("Operation Menu")
                print("-")
                while True:
                    print("choice an operation")
                    print("1-calculate ratio")
                    print("2-check if rectangle is square")
                    print("3-Exit")
                    try:
                        choice=int(input("Enter your choice number :"))
                        if choice<1 or choice>3:
                            print("Invalid number: number should be in range 1 and 3")
                            continue
                    except ValueError:
                        print("Invalid Value:You should enter number to start")
                        continue
                    if choice==1:
                        rectangle_cal_ratio=input("Enter rectangle name :")
                        found_rectangle=None
                        for rectangle in rectangles:
                            if rectangle.name.lower().strip()==rectangle_cal_ratio.lower().strip():
                                found_rectangle=rectangle
                                break
                        if found_rectangle is None:
                            print(f"Rectangle {rectangle_cal_ratio} not found")
                            continue
                        print(f"Rectangle {rectangle_cal_ratio} found ")
                        print(
                            f"Aspect ratio of {found_rectangle.name}"
                            f"Is: {found_rectangle.aspect_ratio():.2f}"
                        )
                    elif choice==2:
                        rectangle_check=input("Enter Rectangle name:")
                        found_rectangle=None
                        for rectangle in rectangles:
                            if rectangle.name.lower().strip()==rectangle_check.lower().strip():
                                found_rectangle=rectangle
                                break
                        if found_rectangle is None:
                            print(f"rectangle {rectangle_check} not found")
                            continue
                        print(f"Rectangle {rectangle_check} found")
                        print(found_rectangle.is_square())
                    else:
                        print("You press exit")
                        break
            elif rectangle_choice==7:
                print("you press exit")
                break
    elif choice==2:
        while True:
            print("Square Menu")
            print("-")
            print("1-Add square")
            print("2-Display squares")
            print("3-Edit square")
            print("4-Delete square")
            print("5-compare squares")
            print("6-Exit")
            try:
                square_choice=int(input("Enter a number of operation :"))
                if square_choice<1 or square_choice>6:
                    print("Invalid Choice: you should enter a number in range 1 and 6")
                    continue
            except ValueError:
                print("Error: You should enter a number to start")
                continue
            if square_choice==1:
                print("Follow all steps to add a square:")
                try: 
                    square_name=input("Enter square name :")
                    side_length=int(input("Enter  square side length :"))
                except ValueError:
                    print("Invalid Value: You should enter a number:")
                    continue
                new_square=Square(square_name,side_length)
                squares.append(new_square)
                print("Square added")
            elif square_choice==2:
                print("Squares list:")
                print("-"*25)
                if not squares:
                    print("There is no square in list")
                else:
                    for square in squares:
                        print(square.display_info())
                        print("-"*25)
            elif square_choice==3:
                print("follow all step to edit square")
                square_name=input("Enter square name to edit :")
                found_squre=None
                for square in squares:
                    if square.name.lower().strip()==square_name.lower().strip():
                        found_squre=square
                        break
                if found_squre is None:
                    print(f"Square {square_name} is not found")
                    continue
                print (f"square {square_name} found")
                while True:
                    print("what do you want to Edit")
                    print("1-Edit name")
                    print("2-Edit side length")
                    print("3-Edit all")
                    print("4-Exit")
                    try:
                        square_edit_choice=int(input("choice what do you want to  edit in square :"))
                        if square_edit_choice <1 or square_edit_choice>4:
                            print("Invalid Choice: You should enter a number between 1 and 3")
                            continue
                    except ValueError:
                        print("Value Error: you should enter a number")
                    if square_edit_choice==1:
                        new_name=input("Enter square new name:")
                        found_squre.name=new_name
                        print("Square name edited")
                    elif square_edit_choice==2:
                        try:
                            new_side_length=int(input("Enter a new square side length:"))
                            found_squre.side_length=new_side_length
                            print("Square side length edited")
                            continue
                        except ValueError:
                            print("Value Error:You should Enter a number")
                            continue
                    elif square_edit_choice==3:
                        try:
                            new_name=input("Enter new square name:")
                            new_side_length=int(input("Enter new  square side length :"))
                            found_squre.name=new_name
                            found_squre.side_length=new_side_length
                            print("Square name,side length edited")
                            continue
                        except ValueError:
                            print("Value Error: You should enter a number")
                            continue
                    elif square_edit_choice==4:
                        print("You press exit")
                        break
            elif square_choice==4:
                print("Follow all steps to delete saqure")
                square_delete=input("Enter square name that you want to delete :")
                found_squre=None
                for square in squares:
                    if square.name.lower().strip()==square_delete.lower().strip():
                        found_squre=square
                        break
                if found_squre is None:
                    print(f"Square {square_delete} not found")
                    continue
                squares.remove(found_squre)
                print(f"Square {square_delete} is deleted" )
            elif square_choice==5:
                print("follow all steps to compare two squares")
                square_a=input("Enter square A name :")
                found_squre_a=None
                for square in squares:
                    if square.name.lower().strip()==square_a.lower().strip():
                        found_squre_a=square
                        break
                if found_squre_a is None:
                    print(f"square {square_a} is not found")
                    continue
                print(f"square {square_a} is found")
                square_b=input("Enter squre B name :")
                found_squre_b=None
                for square in squares:
                    if square.name.lower().strip()==square_b.lower().strip():
                        found_squre_b=square
                        break
                if found_squre_b is None:
                    print(f"Square{square_b} not found")
                    continue
                print(f"Square {square_b} is found")
                print(found_squre_a.compare_area(found_squre_b))
            elif square_choice==6:
                print("you press Exist")
                break
    elif choice==3:
        while True:
            print("Triangle Menu")
            print("-"*25)
            print("1-Add Triangle")
            print("2-Display Triangle")
            print("3-Edit Triangle")
            print("4-Remove Triangle")
            print("5-Operation")
            print("6-Exit")
            try:
                triangle_choice=int(input("Enter number your choice to strat :"))
                if triangle_choice<1 or triangle_choice>6:
                    print("Invalid choice you should enter number in range 1 and 6")
                    continue
            except ValueError:
                print("Value Error:You should enter a number to start")
            if triangle_choice==1:
                print("Follow all steps to add triangle")
                triangle_name=input("Enter Triangle name :")
                try:
                    side_a=int(input("Enter Triangle side a : "))
                    side_b=int(input("Enter Triangle side b :"))
                    side_c=int(input("Enter Triangle side c :"))
                    new_triangle=Triangle(triangle_name,side_a,side_b,side_c)
                except ValueError:
                    print("Invalid Value:You should enter a number for Side A Side B Side C ")
                    continue
                triangles.append(new_triangle)
                print(f"Triangle {triangle_name} Added")
            elif triangle_choice==2:
                print("Triangles list")
                print("-"*25)
                if not triangles:
                    print("There are not any triangles")
                else:
                    for triangle in triangles:
                        print(triangle.display_info())
                        print("-"*25)
            elif triangle_choice==3:
                    print("follow all steps to edit triangle")
                    triangle_edit=input("Enter Triangle name to edit :")
                    found_triangle=None
                    for triangle in triangles:
                        if triangle.name.lower().strip()==triangle_edit.lower().strip():
                            found_triangle=triangle
                            break
                    if not found_triangle:
                        print(f"Triangle {triangle_edit} not found")
                        continue
                    while True:
                        print(f"Triangle {triangle_edit} found")
                        print("Triangle Edit menu")
                        print("-"*25)
                        print("1-Edit Triangle name")
                        print("2-Edit Triangle Side A")
                        print("3-Edit Triangle Side B")
                        print("4-Edit Triangle Side C")
                        print("5-Edit all")
                        print("6-Exit")
                        try:
                            edit_choice=int(input("Enter the number of your choice to start :"))
                            if edit_choice<1 or edit_choice>6:
                                print("Invalid Choice: You should enter a number in range 1 and 6")
                                continue
                        except ValueError:
                            print("Value Error:You should enter number of your choice to start ")
                            continue
                        if edit_choice==1:
                            new_triangle_name=input("Enter Triangle new name :")
                            found_triangle.name=new_triangle_name
                            print("Edit done")
                            continue
                        elif edit_choice==2:
                            try:
                                new_side_a=int(input("Enter  new value of triangle side a :"))
                                found_triangle.side_a=new_side_a
                                print("Edit done")
                                continue
                            except ValueError:
                                print("Value Error: You should enter a number for Side A")
                                continue
                        elif edit_choice==3:
                            try:
                                new_side_b=int(input("Enter new value of triangle side b :"))
                                found_triangle.side_b=new_side_b
                                print("Edit done")
                                continue
                            except ValueError:
                                print("Value Error: You should enter a number for side b")
                                continue
                        elif edit_choice==4:
                            try:
                                new_side_c=int(input("Enter new value of triangle side c:"))
                                found_triangle.side_c=new_side_c
                                print("Edit done")
                                continue
                            except ValueError:
                               print("Value Error: You should enter a number for side c")
                               continue
                        elif edit_choice==5:
                            try:
                                new_triangle_name=input("Enter new triangle name :")
                                new_side_a=int(input("Enter new value of triangle side a :"))
                                new_side_b=int(input("Enter new value of triangle side b :"))
                                new_side_c=int(input("Enter new value of triangle side c :"))
                                found_triangle.name=new_triangle_name
                                found_triangle.side_a=new_side_a
                                found_triangle.side_b=new_side_b
                                found_triangle.side_c=new_side_c
                                print("Edit done")
                                continue
                            except ValueError:
                               print("Value Error: You shoud enter a number for Triangle Side A, Side B, Side C")
                               continue
                        elif edit_choice==6:
                           print("You press Exit")
                           break
            elif triangle_choice==4:
                print("follow all steps to delete triangle")
                delete_triangle=input("Enter triangle name to delete:")
                found_triangle=None
                for triangle in triangles:
                    if triangle.name.lower().strip()==delete_triangle.lower().strip():
                        found_triangle=triangle
                        break
                if found_triangle is None:
                    print(f"triangle {delete_triangle} not found")
                    continue
                triangles.remove(found_triangle)
                print(f"triangle {delete_triangle} deleted")
            elif triangle_choice==5:
                found_triangle=None
                while True:
                    print("Triangle operation menu")
                    print("-"*25)
                    print("To start any operation Check if triangle exist firstly!")
                    print("-"*25)
                    print("1-find Triangle")
                    print("2-calculate distance between points")
                    print("3-calculate midpoint")
                    print("4-calculate centroid")
                    print("5-check triangle validity")
                    print("6-check triangle type")
                    print("7-Exit")
                    try:
                        Operation_choice=int(input("Enter the number of your choice :"))
                        if Operation_choice<1 or Operation_choice>7:
                            print("Invalid Choice:You should enter number in range 1 and 7 ")
                            continue
                    except ValueError:
                        print("Invalid Value: You should enter a number to start")
                        continue
                    if Operation_choice==1:
                        triangle_name=input("Enter triangle name to find:")
                        for triangle in triangles:
                            if triangle.name.lower().strip()==triangle_name.lower().strip():
                                found_triangle=triangle
                                break
                        if found_triangle is None:
                            print(f"triangle {triangle_name} is not found")
                            continue
                        print(f"Triangle {triangle_name} is found")
                    elif Operation_choice==2:
                        print("Follow all steps to calculate distance between points ")
                        try:
                            x1=int(input("Enter value of point x1 :"))
                            y1=int(input("Enter value of point y1:"))
                            x2=int(input("Enter value of point x2 :"))
                            y2=int(input("Enter value of point y2:"))
                            print(f"Distance between points{found_triangle.distance_between_points(x1,y1,x2,y2):.2f}")
                            continue
                        except ValueError:
                            print("Value Error: You should enter number for x1,y1,x2,y2")
                            continue
                    elif Operation_choice==3:
                        print("Follow all steps to calculate midpoint ")
                        try:
                            x1=int(input("Enter value of x1:"))
                            y1=int(input("Enter value of y1 :"))
                            x2=int(input("Enter value of x2:"))
                            y2=int(input("Enter value of y2 :"))
                            result=found_triangle.midpoint(x1,y1,x2,y2)
                            print(f"calculate midpoint {result[0]:.2f},{result[1]:.2f}")
                            continue
                        except ValueError:
                            print("Value Error: You should enter number for x1,y1,x2,y2")
                            continue
                    elif Operation_choice==4:
                        print("Follow all steps to calculate centroid")
                        try:
                            x1=int(input("Enter value of x1 :"))
                            y1=int(input("Enter value of y1 :"))
                            x2=int(input("Enter value of x2 :"))
                            y2=int(input("Enter value of y2 :"))
                            x3=int(input("Enter value of x3 :"))
                            y3=int(input("Enter value of y3 :"))
                            result=found_triangle.centroid(x1,y1,x2,y2,x3,y3)
                            print(f"calculate centroid= {result[0]:.2f},{result[1]:.2f}")
                            continue
                        except ValueError:
                            print("Value Error: You should enter number for x1,y1,x2,y2,x3,y3")
                            continue
                    elif Operation_choice==5:
                        if found_triangle.is_valid():
                            print("triangle is valid")
                        else:
                            print("triangle is not valid")
                    elif Operation_choice==6:
                        print(found_triangle.triangle_type())
                    elif Operation_choice==7:
                        print("You press Exit")
                        break   
            elif triangle_choice==6:
                print("You press Exit")
                break
    elif choice==4:
        while True:
            print("Cube Menu")
            print("-"*25)
            print("1-Add Cube")
            print("2-Display Cube")
            print("3-Edit Cube")
            print("4-Delete Cube")
            print("5-Exit")
            try:
                cube_choice=int(input("Enter your number choice to start :"))
                if cube_choice<1 or cube_choice>5:
                    print("Invalid choice:You should enter number in range 1 and 5 to start")
            except ValueError:
                print("Value Error: You should enter a number to start !")
                continue
            if cube_choice==1:
                print("Follow all steps to  add cube")
                try:
                    cube_name=input("Enter Cube name :")
                    side_length=int(input("Enter Cube side length :"))
                    new_cube=Cube(cube_name,side_length)
                    cubes.append(new_cube)
                    print(f"Cube {cube_name} Added")
                    continue
                except ValueError:
                    print("Value Error: You should enter a number for cube side length")
                    continue
            elif cube_choice==2:
                print("Cubes list")
                print("-"*25)
                if not cubes:
                    print("There are not any cube")
                else:
                    for cube in cubes:
                        print(cube.display_info())
                        print("-"*25)
            elif cube_choice==3:
                print("Follow all steps to Edit a cube")
                found_cube=None
                cube_Edit=input("Enter cube name to edit : ")
                for cube in cubes:
                    if cube.name.lower().strip()==cube_Edit.lower().strip():
                        found_cube=cube
                        break
                if not found_cube:
                    print(f"Cube {cube_Edit}not found")
                    continue
                print(f"Cube {cube_Edit} found")
                while True:
                    print("Cube Edit menu")
                    print("-"*25)
                    print("1-Edit name")
                    print("2-Edit length")
                    print("3-Edit all")
                    print("4-Exit")
                    try:
                        edit_cube_choice=int(input("Enter your number choice to start :"))
                        if edit_cube_choice<1 or edit_cube_choice>4:
                            print("Invalid choice: You should enter number in range 1 and 4")
                            continue
                    except ValueError:
                        print("Value error: You should enter a number to start ")
                        continue
                    if edit_cube_choice==1:
                        new_cube_name=input("Enter new cube name : ")
                        found_cube.name=new_cube_name
                        print("Cube name edit done")
                    elif edit_cube_choice==2:
                        try:
                            new_cube_side_length=int(input("Enter new cube length:"))
                            found_cube.side_length=new_cube_side_length
                            print("cube side length edit done")
                            continue
                        except ValueError:
                            print("Value error you should enter number for cube side length")
                            continue
                    elif edit_cube_choice==3:
                        try:
                            new_cube_name=input("Enter new cube name :")
                            new_cube_side_length=int(input("Enter new cube side length :"))
                            found_cube.name=new_cube_name
                            found_cube.side_length=new_cube_side_length
                            print("Cube name side length Edit done")
                            continue
                        except ValueError:
                            print("Value Error You should enter number for cube side length")
                            continue
                    elif edit_cube_choice==4:
                        print("You press exit ")
                        break
            elif cube_choice==4:
                cube_delete=input("Enter Cube name to delete : ")
                found_cube=None
                for cube in cubes:
                    if cube.name.lower().strip()==cube_delete.lower().strip():
                        found_cube=cube
                        break
                if found_cube is None:
                    print(f"Cube {cube_delete} not found")
                    continue
                cubes.remove(found_cube)
                print(f"Cube {cube_delete} deleted")
            elif cube_choice==5:
                print("You press Exit")
                break
    elif choice==5:
        while True:
            print("Cylinder Menu")
            print("-"*25)
            print("1-Add Cylinder")
            print("2-Display Cylinder")
            print("3-Edit Cylinder")
            print("4-Delet Cylinder")
            print("5-Exit")
            try:
                cylinder_choice=int(input("Enter number of your choice to start :"))
                if cylinder_choice<1 or cylinder_choice>5:
                    print("Invalid choice: you should enter number in range 1 and 5")
                    continue
            except ValueError:
                print("Value Error: You should enter a number of your choice")
                continue
            if cylinder_choice==1:
                print("Follow all steps to add a cylinder ")
                try:
                    cylinder_name=input("Enter cylinder name :")
                    cylinder_radius=float(input("enter cylinder radius :"))
                    cylinder_height=float(input("Enter cylinder height : "))
                    new_cylinder=Cylinder(cylinder_name,cylinder_radius,cylinder_height)
                    cylinders.append(new_cylinder)
                    print(f"New Cylinder {cylinder_name} Added")
                except ValueError:
                    print("Invalid Value : You should enter a number for cylinder radius,height!")
                    continue
            elif cylinder_choice==2:
                print("Cylinders list")
                print("-"*25)
                if not cylinders:
                    print("There are not any cylinder")
                else:
                    for cylinder in cylinders:
                        print(cylinder.display_info())
                        print("-"*25)
            elif cylinder_choice==3:
                print("Follow all stepd to edit cylinder")
                cylinder_edit=input("Enter Cylinder name to edit :")
                cylinder_found=None
                for cylinder in cylinders:
                    if cylinder.name.lower().strip()==cylinder_edit.lower().strip():
                        cylinder_found=cylinder
                        break
                if cylinder_found is None:
                    print(f"Cylinder {cylinder_edit} is not found")
                    continue
                print(f"Cylinder {cylinder_edit} is found")
                while True:
                    print("Cylinder Edit Menu")
                    print("-"*25)
                    print("1-Edit name")
                    print("2-Edit radius")
                    print("3-Edit height")
                    print("4-Edit all")
                    print("5-Exit")
                    try:
                        edit_cylinder_choice=int(input("Enter a number of your choice to start :"))
                        if edit_cylinder_choice<1 or edit_cylinder_choice>5:
                            print("Invalid choice: you should enter a number in range 1 and 5")
                            continue
                    except ValueError:
                        print("Value Error: You should enter a number to start")
                        continue
                    if edit_cylinder_choice==1:
                        new_cylinder_name=input("Enter new cylinder name :")
                        cylinder_found.name=new_cylinder_name
                        print("Cylinder Edit name done")
                        continue
                    elif edit_cylinder_choice==2:
                        try:
                            new_cylinder_radius=float(input("Enter cylinder new radius :"))
                            cylinder_found.radius=new_cylinder_radius
                            print("Cylinder Edit radius done")
                            continue
                        except ValueError:
                            print("Invalid Value:You should enter a number for cylinder radius")
                            continue
                    elif edit_cylinder_choice==3:
                        try:
                            new_cylinder_height=float(input("Enter new cylinder height : "))
                            cylinder_found.height=new_cylinder_height
                            print("Cylinder Edit height done")
                            continue
                        except ValueError:
                            print("Invalid Value: You should enter a number for cylinder height")
                            continue
                    elif edit_cylinder_choice==4:
                        try:
                            new_cylinder_name=input("Enter new cylinder name :")
                            new_cylinder_radius=float(input("Enter new cylinder radius :"))
                            new_cylinder_height=float(input("Enter new cylinder height : "))
                            cylinder_found.name=new_cylinder_name
                            cylinder_found.radius=new_cylinder_radius
                            cylinder_found.height=new_cylinder_height
                            print("Cylinder Edit Name,Radius,Height is Done")
                            continue
                        except ValueError:
                            print("Invalid Value: You should enter a number for Radius,Height")
                            continue
                    elif edit_cylinder_choice==5:
                        print("You press Exit")
                        break
            elif cylinder_choice==4:
                cylinder_delete=input("Enter cylinder name to delete:")
                found_cylinder=None
                for cylinder in cylinders:
                    if cylinder.name.lower().strip()==cylinder_delete.lower().strip():
                        found_cylinder=cylinder
                        break
                if found_cylinder is None:
                    print(f"Cylinder {cylinder_delete} is not found")
                    continue
                cylinders.remove(found_cylinder)
                print(f"Cylinder {cylinder_delete} delete")    
            elif cylinder_choice==5:
                print("You press exit")
                break
    elif choice==6:
        while True:
            print("Circle Menu")
            print("-"*25)
            print("1-Add Circle")
            print("2-Display Circle")
            print("3-Edit Circle")
            print("4-Delete Circle")
            print("5-Operation")
            print("6-Exist")
            try:
                circle_choice=int(input("Enter number of your choice to start :"))
                if circle_choice<1 or circle_choice>6:
                    print("Invalid Choice: You should enter a number in range 1 and 6")
                    continue
            except ValueError:
                print("Value Error: You should enter number for your choice")
                continue
            if circle_choice==1:
                new_circle_name=input("Enter new circle name : ")
                try:
                    new_circle_radius=float(input("Enter new circle radius : "))
                    new_circle=Circle(new_circle_name,new_circle_radius)
                    circles.append(new_circle)
                    print(f"Circle {new_circle_name} Added")
                except ValueError:
                    print("Value Error: You shoulde enter number for circle radius ")
                    continue
            elif circle_choice==2:
                print("Circle list")
                print("-"*25)
                for circle in circles:
                    print(circle.display_info())
            elif circle_choice==3:
                print("follow all steps to edit a circle")
                circle_edit=input("Enter name circle to edit :")
                found_circle_edit=None
                for circle in circles:
                    if circle.name.lower().strip()==circle_edit.lower().strip():
                        found_circle_edit=circle
                        break
                if found_circle_edit is None:
                    print(f"Circle {circle_edit} is not found")
                    continue
                print(f"circle {circle_edit} found")
                while True:
                        print("Circle edit Menu")
                        print("-"*25)
                        print("1-Edit name")
                        print("2-Edit radius")
                        print('3-Edit all')
                        print("4-Exit")
                        try:
                            circle_edit_choice=int(input("Enter number of your choice to start edit : "))
                            if circle_edit_choice<1 or circle_edit_choice>4:
                                print("Invalid choice: you should enter a number in range 1 and 4")
                                continue
                        except ValueError:
                            print("Value Error: You should enter number for circle radius!")
                            continue
                        if circle_edit_choice==1:
                            new_circle_name=input("Enter new circle name :")
                            found_circle_edit.name=new_circle_name
                            print("Edit circle name is done")
                            continue
                        elif circle_edit_choice==2:
                            try:
                                new_circle_radius=float(input("Enter new circle radius :"))
                                found_circle_edit.radius=new_circle_radius
                                print("Circle radius Edited")
                                continue
                            except ValueError:
                                print("ValueError: You should enter number for circle radius!")
                                continue
                        elif circle_edit_choice==3:
                            new_circle_name=input("Enter new circle name :")
                            try:
                                new_circle_radius=float(input("Enter new circle radius : "))
                                found_circle_edit.name=new_circle_name
                                found_circle_edit.radius=new_circle_radius
                                print("Circle name,radius Edited")
                                continue
                            except ValueError:
                                print("ValueError:You should enter number for circle radius!!")
                                continue
                        elif circle_edit_choice==4:
                            print("You press exit")
                            break
            elif circle_choice==4:
                circle_delete=input("Enter circle name to delete: ")
                found_circle=None
                for circle in circles:
                    if circle.name.lower().strip()==circle_delete.lower().strip():
                        found_circle=circle
                        break
                if found_circle is None:
                    print(f"Circle {circle_delete} not found")
                    continue
                circles.remove(found_circle)
                print(f"Circle {circle_delete} deleted")
            elif circle_choice==5:
                circle_operation=input("Enter circle name:")
                found_circle_operation=None
                for circle in circles:
                    if circle.name.lower().strip()==circle_operation.lower().strip():
                        found_circle_operation=circle
                        break
                if found_circle_operation is None:
                    print(f"Circle {circle_operation} not found")
                    continue
                print(f"Circle {circle_operation}is found")   
                while True:
                    print("Operation Menu")
                    print("1-calculate arc length")
                    print("2-calculate sector area")
                    print("3-calculate distance from center")
                    print("4-calculate point position")
                    print("5-Exit")
                    try:
                        operation_circle=int(input("Enter your operation number to start :"))
                        if operation_circle<1 or operation_circle>5:
                            print("Invalid choice: You should enter number in range 1 and 5 !")
                            continue
                    except ValueError:
                        print("Value Error: You should enter number for your choice")
                        continue
                    if operation_circle==1:
                        try:
                            o=float(input("Enter value of O to Calculate arc length :"))
                            print(f"{found_circle_operation.arc_length(o):.2f}")
                            continue
                        except ValueError:
                            print("Value Error: You should enter number to Calculate arc length")
                            continue
                    elif operation_circle==2:
                        try:
                            o=float(input("Enter value of o to Calculate sector area : "))
                            print(f"{found_circle_operation.sector_area(o):.2f}")
                            continue
                        except ValueError:
                            print("Value Error: You should enter number to Calculate sector area")
                            continue
                    elif operation_circle==3:
                        try:
                            x=float(input("Enter x value: "))
                            h=float(input("Enter h value: "))
                            y=float(input("Enter y value: "))
                            k=float(input("Enter k value: "))
                            print(f"distance from center: {found_circle_operation.distance_from_center(x,h,y,k):.2f}")
                            continue
                        except ValueError:
                            print("ValueError: you should enter number for value X,H,Y,K")
                            continue
                    elif operation_circle==4:
                        try:
                            x=float(input("Enter x value: "))
                            h=float(input("Enter h value: "))
                            y=float(input("Enter y value: "))
                            k=float(input("Enter k value: "))
                            print(f"point position: {found_circle_operation.point_position(x,h,y,k)}")
                            continue
                        except ValueError:
                            print("ValueError: you should enter number for value X,H,Y,K")
                            continue
                    elif operation_circle==5:
                        print("You press exit")
                        break

            elif circle_choice==6:
                print("You press exit")
                break
    elif choice==7:
        while True:
            print("Sphere Menu")
            print("-"*25)
            print("1-Add sphere")
            print("2-display sphere")
            print("3-Edit sphere")
            print("4-Delete sphere")
            print("5-Exit")
            try:
               sphere_choice=int(input("Enter number of your choice to start : "))
               if sphere_choice<1 or sphere_choice>5:
                   print("InvalidChoice: You should enter number in range 1 and 5")
                   continue
            except ValueError:
                print("ValueError: You should enter number to start")
                continue
            if sphere_choice==1:
               new_sphere_name=input("Enter new sphere name: ")
               try:
                  new_sphere_radius=float(input("Enter new sphere radius :"))
                  new_sphere=Sphere(new_sphere_name,new_sphere_radius)
                  spheres.append(new_sphere)
                  print(f"Sphere {new_sphere_name} Added")
               except ValueError:
                    print("ValueError: You should enter number for sphere radius!")
            elif sphere_choice==2:
                print("spheres list")
                print("-"*25)
                if not spheres:
                   print("There are not any sphere")
                else:
                    for sphere in spheres:
                        print(sphere.display_info())
            elif sphere_choice==3:
                sphere_edit=input("Enter sphere name to edit : ")
                found_sphere=None
                for sphere in spheres:
                    if sphere.name.lower().strip()==sphere_edit.lower().strip():
                        found_sphere=sphere
                        break
                if found_sphere is None:
                    print(f"Sphere {sphere_edit} is not found")
                    continue
                print(f"Sphere {sphere_edit} is found")
                while True:
                    print("Sphere edit menu")
                    print("-"*25)
                    print("1-Edit Sphere name")
                    print("2-Edit sphere radius")
                    print("3-Edit all")
                    print("4-Exit")
                    try:
                        edit_choice=int(input("Enter number of your choice to start :"))
                        if edit_choice<1 or edit_choice>4:
                            print("InvalidChoice:You should enter number in range 1 and 4")
                            continue
                    except ValueError:
                        print("ValueError: You should enter number for your choice")
                        continue
                    if edit_choice==1:
                        new_sphere_name=input("Enter new sphere name :")
                        found_sphere.name=new_sphere_name
                        print("Sphere name Edited")
                        continue
                    elif edit_choice==2:
                        try:
                            new_sphere_radius=float(input("Enter new sphere radius :"))
                            found_sphere.radius=new_sphere_radius
                            print("Sphere radius Edited")
                            continue
                        except ValueError:
                            print('ValueError: You should enter number for sphere radius !')
                            continue
                    elif edit_choice==3:
                        new_sphere_name=input("Enter new sphere name :")
                        try:
                            new_sphere_radius=float(input("Enter new sphere radius :"))
                            found_sphere.name=new_sphere_name
                            found_sphere.radius=new_sphere_radius
                            print("Sphere Name,radius Edited")
                            continue
                        except ValueError:
                            print("ValueError:You should enter number for radius!")
                            continue
                    elif edit_choice==4:
                        print("You press exit")
                        break
            elif sphere_choice==4:
                sphere_delete=input("Enter sphere name to delete :")
                found_sphere=None
                for sphere in spheres:
                    if sphere.name.lower().strip()==sphere_delete.lower().strip():
                        found_sphere=sphere
                        break
                if found_sphere is None:
                    print(f"Sphere {sphere_delete} not found")
                    continue
                spheres.remove(found_sphere)
                print(f"Sphere {sphere_delete} is deleted")
            elif sphere_choice==5:
               print("You press exit")
               break
    elif choice==8:
        print("You press Exit")
        print("-"*25)
        print("Thank you for using our program ")
        print("Copy right :Code flow 29/8/2026")
        print("Program written by: Mohamed wassim tatari/Tangier/Morocco")
        break


            



    


            



        

            

                

                
    
                






            
                

                   







                        

                
            
                                        
                


                    
            


                
                

            
            
            
    
    

    
                        
        
        




