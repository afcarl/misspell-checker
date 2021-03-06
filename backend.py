"""
Mis-spell-checker:
1) different difficulty settings:low medium and high
2) misspells between 40-60% of the words you write
"""
import sys
import random
class MissSpell:
    def __init__(self,level,percentage=40):
        if percentage in xrange(40,70,10):
            self.percentage = percentage
        if level.lower() in ["low","medium","high"]:
            self.level = level.lower()
        else:
            print "level is not properly set, please use low, medium, or high"
            sys.exit(0)

    def checker(self,text):
        if self.level == "low":
            return self.low_checker(text)
        elif self.level == "medium":
            return self.medium_checker(text)
        elif self.level == "high":
            return self.high_checker(text)
        else:
            print "You have some how gotten around setting a level, we cannot proceed without this"
            sys.exit(0)

    def low_checker(self,text):
        words = text.split(' ')
	print len(words) * (.01*self.percentage)
        words_to_misspell = int(len(words)*(.01*self.percentage))
        if words_to_misspell == 0: words_to_misspell = 1
        count = 0
        indexes_used = []
        while count < words_to_misspell:
            index = random.randint(0,len(words)-1)
            indexes_used.append(index)
            if index in indexes_used:
                index = random.randint(0,len(words)-1)
                while index in indexes_used:
                    indexes_used.append(index)
                    index = random.randint(0,len(words)-1)
            word = words[index]
            characters = [x for x in word]
            vowels = [x for x in "aeiou"]
            consonants = [x for x in "bcdfghjklmnpqrstvxzwy"]
            vowel_mapping = {"a":"e",
                             "i":"o",
                             "u":"a",
                             "o":"u",
                             "e":"i"
                             }
            consonants_mapping ={"l":"r",
                                 "t":"v",
                                 "q":"w",
                                 "x":"z",
                                 "b":"r",
                                 "k":"l"
                                 }
            new_word = []
            for ind,letter in enumerate(characters):
                if letter in vowels:
                    new_word.append(vowel_mapping[letter])
                else:
                    if ind%3==0 or ind%4==1:
                        if letter in consonants_mapping.keys():
                            new_word.append(consonants_mapping[letter])
                        else:
                            new_word.append(letter)
                    else:
                        new_word.append(letter)
            words[index] = ''.join(new_word)
            count += 1

        return ' '.join(words)

    def swap(self,first,second):
        return second,first
        

    def medium_checker(self,text):
        words = text.split(' ')
        words_to_misspell = int(len(words)*(.1*self.percentage))
        if words_to_misspell == 0: words_to_misspell = 1
        count = 0
        indexes_used = []
        while count < words_to_misspell:
            index = random.randint(0,len(words)-1)
            indexes_used.append(index)
            if index in indexes_used:
                index = random.randint(0,len(words)-1)
                while index in indexes_used:
                    indexes_used.append(index)
                    index = random.randint(0,len(words)-1)
            word = words[index]
            characters = [x for x in word]
            vowels = [x for x in "aeiou"]
            consonants = [x for x in "bcdfghjklmnpqrstvxzwy"]
            vowel_mapping = {"a":"e",
                             "i":"o",
                             "u":"a",
                             "o":"u",
                             "e":"i"
                             }
            consonants_mapping ={"l":"r",
                                 "t":"v",
                                 "q":"w",
                                 "x":"z",
                                 "b":"r",
                                 "k":"l",
                                 "f":"g",
                                 "m":"n",
                                 "v":"s"
                                 }
            new_word = []
            for ind,letter in enumerate(characters):
                if letter in vowels:
                    new_word.append(vowel_mapping[letter])
                else:
                    if ind%3==0 or ind%4==1:
                        if letter in consonants_mapping.keys():
                            new_word.append(consonants_mapping[letter])
                        else:
                            new_word.append(letter)
                    else:
                        new_word.append(letter)
            words[index] = ''.join(new_word)
            count += 1
            for i in xrange(len(words)):
                offset = random.randint(0,4)
                if offset+index < len(words): 
                    words[index+offset],words[index] = self.swap(words[index],words[index+offset])
                elif offset < len(words)-1 and index< len(words)-1:
                    words[index],words[index+1] = self.swap(words[index],words[index+1])
                else:
                    continue
        return ' '.join(words)

    def high_checker(self,text):
        words = text.split(' ')
        words_to_misspell = int(len(words)*(.1*self.percentage))
        if words_to_misspell == 0: words_to_misspell = 1
        count = 0
        indexes_used = []
        while count < words_to_misspell:
            index = random.randint(0,len(words)-1)
            indexes_used.append(index)
            if index in indexes_used:
                index = random.randint(0,len(words)-1)
                while index in indexes_used:
                    indexes_used.append(index)
                    index = random.randint(0,len(words)-1)
            word = words[index]
            characters = [x for x in word]
            vowels = [x for x in "aeiou"]
            consonants = [x for x in "bcdfghjklmnpqrstvxzwy"]
            vowel_mapping = {"a":"e",
                             "i":"o",
                             "u":"a",
                             "o":"u",
                             "e":"i"
                             }
            consonants_mapping ={"l":"r",
                                 "t":"v",
                                 "q":"w",
                                 "x":"z",
                                 "b":"r",
                                 "k":"l",
                                 "f":"g",
                                 "m":"n",
                                 "v":"s"
                                 }
            new_word = []
            for ind,letter in enumerate(characters):
                if letter in vowels:
                    new_word.append(vowel_mapping[letter])
                else:
                    if ind%3==0 or ind%4==1:
                        if letter in consonants_mapping.keys():
                            new_word.append(consonants_mapping[letter])
                        else:
                            new_word.append(letter)
                    else:
                        new_word.append(letter)
            first,second = self.swap(new_word[:len(new_word)/2],new_word[len(new_word)/2:]) 
            new_word = first + second
            words[index] = ''.join(new_word)
            
            count += 1
            for i in xrange(len(words)):
                offset = random.randint(0,4)
                if offset+index < len(words): 
                    words[index+offset],words[index] = self.swap(words[index],words[index+offset])
                elif offset < len(words)-1 and index< len(words)-1:
                    words[index],words[index+1] = self.swap(words[index],words[index+1])
                else:
                    continue
        return ' '.join(words)

        
