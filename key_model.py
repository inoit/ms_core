import msvcrt

#init keymap
keymap = {(8,None):'backspace',(13,None):'enter',(27,None):'esc'}
keymap.update({(i,None):chr(i) for i in range(32,127)})
keymap.update({(224,72):'up',(224,80):'down',(224,75):'left',(224,77):'right'})
#end init,start function

def keyboard(debug=False):
	ch = ord(msvcrt.getch())
	ch1 = ord(msvcrt.getch()) if msvcrt.kbhit() else None
	if debug:
		return '(ch:%s,ch1:%s)'%(ch,ch1)
	try:
		return keymap[(ch,ch1)]
	except:
		return 'notmach'

def input_box(max_len=6,keypad=True):
	text = []
	while True:
		ch = keyboard()
		if ch == 'backspace':
			if text:
				text.pop()
				print('\b \b',end='',flush=True)
		elif ch == 'enter':
			print('\n')
			break
		elif len(ch) == 1:
			if len(text) < max_len:
				text.append(ch)
				ch = ch if keypad else '*'
				print(ch,end='',flush=True)
	return ''.join(text)

if __name__ == '__main__':
	print(keyboard())
	print(keyboard(True))
	print(input_box())
	print(input_box(keypad=False))