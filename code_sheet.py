Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;
>>> a+=30;
>>> a%=3;
>>> a
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3)and(7<4)or (18==3))and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True==False)or(False>True))and(False<=True)
False
>>> 
>>> s1='Nice to have it'
>>> s2='here'
>>> s3 = s1 + s2
>>> 
>>> s3
'Nice to have ithere'
>>> 
>>> a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3]
[5, [100, 200, ['hello']], 23, 11]
>>> a[3][1]
[100, 200, ['hello']]
>>> a[3][1][2]
['hello']
>>> 
>>> a.insert(0,'s1')
>>> a
['s1', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.insert(7,'s2')
>>> a
['s1', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 's2']
>>> 
>>> d=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
>>> for i in d:
	if d==237:
		print(d)
		break;
	elif d % 2 == 0:
		print(d)

		
Traceback (most recent call last):
  File "<pyshell#40>", line 5, in <module>
    elif d % 2 == 0:
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> TypeError: unsupported operand type(s) for %: 'list' and 'int'
SyntaxError: invalid syntax
>>> 
>>> z={'white','black','red'}
>>> x={'red','green'}
>>> v = z.difference(x)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    v = z.difference(x)
NameError: name 'x' is not defined
>>> 
>>> 
>>> z={'white','black','red'}
>>> x={'red','green'}
>>> z.difference(x)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    z.difference(x)
NameError: name 'x' is not defined
>>> z={'white','black','red'}
>>> x={'red','green'}
>>> z.difference(x)
{'white', 'black'}
>>> 
>>> 
KeyboardInterrupt
>>> 