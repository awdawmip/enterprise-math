#!/usr/bin/env python3
"""Exact three-parameter R5 14-edge Blackwell chamber, including eight vertex certificates."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from runpy import run_path

p = Path(__file__).resolve().parents[1] / "brc_r5_two_dimensional_14edge_fan_20261109_t11" / "VERIFY_2D.py"
c = run_path(str(p))
Q=c["Q"]; add=c["add"]; linear=c["linear"]; masses=c["masses"]; times=c["times"]
slack=c["slack"]; lawful=c["lawful"]; verify=c["verify"]
X0=c["X0"]; X1=c["X1"]; Y0=c["Y0"]; Y1=c["Y1"]
A0=c["A0"]; AH=c["AH"]; SA=c["SA"]; D=c["D"]
DX=c["DX"]; DY=c["DY"]; R=c["R"]
K=Q("-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1")
DX2=tuple(t-u for t,u in zip(DX,K))
HX=Q("-821541312/1111424393 -3044390098/1111424393 -821541312/1111424393 -3998784193/4445697572 -339119685/1111424393 -1775935407/4445697572 0")
HY=Q("-7832/11283 -30398/11283 -7832/11283 -13303/15044 -4802/11283 -5781/15044 -15199/56415")
H={(0,0):-F(23,36),(6,6):-F(13,36),(2,2):F(1)}
expected=Q("-23/36 0 1 1 0 0 -13/36")

def increment(f,d,func):
    return tuple(b-a for a,b in zip(func(f),func(add(f,d,F(1)))))

assert increment(X0,HX,masses)==increment(Y0,HY,masses)==expected
assert increment(X0,HX,times)==increment(Y0,HY,times)
assert HX[0]==HX[2] and HY[6]==HY[1]/10 and HY[4]-HY[6]==F(9,40)*HY[2]
assert sum(H.values())==0 and sum(R[j]*w for (i,j),w in H.items())==0
assert set(H).issubset(SA)

def flow(lam,delta,eta):
    x=add(add(linear(X0,X1,lam),DX2,delta),HX,eta)
    y=add(add(linear(Y0,Y1,lam),DY,delta),HY,eta)
    weights=tuple((1-2*lam)*a+2*lam*b+delta*D.get(edge,F(0))+eta*H.get(edge,F(0))
        for edge,a,b in zip(SA,A0,AH))
    return x,y,weights

lam_range=(F(1,5),F(3,10))
delta_range=(F(1,480),F(1,160))
eta_range=(-F(1,1000),F(1,1000))
mins=[]
for n,(lam,delta,eta) in enumerate(product(lam_range,delta_range,eta_range)):
    x,y,weights=flow(lam,delta,eta)
    assert lawful(x) and lawful(y) and all(v>=0 for v in slack(x)+slack(y))
    assert x[0]==x[2] and y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert times(x)==times(y)
    assert sum(masses(x))==sum(masses(y))==1
    assert sum(R[i]*v for i,v in enumerate(masses(x)))==1
    assert sum(R[i]*v for i,v in enumerate(masses(y)))==1
    positive,min_weight=verify(SA,weights,x,y)
    assert positive==14 and min_weight>0
    mins.append(min_weight)
    print("PASS_EXACT_VERTEX",n,"lambda",lam,"delta",delta,"eta",eta,"edges",positive,"min_weight",min_weight)
assert min(mins)==F(36079,6240000)
assert increment(X0,DX2,masses)==Q("-1/2 0 0 1 0 0 -1/2")
assert masses(Y1)[1]-masses(Y0)[1]==-F(367,24000)
assert increment(X0,HX,masses)[2]==1 and increment(Y0,HY,masses)[1]==0
# Jacobian of (nu_0,mu_1,nu_2) w.r.t. (lambda,delta,eta).
# Its columns are (a,-367/24000,c), (-1/2,0,0), (-23/36,0,1).
det=(masses(Y1)[1]-masses(Y0)[1])/2
assert det==-F(367,48000)
print("PASS_EXACT_THREE_DIMENSIONAL_MARGINAL_JACOBIAN",det)
print("PASS_ALL_REAL_3D_BOX_BY_AFFINE_VERTEX_CERTIFICATES",
      lam_range,delta_range,eta_range,"MIN_EDGE",min(mins))
