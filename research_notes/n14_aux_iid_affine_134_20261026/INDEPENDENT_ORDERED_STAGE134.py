"""N14 Stage134 independent-in-implementation exact literal ordered-word DFS.
Recomputes recursive Bellman and enumerates integer-weight sample histories.
Author-side finite auxiliary iid model only. No native result or independent Driver review.
"""
from fractions import Fraction as R
from functools import lru_cache
from collections import defaultdict
from itertools import product
import json
from pathlib import Path
N=14
p=(3,1,20); q=(1,1,10)
den_p=24**N; den_q=12**N
k=R(48012912,81457); ell=R(45307624,81457)
B=(11,0,1); G=(9,3,3)
@lru_cache(None)
def choice(n,a,b):
    offers={'P':k*R(2**(a+b),3**a),'Q':ell}
    if n<N:
        offers['C']=1+sum(R(p[j],24)*choice(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
    minimum=min(offers.values())
    return minimum,tuple(action for action,v in offers.items() if v==minimum)
assert choice(0,0,0)[0]==R(2442656918158809916870213,5949675882197721022464)
assert choice(*B)[1]==('Q','C') and choice(*G)[1]==('Q','C')
def corner(w,z):
    sums=[0,0,0,0]
    hits=defaultdict(lambda:[0,0,0])
    visits=[0,0]
    def travel(n,a,b,wp,wq):
        visits[0]+=1
        s=(n,a,b)
        if s in (B,G):
            h=hits[s]
            h[0]+=1
            h[1]+=wp*24**(N-n)
            h[2]+=wq*12**(N-n)
        if s==B:action='Q' if w else 'C'
        elif s==G:action='Q' if z else 'C'
        else:action=choice(n,a,b)[1][0]
        assert action in choice(n,a,b)[1]
        if action=='C':
            assert n<N
            for j in range(3):
                travel(n+1,a+(j==0),b+(j==1),wp*p[j],wq*q[j])
        else:
            visits[1]+=1
            aP=wp*24**(N-n)
            aQ=wq*12**(N-n)
            if action=='Q':sums[0]+=aP
            else:sums[1]+=aQ
            sums[2]+=n*aP
            sums[3]+=n*aQ
    travel(0,0,0,1,1)
    return {
      'moments':[str(R(sums[0],den_p)),str(R(sums[1],den_q)),str(R(sums[2],den_p)),str(R(sums[3],den_q))],
      'prefix_visits':visits[0], 'terminal_words':visits[1],
      'first_hits':{str(s):{'word_count':h[0],'P':str(R(h[1],den_p)),'Q':str(R(h[2],den_q))} for s,h in hits.items()}
    }
C={f'{w}{z}':corner(w,z) for w,z in product((0,1),repeat=2)}
M={key:tuple(map(R,c['moments'])) for key,c in C.items()}
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,v:tuple(x*v for x in a)
base=M['00'];dB=sub(M['10'],base);dG=sub(M['01'],base)
assert M['11']==add(add(base,dB),dG)
err=lambda x:x[0]-x[1]
w0=-err(base)/err(dB)
slope=-err(dG)/err(dB)
assert w0==R(29148450914061437,81438720000000000)
assert slope==-R(4650723,19280000000)
path=lambda z:add(add(base,mul(dB,w0+slope*z)),mul(dG,z))
ends=[path(R(z)) for z in (0,1)]
for v in ends:
    assert v[0]==v[1] and v[2]>v[3]
    assert v[2]+ell*v[0]+k*v[1]==choice(0,0,0)[0]
assert ends[0][0]==R(36703010861169506695,105616844785075617792)
assert ends[1][0]==R(36703016772992738695,105616844785075617792)
assert 0<w0+slope<w0<1
assert all(C[key]['first_hits'][str(B)]==C['00']['first_hits'][str(B)] for key in C)
assert all(C[key]['first_hits'][str(G)]==C['00']['first_hits'][str(G)] for key in C)
out={'status':'PASS_AUTHOR_INTEGER_LITERAL_HISTORY','corners':C,'w0':str(w0),
     'w_slope':str(slope),'endpoints':[[str(x) for x in v] for v in ends]}
Path(__file__).with_name('ordered_evidence134.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('PASS AUTHOR STAGE134 INTEGER LITERAL-WORD DFS')
print('HITS',C['00']['first_hits'])
print('VISITS',{key:(v['prefix_visits'],v['terminal_words']) for key,v in C.items()})
