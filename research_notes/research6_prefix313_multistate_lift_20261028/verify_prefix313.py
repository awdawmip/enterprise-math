#!/usr/bin/env python3
"""PREFIX-313 exact source-tagged BRC; auxiliary static five-Port S7-3 model."""
from fractions import Fraction as F
import json

Z=(F(0),F(0))
ONE=(F(1),F(0))
I=(F(0),F(1))
def G(x,y=0): return (F(x),F(y))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def conj(a): return (a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,r): return (a[0]*r,a[1]*r)
def norm(a): return mul(a,conj(a))[0]
def summa(xs):
    s=Z
    for x in xs:s=add(s,x)
    return s

A=(
 ((G(4),G(4),Z)),
 ((Z,G(-4),G(4))),
 ((G(-5,3),Z,G(-3,1))),
 ((G(-2,-2),G(4,4),G(2,2))),
 ((G(-2),Z,G(5,2))),
)
RHO={'Q0':None,'Q1':ONE,'Qi':I}
counts={'masses':0,'ordered_pairs':0,'gram_entries':0}
def amp(j,s): return summa(mul(A[j][k],s[k]) for k in range(3))
def mass(j,s,ref=None):
    paths=[('source:'+str(k+1),scale(mul(A[j][k],s[k]),F(1,8))) for k in range(3)]
    if ref is not None:paths.append(('reference',ref))
    assert len(set(label for label,_ in paths))==len(paths)
    out=Z
    for label_a,a in paths:
        for label_b,b in paths:
            out=add(out,mul(a,conj(b)))
            counts['ordered_pairs']+=1
    counts['masses']+=1
    assert out[1]==0 and out[0]>=0
    return out[0]
def S(t):return tuple(G(t[2*k],t[2*k+1]) for k in range(3))
def plus(x,y):return tuple(add(x[k],y[k]) for k in range(3))
def minus(x,y):return tuple(sub(x[k],y[k]) for k in range(3))
def times(x,r):return tuple(scale(z,r) for z in x)
def coords(x):return tuple(z for pair in x for z in pair)
def d2(x,y):return sum((p-q)**2 for p,q in zip(coords(x),coords(y)))
def rank(mat):
    M=[list(map(F,row)) for row in mat]
    nr=len(M);nc=len(M[0]);h=0
    for j in range(nc):
        pivot=next((i for i in range(h,nr) if M[i][j]),None)
        if pivot is None:continue
        M[h],M[pivot]=M[pivot],M[h]
        factor=M[h][j];M[h]=[x/factor for x in M[h]]
        for i in range(nr):
            if i!=h and M[i][j]:
                f=M[i][j];M[i]=[M[i][k]-f*M[h][k] for k in range(nc)]
        h+=1
        if h==nr:break
    return h
def lifted_rank(v,w):
    rows=[];rhs=[]
    for j in range(5):
        for d in (v,w):
            p=amp(j,d)
            row=[]
            for coefficient in A[j]:
                t=mul(coefficient,conj(p))
                row.extend((2*t[0],-2*t[1]))
            rows.append(row);rhs.append(-norm(p))
    return rank(rows),rank([row+[rhs[i]] for i,row in enumerate(rows)])
def fstr(x):
    return str(x.numerator) if x.denominator==1 else str(x.numerator)+'/'+str(x.denominator)

target=((G(46),G(-16),Z),(G(-16),G(32),G(16)),(Z,G(16),G(47)))
for i in range(3):
    for j in range(3):
        assert summa(mul(conj(row[i]),row[j]) for row in A[2:])==target[i][j]
        counts['gram_entries']+=1

B=(S((-2,0,0,-2,1,0)),S((0,-2,2,0,0,1)),S((0,2,2,0,0,-1)))
T=tuple(times(x,F(4,9)) for x in B)
Q=(128,80,74,200,85)
width=[];proofrows=[]
for j in range(5):
    p=[amp(j,b) for b in B]
    assert [norm(z) for z in p]==[Q[j]]*3
    readings={label:[mass(j,x,rho) for x in T] for label,rho in RHO.items()}
    assert len(set(readings['Q0']))==1 and readings['Q0'][0]==F(Q[j],324)
    refs={}
    for label in ('Q1','Qi'):
        lo=min(readings[label]);hi=max(readings[label]);y=(lo+hi)/2
        assert hi-lo<=2 and all(abs(y-v)<=1 for v in readings[label])
        refs[label]={'min':fstr(lo),'max':fstr(hi),'common_observation':fstr(y)}
    wr=(max(v[0] for v in p)-min(v[0] for v in p))/18
    wi=(max(v[1] for v in p)-min(v[1] for v in p))/18
    width.append((fstr(wr),fstr(wi)))
    d1=sub(p[1],p[0]);d2_=sub(p[2],p[0])
    orient=mul(conj(d1),d2_)[1]
    assert orient!=0
    proofrows.append({'port':j,'raw_A_times_B':[[fstr(z[0]),fstr(z[1])] for z in p],
       'BRC_Q0':fstr(readings['Q0'][0]),'area2_num':fstr(orient),'references':refs})
assert width==[('8/9','8/9'),('2/3','2/3'),('2/3','7/9'),('2/3','8/9'),('11/18','1')]
assert lifted_rank(minus(B[1],B[0]),minus(B[2],B[0]))==(6,6)

centre=times(S((-8,0,18,-8,4,0)),F(4,117))
weights=(F(4,13),F(9,26),F(9,26))
barycentre=tuple(summa(scale(T[i][j],weights[i]) for i in range(3)) for j in range(3))
assert sum(weights)==1 and all(x>0 for x in weights) and barycentre==centre
assert [d2(x,centre) for x in T]==[F(16,13)]*3
pairdist=[d2(T[i],T[j]) for i,j in ((0,1),(0,2),(1,2))]
assert pairdist==[F(32,9),F(32,9),F(320,81)]
assert max(pairdist)/4==F(80,81)<F(16,13)<F(1062562,458329)

e1=S((1,0,0,0,0,0));e2=S((0,0,1,0,0,0));zero=S((0,0,0,0,0,0))
no_go_width=[]
for j in range(5):
    diffs=[]
    for state in (zero,e1,e2):
        b=mass(j,state)
        diffs.append((mass(j,state,ONE)-b-1,mass(j,state,I)-b-1))
    wr=(max(a for a,b in diffs)-min(a for a,b in diffs))/2
    wi=(max(b for a,b in diffs)-min(b for a,b in diffs))/2
    assert wr<=1 and wi<=1
    no_go_width.append((fstr(wr),fstr(wi)))
assert no_go_width==[('1/2','0'),('1/2','0'),('5/8','3/8'),('3/4','3/4'),('1/4','0')]
assert lifted_rank(e1,e2)==(4,5)
p=scale(amp(3,e1),F(1,8));q=scale(amp(3,e2),F(1,8))
assert p==G(F(-1,4),F(-1,4)) and q==scale(p,-2) and norm(p)==F(1,8)
out={
 'schema':'PREFIX313_MULTISTATE_LIFT_EXACT_BRC_V1',
 'scope':'S7-3 q=1, auxiliary Q(i)^3, five exact Q0, ten independent Q1/Qi epsilon=1',
 'source_pins':{'PREFIX299_BLOB':'b6acffe158f014469235f5428d2889ff43b62810',
                'PREFIX312_BLOB':'c2b0e2fb3c79c4c4667ed1b402e593813d99b774'},
 'matrix_A':[[[fstr(z[0]),fstr(z[1])] for z in row] for row in A],
 'triple':{
   'raw_B':[[[fstr(z[0]),fstr(z[1])] for z in s] for s in B],
   'scale':'4/9','common_Q0_numerators':list(Q),'common_Q0_denominator':324,
   'widths':width,'port_evidence':proofrows,'lift_ranks':[6,6],
   'centre_real6':[fstr(x) for x in coords(centre)],
   'contact_weights':[fstr(x) for x in weights],
   'squared_pair_distances':[fstr(x) for x in pairdist],
   'squared_half_diameter':'80/81','squared_miniball_radius':'16/13',
   'PREFIX311_full_model_pair_bound':'1062562/458329'},
 'invalid_triple':{'v':'e1','w':'e2','widths':no_go_width,
                   'lift_ranks':[4,5],'R2_Uv':['-1/4','-1/4'],
                   'R2_Uw':['1/2','1/2'],'R2_norm_Uv_sq':'1/8'},
 'direct_labelled_BRC':counts,'result':'PASS',
 'unresolved':'Does a true same-Q0 multistate fibre reach radius^2 greater than full pairwise L?'
}
with open('RESULTS_PREFIX313.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps({'result':out['result'],'counts':counts,'miniball':'16/13',
                  'half_diameter':'80/81','inconsistent_lift_ranks':[4,5]}))
