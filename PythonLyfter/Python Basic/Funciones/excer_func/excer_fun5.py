

the_life = 'La Vida es Bella en USA'

def dif_in_words(string1):
    counter_M = 0
    counter_m = 0
    for word in string1:
        if word.isupper():
            counter_M += 1
        elif word.islower():
            counter_m += 1
    print(f"There's {counter_M} upper cases and {counter_m} lower cases")


dif_in_words(the_life)