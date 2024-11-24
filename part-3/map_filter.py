'''
So, what are `map` and `filter`?  

- `map`: This function applies a function to every item in an iterable, like a list, and returns a new iterable with the results.  

- `filter`: This function filters elements of an iterable based on a condition, keeping only the items that satisfy it.
'''

### **Using `map` Function**  

# Example 1: Squaring Numbers  
numbers = [1,2,3,4,5,6]
map_squares = list(map(lambda num: num**2, numbers))
# print(map_squares)


# Example 2: Converting string to upper 
words = ["hello", "World", "python", "map", "learNing"]

upper_case_words = list(map(lambda word: word.upper(), words))

# print(upper_case_words)


### **Using `filter` Function**  

# Example 3: Filtering Even Numbers 
numbers = [1,4,7,8,3,6,10]

even_numbers = list(filter(lambda num:num%2==0, numbers))

# print(even_numbers)


# Example 4: Filtering Words by Length
words = ["hello", "World", "python", "map", "learNing"]

filter_words = list(filter(lambda word: len(word)<=5,words))

# print(filter_words)



### **Combining `map` and `filter`**  
# Here's a cool part: you can use `map` and `filter` together!

# Example 5: Filtering Even Numbers and Squaring Them

numbers = [1,4,7,8,3,6,10]

even_square_numbers = list(map(lambda num:num**2, filter(lambda num: num%2==0, numbers)))

print(even_square_numbers)

