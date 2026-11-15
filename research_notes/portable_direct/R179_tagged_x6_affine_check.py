"""R179 exact tagged branch/source X6 affine bridge, standalone plus optional native test."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import random

STEPS=tuple((i,s) for i in range(6) for s in (-1,1))
IDS=("a","b","c")
SOURCES=("red","blue")
K=12+len(IDS)+len(SOURCES)+1
ID_CODE={x:12+i for i,x in enumerate(IDS)}
SOURCE_CODE={x:12+len(IDS)+i for i,x in enumerate(SOURCES)}
END=K-1
DIM=13

def token_word(identifier,source,path):
    return (ID_CODE[identifier],SOURCE_CODE[source],
            *(STEPS.index(s) for s in path),END)

def decode_atoms(w):
    result=[]
    i=0
    while i<len(w):
        if w[i] not in ID_CODE.values() or i+1>=len(w) or w[i+1] not in SOURCE_CODE.values():
            raise ValueError("invalid atom prefix")
        identifier=IDS[w[i]-12]
        source=SOURCES[w[i+1]-12-len(IDS)]
        i+=2
        path=[]
        while i<len(w) and w[i]<12:
            path.append(STEPS[w[i]])
            i+=1
        if i>=len(w) or w[i]!=END:
            raise ValueError("missing atom terminator")
        i+=1
        result.append((identifier,source,tuple(path)))
    return tuple(result)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def mul(s,a):
    return tuple(s*x for x in a)

def stats(w):
    d=j=(0,)*6
    h=m=0
    for t in w:
        if not 0<=t<K:
            raise ValueError("unknown token")
        h=K*h+t
        if t<12:
            i,s=STEPS[t]
            e=tuple(s if k==i else 0 for k in range(6))
            d=add(d,e)
            j=add(j,d)
            m+=1
    return len(w),m,d,j,h

def compose_stats(a,b):
    la,ma,da,ja,ha=stats(a)
    lb,mb,db,jb,hb=stats(b)
    return (la+lb,ma+mb,add(da,db),add(add(ja,jb),mul(mb,da)),K**lb*ha+hb)

def action(w):
    l,m,d,j,h=stats(w)
    a=[[0]*DIM for _ in range(DIM)]
    for i in range(6):
        a[i][i]=a[6+i][6+i]=1
        a[6+i][i]=m
    a[12][12]=K**l
    return tuple(map(tuple,a)),tuple(d)+tuple(j)+(h,)

def then(first,later):
    a,b=first
    c,d=later
    aa=tuple(tuple(sum(c[i][k]*a[k][j] for k in range(DIM))
                   for j in range(DIM)) for i in range(DIM))
    bb=tuple(sum(c[i][k]*b[k] for k in range(DIM))+d[i] for i in range(DIM))
    return aa,bb

def packet(terms):
    out=Counter()
    for weight,w,multiplicity in terms:
        weight=Fraction(weight)
        assert weight>0 and multiplicity>0
        out[(weight,action(w))]+=multiplicity
    return out

def packet_then(a,b):
    out=Counter()
    for (wa,fa),ca in a.items():
        for (wb,fb),cb in b.items():
            out[(wa*wb,then(fa,fb))]+=ca*cb
    return out

def execute():
    assert K==18
    raw=0
    for n in range(4):
        codes=set()
        for w in product(range(K),repeat=n):
            code=stats(w)[-1]
            assert code not in codes
            codes.add(code)
            raw+=1
        assert len(codes)==K**n
    small=(STEPS[0],STEPS[1])
    paths=[p for n in range(4) for p in product(small,repeat=n)]
    atoms=[(i,s,p) for i in IDS for s in SOURCES for p in paths]
    words=[token_word(*a) for a in atoms]
    assert len(words)==90
    assert len({action(w) for w in words})==90
    assert all(decode_atoms(w)==(a,) for a,w in zip(atoms,words))
    pairs=0
    for a in words:
        for b in words:
            assert stats(a+b)==compose_stats(a,b)
            assert decode_atoms(a+b)==decode_atoms(a)+decode_atoms(b)
            pairs+=1
    rng=random.Random(179)
    for _ in range(500):
        a,b=rng.choice(words),rng.choice(words)
        assert then(action(a),action(b))==action(a+b)
    wa=token_word("a","red",(STEPS[1],STEPS[0]))
    wb=token_word("b","red",(STEPS[1],STEPS[0]))
    assert action(wa)!=action(wb)
    assert len(packet([(Fraction(1,2),wa,1),(Fraction(1,2),wb,1)]))==2
    assert len(packet([(Fraction(1,2),wa,1),(Fraction(1,2),wa,1)]))==1
    for _ in range(50):
        a,b,c,d=(rng.choice(words) for _ in range(4))
        u=Fraction(rng.randint(1,5),rng.randint(1,5))
        v=Fraction(rng.randint(1,5),rng.randint(1,5))
        left=packet([(u,a,1),(v,b,2)])
        right=packet([(v,c,1),(u,d,3)])
        direct=packet([(u*v,a+c,1),(u*u,a+d,3),
                       (v*v,b+c,2),(v*u,b+d,6)])
        assert packet_then(left,right)==direct
    native={"attempted":True,"imported":False,"passed":False,"error":None}
    try:
        from enterprise_math.brc_transport import Affine,EffectHistogram
        native["imported"]=True
        p=Affine(*action(wa))
        q=Affine(*action(wb))
        assert p.then(q)==Affine(*action(wa+wb))
        hist=EffectHistogram.from_terms(DIM,[
            (Fraction(1,2),p,1),(Fraction(1,2),q,1)])
        assert len(hist.entries)==2
        assert sum(c for _,_,c in hist.then(hist).entries)==4
        native["passed"]=True
    except ModuleNotFoundError as e:
        native["error"]="native package unavailable: "+str(e)
    return {
        "schema":"R179_TAGGED_X6_PROVENANCE_AFFINE_EXACT_VERIFICATION_V1",
        "radix":K,"native_axis_count":6,"signed_step_symbols":12,
        "branch_ids":list(IDS),"source_symbols":list(SOURCES),
        "affine_dimension":DIM,
        "exhaustive_raw_words_length_0_to_3":raw,
        "atomic_branch_source_path_cases":len(atoms),
        "exhaustive_atom_pair_composition_checks":pairs,
        "matrix_affine_composition_checks":500,
        "positive_packet_product_checks":50,
        "distinct_id_same_path_weight_witness":"two_effect_entries",
        "native_brc_integration":native,"exact_arithmetic":True,
        "result":"R179_NATIVE_EXACT_PASS" if native["passed"] else "R179_REFERENCE_EXACT_PASS"
    }

if __name__=="__main__":
    print(json.dumps(execute(),ensure_ascii=False,sort_keys=True,indent=2))
