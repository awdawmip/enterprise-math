"""EC49DG: exact six-axis tag-safe gates and affine-collinear non-degeneracy.
Uses the unchanged prior EC49DE/DF signed-X6/BRC checkers in this directory.
All finite claims use integer arithmetic (determinants mod 1000003 only
for nonvanishing witnesses); the all-h assertion is proved in README_EC49DG.md.
"""
from collections import defaultdict
from itertools import combinations
from math import prod
import VERIFY_EC49DD as E
import VERIFY_EC49DE_COMPACT as Tag
import VERIFY_EC49DF_Q0 as Prev

MOD = 1000003
# Safe axes E3..E6 lie on y=2x+1; E1 breaks the affine line.
X_GATE = (2,3,1,2,3,4)
Y_GATE = (4,7,3,5,7,9)
AXES = (1,3,4)
# In the second example, ALL SIX positive-axis weight pairs lie on y=2x+1.
X_COL = (2,3,1,2,3,4)
Y_COL = tuple(2*t+1 for t in X_COL)
WORDS = {
    0: ('3333','3334','3344'),
    2: ('1233','1234','1244'),
    1: ('2133','2134','2144'),
    3: ('1213','1214','2123'),
}
EXPECTED_BLOCK_DET = {0:-18, 2:-420, 1:-420, 3:420}

def d3(m):
    a,b,c=m
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

def matrix_gate(x,y,axes):
    return [[z[j-1] for j in axes] for z in (x,y)] + [[1]*3]

def positive_weight(p, w):
    return prod(w[a-1] for a in p if a>0)

def negative_extreme_prefix(q, h):
    positives=tuple(map(int,q))
    assert len(positives)==4 and all(1<=a<=6 for a in positives)
    # Need D=(-2h,0,0,0,0,0), with exactly four positive steps.
    negative=(-1,)*(2*h+positives.count(1))
    for a in range(2,7):negative+=(-a,)*positives.count(a)
    p=positives+negative
    assert len(p)==2*h+8
    assert E.endpoint(p)==(-2*h,0,0,0,0,0)
    return p

def check_collinear_extreme():
    assert all(Y_COL[j]==2*X_COL[j]+1 for j in range(6))
    minors={lab:d3([[positive_weight(tuple(map(int,q)),w) for q in qs]
                      for w in (X_COL,Y_COL)]+[[1,1,1]])
            for lab,qs in WORDS.items()}
    assert minors==EXPECTED_BLOCK_DET,minors
    trials=0
    for h in range(2,21):
        future=E.word('e'*h)
        assert E.endpoint(future)==(2*h,0,0,0,0,0)
        assert E.tag(future)==0
        suffix_x=positive_weight(future,X_COL)
        suffix_y=positive_weight(future,Y_COL)
        assert suffix_x==4**h and suffix_y==75**h
        paths=[]; rows=[]
        for lab,qs in WORDS.items():
            group=[negative_extreme_prefix(q,h) for q in qs]
            assert all(E.tag(p)==lab and E.tag(p+future)==lab for p in group)
            paths+=group
            rows.extend((lab,channel) for channel in (0,1,2))
        M=[]
        for lab,ch in rows:
            M.append([((positive_weight(p+future,X_COL) if ch==0 else
                        positive_weight(p+future,Y_COL) if ch==1 else 1)
                       if E.tag(p+future)==lab else 0) for p in paths])
        observed=Prev.det_mod(M)
        predicted=pow(suffix_x*suffix_y,4,MOD)*prod(minors.values())%MOD
        assert observed==predicted and observed!=0,(h,observed,predicted)
        trials+=1
    return {'h_range':'2..20','extreme_fibers':trials,
            'true_minors':minors,'all_six_axis_pairs_affine_collinear':True}

def check_all_axis_gate():
    assert d3(matrix_gate(X_GATE,Y_GATE,AXES))==-1
    for subset in combinations((3,4,5,6),3):
        assert d3(matrix_gate(X_GATE,Y_GATE,subset))==0
    # Actual primitive paths and complete suffix languages, no semantic proxy.
    exact={j:Tag.suffixes(j) for j in range(1,6)}
    out={};tested=0
    for h in range(2,6):
        combined=defaultdict(list)
        for j in range(1,h+1):
            for disp,L in exact[j].items():combined[disp].extend(L)
        sums=[0,0];per=0
        for s in range(-h,h+1):
            for v in range(h-abs(s)+1):
                base=Tag.paths(h,s,v)
                for mode,language in enumerate((exact[h],combined)):
                    suffixes=language[(-2*s,-2*v)]
                    rows,T=Prev.independent_rows(base,suffixes)
                    defect=h-abs(s)-v
                    r=4 if defect==0 else 6 if (mode==1 or defect%2==0) else 5
                    assert len(rows)==r
                    indexes=next((cc for cc in combinations(range(len(base)),r)
                        if Prev.det_mod([[t[i] for i in cc] for t in T])),None)
                    assert indexes is not None
                    selected=[base[i] for i in indexes]
                    paths=[(axis,-axis)+tuple(p) for p in selected for axis in AXES]
                    assert all(len(p)==2*h+8 and E.endpoint(p)==(2*s,2*v,0,0,0,0)
                               for p in paths)
                    M=[]
                    for suffix,tag in rows:
                        is_tag=[E.tag(p+suffix)==tag for p in paths]
                        for ch in (0,1,2):
                            M.append([(positive_weight(p+suffix,X_GATE) if ch==0
                                       else positive_weight(p+suffix,Y_GATE) if ch==1
                                       else 1) if ok else 0
                                      for p,ok in zip(paths,is_tag)])
                    assert Prev.det_mod(M)!=0,(h,s,v,mode)
                    sums[mode]+=3*r;tested+=1;per+=1
        assert sums==[(3*(11*h*h+15*h+8))//2,18*h*h+24*h+12]
        out[h]={'minors':per,'exact_dim':sums[0],'cumulative_dim':sums[1]}
    return {'h_range':'2..5','genuine_full_rank_minors':tested,
            'E134_det':-1,'E345_E346_E356_E456_det':0,'per_h':out}

if __name__=='__main__':
    import json
    result={'status':'PASS','modulus':MOD,
            'six_axis_gate':check_all_axis_gate(),
            'collinear_extreme':check_collinear_extreme()}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
