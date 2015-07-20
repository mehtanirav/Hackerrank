# Matching questions with answers
# Algortihm: Calculate the similarity score between the question and every sentence in
# the passage. The sentence with highest similarity score is most likely to contain the answer.
# Next, calculate similarity score between that sentence and the all the answers. The answer with
# highest similarity score is most likely to be the answer to the question

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

	if len(y_tokens) == 1 and y_tokens[0] in x_tokens:
		return x_tokens.count(y_tokens[0])

	x_bigrams = set(bigrams(x_tokens))
	y_bigrams = set(bigrams(y_tokens))

	intersection_set = x_bigrams.intersection(y_bigrams)
	return len(intersection_set)

def generate_passage_answers_scores(passage_sentence, answers):
	scores = []
	for answer in answers:
		scores.append(generate_similarity_score(passage_sentence, answer))
	return scores

def generate_questions_passage_scores(questions, passage_sentences):
	scores = []
	for q_index, question in enumerate(questions):
		scores.append([])
		for _, sentence in enumerate(passage_sentences):
			scores[q_index].append(generate_similarity_score(question, sentence))
	return scores

def read_passage():
	passage_sentences = []
	passage_sentences = re.split(r'[\.\?]', raw_input())
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

	for score_array in questions_passage_scores: # for each question
		
		m = max(score_array)
		for index, score in enumerate(score_array):
			if score == m:
				passage_index = index
				break
		related_passage_sentence = passage_sentences[passage_index] # find the passage sentence with highest similarity score

		passage_answers_scores = generate_passage_answers_scores(related_passage_sentence, answers)

		max_so_far  = -1
		for i, pass_answer_score in enumerate(passage_answers_scores):
			if pass_answer_score >= max_so_far and selected_answers[i] == False:
				max_index = i
				max_so_far = pass_answer_score

		print answers[max_index]
		selected_answers[max_index] = True