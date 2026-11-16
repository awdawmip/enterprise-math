"""Integer-grid Newton certificate for terminal column ratios, with exact finite controls."""
from fractions import Fraction as F
from math import prod
import json

def V(w):
    return (w+2)*(w+3)*(w+4)

def cleared_R(w,Y):
    # R=(W+32W²/3Y + ...), expressed without negative powers.
    # Actual ratio is (3Y+32W)(2+W)/[(1+5W)(6Y+W)].
    z=V(w)
    return (2520*Y+32*z)*(1680+z), (840+5*z)*(5040*Y+z)

def difference_poly(n,z):
    w=n+32
    # Positive factor 36(1+z)^2(4w+8) clears both one-step Y denominators.
    y0=6*(1+z); y1=y0*(4*w+8)
    n0=(2520+32*V(w)*y0)*(1680+V(w))
    d0=(840+5*V(w))*(5040+V(w)*y0)
    n1=(2520*(4*w+5)+32*V(w+1)*y1)*(1680+V(w+1))
    d1=(840+5*V(w+1))*(5040*(4*w+5)+V(w+1)*y1)
    return n0*d1-n1*d0

def differences(row):
    out=[]
    while row:
        out.append(row[0]);row=[b-a for a,b in zip(row,row[1:])]
    return out

def main():
    # Newton binomial coefficients do not have fixed sign at arbitrary real z.
    # Extract ordinary power coefficients in real z (degree <=2), first.
    raw=[]
    for n in range(15):      # degrees <=13 in n before cancellation, 2 in z
        a,b,c=(difference_poly(n,z) for z in (0,1,2))
        quad=(c-2*b+a)//2
        assert c-2*b+a == 2*quad
        raw.append((a,b-a-quad,quad))
    cert=[differences(list(row)) for row in zip(*raw)]
    assert all(row[0]>0 and min(row)>=0 for row in cert)
    assert all(row[-1]==0 for row in cert)
    # For integer n>=0, binom(n,r)>=0; for real z>=0 all z^i>=0.
    Y=F(1)
    records={}
    by_w={}
    ratios={}
    for w in range(2,101):
        if w>2:
            Y*=F(4*w+1,4*w+4)
        W=F(V(w),840)
        ends=[(F(5),F(3,32)),(F(5,4),F(3,2)),(F(1,2),F(6))]
        p=[(1+W/(e*Y))/(1+j*W) for j,e in ends]
        zero=[1/(1+j*W) for j,e in ends]
        i,j=p.index(max(p)),p.index(min(p))
        assert (i,j)==(0,1 if w<=3 else 2)
        R=p[i]/p[j]
        by_w[w]=R
        E=(p[i]-p[j])/(zero[j]-zero[i])
        if w>=4:
            assert E==(W+F(7,3))/Y-1
            n,d=cleared_R(w,Y)
            assert R==n/d
        if w==34:
            assert Y<F(1,6)
        if w in (2,3,4,14,15,21,34,100):
            records[w]=dict(ratio_floor_1e8=R.numerator*10**8//R.denominator,
                            real_to_frozen_gap_floor_1e8=E.numerator*10**8//E.denominator)
        ratios[w]=E
    assert len(set(by_w.values()))==99
    assert all(by_w[w]<by_w[w+1] for w in range(2,21))
    assert all(by_w[w]>by_w[w+1] for w in range(21,100))
    assert by_w[14]<F(32,5)<by_w[100]<by_w[15]
    assert ratios[2]<ratios[4]<ratios[3]<ratios[5]
    assert all(ratios[w]<ratios[w+1] for w in range(4,100))
    return dict(coefficient_min_per_real_power=[min(v for v in row if v) for row in cert],
                nonzero_integer_orders=[sum(bool(v) for v in row) for row in cert],
                inventory_newton_degree_bound=13, inventory_newton_origin=32,
                real_parameter='Y=1/(6*(1+z))', branch_peak_stock=21,
                ratio_limit='32/5', records=records)

if __name__=='__main__':
    print(json.dumps(main(),indent=2))
