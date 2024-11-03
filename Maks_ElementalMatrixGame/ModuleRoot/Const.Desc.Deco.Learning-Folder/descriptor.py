class DescriptorExample:
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Value must be non-negative')
        instance._value = value

class MyClass:
    my_descriptor = DescriptorExample(0)

obj = MyClass()
obj.my_descriptor = 5  # This will work
print(obj.my_descriptor)  # Output: 5

obj.my_descriptor = -1  # This will raise a ValueError

# In Python, descriptors are a more advanced feature that allow you to customize how attributes are accessed and modified on instances of a class. They provide a way to control the behavior of attributes beyond what traditional methods and properties offer.
# Descriptors are typically implemented as class attributes (defined within a class) and consist of three special methods: __get__(), __set__(), and __delete__(). These methods are called when the attribute is accessed, assigned, or deleted, respectively.
# When an attribute is accessed on an instance of a class, Python's attribute lookup rules check for the presence of descriptors. If a descriptor is found, its __get__() method is called to retrieve the attribute value.
# Similarly, when an attribute is assigned a value, the __set__() method of the descriptor is invoked, allowing custom behavior during assignment.
# Descriptors provide a powerful way to implement properties with custom behavior, validate attribute values, or control access to attributes
# In this example, DescriptorExample is a descriptor class that controls the behavior of the my_descriptor attribute in the MyClass class.

# In this example, DescriptorExample is a descriptor class that controls the behavior of the my_descriptor attribute in the MyClass class.

#
#
#
#
#
#
# 
#
#
#
#
#
#