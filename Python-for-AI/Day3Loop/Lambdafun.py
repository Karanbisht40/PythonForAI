def square(x):
    return x*2
print(square(3))

#lambda function
square = lambda x: x*2
print(square(3))

add = lambda a,b: a+b
print(add(2,3))

#lambda with map()
numbers= [ 1,2,3,4,5]
square = list(map( lambda x: x**2, numbers))
print(square)

#lambda with filter
numbers = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x: x%2==0, numbers))
print(even)

#lambda with sorted -sort by len
words= ["apple","kiwi","banana"]
words.sort(key= lambda words: len(words))
print(words)