import streamlit as st


def load_vocab(file_path):
	with open(file_path, 'r') as f:
		lines = f.readlines()
		words = sorted(set([line.strip().lower() for line in lines]))
	return words


def initialize_distances(len1, len2):
	distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]
	for i in range(len1 + 1):
		distances[i][0] = i
	for j in range(len2 + 1):
		distances[0][j] = j
	return distances


def compute_distances(token1, token2, distances):
	len1, len2 = len(token1), len(token2)
	for i in range(1, len1 + 1):
		for j in range(1, len2 + 1):
			if token1[i - 1] == token2[j - 1]:
				distances[i][j] = distances[i - 1][j - 1]
			else:
				distances[i][j] = min(
					distances[i - 1][j] + 1,  # Deletion
					distances[i][j - 1] + 1,  # Insertion
					distances[i - 1][j - 1] + 1  # Substitution
				)


def levenshtein_distance(token1, token2):
	len1, len2 = len(token1), len(token2)
	distances = initialize_distances(len1, len2)
	compute_distances(token1, token2, distances)
	return distances[len1][len2]


vocabs = load_vocab(file_path = 'data/vocab.txt')

word = st.text_input('Word :')

if st.button(" Compute "):

	# compute levenshtein distance
	leven_distances = dict()
	for vocab in vocabs:
		leven_distances[vocab] = levenshtein_distance(word, vocab)

	# sorted by distance
	sorted_distences = dict(sorted(leven_distances.items(), key = lambda item: item[1]))
	correct_word = list(sorted_distences.keys())[0]
	st.write('Correct word : ', correct_word)

	col1, col2 = st.columns(2)
	col1.write('Vocabulary :')
	col1.write(vocabs)

	col2.write('Distances :')
	col2.write(sorted_distences)
