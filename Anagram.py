def anagram(s,v):
    
    if len(s)==len(v):
        for i in s:
            if i not in v:
                print("Not an Anagram")
            break 
    else:
        print("Anagram")
a="divya"
b="vidya"
anagram(a, b)

#String Compression




