#!/usr/bin/env python3
"""C271 self-contained author exact checker: all 595 C254 two-box hulls.
Only standard-library Fraction. The C195/H168 auxiliary, NOT native GF(2)-BRC.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
BOX_DATA="4/543,43/62,4/5,9/11,9/613,57/79,38/47,121/147;3/407,5/7,60/77,4/5,7/477,18/25,53/67,9/11;3/407,5/7,18/23,4/5,6/409,31/43,87/109,4/5;3/407,5/7,4/5,81/101,7/477,31/43,21/26,76/93;2/271,7/10,60/77,4/5,6/409,42/59,11/14,4/5;2/271,7/10,4/5,13/16,6/409,27/38,4/5,58/71;2/271,12/17,26/33,4/5,3/233,12/17,59/74,4/5;1/135,16/23,18/23,9/11,3/205,5/7,4/5,9/11;1/135,7/10,26/33,4/5,3/283,7/10,27/34,4/5;1/135,7/10,4/5,49/61,2/137,7/10,4/5,31/38;1/135,12/17,4/5,57/71,3/205,12/17,4/5,30/37;1/127,16/23,18/23,4/5,1/106,16/23,4/5,13/16;3/371,7/10,15/19,4/5,2/171,17/24,53/67,4/5;1/123,34/49,15/19,4/5,1/69,7/10,59/74,4/5;1/123,26/37,48/61,4/5,1/78,27/38,15/19,4/5;1/119,19/27,4/5,17/21,3/205,12/17,4/5,69/85;1/119,12/17,18/23,13/16,3/205,12/17,11/14,9/11;1/119,12/17,15/19,13/16,1/74,12/17,15/19,22/27;1/119,5/7,60/77,19/24,1/69,28/39,34/43,41/51;1/119,5/7,18/23,17/21,3/205,5/7,59/74,9/11;1/117,19/27,4/5,21/26,1/85,22/31,4/5,17/21;1/105,7/10,53/68,9/11,3/205,18/25,53/67,23/28;1/105,12/17,4/5,13/16,1/74,42/59,21/26,9/11;1/104,34/49,18/23,4/5,1/69,7/10,34/43,4/5;1/104,34/49,4/5,41/51,1/69,30/43,4/5,22/27;1/103,7/10,27/34,4/5,2/155,22/31,87/109,4/5;1/103,12/17,18/23,21/26,1/86,12/17,18/23,13/16;2/189,7/10,32/41,4/5,3/205,19/27,37/47,4/5;1/93,16/23,18/23,13/16,2/137,7/10,15/19,9/11;1/93,12/17,18/23,19/24,6/409,27/38,15/19,4/5;1/93,12/17,18/23,21/26,1/69,12/17,11/14,17/21;1/93,12/17,19/24,13/16,1/69,12/17,27/34,13/16;1/89,12/17,15/19,21/26,1/69,12/17,15/19,13/16;1/88,12/17,26/33,4/5,3/232,29/41,72/91,4/5;1/77,7/10,26/33,4/5,6/409,12/17,63/79,4/5"
U=tuple(F(a,b) for a,b in zip(NUM,DEN))
Q=2**128; H=2**166; A=F(6912*50000**2,17**2)
Z=F(141421356237309504880,10**20)
I=(5,50,55,56)
J=tuple(k for k in range(79) if k not in I)
assert len(U)==79 and all(U[k]<U[k+1] for k in range(78))
assert U[54]==F(7,9) and U[55]==F(15,19) and U[56]==F(17,21)
assert U[56]-U[54] == F(2,63) < Z-U[56]
D=[]
for item in BOX_DATA.split(';'):
    z=tuple(map(F,item.split(',')))
    assert len(z)==8
    l,h=z[:4],z[4:]
    assert all(U[p-1]<l[d]<=h[d]<U[p+1] for d,p in enumerate(I))
    assert l[2]<l[3] and h[2]<h[3]
    D.append((l,h))
assert len(D)==35
basic_delta=[h[2]-l[3] for l,h in D]
assert [k for k,g in enumerate(basic_delta) if g>0]==[3]
assert [k for k,g in enumerate(basic_delta) if g==0]==[11]
assert basic_delta[3]==F(15,2626)


# C274 addendum: global collision collar, exact 128-interval proof.
# Author research only; no Source claim and no native BRC/X6 transfer.
from itertools import combinations
import json

A_MIN=min(lo[0] for lo,hi in D)
B_MIN=min(lo[1] for lo,hi in D)
EPS_MAX=F(1,3077)
assert A_MIN==F(4,543) and B_MIN==F(43,62)
assert U[54]==F(7,9) and U[55]==F(15,19) and U[56]==F(17,21)
assert 54 in J and 55 not in J and 56 not in J
assert Z+U[54]-2*U[56]>0
assert all(A_MIN<=lo[0]<=hi[0]<U[55] and
           B_MIN<=lo[1]<=hi[1]<U[55] for lo,hi in D)

def residue_over_q(t):
    """Return exact R(A_MIN,B_MIN,t)/Q."""
    assert U[55]<=t<=U[56] and t<Z
    value=2*(Z-t)*A/H/((2-t*t)*(3-t*t))**3
    for j in J:
        assert t!=U[j]
        value*=(Z-U[j])/abs(t-U[j])
    for p in (A_MIN,B_MIN):
        value*=(Z-p)/(t-p)
    return value

def log_derivative(t):
    """Exact derivative of log(R(A_MIN,B_MIN,t))."""
    assert U[55]<=t<=U[56]
    out=-1/(Z-t)+6*t/(2-t*t)+6*t/(3-t*t)
    for j in J:
        out-=1/(t-U[j])
    for p in (A_MIN,B_MIN):
        out-=1/(t-p)
    return out

def derivative_certificate(n=128):
    """Each cell: log R strictly convex, hence derivative monotone.
    R(t)/Q >= R(mid)/Q * (1-h*K), h=halfwidth,
    K=max(abs(logR'(left)),abs(logR'(right))).
    Strict log convexity follows from the fixed u54 term:
      1/(t-u54)^2 > 1/(Z-t)^2.
    """
    start,stop=U[55],U[56]
    minimum=None; index=None
    for i in range(n):
        left=start+(stop-start)*F(i,n)
        right=start+(stop-start)*F(i+1,n)
        mid=(left+right)/2
        k=max(abs(log_derivative(left)),abs(log_derivative(right)))
        v=k*(right-left)/2
        assert 0<=v<1
        lower=residue_over_q(mid)*(1-v)
        assert lower>EPS_MAX,("bound fails",i)
        if minimum is None or lower<minimum:
            minimum,index=lower,i
    return minimum,index

def factorwise_lower(left,right):
    """Different method: direct monotone bound per positive factor."""
    out=2*(Z-right)*A/H/((2-left*left)*(3-left*left))**3
    for j in J:
        u=U[j]
        assert u<left or u>right
        out*=(Z-u)/max(abs(left-u),abs(right-u))
    for p in (A_MIN,B_MIN):
        out*=(Z-p)/(right-p)
    return out

def independent_factorwise_check(n=768):
    start,stop=U[55],U[56]
    mini=None;pos=None
    for i in range(n):
        left=start+(stop-start)*F(i,n)
        right=start+(stop-start)*F(i+1,n)
        lower=factorwise_lower(left,right)
        assert lower>F(1,3100),("interval fails",i)
        if mini is None or lower<mini:
            mini,pos=lower,i
    return mini,pos

def prove_hull_witnesses():
    classes={"safe":0,"touch":0,"cross":0};degenerate=[]
    for i,j in combinations(range(len(D)),2):
        lo=tuple(min(D[i][0][k],D[j][0][k]) for k in range(4))
        hi=tuple(max(D[i][1][k],D[j][1][k]) for k in range(4))
        gap=hi[2]-lo[3]
        if gap<0:
            classes["safe"]+=1
            continue
        kind="touch" if gap==0 else "cross"
        classes[kind]+=1
        a=(lo[0]+hi[0])/2; b=(lo[1]+hi[1])/2
        t=(hi[2]+lo[3])/2
        x=t-EPS_MAX/2; y=t+EPS_MAX/2
        assert lo[0]<=a<=hi[0] and lo[1]<=b<=hi[1]
        assert lo[2]<x<hi[2] and lo[3]<y<hi[3]
        assert U[55]<x<y<U[56] and a<b<x
        if lo[1]==hi[1]:degenerate.append([i,j])
    assert classes=={"safe":363,"touch":124,"cross":108}
    assert degenerate==[[6,10],[8,9]]
    return classes,degenerate

def run():
    first,idx=derivative_certificate()
    second,idx2=independent_factorwise_check()
    classes,degen=prove_hull_witnesses()
    record={
      "result":"C274_GLOBAL_COLLAR_AUTHOR_EXACT_PASS",
      "model":"C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY",
      "input_origin_git_blob_sha1":"118716c5425fdabc4d2421ddac6816e7478a22e3",
      "minimum_a":str(A_MIN),"minimum_b":str(B_MIN),
      "t_interval":["15/19","17/21"],
      "epsilon_max":str(EPS_MAX),"primary_exact_cells":128,
      "primary_minimum_cell":idx,
      "primary_min_lower_num":str(first.numerator),
      "primary_min_lower_den":str(first.denominator),
      "primary_gt_1_over_3077":3077*first.numerator>first.denominator,
      "secondary_factorwise_cells":768,
      "secondary_minimum_cell":idx2,
      "secondary_gt_1_over_3100":3100*second.numerator>second.denominator,
      "collar_witnesses":classes["touch"]+classes["cross"],
      "hull_counts":classes,"fixed_b_pairs":degen,
      "entire_232_hull_classification":False,
      "native_claim_or_driver_admission":False
    }
    print("C274_GLOBAL_COLLAR_EXACT_PASS 128 768 EPS=1/3077 COLLAR_HULLS=232")
    print(json.dumps(record,ensure_ascii=False,indent=2))
    return record

if __name__=="__main__":run()
