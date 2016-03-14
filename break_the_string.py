
def break_text(text,max_len):
	l=[]
	start=0
	while start<len(text):
		space=text.rfind(" ",start,start+max_len+1)
		if space == -1:
			#no space found
			#print word more than max_len
			space=text.find(" ",start)
			if space != -1:
				l.append(text[start:space])
			else:
				l.append(text[start:])
				break
		else:
			l.append(text[start:space])
		start=space+1

	return l

