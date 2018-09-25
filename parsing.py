from sys import stdin


INPUT,I = stdin.buffer.read(),0
SPACE,CR,LPAR,RPAR,ZERO,NINE,NEG = ord(' '),ord('\n'),ord('('),ord(')'),ord('0'),ord('9'),ord('-')

def has_next(): return I<len(INPUT)
def is_digit(): return ZERO <= INPUT[I] <= NINE
def is_par(): return INPUT[I] == LPAR or INPUT[I] == RPAR
def is_neg(): return INPUT[I] == NEG
def read_blanks():
	global INPUT,I
	while has_next() and not is_digit() and not is_par() and not is_neg():
		I+=1
def read_par():
	global INPUT,I
	ans,I = chr(INPUT[I]),I+1
	return ans
def read_num():
	global INPUT,I
	ans = 0
	while has_next() and is_digit():
		ans,I = int(chr(INPUT[I]))+ans*10,I+1
	return ans
def read_neg_num():
	global INPUT,I
	ans = 0
	I+=1
	while has_next() and is_digit():
		ans,I = int(chr(INPUT[I]))+ans*10,I+1
	return ans*-1

def next_token():
	global INPUT,I
	ans = None
	read_blanks()
	if I!=len(INPUT):	
		if is_digit(): ans = read_num()
		elif is_neg(): ans = read_neg_num()
		else: ans = read_par()
	return ans
