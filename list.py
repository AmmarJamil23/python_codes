digit = [1,2,3,4,5, 'a', True, 55.56]
print(digit)
print(type(digit))
print(len(digit))

print(digit[1])
print(digit[4])

v = 2
print(digit[v])

print(2 in digit)

print(-3 in digit)

def make_tea(ing):
    for i in ing:
        print('put', i, 'in')
    return ing

ing = ['water', 'cinnamon', 'tea leaves', 'sugar', 'milk']
mt = make_tea(ing)
print(mt)



def count(sequence, value):
    count = 0
    for i in sequence:
        if i == value:
            count = count + 1
    return count

seq = [23, 45, 24, 88, 1, 9, 4, 4, 4]
print(count(seq, 4))
print(count(seq, 'abc'))

print(seq[0:3])

#modifying elements
seq[0] = 34
seq[1] = True
print(seq)
print(seq[-1])