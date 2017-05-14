from collections import Counter

string_t = 'Hello my friend! How are you? Would you like to have a cup of tea?'

def filter_specail(s, special_set = ['?', '!', ',', '\\', '/']):
	for _, item in enumerate(special_set):
		s = s.replace(item, '')
	return s

new_s = map(filter_specail, [string_t])
new_s = map(lambda x: x.lower(), new_s)
new_s = map(lambda x: x.split(), new_s)
print new_s

def shuffle(s):
	return {s:1}

new_s = map(shuffle, new_s[0])
print new_s

count_dict = reduce(lambda x, y: Counter(x) + Counter(y), new_s)

print count_dict