"""EC49CT independent literal path / signed endpoint / ordered tags / BRC / minor audit.
Reads four JSON witnesses; uses Python 3 stdlib, no author-side DP or prior modules.
Nonzero determinants are rank LOWER bounds; analytic proof is in README_EC49CT.md.
"""
import json,sys
from pathlib import Path
P=1000003
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),
     'd':(2,1,-2,-1),'e':(3,1,1,-3)}
WEIGHTS=((2,3,3,2,1,1),(3,2,3,2,1,1))

def loc(word):
    out=[0]*6
    for x in word:
        assert 1<=abs(x)<=6
        out[abs(x)-1]+=1 if x>0 else -1
    return tuple(out)

def wt(word,c):
    if c==2:return 1
    t=1
    for x in word:
        if x>0:t*=WEIGHTS[c][x-1]
    return t

def tag(word):
    a=any(x==1 and y==2 for x,y in zip(word,word[1:]))
    b=any(x==2 and y==1 for x,y in zip(word,word[1:]))
    return 2*int(a)+int(b)

def det_mod(mat):
    n=len(mat)
    assert all(len(v)==n for v in mat)
    a=[[v%P for v in row] for row in mat];result=1
    for col in range(n):
        pivot=next((j for j in range(col,n) if a[j][col]),None)
        if pivot is None:return 0
        if pivot!=col:a[col],a[pivot]=a[pivot],a[col];result=-result
        x=a[col][col];result=result*x%P
        inv=pow(x,-1,P)
        for j in range(col+1,n):
            if a[j][col]:
                mult=a[j][col]*inv%P
                for k in range(col+1,n):a[j][k]=(a[j][k]-mult*a[col][k])%P
                a[j][col]=0
    return result%P

def suffix(name):
    assert all(ch in OPS for ch in name)
    out=()
    for ch in name:out+=OPS[ch]
    return out

def audit(filename):
    o=json.loads(Path(filename).read_text());n=o['n'];rows_total=rank_total=0
    assert o['p']==P and o['target_count']==25
    for b in o['blocks']:
        d=tuple(b['target']);ps=[tuple(p) for p in b['paths']]
        assert all(len(p)==n and loc(p)==d for p in ps)
        assert b['actual_mod_rank']==len(ps)
        assert b['rank_bound']==len(b['selected_rows'])
        rs=[tuple(x) for x in b['selected_rows']]
        assert all(1<=len(k)<=4 and all(ch in OPS for ch in k)
                   and 0<=t<=3 and 0<=c<=2 and loc(suffix(k))==tuple(-x for x in d)
                   for k,t,c in rs)
        M=[[wt(p+suffix(k),c) if tag(p+suffix(k))==t else 0 for p in ps]
           for k,t,c in rs]
        determinant=det_mod(M) if len(ps)==len(rs) else 0
        assert determinant==b['minor_mod_p'],(d,determinant,b['minor_mod_p'])
        if len(ps)==len(rs):assert determinant!=0
        else:
            assert d==(-8,0,0,0,0,0) and len(ps)==11 and len(rs)==12
            small=det_mod([row[:11] for row in M[:11]])
            assert small==920330,(small,filename)
        if n==14 and d==(-8,0,0,0,0,0):
            for p in ps:
                word=p+suffix('eeee')
                if tag(word)==3:
                    assert wt(word,0)*15943230+wt(word,1)*622080==622080*15943230
        rank_total+=len(ps);rows_total+=len(rs)
    assert rank_total==o['real_path_mod_rank']
    assert rows_total==o['abstract_rank_bound']
    print(Path(filename).name,'25 authentic target fibers; signed BRC rank',rank_total,'/',rows_total)
    return n,rank_total,rows_total

if __name__=='__main__':
    files=sys.argv[1:] or [f'EC49CT_CERT_n{n}_{k}.json' for n in (14,16) for k in ('S4','SLE4')]
    checks=[audit(x) for x in files]
    if len(checks)==4:assert checks==[(14,365,366),(14,395,396),(16,366,366),(16,396,396)]
    print('PASS independently recalculated 100 target fiber residues and 4 ranks')
