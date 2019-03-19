def sum_array(array):

    '''Return sum of all items in array'''
    if type(array) == int:
        return array
    sum = 0
    for e in array:
        if type(e) == list:
            sum = sum + sum_array(e)
        else:
            sum = sum + e
    return sum

sum_array([1,[2,3],[4,[5,[6,7]]]])


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibonacci(20)


def factorial( n ):

'''Return n!'''
    if n < 1:   # base case
        return 1
    else:
        return n * factorial( n - 1 )  # recursive call

factorial(6)

'''Return word in reverse'''
def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]

reverse("Lucky")
