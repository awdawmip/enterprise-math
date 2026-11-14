"""PREFIX-784 exact rational finite regression for asymmetric private-corner observers.
Assumptions: one shared scalar corner, independently selectable base/reflected
private sums in closed intervals; no native BRC execution or Gamma recurrence.
"""
from fractions import Fraction as F
from random import Random
import json

def affine(p=0, b=0):
    return (F(p), F(b))

def lower_upper_for_sign(A, B, base, refl, H, Hp, positive):
    # The observed differences are x_i+h+u_i, -(x_i+h'+v_i).
    # positive=True: all differences >=0; else all <=0.
    if positive:
        LI = [affine(0, H[0])] + [affine(b, -a-u) for a,b,(l,u) in zip(A,B,base)]
        UI = [affine(0,H[1])]
        LJ = [affine(0,Hp[0])]
        UJ = [affine(0,Hp[1])] + [affine(b,-a-l) for a,b,(l,u) in zip(A,B,refl)]
    else:
        LI = [affine(0,H[0])]
        UI = [affine(0,H[1])] + [affine(b,-a-l) for a,b,(l,u) in zip(A,B,base)]
        LJ = [affine(0,Hp[0])] + [affine(b,-a-u) for a,b,(l,u) in zip(A,B,refl)]
        UJ = [affine(0,Hp[1])]
    return LI,UI,LJ,UJ

def exact_window(A, B, base, refl, H, Hp, delta, positive):
    LI,UI,LJ,UJ=lower_upper_for_sign(A,B,base,refl,H,Hp,positive)
    lower=F(0); upper=None
    for lows,ups,extra in ((LI,UI,F(0)),(LJ,UJ,F(0)),
                            (LI,UJ,delta),(LJ,UI,delta)):
        for p,r in lows:
            for pp,rr in ups:
                k=p-pp; limit=rr+extra-r
                if k==0:
                    if limit<0: return None
                elif k>0:
                    u=limit/k
                    if upper is None or u<upper:upper=u
                else:
                    lower=max(lower,limit/k)
    if upper is not None and (lower>upper or upper<=0):return None
    return (lower,upper) # Actual q-domain (0,infty), so 0 is excluded.

def intervals_at_q(A,B,base,refl,H,Hp,delta,q,positive):
    x=[a-q*b for a,b in zip(A,B)]
    if positive:
        I=(max([H[0]]+[-xx-u for xx,(l,u) in zip(x,base)]),H[1])
        J=(Hp[0],min([Hp[1]]+[-xx-l for xx,(l,u) in zip(x,refl)]))
    else:
        I=(H[0],min([H[1]]+[-xx-l for xx,(l,u) in zip(x,base)]))
        J=(max([Hp[0]]+[-xx-u for xx,(l,u) in zip(x,refl)]),Hp[1])
    return I,J

def independent_feasible_at_q(A,B,base,refl,H,Hp,delta,q,positive):
    I,J=intervals_at_q(A,B,base,refl,H,Hp,delta,q,positive)
    if I[0]>I[1] or J[0]>J[1]:return False
    return max(I[0]-J[1],J[0]-I[1],F(0))<=delta

def in_window(q,window):
    return window is not None and q>0 and q>=window[0] and (window[1] is None or q<=window[1])

def fm(q):return str(q.numerator)+'/'+str(q.denominator)

def fmt_window(w):return None if w is None else [fm(w[0]),None if w[1] is None else fm(w[1])]

# Witness: 0 included in every private interval, no shared error or defect.
A=[F(1),F(8)];B=[F(1),F(2)]
base=[(F(0),F(1)),(F(-2),F(0))]
refl=[(F(0),F(3)),(F(-6),F(0))]
H=Hp=(F(0),F(0));delta=F(0)
wplus=exact_window(A,B,base,refl,H,Hp,delta,True)
wminus=exact_window(A,B,base,refl,H,Hp,delta,False)
assert wplus==(F(1),F(2)),wplus
assert wminus==(F(3),F(4)),wminus
assert A[1]*B[0]-A[0]*B[1]==6
for q in (F(1),F(3,2),F(2),F(5,2),F(3),F(7,2),F(4)):
    for sign,window in ((True,wplus),(False,wminus)):
        assert independent_feasible_at_q(A,B,base,refl,H,Hp,delta,q,sign)==in_window(q,window)
# In open gap (2,3): base cell1 strictly negative, cell2 strictly positive.
# The margin against zero for both normalized signs is min(q-2, 6-2q).
assert min(F(5,2)-2,6-2*F(5,2))==F(1,2)

rng=Random(20261114784)
counts={'cases':0,'q_probes':0,'both_orientation_windows':0,
        'no_orientation_window':0,'nonconvex_exhibit':1,'exact_boundary_checks':0}
for case in range(1536):
    n=rng.choice((1,2,3))
    A=[F(rng.randint(-5,10),rng.choice((2,3,5))) for _ in range(n)]
    B=[F(rng.randint(1,8),rng.choice((2,3,5))) for _ in range(n)]
    def rand_iv():
        return (F(-rng.randint(0,5),rng.choice((2,3,5))),
                F(rng.randint(0,5),rng.choice((2,3,5))))
    base=[rand_iv() for _ in range(n)];refl=[rand_iv() for _ in range(n)]
    H=rand_iv();Hp=rand_iv()
    delta=F(rng.randint(0,5),rng.choice((2,3,5)))
    wins=[exact_window(A,B,base,refl,H,Hp,delta,sgn) for sgn in (True,False)]
    counts['cases']+=1
    if all(x is not None for x in wins):counts['both_orientation_windows']+=1
    if all(x is None for x in wins):counts['no_orientation_window']+=1
    probes=[F(rng.randint(1,24),rng.choice((2,3,5))) for _ in range(4)]
    for w in wins:
        if w is not None:
            if w[0]>0:probes.append(w[0]);counts['exact_boundary_checks']+=1
            if w[1] is not None and w[1]>0:
                probes.append(w[1]);counts['exact_boundary_checks']+=1
            if w[1] is not None and w[1]>w[0]:probes.append((w[0]+w[1])/2)
    for q in probes:
        if q<=0:continue
        for positive,w in zip((True,False),wins):
            assert in_window(q,w)==independent_feasible_at_q(A,B,base,refl,H,Hp,delta,q,positive), (case,q,positive,w)
            counts['q_probes']+=1

out={'schema':'PREFIX784_R6_ASYMMETRIC_POINTWISE_WINDOWS_V1',
     'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'scope':'two or more abstract adjacent Gamma auxiliary scalar cells, shared corner and independently selectable asymmetric private-error intervals; no native transfer',
     'theorem':'Sign-loss q set is union of at most two rational closed intervals intersected with q>0, computed by four families of affine lower-vs-upper comparisons. It can be disconnected even when 0 belongs to each private interval.',
     'witness':{'A':['1/1','8/1'],
                'B':['1/1','2/1'],'base':[['0/1','1/1'],['-2/1','0/1']],
                'reflected':[['0/1','3/1'],['-6/1','0/1']],
                'shared':'h=h_prime=0, delta=0',
                'all_nonnegative_window':fmt_window(wplus),'all_nonpositive_window':fmt_window(wminus),
                'strict_two_sign_gap':'(2,3)',
                'strict_normalized_sign_margin':'min(q-2,6-2q) for 2<q<3',
                'q_5_2_margin':'1/2','determinant_D':'6/1'},
     'regression':counts,'arithmetic':'Python standard library Fraction, fixed-seed rational randomized probes; universal result from direct interval proof',
     'admission':'AUTHOR_PROVED / EXACT_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED',
     'status':'ALL_CHECKS_PASS PREFIX784 ASYMMETRIC_CORNER_WINDOWS'}
with open('PREFIX784_R6_ASYMMETRIC_CORNER_WINDOWS_RESULTS.json','w',encoding='utf-8') as f:
    json.dump(out,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps({'status':out['status'],'witness':out['witness'],'regression':counts},indent=2))
