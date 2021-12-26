from scipy.spatial.distance import cosine
import numpy as np

AMOUNT_OF_CLOSEST_WORDS = 10

words = dict()

with open("vocabulus/words.txt") as f:
	for line in f:
		line = line.split()
		word = line[0]
		vector = np.array([float(i) for i in line[1:]])
		words[word] = vector

def distance(word1, word2):
	return cosine(word1, word2)

def closest_words(word):
	distances = dict()
	for w in words:
		distances[w] = distance(words[w], word)

	return sorted(distances, key=lambda w: distances[w])[:AMOUNT_OF_CLOSEST_WORDS]

def closest_word(word):
	return closest_words(word)[0]

# Returns a new word by applying the relationship of the two words to the target word
def get_word(relation_word1, relation_word2, target_word):
	relation_word1_vec = words[relation_word1]
	relation_word2_vec = words[relation_word2]
	target_word_vec = words[target_word]

	output_word = closest_word(relation_word1_vec - relation_word2_vec + target_word_vec)
	if output_word != target_word:
		return output_word
	else:
		return closest_word(relation_word2_vec - relation_word1_vec + target_word_vec)
