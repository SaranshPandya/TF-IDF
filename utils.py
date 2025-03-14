# implimenting TF-IDF algorithm

"""

First implimenting word_to_index mapping
After that implimenting count vectorizer
and finally implimenting TF-IDF algorithm

"""

import nltk
from colorama import Fore, Style

class WordToIndex:
    def readtext(self, document_name):
        try:
            with open(document_name, 'r') as file:
                text = file.read()
                words = text.split() 

        except FileNotFoundError:
            print(Fore.RED+"File not found\n")
        
        except Exception as e:
            print(Fore.RED+f"Exception: {e}")

        finally:
            if file:
                file.close()

        return words

    def word_to_index(self, documents):
        documents = self.readtext(documents)
        current_index = 0
        word2index = {}

        for doc in documents:
            tokens = nltk.word_tokenize(doc)
            for token in tokens:
                if token not in word2index:
                    word2index[token] = current_index
                    current_index += 1
        
        return word2index

