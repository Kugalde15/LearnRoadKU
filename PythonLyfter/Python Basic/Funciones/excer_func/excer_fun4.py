

def reverse():
    word = 'Me gusta el deporte'
    result = ''

    for char in range(len(word)):
        result += word[-(char+1)]
    return result

rev = reverse()
print (rev)