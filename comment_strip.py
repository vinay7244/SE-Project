import re
def comment_strip(txt):
	return re.sub('//.*?\n|/\*.*?\*/', '', txt, flags=re.S)
