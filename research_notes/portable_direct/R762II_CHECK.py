#!/usr/bin/env python3
"""R762II: exact finite check of Port-induced-edge extremal bounds."""
from itertools import combinations
from functools import lru_cache

axes=range(6)
ports=list(combinations(axes,2))
supports=list(combinations(axes,3))
port_index={p:i for i,p in enumerate(ports)}
triangle_edges=[]
for s in supports:
    v=[port_index[p] for p in combinations(s,2)]
    triangle_edges.extend([tuple(sorted((v[0],v[1]))),tuple(sorted((v[0],v[2]))),tuple(sorted((v[1],v[2])))])
assert len(ports)==15 and len(supports)==20 and len(set(triangle_edges))==60

f=[0]*16
arg=[None]*16
for mask in range(1<<15):
    sz=mask.bit_count()
    e=sum((mask>>u&1) and (mask>>v&1) for u,v in triangle_edges)
    if arg[sz] is None or e>f[sz]:
        f[sz]=e;arg[sz]=mask

@lru_cache(None)
def max_edges_in_components(number,vertices):
    """Upper bound allowing independent maximizers f(s) for each component."""
    if number==0:
        return 0 if vertices==0 else -10**9
    if vertices<number: return -10**9
    return max(f[s]+max_edges_in_components(number-1,vertices-s)
               for s in range(1,vertices-number+2))

bounds=[]
for k in range(8):
    c=2*k+1
    max_inside=max(max_edges_in_components(c,v) for v in range(c,16))
    max_types=min(20,k+max_inside)
    upper=3*max_types+k
    bounds.append((k,c,max_inside,max_types,upper))

assert f[5]==10 and f[6]==12 and f[7]==15,(f[5],f[6],f[7])
assert bounds[4][2]==15 and bounds[4][3]==19,bounds[4]
assert bounds[5][3]==15 and bounds[6][3]==9 and bounds[7][3]==7,bounds
assert max(row[4] for row in bounds)==63,bounds
print('PASS R762II')
print('F_L(K6)(0..15):',f)
print('k / #components / maximal internal edges / maximal support types / event upper:')
for row in bounds: print(*row,sep=' / ')
print('7-Port extremizer:', [''.join(map(str,ports[i])) for i in range(15) if (arg[7]>>i)&1])
