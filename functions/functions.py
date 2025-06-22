def fn(name):
    greeting = f"Hello {name}"
    print(greeting)

fn("Fulgence")

def area(length,width):
    area = length * width
    return area

area(4,5)

def remainder(number):
    remainder = number % 2
    if remainder == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is odd")

remainder(3)