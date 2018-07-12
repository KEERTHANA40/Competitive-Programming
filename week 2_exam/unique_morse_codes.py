def unique(words):
       
    MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
             "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-",
             "...-", ".--", "-..-", "-.--", "--.."]

    morse_word = set()
    for word in words:
        morse_word.add(''.join([MORSE[ord(k)-97] for k in word]))
    print(len(morse_word))


unique(["gin", "zen", "gig", "msg"])
unique(["a", "z", "g", "m"])
unique(["bhi", "vsv", "sgh", "vbi"])
unique(["a", "b", "c", "d"])
unique(["hig", "sip", "pot"])