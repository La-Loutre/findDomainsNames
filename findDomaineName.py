

def find_tld_words(words_list,tld_list):
    result = open("generated_domains_names.txt","w")
    possibles_names = []
    for word in words_list:
        word_length = len(word)
        for tld in tld_list:
            tld_length = len(tld)
            if tld_length >= word_length:
                continue
            word_short = word[0:word_length-tld_length]
            word_short+= tld
            if str.lower(word_short) == str.lower(word):
                result.write(str.lower(word[0:word_length-tld_length])+"."+str.lower(tld))
                result.write('\n')
    result.close()


def create_list(words_file):
    words = []
    for line in words_file:
        line = line.strip()
        words.append(line)
    return words

tld_file = open("tlds.txt","r")
words_file = open("/usr/share/dict/words","r")

words_list = create_list(words_file)
tld_list  = create_list(tld_file)
tld_file.close()
words_file.close()

find_tld_words(words_list,tld_list)
