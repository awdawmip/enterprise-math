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

def seam_sample(i,j):
    a,b=D[i];c,d=D[j]
    lo=tuple(min(x,y) for x,y in zip(a,c))
    hi=tuple(max(x,y) for x,y in zip(b,d))
    gap=hi[2]-lo[3]
    if gap<0:return None
    assert hi[2]>lo[2] and hi[3]>lo[3]
    t=(hi[2]+lo[3])/2
    x=(lo[0]+hi[0])/2
    y=(lo[1]+hi[1])/2
    assert U[55]<t<U[56] and x<y<t<Z
    assert lo[2]<=t<=hi[2] and lo[3]<=t<=hi[3]
    q=F(Q)*A/H/((2-t*t)*(3-t*t))**3
    slope=6*t/(2-t*t)+6*t/(3-t*t)
    curv=6*(2+t*t)/(2-t*t)**2+6*(3+t*t)/(3-t*t)**2
    for k in J:
        q*=(Z-U[k])/abs(t-U[k])
        slope-=1/(t-U[k])
        curv+=1/(t-U[k])**2
    for e in (x,y):
        q*=(Z-e)/abs(t-e)
        slope-=1/(t-e)
        curv+=1/(t-e)**2
    assert q>0
    # Symbolic proof of C>0 uses L''>1/(Z-t)^2 from index 54 alone.
    assert 0<t-U[54]<Z-t
    assert curv>1/(Z-t)**2
    quad=q*((Z-t)*(slope*slope+curv)+2*slope)/4
    completed_square=q*((Z-t)*(slope+1/(Z-t))**2+(Z-t)*curv-1/(Z-t))/4
    assert quad==completed_square and quad>0
    res=2*(Z-t)*q
    assert F(Q,4096)<res<F(Q,2048)
    return gap,res,quad

if __name__=='__main__':
    safe=touch=overlap=0
    residues=[];qs=[]
    for i in range(35):
        for j in range(i+1,35):
            value=seam_sample(i,j)
            if value is None:safe+=1
            else:
                gap,res,quad=value
                if gap==0:touch+=1
                else:assert gap>0;overlap+=1
                residues.append(res);qs.append(quad)
    assert (safe,touch,overlap)==(363,124,108)
    assert len(residues)==232 and all(r>0 for r in residues) and all(c>0 for c in qs)
    assert min(residues)>F(Q,4096) and max(residues)<F(Q,2048)
    print('C271_AUXILIARY_SEAM_STANDALONE_EXACT_PASS',
          'safe',safe,'boundary_touch',touch,'interior_overlap',overlap,
          'R_RANGE:(Q/4096,Q/2048)','positive_quadratic',len(qs))



from itertools import combinations
# ----- C273: appended high-dimensional seam neighborhood exact certificate -----
# Original C271 data and its validation remain intact above this line.
# C273 adds 230 full 4-dimensional positive regions and 2 relative 3D regions.
# Author-scope auxiliary mathematics only; not a native X6 or phase theorem.
DELTA273=F(1,20000)
EPS_CROSS273=F(1,2800)
EPS_TOUCH273=F(1,3100)
assert 39*2800>40*2720 and 39*3100>40*3014

def c273_residue_lower(a,b,t):
    """Exact factorwise lower bound for R(a,b,t)/Q on the DELTA273 box."""
    tm=t-DELTA273;tx=t+DELTA273
    assert U[55]<tm<tx<U[56]
    out=F(2)*(Z-tx)*A/H/((2-tm*tm)*(3-tm*tm))**3
    for j in J:
        assert tm>U[j] or tx<U[j]
        out *= (Z-U[j])/max(abs(tm-U[j]),abs(tx-U[j]))
    for p in (a,b):
        assert p+DELTA273<tm
        out *= (Z-p-DELTA273)/(tx-p+DELTA273)
    return out

def c273_check():
    classes={"safe":0,"cross":0,"touch":0}
    fixed_b=[]; min_ratios={"cross":None,"touch":None}
    for i,j in combinations(range(35),2):
        lo=tuple(min(x,y) for x,y in zip(D[i][0],D[j][0]))
        hi=tuple(max(x,y) for x,y in zip(D[i][1],D[j][1]))
        gap=hi[2]-lo[3]
        if gap<0:
            classes["safe"]+=1
            continue
        a,b=(lo[0]+hi[0])/2,(lo[1]+hi[1])/2
        t=(hi[2]+lo[3])/2
        d=DELTA273
        assert lo[0]<a-d<a+d<hi[0]
        if lo[1]==hi[1]:
            assert gap==0 and b==lo[1]
            fixed_b.append((i,j))
        else:
            assert lo[1]<b-d<b+d<hi[1]
        if gap>0:
            name="cross";e=EPS_CROSS273
            assert lo[2]<t-d-e/2<t+d<hi[2]
            assert lo[3]<t-d<t+d+e/2<hi[3]
            assert U[55]<t-d-e/2 and t+d+e/2<U[56]
            assert b+d<t-d-e/2
        else:
            name="touch";e=EPS_TOUCH273
            assert hi[2]==lo[3]==t
            reach=F(11,20)*e
            assert lo[2]<t-reach and t+reach<hi[3]
            assert U[55]<t-reach and t+reach<U[56]
            assert b+d<t-reach
            assert F(1,20)*e<d
        assert a+d<b-d
        Rlower=c273_residue_lower(a,b,t)
        assert Rlower>e
        if min_ratios[name] is None or Rlower<min_ratios[name][0]:
            min_ratios[name]=(Rlower,(i,j))
        classes[name]+=1
    assert classes=={"safe":363,"cross":108,"touch":124}
    assert fixed_b==[(6,10),(8,9)]
    print("C273_230_4D_PLUS_2_RELATIVE_3D_EXACT_PASS",
          "cross",classes["cross"],"touch",classes["touch"],
          "fixed_b",fixed_b,
          "cross_min_pair",min_ratios["cross"][1],
          "touch_min_pair",min_ratios["touch"][1],
          "cross_min_lower_R_over_Q_approx",float(min_ratios["cross"][0]),
          "touch_min_lower_R_over_Q_approx",float(min_ratios["touch"][0]))
if __name__=="__main__":
    c273_check()
