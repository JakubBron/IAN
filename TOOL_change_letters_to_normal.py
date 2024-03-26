import os

for root, directory, files in os.walk('.'):
	for file in files:
		if file[-3:].lower() == '.py':
			print('Changing in ' + root + '/' + file)
			
			new_file = ''
			
			with open(os.path.join(root, file)) as f:
				for line in f:
					new_line = line.replace('ą', 'a')
					new_line = new_line.replace('Ĺ', 'l')
					new_line = new_line.replace('‚Ă', 'o')
					new_line = new_line.replace('™', 'e')
					new_line = new_line.replace('ż', 'z')
					new_line = new_line.replace('ź', 'z')
					new_line = new_line.replace('ś', 's')
					new_line = new_line.replace('ń', 'n')
					new_file += new_line
						
			with open(os.path.join(root, file), 'w') as f:
				f.write(new_file)
input('done!')