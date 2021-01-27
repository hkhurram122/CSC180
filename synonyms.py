
import math

# Project 3 ESC180
# Group: Hassan Khurram and Muhammad Ahsan Kaleem


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)



def cosine_similarity(vec1, vec2):
    vec1_keys = list(vec1.keys())
    vec1_values = list(vec1.values())
    vec2_keys = list(vec2.keys())
    vec2_values = list(vec2.values())
    numerator = 0
    for i in range(len(vec1_keys)):
        for j in range(len(vec2_keys)):
            if vec1_keys[i] == vec2_keys[j]:
                numerator += vec1_values[i] * vec2_values[j]
    denominator = norm(vec1) * norm(vec2)
    return numerator/denominator
    


def build_semantic_descriptors(sentences):
    """ takes in a list of a lists (inner list is a sentence with words as elements)

        returns a 2D dictionary d such that for every word w in atleast 1 sentence, d[w] is
        itself a dictionary (semantic of w)
    """
    d = {}
    for i in range(len(sentences)):
        ls = list(set(sentences[i]))
        for j in range(len(ls)):
            word = ls[j]
            if word not in d.keys():
                d[word] = {} 
            ls1 = ls[:]
            ls1.remove(word)
            for k in range(len(ls1)):
                if ls1[k] not in d[word].keys():
                    d[word][ls1[k]] = 1   
                else:
                    d[word][ls1[k]] += 1  
    return d



def build_semantic_descriptors_from_files(filenames): 
    all_sentences = []
    temp = []
    for file in filenames:  
        f1 = open(file, "r", encoding="latin1")
        f = f1.read()
        sentence_str = ''
        for e in range(len(f)):                       
            if f[e].isalpha() == True or f[e] == ' ' or f[e] == '.':
                sentence_str = sentence_str + f[e]
            elif f[e] == '?' or f[e] == '!':
                sentence_str = sentence_str + '.'
            elif f[e] == '\n':
                sentence_str = sentence_str + ' '
            elif f[e] == '-':
                sentence_str = sentence_str + ' '
            elif e < len(f) - 1:
                if f[e:e+2] == '--':
                    sentence_str = sentence_str + ' '
        sentence_str = sentence_str.lower()
        sentences = sentence_str.split('.')
        temp.append(sentences)
    for b in range(len(temp)):
        all_sentences += temp[b]
    all_sentences = [x.split(' ') for x in all_sentences]
    semantics_dict = build_semantic_descriptors(all_sentences)
    del semantics_dict['']
    for i in list(semantics_dict.keys()):
        if '' in list(semantics_dict[i].keys()):
            del semantics_dict[i]['']

    return semantics_dict
    



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    """Out of the choices, returns the choice that returns the greatest
    cos similarity. Otherwise return -1 if similarity cannot be computed."""
    similarities = {}
    for choice in choices:
        if choice in list(semantic_descriptors.keys()):    
            cos_sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])       
            similarities[choice] = cos_sim
        else:
            similarities[choice] = -1
    #print(similarities)
    return max(similarities, key=similarities.get)



def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    new_f = open(filename, "r") 
    f = new_f.read()
    lines = f.split('\n')
    n_correct = 0
    n_total = 0
    for v in range(len(lines)):
        line = lines[v].split(' ')
        #print (line)  
        choices = line[2:] 
        if line == ['']:
            continue
        w_guess = most_similar_word(line[0], choices, semantic_descriptors, cosine_similarity)
        #print (line[1] + '        ' + str(w_guess))   
        if w_guess == line[1]:  
            n_correct += 1
        n_total += 1
    return (n_correct/n_total) * 100



'''
if __name__ == "__main__":
    #Testing code:
    import time
    start_time = time.time()
    filenames = ["gutenberg1.txt", "gutenberg2.txt"]
    semantics = build_semantic_descriptors_from_files(filenames)
    res = run_similarity_test("test.txt", semantics, cosine_similarity)
    print(str(res) +  " percent of the guesses were correct")
    print (time.time() - start_time)

'''
