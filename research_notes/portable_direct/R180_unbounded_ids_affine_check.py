"""R180: unbounded integer branch/provenance IDs, exact 17-token X6 affine register."""
from fractions import Fraction
from itertools import product
import json, random

STEPS=tuple((i,s) for i in range(6) for s in (-1,1))
BIT0,BIT1,START,END,SEP=12,13,14,15,16
K=17; DIM=13

def binary(n):
    assert isinstance(n,int) and n>=0
    return tuple(BIT1 if c=='1' else BIT0 for c in bin(n)[2:])

def atom(identifier,source,path):
    return (START,)+binary(identifier)+(SEP,)+binary(source)+tuple(STEPS.index(s) for s in path)+(END,)

def parse(w):
    result=[]; i=0
    while i<len(w):
        assert w[i]==START
        i+=1
        bits=[]
        while i<len(w) and w[i] in (BIT0,BIT1): bits.append(str(w[i]-BIT0));i+=1
        assert bits and (len(bits)==1 or bits[0]=='1') and i<len(w) and w[i]==SEP
        identifier=int(''.join(bits),2);i+=1
        bits=[]
        while i<len(w) and w[i] in (BIT0,BIT1): bits.append(str(w[i]-BIT0));i+=1
        assert bits and (len(bits)==1 or bits[0]=='1')
        source=int(''.join(bits),2)
        path=[]
        while i<len(w) and w[i]<12: path.append(STEPS[w[i]]);i+=1
        assert i<len(w) and w[i]==END
        i+=1;result.append((identifier,source,tuple(path)))
    return tuple(result)

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(n,a):return tuple(n*x for x in a)
def stats(w):
    d=j=(0,)*6; h=m=0
    for t in w:
        assert 0<=t<K
        h=K*h+t
        if t<12:
            i,s=STEPS[t]; d=add(d,tuple(s if k==i else 0 for k in range(6)));j=add(j,d);m+=1
    return len(w),m,d,j,h

def action(w):
    l,m,d,j,h=stats(w)
    mat=[[0]*DIM for _ in range(DIM)]
    for k in range(6):mat[k][k]=mat[6+k][6+k]=1;mat[6+k][k]=m
    mat[-1][-1]=K**l
    return tuple(map(tuple,mat)),tuple(d)+tuple(j)+(h,)

def compose_stats(a,b):
    la,ma,da,ja,ha=stats(a);lb,mb,db,jb,hb=stats(b)
    return la+lb,ma+mb,add(da,db),add(add(ja,jb),mul(mb,da)),K**lb*ha+hb

def then(a,b):
    mat,x=a;mat2,y=b
    new=tuple(tuple(sum(mat2[i][k]*mat[k][j] for k in range(DIM)) for j in range(DIM)) for i in range(DIM))
    vec=tuple(sum(mat2[i][k]*x[k] for k in range(DIM))+y[i] for i in range(DIM))
    return new,vec

def test():
    for n in range(4):
        assert len({stats(w)[-1] for w in product(range(K),repeat=n)})==K**n
    ids=[0,1,2,3,7,8,31,32,2**65+3]
    sources=[0,1,10,2**65+17]
    paths=[p for n in range(3) for p in product((STEPS[0],STEPS[1]),repeat=n)]
    atoms=[(i,s,p) for i in ids for s in sources for p in paths]
    words=[atom(*x) for x in atoms]
    assert len(words)==252 and len({action(w) for w in words})==252
    assert all(parse(w)==(x,) for w,x in zip(words,atoms))
    for a in words:
        for b in words:
            assert stats(a+b)==compose_stats(a,b)
            assert parse(a+b)==parse(a)+parse(b)
    rng=random.Random(180)
    for _ in range(240):
        a,b=rng.choice(words),rng.choice(words)
        assert then(action(a),action(b))==action(a+b)
    # Equal spatial paths and source with distinct arbitrarily large IDs survive.
    x=atom(2**65+3,2**65+17,(STEPS[1],STEPS[0]))
    y=atom(32,2**65+17,(STEPS[1],STEPS[0]))
    assert action(x)!=action(y)
    native={"attempted":True,"imported":False,"passed":False,"error":None}
    try:
        from enterprise_math.brc_transport import Affine,EffectHistogram
        native['imported']=True
        ha=EffectHistogram.from_terms(DIM,[(Fraction(1,3),Affine(*action(x)),1),(Fraction(1,3),Affine(*action(y)),1)])
        assert len(ha.entries)==2
        assert Affine(*action(x)).then(Affine(*action(y)))==Affine(*action(x+y))
        native['passed']=True
    except ModuleNotFoundError as e:
        native['error']='native package unavailable: '+str(e)
    return {"schema":"R180_UNBOUNDED_TAGGED_ID_AFFINE_V1","radix":K,
            "symbol_types":"12 steps, binary 0/1, start, end, separator",
            "id_domain":"nonnegative integers of unbounded size",
            "affine_dim":DIM,
            "raw_words_length_0_to_3":sum(K**j for j in range(4)),
            "atomic_cases":len(atoms),"exhaustive_atom_pair_checks":len(words)**2,
            "exact_matrix_checks":240,"source_id_max_tested":str(max(sources)),
            "branch_id_max_tested":str(max(ids)),
            "native_brc_integration":native,"exact_reference":True,"result":"R180_REFERENCE_EXACT_PASS"}

if __name__=='__main__':print(json.dumps(test(),sort_keys=True,indent=2))
