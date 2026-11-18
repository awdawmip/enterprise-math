#!/usr/bin/env python3
"""EC49CV self-contained deterministic literal certificate replay.
Python 3 stdlib. All arithmetic integer / exact Fraction / F_1000003.
Input EC49CV_COMPACT_CERT.json.xz.b64 is actual condensed path index list;
no assertion depends on trusting its claimed ranks or determinants.
"""
import base64,itertools,json,lzma,random,sys
from fractions import Fraction
from pathlib import Path
P=1000003; N=24
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}
W=((2,3,3,2,1,1),(3,2,3,2,1,1))


def pos(word):
    ans=[0]*6
    for a in word:ans[abs(a)-1]+=1 if a>0 else -1
    return tuple(ans)

def tag(word):
    A=B=False
    for i in range(len(word)-1):
        A|=word[i:i+2]==(1,2);B|=word[i:i+2]==(2,1)
    return 2*int(A)+int(B)

def factors(word):
    a=b=1
    for x in word:
        if x>0:a*=W[0][x-1];b*=W[1][x-1]
    return (a,b,1)

def suffix(word):return tuple(x for a in word for x in OPS[a])

def sample(target,rng,attempt):
    u=target[0]//2;v=target[1]//2
    base=[(1 if u>=0 else -1)]*(2*abs(u))+[2]*(2*v)
    axes=(1,2,3,4,5,6)
    distributions=((30,30,14,11,8,7),(46,46,3,3,1,1),(12,12,28,20,14,14))
    path=base[:]
    for _ in range((N-len(base))//2):
        x=rng.choices(axes,weights=distributions[(attempt//307)%3],k=1)[0]
        path.extend((x,-x))
    rng.shuffle(path)
    return tuple(path)

def rare_paths():
    return ((1,)*8+(3,-3)*4+(2,)*8,
            (1,)*8+(3,-3)*3+(4,-4)+(2,)*8,
            (1,-1)+(1,)*8+(3,-3)*3+(2,)*8)

def qrank(matrix):
    piv={}
    for row in matrix:
        x=list(map(Fraction,row))
        for j in sorted(piv):
            if x[j]:
                a=x[j];x=[v-a*t for v,t in zip(x,piv[j])]
        j=next((j for j,v in enumerate(x) if v),None)
        if j is not None:piv[j]=[v/x[j] for v in x]
    return len(piv)

def det_mod(matrix):
    n=len(matrix);a=[[v%P for v in row] for row in matrix];det=1
    assert all(len(r)==n for r in a)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return 0
        if j!=k:a[j],a[k]=a[k],a[j];det=-det
        d=a[j][j];det=det*d%P;iv=pow(d,-1,P)
        for i in range(j+1,n):
            f=a[i][j]*iv%P
            if f:
                a[i][j]=0
                for col in range(j+1,n):a[i][col]=(a[i][col]-f*a[j][col])%P
    return det%P

def from_initial(q,s):
    a,b=divmod(q,3)
    for x in s:
        a=2 if a==2 or (a==1 and x==2) else int(x==1)
        b=2 if b==2 or (b==1 and x==1) else int(x==2)
    return 2*int(a==2)+int(b==2)

def replay(path):
    compressed=Path(path).read_text().strip()
    artifact=json.loads(lzma.decompress(base64.b64decode(compressed)).decode())
    assert (artifact['n'],artifact['h'],artifact['p'])==(24,8,P)
    ranks=[];rows_total=0
    for block in artifact['blocks']:
        target=tuple(block['target'])
        suffix_rows=[(suffix(word),tagged) for word,tagged in block['selected_suffix_rows']]
        assert len(suffix_rows)==block['per_type_rank']
        initial_patterns=[tuple(int(from_initial(q,ss)==label) for q in range(9)) for ss,label in suffix_rows]
        assert qrank(initial_patterns)==len(suffix_rows)
        assert all(1<=len(word)<=8 for word,_ in block['selected_suffix_rows'])
        assert len(block['candidate_indices'])==3*len(suffix_rows)
        assert target[2:]==(0,0,0,0)
        u=target[0]//2;v=target[1]//2
        assert v>=0 and abs(u)+v<=8
        assert len(suffix_rows)==(4 if abs(u)+v==8 else 6)
        rng=random.Random(block['seed'])
        indices=block['candidate_indices'];wanted=set(i for i in indices if i>=0)
        saved={}
        for i in range(max(wanted,default=-1)+1):
            path=sample(target,rng,i)
            if i in wanted:saved[i]=path
        paths=[saved[i] if i>=0 else rare_paths()[-i-1] for i in indices]
        assert all(len(p)==N and pos(p)==target for p in paths)
        if any(i<0 for i in indices):assert target[:2]==(8,8)
        rows=[[] for _ in range(len(indices))]
        for word in paths:
            col=[]
            for ss,lab in suffix_rows:
                entire=word+ss
                assert pos(entire)==(0,0,0,0,0,0)
                col.extend(factors(entire) if tag(entire)==lab else (0,0,0))
            for j,x in enumerate(col):rows[j].append(x)
        det=det_mod(rows)
        assert det==block['minor_mod_p'] and det>0,(target,det,block['minor_mod_p'])
        ranks.append(len(indices));rows_total+=len(indices)
    assert len(artifact['blocks'])==81
    assert rows_total==1356==artifact['abstract_rank_bound']
    return {'status':'PASS','fibers':len(ranks),'rank':rows_total,'modulus':P,
            'nonzero_independent_real_X6_minors':len(ranks)}

if __name__=='__main__':
    path=sys.argv[1] if len(sys.argv)>1 else 'EC49CV_COMPACT_CERT.json.xz.b64'
    print(json.dumps(replay(path),sort_keys=True))
