function myDecorator(targetFunction) {
    return function (...args) {
      console.log('Function was called');
      return targetFunction.apply(this, args);
    };
  }
  
  function greet(name) {
    console.log('Hello,', name);
  }
  
  const decoratedGreet = myDecorator(greet);
  
  decoratedGreet('Alice');

  // Here's how the code works:
1.
// function myDecorator(targetFunction) { ... }: This defines the myDecorator function, which takes one parameter, targetFunction. This is the function that you want to decorate or enhance.
2.
// return function(args) { ... }: This is the heart of the decorator pattern. It returns an anonymous function that takes an args parameter. This anonymous function becomes the new version of the targetFunction after decoration.
3.
// console.log('Function was called');: This line logs a message to the console whenever the decorated function is called. This is a simple example of adding behavior to the original function.
4.
// return targetFunction.apply(this, args);: This line invokes the targetFunction with the this context of the decorated function and passes the args to it. Essentially, it calls the original function with the provided arguments.


// In summary, the myDecorator function takes a targetFunction, creates a new function that logs a message when called, and then calls the `targetFunction with the same arguments. This way, you can add behavior before or after the execution of the original function without modifying its code directly.

// In the example provided, the greet function is decorated using myDecorator, creating a new function called decoratedGreet. When decoratedGreet('Alice') is called, the message "Function was called" is logged to the console, and then the greet function is invoked with the argument 'Alice', resulting in the output "Hello, Alice".