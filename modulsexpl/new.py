
def key_generetor(passcode):
    key_word = 0
    for letter in passcode:
        key_word = key_word + ord(letter)
    return key_word
print("varbl name is",__name__)
if __name__=='__main__':
    
    print("the secret key for apple is")
    print(key_generetor("apple"))