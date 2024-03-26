import os

for root, directory, files in os.walk('.'):
	for file in files:
		if file[-3:].lower() == '.py':
			print('Changing in ' + root + '/' + file)
			
			new_file = ''
			
			with open(os.path.join(root, file)) as f:
				for line in f:
					new_file += line.replace(' ' + '   ', '\t')
						
			with open(os.path.join(root, file), 'w') as f:
				f.write(new_file)
input('done!')