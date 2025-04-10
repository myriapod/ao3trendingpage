# 1. Create a Decorator to Log Function Arguments and Return Value

def decorator1(func):
    def wrap(*args, **kwargs):
        # Log the function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        # Call the original function
        result = func(*args,**kwargs)
        
        # Log the return value
        print(f"{func.__name__} returned: {result}")
        
        # Return the result
        return result
    return wrap

# Example usage
@decorator1
def add_numbers(a,b):
    return a + b

# Call the decorated function
#result = add_numbers(2,3)
#print("Result", result)

# 2. Create a Decorator to Measure Function Execution Time
import time

def decorator2(func):
    def wrapper(*args, **kwargs):
        # Start timer
        start_time = time.time()
        # Call the function and time it
        result = func(*args, **kwargs)
        # End time
        end_time = time.time()
        duration = end_time-start_time
        
        print(f"{func.__name__} took {duration} seconds to complete")
        return result
    return wrapper

@decorator1
@decorator2
def while_loop(a):
    i=0
    while i<a:
        time.sleep(1)
        i+=1
    return i

#result = while_loop(3)
#print(result)

# 5. Implement a Decorator to Validate Function Arguments
def decorator5(func):
    def wrapper5(*args, **kwargs):
        for i in args:
            if type(i) != int:
                print(f"{i} is not in the correct type for the function {func.__name__}")
                return f"Can't use function {func.__name__}"
        # if it's okay, call the function
        result = func(*args, **kwargs)
        return result
    return wrapper5

@decorator5
def multiply(a,b):
    return a*b

#print(multiply(3.4,4))

# 7. Implement a Decorator to Enforce Rate Limits on a Function
def rate_limits(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset = time.time()
        
        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset
            
            # Elapsed time since last reset
            elapsed = time.time() - last_reset
            
            # If elapsed time is greater than the period, reset the timer
            if elapsed > period:
                calls = 0
                last_reset = time.time()
                
            # Check if the call count has reached the maximum limit
            if calls >= max_calls:
                raise Exception("Rate limit exceeded. Please try again later")
            
            # Increment the call counts
            calls += 1
            
            # call the function
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@rate_limits(max_calls=2, period=10)
def api_call():
    print("API call executed successfully...")
    time.sleep(5)

# Make API calls
"""for _ in range(8):
    try:
        api_call()
    except Exception as e:
        print(f"Error occurred: {e}")"""
        
        
# 12. Implement a Decorator for Caching with Expiration Time
def cache_with_expiry(expiry_time):
    def decorator(func):
        cache = {}
        
        def wrapper(*args, **kwargs):
            nonlocal cache
            key = (*args, *kwargs.items())
            if key in cache:
                value, timestamp = cache[key]
                if time.time() - timestamp < expiry_time:
                    print("Retrieving value from cache...")
                    return value
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator

@cache_with_expiry(expiry_time=5)
def calculate_multiply(x, y):
    print("Calculating the product of two numbers...")
    return x*y
"""
print(calculate_multiply(25,5))
print(calculate_multiply(25,4))
print(calculate_multiply(20,5))
print(calculate_multiply(25,5))
"""

