from graphviz import *
d = Digraph(engine = 'neato')
d.attr('node', style = 'filled', color = 'goldenrod2', shape = 'septagon', size = '7.5')

d.node('a','7th Edition')
d.node('b','32V')
d.node('c','V7M')
d.node('d','Xenix')
d.node('e','UniPlus+')

d.node('32v_a','3 BSD')
d.node('32v_b','4 BSD')
d.node('K','4.1 BSD')

d.node('A','4.2 BSD')
d.node('B','4.3 BSD')
d.node('C','Ultrix-32')

d.node('M','8th Edition')
d.node('N','9th Edition')

d.node('O', '1 BSD')
d.node('P', '2 BSD')
d.node('Q', '2.8 BSD')
d.node('R', 'Ultrix-11')
d.node('S', '2.9 BSD')

d.edges(['ab','ac','ad','ae'])
d.edge('b','32v_a')
d.edge('32v_a','32v_b')
d.edge('32v_b','K')
d.edge('K','A')
d.edges(['AB','AC'])
d.edge('K','M')
d.edge('M','N')
d.edge('O','P')
d.edge('P','Q')
d.edges(['QR','QS'])

d.edge('K','Q')

print(d.source)

d.render(view = True)