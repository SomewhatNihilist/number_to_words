
def is_number(n):
	for m in str(n):
		if m not in "1234567890.-":
			return False
	return True

def sub_numbers_to_words_en(n):
	"""Converts a 1-3 digit number to format "x(hundreds) y(tens) z(units) " """
	pass

def sub_numbers_to_words_es(n):
	"""Convierte un numero de 1-3 digitos al formato "x(cientos) y(decenas) z(unidades) " ej. 123 a "ciento veintitres " 
	if the input is longer than 3 digits, returns "" """
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
