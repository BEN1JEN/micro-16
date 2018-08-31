def discard(word, discard_char):
	clean_word = ""
	for i in range(len(word)):
		char = word[i:i+1]
		if char != discard_char:
			clean_word = clean_word + char
	return clean_word

def get_until(word, seperator):
	until_word = ""
	i = 0
	char = ""
	while char != seperator and i < len(word):
		char = word[i:i+1]
		if char != seperator:
			until_word = until_word + char
		i += 1
	return until_word, i

def seperate(word, seperator):
	words = []
	until_word = ""
	for i in range(len(word)+1):
		char = word[i:i+1]
		if char == seperator:
			words.append(until_word)
			until_word = ""
		else:
			until_word = until_word + char
	words.append(until_word)
	return words
