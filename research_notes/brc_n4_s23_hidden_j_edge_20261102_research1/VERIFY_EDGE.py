"""Exact BRC S23 J(t) sharp fixed-bank edge certificate. No continuum sampling assumption."""
from fractions import Fraction as F
import json
N=50400
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
G=(0,0,1,2,2,3)
PAIRS=('34 24 34 24','34 23 34 34','34 34 34 23','24 24 12 12','12 12 24 34','12 13 23 24','23 34 12 13','24 34 12 14')
FREE=('5/7 0 2/7 0;3/7 0 2/7 2/7;3/7 0 1/35 19/35;3/7 10/21 0 2/21','11/21 10/21 0 0;10/21 11/21 0 0;1/21 10/21 0 10/21;0 0 11/21 10/21','1/2 0 1/2 0;1/2 1/2 0 0;1/2 0 1/2 0;1/2 0 1/2 0')

def val(s):
    x=N*F(s)
    assert x.denominator==1
    return int(x)
def mix(rows):
    out=[]
    for weights in M:
        row=tuple(F(sum(weights[k]*rows[k][j] for k in range(6)),20) for j in range(4))
        assert sum(row)==N and all(x.denominator==1 and x>=0 for x in row)
        out.append(tuple(int(x) for x in row))
    return tuple(out)
def decode(rows):return mix(tuple(rows[g] for g in G))
def pair(s):return tuple(tuple(N*x.count(str(j))//2 for j in range(1,5)) for x in s.split())
def kernel(s):return tuple(tuple(val(x) for x in row.split()) for row in s.split(';'))
bank=tuple(decode(pair(s)) for i,s in enumerate(PAIRS) if i!=4)+tuple(decode(kernel(s)) for s in FREE)
# Original causal law F(a,b,c); for J(t) A-side a_A=1, and B-side a_B=t,b=0,
# c_BU1=1 only for BU1. Thus the six pre-mixing source rows are affine in t.
def prep(t):
    assert F(0)<=t<=F(1)
    a=F(N)*t;b=F(N)-a
    rows=((N,0,0,0),)*3+((a,0,0,b),(a,0,b,0),(a,0,0,b))
    return tuple(tuple(sum(F(weights[k])*rows[k][j] for k in range(6))/20 for j in range(4)) for weights in M)
def risk(i,t):
    p=prep(t);q=bank[i];best=None
    for row in range(6):
        for mask in range(16):
            v=sum(p[row][j]-q[row][j] for j in range(4) if mask>>j&1)/N
            if best is None or v>best[0]:best=(v,row,tuple(j+1 for j in range(4) if mask>>j&1))
    return best
names=('D1','D2','D3','D4','D6','D7','D8','K1','K2','K3')
tstar=F(17,63)
critical=[risk(i,tstar) for i in range(10)]
assert [v[0] for v in critical]==[F(1)]*4+[F(40,63)]+[F(1)]*2+[F(40,63),F(277,315),F(46,63)]
assert risk(4,F(0))[0]==F(1,2) and risk(7,F(1))[0]==F(4,7)
assert risk(4,tstar)[0]==risk(7,tstar)[0]==F(40,63)
# For each fixed decoder, max-row TV is convex in t since all six P_i(J(t)) are affine.
# On [0,tstar], D6 endpoint risks are 1/2 and 40/63; on [tstar,1],
# K1 endpoint risks are 40/63 and 4/7. Hence all J(t) have risk <=40/63.
# At tstar, all ten decoders have risk >=40/63, yielding equality.
# The opposite endpoints have STRICTLY lower risks, so convex chords prove uniqueness.
report={'pass':'PASS_BRC_S23_J_EDGE_SHARP_40_63_20261102',
 'pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
 'statement':'For fixed seven D1,D2,D3,D4,D6,D7,D8 and K1,K2,K3, max over real t in [0,1] of min-bank max-six-source TV(J(t)) equals 40/63, uniquely at t=17/63.',
 't_star':str(tstar),'sharp_radius':'40/63','left_upper_decoder':'D6','left_endpoints':{'t=0':'1/2','t=17/63':'40/63'},'right_upper_decoder':'K1','right_endpoints':{'t=17/63':'40/63','t=1':'4/7'},
 'critical_risk_event_witnesses':[{'decoder':names[i],'risk':str(v),'source_row_0based':r,'stop_event_atoms_1based':list(event)} for i,(v,r,event) in enumerate(critical)],
 'verification':'Python Fraction exact; event definition max of all 16 stopping subsets per each six original prepared input; convexity supplies all-real interval upper, exact critical events supply lower; no floating-point.'}
print(json.dumps(report,indent=2))
