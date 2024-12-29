"""
File: interactive.py
Name: Joseph
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

from submission import extractWordFeatures
from util import interactivePrompt


def main():
	weights = {}
	with open('weights', 'r', encoding="utf-8") as f:
		for line in f:
			key, value = line.split()
			weights[key] = float(value)
	interactivePrompt(extractWordFeatures, weights)


if __name__ == '__main__':
	main()
