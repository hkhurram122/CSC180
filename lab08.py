# Problem 1 
filename = "data2.txt"
'''
f = open(filename)
for line in f:
    if line.lower().find("lol") != -1:
        print(line)
'''
# Problem 2
def dict_to_str(d):
    """return a str containing each k, v in d"""
    str1 = ''
    for k, v in d.items(): 
        str1 += str(k) + ', ' + str(v) + '\n'
    return str1
# Problem 3
def dict_to_str_sorted(d):
    # KEYS in the string must be sorted in ascending order
    str1 = ''
    keys = sorted(d.keys())
    for k in keys:
        str1 += str(k) + ', ' + str(d[k]) + '\n'
    return str1

# Problem 4

# 4 a 
# takes in a word and returns the number of syllables in it

filename_1 = "dict.txt"
f1 = open(filename_1)

d_syllables = {}
for line in f1:
    l = [c for c in line.split(' ') if c != ''] 
    l = [''.join(x for x in i if x.isalpha()) for i in l] # removed digits
    d_syllables[l[0]] = l[1::]  # first index is word, all others are phones 
#print(d_syllables)

# 4 b
filename_2 = "phones.txt"
f3 = open(filename_2)

d_phones = {} # keys are phone codes, values are categories
for line in f3:
    temp = line.split()
    d_phones[temp[0].strip()] = temp[1].strip()
#print(d_phones)



# 4 c
def num_vowels(word):
    """Takes in a word, and returns the number of vowels in a word"""
    word = word.upper()
    phones = []
    for w in d_syllables.keys():
        if word.upper() == w:
            phones.extend(d_syllables[w])
    ctr = 0
    for i in range(len(phones)):
        for k in d_phones.keys():
            if phones[i] == k and d_phones[k] == 'vowel':
                ctr += 1
    return ctr

print(num_vowels("abandonment"))



def fkrg(text):
    #for now assumes that the text is inputted in one line 
    text_list = text.split(' ')
    word_list = []
    for e in range(len(text_list)):
        word = ''
        for f in range(len(text_list[e])):
            if text_list[e][f].isalpha() == True:
                word += text_list[e][f]
        word_list.append(word)
    sentences = text.split('.')
    total_words = len(text_list)
    total_sentences = len(sentences)
    total_syllables = 0
    for g in range(len(word_list)):
        total_syllables += num_vowels(word_list[g])
    return ((0.39)*(total_words/total_sentences) + (11.8)*(total_syllables/total_words) - 15.59)

print (fkrg("This is a rather sophisticated text that I shall use to test this function."))
print (fkrg("hi this is just a random text"))


print("\n")





# Problem 5
def readability(text):
    """Evaluates the readability grade level of a text"""
    words, sentences, syllables = 0,0,0
    for i in range(len(text)):
        if (text[i] == ' '):
            words += 1
        if (text[i] == '.' or text[i] == '!' or text[i] == '?'):
            sentences += 1
    txt_l = [c for c in text.split(' ') if c.isalpha()] 
    for word in txt_l:
        syllables += num_vowels(word)
    
    return ((.39*(words/max([1,sentences])))+(11.8*(syllables/words)) - 15.59)

print(readability("This is a rather sophisticated text that I shall use to test this function."))
print(readability("hi this is just a random text"))

