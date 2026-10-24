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




from itertools import combinations
import json
# Original C275 endpoints: distinct low-side witnesses, unchanged 79-node F.
WITNESSES = ((F(1,93), F(12,17), F(27,34), F(101,125)),
             (F(1,100), F(703,1000), F(27,34), F(101,125)))
EPS = F(1,10000)
N = 4096
K = [437,437,437,437,437,437,437,437,437,558,437,437,339,437,558,339,339,437,437,498,553,498,428,553,453,453,358,574,486,541,486,418,541,442,442,351,563,399,351,409,399,436,399,452,376,334,334,376,452,399,334,399,409,423,334,334,334,351,399,598,618,598,598,640,598,598,476,652,612,612,649,612,659,612,583,659,612,612,674,612,612,619,654,600,733,623,639,451,676,618,618,618,635,618,640,635,618,618,679,618,617,651,651,719,505,634,614,585,622,497,674,643,650,669,633,670,582,504,670,621,651,603,583,650,749,700,651,651,693,629,601,741,538,526,702,756,404,691,657,657,657,711,650,607,698,488,647,643,641,502,558,619,463,637,507,633,584,613,598,571,612,511,438,631,491,530,625,642,579,593,599,577,464,451,321,424,471,308,308,406,423,584,366,633,591,587,505]

def fixed_weights():
    out={}
    for j in J:
        b=F(Q)*A/H/((2-U[j]*U[j])*(3-U[j]*U[j]))**3
        for r in range(79):
            if r!=j: b *= (Z-U[r])/abs(U[j]-U[r])
        out[j]=b.numerator//b.denominator
        assert out[j]>0
    assert len(out)==75
    return out

def original_f(v,w):
    result=F(0)
    for j in J:
        mass=F(w[j])
        for p,x in zip(I,v):
            mass*=(Z-x)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-x)
        result+=mass
    for d,p in enumerate(I):
        x=v[d]
        mass=F(Q)*A/H/((2-x*x)*(3-x*x))**3
        for j in J:
            mass*=(Z-U[j])/abs(x-U[j])
        for other,y in enumerate(v):
            if d!=other:
                mass*=(Z-y)/abs(x-y)
        result+=mass
    return result

def pairs():
    for i,j in combinations(range(35),2):
        lo=tuple(min(D[i][0][d],D[j][0][d]) for d in range(4))
        hi=tuple(max(D[i][1][d],D[j][1][d]) for d in range(4))
        delta=hi[2]-lo[3]
        kind="safe" if delta<0 else "touch" if delta==0 else "cross"
        yield (i,j),lo,hi,kind

def contained(v,lo,hi):
    return all(lo[d]<=v[d]<=hi[d] for d in range(4))

def legal(v):
    return (all(U[p-1]<v[d]<U[p+1] for d,p in enumerate(I))
            and v[0]<v[1]<v[2]<v[3] and all(Z-x>0 for x in v))

def positive(lo,hi):
    a=(lo[0]+hi[0])/2
    b=(lo[1]+hi[1])/2
    t=(hi[2]+lo[3])/2
    return (a,b,t-EPS/2,t+EPS/2)

def chords():
    result=[]
    safe=touch=cross=0
    for pair,lo,hi,kind in pairs():
        if kind=="safe":
            safe+=1
            continue
        if kind=="touch":touch+=1
        else:cross+=1
        witness=next((q for q,w in enumerate(WITNESSES) if contained(w,lo,hi)),None)
        if witness is None:continue
        low=WITNESSES[witness]
        high=positive(lo,hi)
        assert legal(low) and legal(high)
        assert contained(low,lo,hi) and contained(high,lo,hi)
        result.append((pair,kind,witness,low,high,lo,hi))
    assert (safe,touch,cross)==(363,124,108),(safe,touch,cross)
    assert len(result)==187
    assert sum(row[1]=="touch" for row in result)==111
    assert sum(row[1]=="cross" for row in result)==76
    return result

def point(low,high,k):
    return tuple((N-k)*x/N+k*y/N for x,y in zip(low,high))

def bisection(low,high,w):
    a,b=0,N
    assert original_f(low,w)<Q and original_f(high,w)>Q
    while b-a>1:
        m=(a+b)//2
        f=original_f(point(low,high,m),w)
        if f<Q:a=m
        elif f>Q:b=m
        else:raise ArithmeticError("exact rational root met; separate case")
    return a

def check(regenerate=False):
    w=fixed_weights()
    cases=chords()
    assert len(K)==len(cases)==187
    count={"touch":0,"cross":0}
    minlo=minhi=None
    rows=[]
    for index,(pair,kind,which,low,high,hlo,hhi) in enumerate(cases):
        k=K[index]
        assert 0<=k<N
        xlo,xhi=point(low,high,k),point(low,high,k+1)
        assert legal(xlo) and legal(xhi)
        assert contained(xlo,hlo,hhi) and contained(xhi,hlo,hhi)
        flo,fhi=original_f(xlo,w),original_f(xhi,w)
        assert flo<Q*(1-F(1,10**9)),("left margin",pair,k)
        assert fhi>Q*(1+F(1,10**8)),("right margin",pair,k)
        if regenerate:assert bisection(low,high,w)==k,("regeneration",pair,k)
        l=(Q-flo)/Q; r=(fhi-Q)/Q
        minlo=l if minlo is None else min(l,minlo)
        minhi=r if minhi is None else min(r,minhi)
        count[kind]+=1
        rows.append({"hull":list(pair),"kind":kind,"negative_witness":which,
                     "k":k,"lambda_left":str(k)+"/4096",
                     "lambda_right":str(k+1)+"/4096","strict":True})
    assert count=={"touch":111,"cross":76}
    assert (min(K),max(K))==(308,756)
    return {"status":"C280B_187_EXACT_DYADIC_BRACKETS_PASS",
            "model":"C195_H168_POSITIVE_RATIONAL_AUXILIARY",
            "source_admitted":False,"independent_driver_review":False,
            "tested_regeneration":regenerate,"count":len(rows),"k_min_max":[min(K),max(K)],
            "kinds":count,"lambda_denominator":N,
            "strict_lower_margin":"1/1000000000",
            "strict_upper_margin":"1/100000000",
            "minimum_margins_display_only":[float(minlo),float(minhi)],
            "certificates":rows}

if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("--regenerate",action="store_true")
    ap.add_argument("--certificate",type=str)
    opts=ap.parse_args()
    result=check(regenerate=opts.regenerate)
    if opts.certificate:
        with open(opts.certificate,"w",encoding="utf-8") as f:
            json.dump(result,f,ensure_ascii=False,indent=2)
            f.write("\n")
    print(json.dumps({k:v for k,v in result.items() if k!="certificates"},
                     ensure_ascii=False,indent=2))
