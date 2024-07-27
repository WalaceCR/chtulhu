seq = 'AUUCCUUCTGG'
seq = seq.replace('A', 'G')
seq = seq.replace('U', 'T')


G = seq.count('G')
C = seq.count('C')
T = seq.count('T')

print(G, C, T)