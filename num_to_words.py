
def is_number(n):
	try: float(n)
	except: return False
	#for m in str(n):
	#	if m not in "1234567890.-":
	#		return False
	return True

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
	n = float(n)
	if n == 0:
		return "zero"
	sing = n / abs(n)
	n = abs(n)
	m = 0.0
	if not n - int(n) == 0:
		m = "{:.30f}".format(n - int(n)) #12.345 to "0.345"
		m = m.rstrip("0")
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
	n = float(n)
	if n == 0:
		return "cero"
	sing = n / abs(n)
	n = abs(n)
	m = 0.0
	if not n - int(n) == 0:
		m = "{:.30f}".format(n - int(n)) #12.345 a "0.345"
		m = m.rstrip("0")
	n = str(int(n))
	length = len(n)
	tri = []
	out = ""
	for not_important in range((length+2)/3): #12345678 a ['678', '345', '12']
		tri.append(n[-3:])
		n = n[:-3]
	lentri = len(tri)
	for i in range(lentri-1, -1, -1):
		if lentri == 5: #Trillones
			if tri[i] == '1':
				out = "un trillon "
			else:
				out = sub_numbers_to_words_es(tri[i]) + "trillones "
			lentri -= 1
			continue
		elif lentri == 4: #Billones
			if int(tri[i]) == 0:
				continue
			if tri[i] == '1' or tri[i] == '001':
				out = out + "un billon "
			else:
				out = out + sub_numbers_to_words_es(tri[i]) + "billones "
			lentri -= 1
			continue
		elif lentri == 3: #Millones
			if int(tri[i]) == 0:
				continue
			if tri[i] == '1' or tri[i] == '001':
				out = out + "un millon "
			else:
				out = out + sub_numbers_to_words_es(tri[i]) + "millones "
			lentri -= 1
			continue
		elif lentri == 2: #Miles
			if int(tri[i]) == 0:
				continue
			if tri[i] == '1' or tri[i] == '001':
				out = out + "mil "
			else:
				out = out + sub_numbers_to_words_es(tri[i]) + "mil "
			lentri -= 1
			continue #Es esto reundante?
		else: #Unidades
			out = out + sub_numbers_to_words_es(tri[i])
	if m:
		if out == "":
			out = "cero "
		out = out + "punto "
		m = str(m)[2:] #Remueve "0." de m
		for i in m:
			if i == "0":
				out = out + "cero "
			out = out + sub_numbers_to_words_es(i)
	if sing < 0:
		out = "menos " + out
	out.rstrip()
	return out

#Test, float input
"""
while 1:
	inp = float(raw_input("num: "))
	print "float:{} ; int:{} ; decimal:{}".format(float(inp), int(inp), inp-int(inp))
	print numbers_to_words_en(inp)
	print numbers_to_words_es(inp)
"""
#Test2, string input
"""
while 1:
	inp = raw_input("num: ")
	if inp == "exit": break
	print numbers_to_words_en(inp)
	print numbers_to_words_es(inp)
"""
