
import random

# Problem 1 
'''
ls_words = open("text.txt", encoding="latin-1").read().split()
'''



# 1 a 
# store words in a text as keys in a dict, frequency are values

ls_words = ["I", "am", "a", "sick", "man.", "I", "am", "a", 
"spiteful", "man.", "I", "am", "an", "unattractive", "man.", "I", 
"believe", "my", "liver", "is", "diseased.", "However,", "I", "know",
"nothing", "at", "all", "about", "my", "disease,", "and", "do", "not",
"know", "for", "certain", "what", "ails", "me."]

d_words = {}
for w in set(ls_words): # set() removes all repeats
    d_words[w] = ls_words.count(w)
print(d_words)



# 1 b
def top10(L):
    """Takes in a list L of a 100 different integers, returns a list of the 10 largest ints"""
    L1 = sorted(L, reverse=True)
    return (L1[0:10])

l = [random.randint(1,100) for i in range(15)]
#print(top10(l))



# 1 c 
# sort the data by word counts (values)

def swap(d):
    s_d = {} 
    for key, value in d.items(): 
        if value in s_d: 
            s_d[value].append(key) 
        else: 
            s_d[value]=[key] 
    return s_d

def top_words(d_words):
    # swap keys and values in d_words
    d_swapped = swap(d_words)
    d_sorted = dict(sorted(d_swapped.items(), reverse=True))
    
    t_words = []
    for k in d_sorted:
        t_words.extend(d_sorted[k])
    return t_words[0:10]

s = top_words(d_words)
print(s)


# Problem 2 



''.join([])



# Problem 3 

import urllib.request

def num_results(terms): #term means the search term, which should be a string, assumes one word without spaces  
    #change it so that u can add more words
    term_list = terms.split(' ')
    new_str = ''.join([term_list[i]+"+" for i in range(len(term_list)) if i < len(term_list) - 1] + [(term_list[-1])])
    f = urllib.request.urlopen('https://ca.search.yahoo.com/search?p=' + new_str + '&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8')
    page = f.read().decode("utf-8")
    f.close()
    
    all_instances = []
    for a in range(len(page) - 9):
        if page[a:a+8] == ' results' and page[a-1] != '#':
            all_instances.append(page[a-14:a])

    for b in range(len(all_instances)): 
        count = 0
        for c in range(len(all_instances[b])):
            if all_instances[b][c].isdigit():
                count += 1 # number of digits    
        if count/len(all_instances[b]) > 0.3: # converting string of numbers (with commas) to an int
            num_str = ''
            for d in range(len(all_instances[b])):
                if all_instances[b][d].isdigit():
                    num_str += all_instances[b][d]
            return int(num_str)
#print (num_results('Random')) 


def choose_variant(L): 
    #L should be a list containing 2 strings, like ["five-year anniversary", "fifth anniversary"]
    if num_results(L[0]) > num_results(L[1]):
        return L[0]
    return L[1]

print (choose_variant(["top ranked school uoft", "top ranked school waterloo"]))



