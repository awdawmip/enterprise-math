#!/usr/bin/env python3
"""Independent literal-history DFS with exact integer P/Q numerator weights."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

N=14
p=(3,1,20); q=(1,1,10)
B=(11,0,1); G=(13,6,4)
K=F(214326,401); L=F(203912,401)

@lru_cache(None)
def bell(s):
    n,a,b=s
    options={'P':K*F(2**(a+b),3**a),'Q':L}
    if n<N:
        child=(bell((n+1,a+1,b))[0],bell((n+1,a,b+1))[0],bell((n+1,a,b))[0])
        options['C']=1+sum((F(p[i],24)*child[i] for i in range(3)),F(0))
    minimum=min(options.values())
    return minimum,tuple(k for k,v in options.items() if v==minimum)

denP=24**N;denQ=12**N
powP=[24**(N-n) for n in range(N+1)]
powQ=[12**(N-n) for n in range(N+1)]
all_corners={}
for w,z in ((0,0),(1,0),(0,1),(1,1)):
    aggregate=[0,0,0,0]
    first={B:[0,0,0],G:[0,0,0]}
    nodes=[0,0]
    def visit(n,a,b,mP,mQ):
        nodes[0]+=1
        state=(n,a,b)
        if state in first:
            r=first[state];r[0]+=1
            r[1]+=mP*powP[n];r[2]+=mQ*powQ[n]
        _,ties=bell(state)
        if len(ties)==1:action=ties[0]
        elif state==B:action='Q' if w else 'C'
        elif state==G:action='C' if z else 'Q'
        else:raise RuntimeError((state,ties))
        if action!='C':
            nodes[1]+=1
            wP=mP*powP[n]; wQ=mQ*powQ[n]
            if action=='Q':aggregate[0]+=wP
            else:aggregate[1]+=wQ
            aggregate[2]+=n*wP
            aggregate[3]+=n*wQ
            return
        visit(n+1,a+1,b,mP*p[0],mQ*q[0])
        visit(n+1,a,b+1,mP*p[1],mQ*q[1])
        visit(n+1,a,b,mP*p[2],mQ*q[2])
    visit(0,0,0,1,1)
    vec=[F(aggregate[0],denP),F(aggregate[1],denQ),
         F(aggregate[2],denP),F(aggregate[3],denQ)]
    all_corners[f'{w}{z}']={
        'values':[str(v) for v in vec],
        'visited_prefixes':nodes[0],
        'terminal_histories':nodes[1],
        'first_hit':{str(s):{
            'literal_words':row[0],
            'P_mass':str(F(row[1],denP)),
            'Q_mass':str(F(row[2],denQ))
        } for s,row in first.items()}
    }
    print('corner',w,z,'prefixes',nodes,'M',vec)

base=json.loads(Path(__file__).with_name('certificate137.json').read_text(encoding='utf-8'))
M00=[F(v) for v in base['M00']]
dB=[F(v) for v in base['dB']]
dG=[F(v) for v in base['dG']]
for w,z in ((0,0),(1,0),(0,1),(1,1)):
    actual=[F(v) for v in all_corners[f'{w}{z}']['values']]
    expected=[M00[i]+w*dB[i]+z*dG[i] for i in range(4)]
    assert actual==expected,(w,z,actual,expected)
for s in (B,G):
    parts=[all_corners[k]['first_hit'][str(s)] for k in ('00','10','01','11')]
    assert all(row==parts[0] for row in parts)
assert all_corners['00']['first_hit'][str(B)]=={
    'literal_words':11,
    'P_mass':'107421875/1451188224',
    'Q_mass':'107421875/725594112'
}
assert all_corners['00']['first_hit'][str(G)]=={
    'literal_words':9692,
    'P_mass':'302875/4696546738176',
    'Q_mass':'302875/3343537668096'
}
assert [all_corners[k]['visited_prefixes'] for k in ('00','10','01','11')]==[680548,680416,709624,709492]
Path(__file__).with_name('ordered_certificate137.json').write_text(
    json.dumps(all_corners,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'
)
print('PASS_STAGE137_INDEPENDENT_ORDERED')
