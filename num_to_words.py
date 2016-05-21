
def is_number(n):
	for m in str(n):
		if m not in "1234567890.-":
			return False
	return True

def sub_numbers_to_words_en(n):
	"""Converts a 1-3 digit number to format x hundred y (tens) z (units)"""
	pass

def sub_numbers_to_words_en(n):
	"""Convierte un numero de 1-3 digitos al formato x cientos y (decimos) z (unidades)"""
	pass

def numbers_to_words_en(n):
	if not is_number(n):
		return "NaN"
    sing = n / abs(n)
    n = abs(n)
    if n - int(n) == 0:
    	m = n - int(n) #12.345 to 0.345
    n = int(n)
    length = len(str(n))


def numbers_to_words_es(n):
	if not is_number(n):
		return "NaN"
    sing = n / abs(n)
    n = abs(n)
    if n - int(n) == 0:
    	m = n - int(n)
    n = int(n)
    length = len(str(n))
