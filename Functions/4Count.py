def count(s):
    v="AEIOUaeiou"
    vowels=0
    consonants=0
    d="0123456789"
    digits=0
    for i in s:
        if i in v:
            vowels+=1
        
        if i in d:
            digits+=1
        else:
            consonants+=1
       
    return('Vowels =', vowels, 'Consonants =', consonants, 'Digits =', digits)

print(count("Mahak2007"))
