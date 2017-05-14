from collections import Counter

string_t = "Hello my friend! How are you? Would you like to have a cup of tea? Could you please tell a story about yourself?"

print "Original String: \n", string_t, "\n"

def filter_specail(s, special_set = ['?', '!', ',', '\\', '/']):
	for _, item in enumerate(special_set):
		s = s.replace(item, '')
	return s

new_s = map(filter_specail, [string_t])
new_s = map(lambda x: x.lower(), new_s)
new_s = map(lambda x: x.split(), new_s)
print "After filter special character(lower() and split()): \n", new_s, "\n"

def shuffle(s):
	return {s:1}

new_s = map(shuffle, new_s[0])
print "After shuffle: \n", new_s, "\n"

count_dict = reduce(lambda x, y: Counter(x) + Counter(y), new_s)

print "After 'reduce' we get final result dictionary: \n", count_dict
