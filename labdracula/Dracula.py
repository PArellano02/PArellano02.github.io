#access the html and turn in into Izbicky.html

file = open('labdracula/Dracula.html','r', encoding = 'utf-8')
text = file.read()


text = text.replace('Dracula', ' <strong>Izbicki</strong>')
text = text.replace('DRACULA', ' <strong>IZBICKI</strong>')
text = text.replace('D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A' , '<strong>I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I</strong>')
text = text.replace(' count ', ' Professor ')
text = text.replace('Bram Stoker', 'Pedro Arellano')
text = text.replace('Bram &nbsp; Stoker', 'Pedro &nbsp; Arellano')
text = text.replace('Count', ' Professor ')




filew = open('labdracula/Izbicki.html', 'w' , encoding = 'utf-8')
filew.write(text)
