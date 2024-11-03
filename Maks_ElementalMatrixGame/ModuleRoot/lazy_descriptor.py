class LazyDescriptor:
    def __init__(self, factory):
        self.factory = factory
        self.value= None 
        
    def __call__(self):
        if self.value is None:
            self.value = self.factory()
        
        return self.value
    
    
    """A descriptor that evaluates an attribute only once and caches the result.
    This class is useful when you have expensive computations or resources that need to be initialized lazily. By using this descriptor, the attribute is computed or initialized only when it is accessed for the first time, and subsequent accesses return the cached value.
    Attributes:
        factory (callable): A callable that creates and returns the attribute value.
        value: The cached attribute value.
    """
    """
    Initializes the LazyDescriptor.
        Args:
            factory (callable): A callable that takes no arguments and returns the attribute value.
                This callable will be invoked the first time the at"""   
                
    # Evaluates the factory and returns the cached attribute value.
        # Returns:
            # Any: The result of invoking the factory callable.                 