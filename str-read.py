Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import shapely
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import shapely
ModuleNotFoundError: No module named 'shapely'
>>> teste = [{'url': 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506', 'title': 'Local: Icaraí/Niterói', 'image': {'width': 250, 'height': 125, 'url': 'https://maps.googleapis.com/maps/api/staticmap?center=-22.9060867582,-43.1138723506&markers=color:red%7C-22.9060867582,-43.1138723506&maptype=roadmap&size=250x125&zoom=15&key=AIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM', 'proxy_url': 'https://images-ext-2.discordapp.net/external/Pq_Uary9qCW_V9DW2FdXP6rhVzJvvvuKccP5b-IFzJ8/%3Fcenter%3D-22.9060867582%2C-43.1138723506%26markers%3Dcolor%3Ared%257C-22.9060867582%2C-43.1138723506%26maptype%3Droadmap%26size%3D250x125%26zoom%3D15%26key%3DAIzaSyBEeT1GiIFzQddKucuSOuSTP-HRZXVYkfM/https/maps.googleapis.com/maps/api/staticmap'}, 'description': 'IVs: 93.3% (14/15/13) \nCP: 190 \nLevel:33 \nMoves: Splash / Struggle\nhttp://maps.google.com/maps?q=-22.9060867582,-43.1138723506 \nClima: :cloud_rain: \nDisponível até 15:07:33 (5m 50s).', 'type': 'rich', 'thumbnail': {'width': 128, 'height': 128, 'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}}]
>>> teste[0]['thumbnail']
{'width': 128, 'height': 128, 'url': 'https://raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png', 'proxy_url': 'https://images-ext-1.discordapp.net/external/o4BfmiOWImz7owLVpzaFC7WlnC03o2ZA0pfKAwcWWyQ/https/raw.githubusercontent.com/Gladiator10864/PokeAlarm/master/icons/129.png'}
>>> texto[texto.find('CP:'):texto.find('\',texto.find('CP:'))]
				   
SyntaxError: invalid syntax
>>> texto[texto.find('IVs:')+5:texto.find(')')+1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    texto[texto.find('IVs:')+5:texto.find(')')+1]
NameError: name 'texto' is not defined
>>> texto=teste[0]['description']
>>> texto[texto.find('IVs:')+5:texto.find(')')+1]
'93.3% (14/15/13)'
>>> texto[texto.find('IVs:')+5:texto.find('%')+1]
'93.3%'
>>> texto[texto.find('(')+5:texto.find('/')+1]
''
>>> texto[texto.find('(')+1:texto.find('/')+1]
'14/'
>>> 
KeyboardInterrupt
>>> texto[texto.find('(')+1:texto.find('/')]
'14'
>>> texto.splitlines()
['IVs: 93.3% (14/15/13) ', 'CP: 190 ', 'Level:33 ', 'Moves: Splash / Struggle', 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506 ', 'Clima: :cloud_rain: ', 'Disponível até 15:07:33 (5m 50s).']
>>> texto.splitlines()[1]
'CP: 190 '
>>> texto.splitlines()[0]
'IVs: 93.3% (14/15/13) '
>>> txt=texto.splitlines()
>>> txt
['IVs: 93.3% (14/15/13) ', 'CP: 190 ', 'Level:33 ', 'Moves: Splash / Struggle', 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506 ', 'Clima: :cloud_rain: ', 'Disponível até 15:07:33 (5m 50s).']
>>> txt[1]
'CP: 190 '
>>> txt[3]
'Moves: Splash / Struggle'
>>> txt[5]
'Clima: :cloud_rain: '
>>> size(txt)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    size(txt)
NameError: name 'size' is not defined
>>> txt.size()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    txt.size()
AttributeError: 'list' object has no attribute 'size'
>>> txt.size
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    txt.size
AttributeError: 'list' object has no attribute 'size'
>>> len(txt)
7
>>> txt[6]
'Disponível até 15:07:33 (5m 50s).'
>>> txt[7]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    txt[7]
IndexError: list index out of range
>>> txt[0]
'IVs: 93.3% (14/15/13) '
>>> txt[0].split('/')
['IVs: 93.3% (14', '15', '13) ']
>>> txt[0].rstrip('/')
'IVs: 93.3% (14/15/13) '
>>> txt[0].split('(')
['IVs: 93.3% ', '14/15/13) ']
>>> txt[0].split('(').split('/')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    txt[0].split('(').split('/')
AttributeError: 'list' object has no attribute 'split'
>>> txt[0].split('(')
['IVs: 93.3% ', '14/15/13) ']
>>> (txt[0].split('(')).split('/')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    (txt[0].split('(')).split('/')
AttributeError: 'list' object has no attribute 'split'
>>> txt[0].split('(')
['IVs: 93.3% ', '14/15/13) ']
>>> a=txt[0].split('(')
>>> a
['IVs: 93.3% ', '14/15/13) ']
>>> a[0]
'IVs: 93.3% '
>>> a[1].split('/')
['14', '15', '13) ']
>>> a[1].split('/').rstrip(')')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[1].split('/').rstrip(')')
AttributeError: 'list' object has no attribute 'rstrip'
>>> a
['IVs: 93.3% ', '14/15/13) ']
>>> txt[0].split('(')
['IVs: 93.3% ', '14/15/13) ']
>>> txt[0][0:10].split('(')
['IVs: 93.3%']
>>> txt[0][0:len(txt)].split('(')
['IVs: 93']
>>> txt[0]
'IVs: 93.3% (14/15/13) '
>>> txt[0][0:len(txt)]
'IVs: 93'
>>> len(txt)
7
>>> txt
['IVs: 93.3% (14/15/13) ', 'CP: 190 ', 'Level:33 ', 'Moves: Splash / Struggle', 'http://maps.google.com/maps?q=-22.9060867582,-43.1138723506 ', 'Clima: :cloud_rain: ', 'Disponível até 15:07:33 (5m 50s).']
>>> txt[0][0:len(txt[0])]
'IVs: 93.3% (14/15/13) '
>>> txt[0][0:len(txt[0])].split('(')
['IVs: 93.3% ', '14/15/13) ']
>>> txt[0][0:len(txt[0])-1]
'IVs: 93.3% (14/15/13)'
>>> txt[0][0:len(txt[0])-2]
'IVs: 93.3% (14/15/13'
>>> txt[0][0:len(txt[0])-2].split('(')
['IVs: 93.3% ', '14/15/13']
>>> txt[0][0:len(txt[0])-2].split('(')[1]
'14/15/13'
>>> txt[0][0:len(txt[0])-2].split('(')[1].split['/']
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    txt[0][0:len(txt[0])-2].split('(')[1].split['/']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> txt[0][0:len(txt[0])-2].split('(')[1]
'14/15/13'
>>> a=txt[0][0:len(txt[0])-2].split('(')[1]
>>> a.split('/')
['14', '15', '13']
>>> txt[0]
'IVs: 93.3% (14/15/13) '
>>> txt[0][txt[0].find('('):None]
'(14/15/13) '
>>> txt[0][txt[0].find('('):None].split('/')
['(14', '15', '13) ']
>>> txt[0][txt[0].find('(')+1:None].split('/')
['14', '15', '13) ']
>>> txt[0][txt[0].find('(')+1:-1].split('/')
['14', '15', '13)']
>>> txt[0][txt[0].find('(')+1:txt[0].find(')'))].split('/')
SyntaxError: invalid syntax
>>> txt[0][txt[0].find('(')+1:txt[0].find(')')].split('/')
['14', '15', '13']
>>> n=txt[0][txt[0].find('(')+1:txt[0].find(')')].split('/')
>>> n
['14', '15', '13']
>>> n[0]+n[1]
'1415'
>>> x=int(n)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x=int(n)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> x[]=int(n[])
SyntaxError: invalid syntax
>>> x = [int(aux) for aux in n]
>>> x
[14, 15, 13]
>>> c = [inx(j) for j in txt[0][txt[0].find('(')+1:txt[0].find(')')].split('/')]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    c = [inx(j) for j in txt[0][txt[0].find('(')+1:txt[0].find(')')].split('/')]
  File "<pyshell#70>", line 1, in <listcomp>
    c = [inx(j) for j in txt[0][txt[0].find('(')+1:txt[0].find(')')].split('/')]
NameError: name 'inx' is not defined
>>> c = [int(j) for j in txt[0][txt[0].find('(')+1:txt[0].find(')')].split('/')]
>>> c
[14, 15, 13]
>>> sum(c)
42
>>> sum(c)/45
0.9333333333333333
>>> (sum(c)/45)
0.9333333333333333
>>> (sum(c)/45)*100
93.33333333333333
>>> from decimal import *
>>> Decimal(1)
Decimal('1')
>>> Decimal(1) / Decimal(7)
Decimal('0.1428571428571428571428571429')
>>> round((sum(c)/45)*100)
93
>>> round((sum(c)/45)*100,2)
93.33
>>> round((sum(c)/45)*100,1)
93.3
>>> 
