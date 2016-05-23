
def is_number(n):
	"""for m in str(n):
		if m not in "1234567890.-":
			return False"""
	try: int(n)
	except: return False
	else: return True

def sub_numbers_to_words_en(n):
	"""Converts a 1-3 digit number to format "x(hundreds) y(tens) z(units) " """
	n = str(n)
	length = len(n)
	out = ""
	dec = 3
	for m in n:
		if length == 3:
			h = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
			if m != "0":
				out = out + h[int(m)] + " hundred and "
			length -= 1
			continue
		if length == 2:
			d = ["", "", "twenty-", "thirty-", "forty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"]
			dec = int(m)
			out = out + d[dec]
			length -= 1
			continue
		if length == 1:
			if dec == 0 and m == "0":
				out = out[:-4]
				break
			elif dec == 1:
				du = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fithteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
				out = out + du[int(m)]
				break
			elif m == "0":
				out = out[:-1]
				break
			u = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "]
			out = out + u[int(m)]
			break
	return out

def sub_numbers_to_words_es(n):
	"""Convierte un numero de 1-3 digitos al formato "x(cientos) y(decenas) z(unidades) " ej. 123 a "ciento veintitres " 
	if the input is longer than 3 digits, returns '' """
	n = str(n)
	length = len(n)
	out = ""
	dec = 3
	for m in n:
		if length == 3:
			c = ["", "ciento ", "doscientos ", "trescientos ", "cuatrocientos ", "quinientos ", "seiscientos ", "setecientos ", "ochocientos ", "novecientos "]
			out = out + c[int(m)]
			length -= 1
			continue
		if length == 2:
			d = ["", "", "veinti", "treinta y ", "cuarenta y ", "cincuenta y ", "sesenta y ", "setenta y ", "ochenta y ", "noventa y "]
			dec = int(m)
			out = out + d[dec]
			length -= 1
			continue
		if length == 1:
			if dec == 1:
				du = ["diez ", "once ", "doce ", "trece ", "catorce ", "quince ", "dieciseis ", "diecisiete ", "dieciocho ", "diecinueve "]
				out = out + du[int(m)]
				break
			elif m == "0" and dec != 0:
				if dec == 2:
					out = out[:-1] + "e "
				else:
					out = out[:-3]
				break
			u = ["", "uno ", "dos ", "tres ", "cuatro ", "cinco ", "seis ", "siete ", "ocho ", "nueve "]
			out = out + u[int(m)]
			break
	if out == "ciento ":
		out = "cien "
	return out

def numbers_to_words_en(n):
	"""Receives numbers up to 999999999999999.999..."""
	if not is_number(n):
		return "NaN"
	if n == 0:
		return "zero"
	sing = n / abs(n)
	n = abs(n)
	m = 0
	if not n - int(n) == 0:
		m = n - int(n) #12.345 to 0.345
	n = str(int(n))
	length = len(n)
	tri = []
	out = ""
	for not_important in range((length+2)/3): #12345678 to ['678', '345', '12']
		tri.append(n[-3:])
		n = n[:-3]
	lentri = len(tri)
	for i in range(lentri-1, -1, -1):
		if lentri == 5: #Trillions
			out = sub_numbers_to_words_en(tri[i]) + "trillion "
			lentri -= 1
			continue
		elif lentri == 4: #Billions
			if int(tri[i]) == 0:
				continue
			out = out + sub_numbers_to_words_en(tri[i]) + "billion "
			lentri -= 1
			continue
		elif lentri == 3: #Millions
			if int(tri[i]) == 0:
				continue
			out = out + sub_numbers_to_words_en(tri[i]) + "million "
			lentri -= 1
			continue
		elif lentri == 2: #Thousands
			if int(tri[i]) == 0:
				continue
			out = out + sub_numbers_to_words_en(tri[i]) + "thousand "
			lentri -= 1
			continue
		else: #Units
			out = out + sub_numbers_to_words_en(tri[i])
	if m:
		if out == "":
			out = "zero "
		out = out + "point "
		m = str(m)[2:] #Remove leading zero and point
		for i in m:
			if i == "0":
				out = out + "zero "
			out = out + sub_numbers_to_words_en(i)
	if sing < 0:
		out = "minus " + out
	out.rstrip()
	return out

def numbers_to_words_es(n):
	if not is_number(n):
		return "NaN"
	sing = n / abs(n)
	n = abs(n)
	if n - int(n) == 0:
		m = n - int(n)
	n = int(n)
	length = len(str(n))
	pass

"""
while 1:
	inp = float(raw_input("num: "))
	print imp
	print numbers_to_words_en(inp)
	#print numbers_to_words_es(inp)
"""