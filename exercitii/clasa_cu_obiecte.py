# Define a class
class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def my_method(self):
        print("Hello, World!")


# Create an instance of the class
my_object = MyClass("foo", "bar")

# Access the instance's attributes
print(my_object.arg1)  # Output: "foo"
print(my_object.arg2)  # Output: "bar"

# Call the instance's method
my_object.my_method()  # Output: "Hello, World!"
