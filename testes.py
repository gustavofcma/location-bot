Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> teste = []
>>> teste
[]
>>> teste = [{'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'title': 'Local: Icaraí/Niterói', 'image': {'width': 250, 'height': 125, 'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}, 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'type': 'rich', 'thumbnail': {'width': 128, 'height': 128, 'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}}]
>>> teste
[{'type': 'rich', 'thumbnail': {'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'width': 128, 'height': 128, 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}, 'title': 'Local: Icaraí/Niterói', 'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'image': {'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'width': 250, 'height': 125, 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}}]
>>> teste[1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    teste[1]
IndexError: list index out of range
>>> teste{1}
SyntaxError: invalid syntax
>>> teste[1][1]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    teste[1][1]
IndexError: list index out of range
>>> teste
[{'type': 'rich', 'thumbnail': {'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'width': 128, 'height': 128, 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}, 'title': 'Local: Icaraí/Niterói', 'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'image': {'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'width': 250, 'height': 125, 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}}]
>>> teste(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    teste(1)
TypeError: 'list' object is not callable
>>> teste[0]
{'type': 'rich', 'thumbnail': {'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'width': 128, 'height': 128, 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}, 'title': 'Local: Icaraí/Niterói', 'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'image': {'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'width': 250, 'height': 125, 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}}
>>> teste
[{'type': 'rich', 'thumbnail': {'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'width': 128, 'height': 128, 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}, 'title': 'Local: Icaraí/Niterói', 'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'image': {'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'width': 250, 'height': 125, 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}}]
>>> teste[0]
{'type': 'rich', 'thumbnail': {'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'width': 128, 'height': 128, 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}, 'title': 'Local: Icaraí/Niterói', 'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'image': {'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'width': 250, 'height': 125, 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}}
>>> teste[0][1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    teste[0][1]
KeyError: 1
>>> teste[0][0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    teste[0][0]
KeyError: 0
>>> teste[0,1]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    teste[0,1]
TypeError: list indices must be integers or slices, not tuple
>>> teste[0].1
SyntaxError: invalid syntax
>>> teste[0]{0}
SyntaxError: invalid syntax
>>> teste[0]
{'type': 'rich', 'thumbnail': {'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'width': 128, 'height': 128, 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}, 'title': 'Local: Icaraí/Niterói', 'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'image': {'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'width': 250, 'height': 125, 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}}
>>> type(teste)
<class 'list'>
>>> type(teste[0])
<class 'dict'>
>>> index(teste[0])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    index(teste[0])
NameError: name 'index' is not defined
>>> 'type' in teste[0]
True
>>> teste[0]['type']
'rich'
>>> teste[0]['thumbnail']
{'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'width': 128, 'height': 128, 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}
>>> a = "Título: {} \n Texto: {}".format(teste[0]['title'],teste[0]['description'])
>>> a
'Título: Local: Icaraí/Niterói \n Texto: IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).'
>>> a = "Título: {} - Texto: {}".format(teste[0]['title'],teste[0]['description'])
>>> a
'Título: Local: Icaraí/Niterói - Texto: IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).'
>>> titulo = teste[0]['title']
>>> texto = teste[0]['description']
>>> titulo
'Local: Icaraí/Niterói'
>>> texto
'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).'
>>> url = teste[0]['url']
>>> url
'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506'
>>> url
'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506'
>>> url[4:4]
''
>>> url[4:None]
'://maps.google.com/maps?q=-22.9060867582,-43.1138723506'
>>> url[4:8]
'://m'
>>> url['/':None]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    url['/':None]
TypeError: slice indices must be integers or None or have an __index__ method
>>> url[20:30]
'om/maps?q='
>>> url[31:50]
'22.9060867582,-43.1'
>>> url[30:44]
'-22.9060867582'
>>> url.find('-')
30
>>> url[url.find('-'):url.find(',')]
'-22.9060867582'
>>> url[url.find(',-'):None]
',-43.1138723506'
>>> url[url.find(',')+2:None]
'43.1138723506'
>>> url[url.find(',')+1:None]
'-43.1138723506'
>>> title
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    title
NameError: name 'title' is not defined
>>> titulo
'Local: Icaraí/Niterói'
>>> texto
'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).'
>>> texto[texto.find('IVs'):texto.find(')')]
'IVs: 93.3% (14/15/13'
>>> texto[texto.find('IVs'):texto.find(')')+1]
'IVs: 93.3% (14/15/13)'
>>> texto[texto.find('IVs:'):texto.find(')')+1]
'IVs: 93.3% (14/15/13)'
>>> texto[texto.find('CP:'):texto.find('\n')+1]
''
>>> texto[texto.find('CP:'):texto.find('\n',texto.find('CP:'))+1]
'CP: 190 \n'
>>> texto[texto.find('CP:'):texto.find('\',texto.find('CP:'))]
				   
SyntaxError: invalid syntax
>>> texto[texto.find('CP:'):texto.find('\n',texto.find('CP:'))-1]
'CP: 190'
>>> texto[texto.find('CP:'):texto.find('\n',texto.find('CP:'))-2]
'CP: 19'
>>> texto[texto.find('CP:'):texto.find('\n',texto.find('CP:'))-2]
'CP: 19'
>>> texto[texto.find('CP:'):texto.find('\n',texto.find('CP:'))-1]
'CP: 190'
>>> texto[texto.find('CP:')+3:texto.find('\n',texto.find('CP:'))-1]
' 190'
>>> texto[texto.find('CP:')+4:texto.find('\n',texto.find('CP:'))-1]
'190'
>>> texto[texto.find('IVs:')+4:texto.find(')')+1]
' 93.3% (14/15/13)'
>>> texto[texto.find('IVs:')+5:texto.find(')')+1]
'93.3% (14/15/13)'
>>> _texto = texto
>>> a = 'Magikarp♀#0000'
>>> a
'Magikarp♀#0000'
>>> a[:5]
'Magik'
>>> a[:a.find('#')]
'Magikarp♀'
>>> a[:a.find('#')-1]
'Magikarp'
>>> a[a.find('#')-1:a.find('#')]
'♀'
>>> a[a.find('♀'):a.find('♀')-1]
''
>>> a[a.find('♀'):a.find('♀')]
''
>>> a[a.find('♀')-1:a.find('♀')]
'p'
>>> a[a.find('♀')-1:a.find('♀')+1]
'p♀'
>>> a[a.find('♀'):a.find('♀')+1]
'♀'
>>> a[a.find('♀'):a.find('♀')+1]
'♀'
>>> a[a.find(or('♀','♂')):a.find('♀')+1]
SyntaxError: invalid syntax
>>> a[a.find('#')-1:a.find('#')]
'♀'
>>> true(1)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    true(1)
NameError: name 'true' is not defined
>>> True()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    True()
TypeError: 'bool' object is not callable
>>> 1==1
True
>>> 1
1
>>> if(1)
SyntaxError: invalid syntax
>>> if(1):
	print(1)
	else:
		
SyntaxError: invalid syntax
>>> if(1):
	print(1)
else:
	print(0)

	
1
>>> 
