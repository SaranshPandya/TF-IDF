from utils import WordToIndex

indexer = WordToIndex()

# word = indexer.readtext('006.txt')
word_to_index = indexer.word_to_index('006.txt')

print(word_to_index)

