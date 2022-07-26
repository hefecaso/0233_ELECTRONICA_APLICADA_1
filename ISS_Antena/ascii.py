
ace = r'''
	  __^__                                      __^__
         ( ___ )------------------------------------( ___ )
          | / |                                      | \ |
          | / |          ISS antenna program         | \ |
          |___|                                      |___|
         (_____)------------------------------------(_____)
'''

two = r'''
 .-------.
|3      |
 |   ♦   |
 |   ♦   |
 |   ♦   |
|      3|
`-------´
'''

spacer = ' ' * 8  # Space between cards.
for a, b in zip(ace.splitlines(), two.splitlines()):
    print(f'{a}{spacer}{b}')

#Chekpoin menú, falta target ISS
