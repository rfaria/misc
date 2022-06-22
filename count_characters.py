def naive(text):

    freq = {}

    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    return(freq)


if __name__ == '__main__':

    text = input('Insert your text: ')
    
    print('Naive method:', naive(text))
