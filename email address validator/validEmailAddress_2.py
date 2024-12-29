"""
File: validEmailAddress_2.py
Name: Joseph
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  Only one '@' in the middle of str (0.1)
feature2:  '.' before and after '@' (-2)
feature3:  Some strings before and after '@' (0.4)
feature4:  There is '.' in domain name (0.5)
feature5:  There is continuous '.' in local mailbox part or domain name (-2.0)
feature6:  '.' is the first or last word in the local mailbox part (-2.0)
feature7:  There is no white space in email (0.7)
feature8:  There is '\' in the local mailbox part (-2.0)
feature9:  There is '(' or ')' in the local mailbox part (-2.0)
feature10: There is '<' or '>' in the local mailbox part (-2.0)
Accuracy of your model: 0.8846153846153846
"""
import numpy as np
WEIGHT = [                           # The weight vector selected by you
	[],                              # (Please fill in your own weights)
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	score_list = []
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		# print(feature_vector)
		weight_vector = np.asarray([[0.1], [-2], [0.4], [0.5], [-2.0], [-2.0], [0.7], [-2.0], [-2.0], [-2.0]])
		weight_vector = weight_vector.T
		score = weight_vector.dot(feature_vector)
		# print(score)
		for score_num in score:
			score_list.append(score_num[0])
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
	print('accuracy: ' + str(accuracy))


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	# feature_vector = [0] * len(WEIGHT)
	feature_vector = np.zeros((10, 1))
	for i in range(len(feature_vector)):
		if i == 0:
			# 排除@前面沒字串，且@在中間
			feature_vector[i][0] = 1 if maybe_email.split('@')[0] and len(maybe_email.split('@')) == 2 else 0
		###################################
		elif i == 1:
			if feature_vector[0][0]:  # 不可省略 不然到下行時如果沒有@會跳不出if
				feature_vector[i][0] = 1 if '.@' in maybe_email or '@.' in maybe_email else 0
		elif i == 2:
			if feature_vector[0][0]:
				feature_vector[i][0] = 1 if maybe_email.split('@')[0] and maybe_email.split('@')[1] else 0
		elif i == 3:
			if feature_vector[0][0]:
				feature_vector[i][0] = 1 if '.' in maybe_email.split('@')[1] else 0
		elif i == 4:
			if feature_vector[0][0]:
				if maybe_email.split('@')[0]:  # 排除@前面沒字串，否則maybe_email.split('@')[0][0]會string-index-out-of-range
					if "\"" not in maybe_email.split('@')[0][0] and "\"" not in maybe_email.split('@')[0][-1]:
						feature_vector[i][0] = 1 if '' in maybe_email.split('@')[1].split('.') \
													or '' in maybe_email.split('@')[0].split('.') else 0
		elif i == 5:
			if feature_vector[0][0]:
				feature_vector[i][0] = 1 if maybe_email[0] is '.' or maybe_email[-1] is '.' else 0
		elif i == 6:
			if feature_vector[0][0]:
				feature_vector[i][0] = 1 if ' ' not in maybe_email else 0
		elif i == 7:
			if feature_vector[0][0]:
				feature_vector[i][0] = 1 if '\\' in maybe_email.split('@')[0] else 0
		elif i == 8:
			if feature_vector[0][0]:
				feature_vector[i][0] = 1 if '(' in maybe_email.split('@')[0] or ')' in maybe_email.split('@')[0] else 0
		elif i == 9:
			if feature_vector[0][0]:
				feature_vector[i][0] = 1 if '<' in maybe_email.split('@')[0] or '>' in maybe_email.split('@')[0] else 0
		###################################
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	# TODO:
	with open(DATA_FILE, 'r') as f:
		mail_list = []
		for line in f:
			mail_list.append(line.strip())
		return mail_list


if __name__ == '__main__':
	main()
