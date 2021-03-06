# Matching questions with answers
# Algortihm: Calculate the similarity score between the question and every sentence in
# the passage. The sentence with highest similarity score is most likely to contain the answer.
# Next, check if the sentence contains the one of the possible answers. The answer contained in
# that sentence is the answer to the question.

import string
import re
from nltk import bigrams
from nltk.stem import *

stemmer = PorterStemmer()
stopwords_set = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'yo', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

def clean_sentence(sentence):
	sentence = sentence.lower()
	clean_sentence = sentence.translate(string.maketrans("",""), string.punctuation)
	tokens = clean_sentence.split()
	filtered_tokens = filter(lambda x: x not in stopwords_set, tokens)
	stemmed_tokens = [stemmer.stem(token.decode('utf-8-sig')) for token in filtered_tokens]
	return stemmed_tokens

def generate_similarity_score(sentence_x, sentence_y):
	# Algorithm:
		# Convert the sentences to lower case
		# Tokenize the sentences and remove stop words.
		# Calculate bi-grams for the 2 sentences.
		# Score is the number of common bi-grams in the 2 sentences.

	x_tokens = clean_sentence(sentence_x)
	y_tokens = clean_sentence(sentence_y)

	x_bigrams = set(bigrams(x_tokens))
	y_bigrams = set(bigrams(y_tokens))

	x_unigrams = set((x_tokens))
	y_unigrams = set((y_tokens))

	intersection_set_unigrams = x_unigrams.intersection(y_unigrams)
	intersection_set_bigrams = x_bigrams.intersection(y_bigrams)

	return len(intersection_set_unigrams) + len(intersection_set_bigrams)

def generate_questions_passage_scores(questions, passage_sentences):
	scores = []
	for q_index, question in enumerate(questions):
		scores.append([])
		for _, sentence in enumerate(passage_sentences):
			scores[q_index].append(generate_similarity_score(question, sentence))
	return scores

def read_passage():
	passage_sentences = []
	passage_sentences = re.split(r'[\.\?!]', raw_input())
	return passage_sentences

def read_questions():
	questions = []
	for _ in range(5):
		questions.append(raw_input())
	return questions

def read_answers():
	answers = []
	answers = raw_input().split(';')
	return answers

if __name__ == "__main__":
	passage_sentences = read_passage()
	questions = read_questions()
	answers = read_answers()

	questions_passage_scores = generate_questions_passage_scores(questions, passage_sentences)

	selected_answers =  [False for _ in range(5)]
	selected_passage_sentence = [False for _ in range(len(passage_sentences))]

	for score_array in questions_passage_scores: # for each question
		
		max_so_far = -1
		for index, score in enumerate(score_array):
			if score > max_so_far and selected_passage_sentence[index] == False:
				passage_index = index
				max_so_far = score

		related_passage_sentence = passage_sentences[passage_index] # find the passage sentence with highest similarity score
		selected_passage_sentence[passage_index] = True

		for index, answer in enumerate(answers):
			if related_passage_sentence.count(answer) > 0 and selected_answers[index] == False:
				answer_index = index
				found = True

		print answers[answer_index]
		selected_answers[answer_index] = True