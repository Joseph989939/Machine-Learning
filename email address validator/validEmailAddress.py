"""
File: validEmailAddress.py
Name: Joseph
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: TODO: 0.6153846153846154
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	score_list = []
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		# TODO:
		score = 0
		for i in range(len(feature_vector)):
			score += WEIGHT[i][0] * feature_vector[i]  # list of list
		score_list.append(score)
	# calculate accuracy
	right_predict = 0
	for i in range(len(score_list)):
		if i < 13:  # The first 13 (wrong email)
			if score_list[i] <= 0:  # right predict
				right_predict += 1
		else:  # # The last 13 (right email)
			if score_list[i] > 0:
				right_predict += 1
	accuracy = right_predict / 26
	print(accuracy)


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:  # 不可省略 不然到下行時如果沒有@會跳不出if
				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
		###################################
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[0] else 0  # 若是空字串變False, else
		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[-1] else 0
		elif i == 4:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@')[-1] else 0
		elif i == 5:
			if feature_vector[0]:
				feature_vector[i] = 1 if ' ' not in maybe_email else 0
		elif i == 6:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email[len(maybe_email)-4:] == '.com' else 0  # .com，不能用is?
		elif i == 7:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email[len(maybe_email)-4:] == '.edu' else 0  # .edu
		elif i == 8:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email[len(maybe_email)-3:] == '.tw' else 0  # .tw
		elif i == 9:
			if feature_vector[0]:
				feature_vector[i] = 1 if len(maybe_email) > 10 else 0  # length > 10
		###################################
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	# TODO:
	with open(DATA_FILE, 'r') as f:
		mail_list = []
		for line in f:
			mail_list.append(line.strip())
		return mail_list


if __name__ == '__main__':
	main()
