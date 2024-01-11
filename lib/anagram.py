class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):

        def get_letters_list(word):
            letters = []
            for letter in word:
                letters.append(letter)
            return letters
        
        matching_words = []

        for word in word_list:
            if sorted(get_letters_list(self.word)) == sorted(get_letters_list(word)):
                matching_words.append(word)
            elif len(word_list) == 0:
                return []
            else:
                pass
            
        return matching_words
            
        


anagram = Anagram("listen")
print(anagram.match(["enlist", "sausage"]))

