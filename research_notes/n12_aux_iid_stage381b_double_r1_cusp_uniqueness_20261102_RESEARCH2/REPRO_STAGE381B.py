#!/usr/bin/env python3
"""Stage381-B: exact rational Bernstein proof of double r1 contact and Q cusp.
All exact input is inherited from frozen Stage380-B; no external dependencies.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
from hashlib import sha256
from pathlib import Path
import argparse, csv, io

P = (F(2308,10000), F(2345,10000), F(55,100), F(56,100))
Q = (F(2365,10000), F(239,1000), F(57566,100000), F(57574,100000))

# Polynomial in x,y as coefficient dict (i,j) -> Fraction, with exact operations.
def mul(p, q):
    out = {}
    for (i,j), a in p.items():
        for (k,l), b in q.items():
            out[(i+k,j+l)] = out.get((i+k,j+l), F(0)) + a*b
    return {k:v for k,v in out.items() if v}
def add(p, q):
    out = dict(p)
    for k,v in q.items(): out[k] = out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(p, a):return {k:v*a for k,v in p.items() if v*a}
def ev(p, x, y):return sum(a*x**i*y**j for (i,j),a in p.items())
X={(1,0):F(1)};Y={(0,1):F(1)};O={(0,0):F(1)}

def lin(var,a,b):return add(scale(O,a),scale(var,b))
GX=mul(lin(X,1,-1),lin(X,1,-3))   # f'(x)=(1-x)(1-3x)
S =mul(lin(Y,1,-1),lin(Y,-1,3))   # -f'(y)=(1-y)(3y-1)
CX=scale(mul(lin(X,1,-1),lin(X,63,-61)), -F(3,256))
BX=scale(lin(X,1,-2),F(3,4))
BY=scale(lin(Y,1,-2),F(3,16))
CYL=scale(mul(Y,lin(Y,1,-1)),F(3,64))
CYH=scale(mul(Y,lin(Y,18,-25)),F(3,256))

# Signed H_lambda=s*(c_x+lambda*b_x)+4*f'(x)*(c_y+lambda*b_y).
# On r1=0, B_face'>0 and mu=-C_face'/B_face',
# so H_lambda<0 iff mu>lambda.
def H(lam, cy):
    return add(mul(S, add(CX,scale(BX,lam))),
               scale(mul(GX,add(cy,scale(BY,lam))),4))

# Independent closed-form coefficient checks, all entries /256.
def exact_expected(tag):
    terms={
      'P_GT_7_OVER_6':{(2,2):405,(2,1):-1932,(2,0):855,(1,2):420,(1,1):1296,(1,0):-820,(0,2):-153,(0,1):-260,(0,0):189},
      'P_LT_5_OVER_4':{(2,2):405,(2,1):-2028,(2,0):903,(1,2):516,(1,1):1296,(1,0):-852,(0,2):-201,(0,1):-228,(0,0):189},
      'Q_LO_GT_5_OVER_4':{(2,2):405,(2,1):-2028,(2,0):903,(1,2):516,(1,1):1296,(1,0):-852,(0,2):-201,(0,1):-228,(0,0):189},
      'Q_HI_LT_7_OVER_6':{(2,2):-351,(2,1):-1428,(2,0):855,(1,2):1428,(1,1):624,(1,0):-820,(0,2):-405,(0,1):-92,(0,0):189},
    }[tag]
    return {k:F(v,256) for k,v in terms.items()}

# Exact (2,2) Bernstein control coefficients on a rational rectangle.
def bernstein_controls(poly, box):
    xa, xb, ya, yb = box
    dx, dy=xb-xa,yb-ya
    power={}
    for i in range(3):
        for j in range(3):
            value=F(0)
            for (k,l), aa in poly.items():
                if k>=i and l>=j:
                    value += aa * comb(k,i)*xa**(k-i)*dx**i * comb(l,j)*ya**(l-j)*dy**j
            power[(i,j)]=value
    ans=[]
    for i in range(3):
        for j in range(3):
            coeff=sum(power[(k,m)]*F(comb(i,k),comb(2,k))*F(comb(j,m),comb(2,m))
                      for k in range(i+1) for m in range(j+1))
            ans.append((i,j,coeff))
    return ans

def f1(z):return z*(1-z)**2
def r1(x,y):return (4*f1(x)+f1(y))/5-F(21,160)
def r0(x,y):return (4*(1-x)**3+(1-y)**3)/5-F(61,160)
def r2(x,y):return (4*x*x*(1-x)+y*y*(1-y))/5-F(9,160)
def bquadratic(x,y):return F(3,16)*(4*x*(1-x)+y*(1-y))-F(45,256)
def alpha_q(z):return 16*z*z-4*z-3

def check():
    # Stage380-B wedge inputs: P r0<=0<=r1, Q r0<0<=r1,
    # and active quadratic budget. Here we check every NEW algebraic sign.
    assert all(F(0)<v<F(1) for v in P+Q)
    assert P[1]<Q[0] and P[1]<F(1,4) and Q[1]<F(1,4)
    assert P[2]>F(1,2) and Q[2]>F(1,2)
    # mu_x>1, and one-sided nu_y<1 in every required rectangle.
    assert 61*P[0]**2+4*P[0]-1>0
    assert P[2]**2+7*P[2]-4>0
    assert Q[2]**2+7*Q[2]-4>0
    assert 25*Q[2]**2+14*Q[2]-16>0
    # delta cusp: alpha is the unique Q-box root of 16y^2-4y-3.
    assert alpha_q(Q[2])<0<alpha_q(Q[3])
    # d/dx budget along r1=0 is positive: D=(y-x)(6xy-3x-3y+2).
    for box in (P,Q):
        a,b,c,d=box
        assert a>0 and d<1
        assert a<c
        # 6xy-3x-3y+2 increases in x, decreases in y on these rectangles.
        assert 6*a*d-3*a-3*d+2>0
        # Independent exact polynomial identity for D=(1-2x)*s-(2y-1)*g(x).
        for xx in (a,b):
            for yy in (c,d):
                ss=(1-yy)*(3*yy-1);g=(1-xx)*(1-3*xx)
                D=(1-2*xx)*ss-(2*yy-1)*g
                assert D==(yy-xx)*(6*xx*yy-3*xx-3*yy+2)>0

    cases=[
      ('P_GT_7_OVER_6',P,F(7,6),CYL,-1),
      ('P_LT_5_OVER_4',P,F(5,4),CYL,+1),
      ('Q_LO_GT_5_OVER_4',Q,F(5,4),CYL,-1),
      ('Q_HI_LT_7_OVER_6',Q,F(7,6),CYH,+1),
    ]
    rows=[]; summaries=[]
    for tag,box,lam,cy,expected_sign in cases:
        pol=H(lam,cy)
        assert pol==exact_expected(tag), (tag,pol)
        assert all(i<=2 and j<=2 for i,j in pol)
        controls=bernstein_controls(pol,box)
        assert len(controls)==9
        assert all(coef*expected_sign>0 for _,_,coef in controls),tag
        # Confirm at 9 exact source points that explicit derivative expression agrees.
        for xx in (box[0],(box[0]+box[1])/2,box[1]):
            for yy in (box[2],(box[2]+box[3])/2,box[3]):
                ss=(1-yy)*(3*yy-1); gx=(1-xx)*(1-3*xx)
                cxx=-F(3,256)*(1-xx)*(63-61*xx)
                bxx=F(3,4)*(1-2*xx)
                cyy=F(3,64)*yy*(1-yy) if cy is CYL else F(3,256)*yy*(18-25*yy)
                byy=F(3,16)*(1-2*yy)
                expected=ss*(cxx+lam*bxx)+4*gx*(cyy+lam*byy)
                assert ev(pol,xx,yy)==expected
        summaries.append((tag,min(a for _,_,a in controls),max(a for _,_,a in controls)))
        for i,j,a in controls: rows.append((tag,i,j,str(a)))
    # Certified illustrative algebraic isolator for Q: both alpha and its r1 root.
    alo, ahi=F(575693909432,10**12),F(575693909434,10**12)
    xlo, xhi=F(237806902788,10**12),F(237806902794,10**12)
    assert Q[2]<alo<ahi<Q[3] and alpha_q(alo)<0<alpha_q(ahi)
    assert Q[0]<xlo<xhi<Q[1]
    # r1 increasing in x and decreasing in y in this rectangle.
    assert r1(xlo,alo)<0<r1(xhi,ahi)
    # Independent rational enclosure for inherited simultaneous r0=r1 zero.
    xb_lo, xb_hi=F(231083,10**6),F(231085,10**6)
    yb_lo, yb_hi=F(55550,10**5),F(55552,10**5)
    assert r1(xb_lo,yb_lo)>0>r1(xb_lo,yb_hi)
    assert r1(xb_hi,yb_lo)>0>r1(xb_hi,yb_hi)
    assert r0(xb_lo,yb_hi)>0>r0(xb_hi,yb_lo)
    # r1_y<0 and r1_x>0; root y(x) increases; r0(x,y(x)) decreases.
    beta_lo=F(15,16)*r2(xb_lo,yb_lo)
    beta_hi=F(15,16)*r2(xb_hi,yb_hi)
    assert F(377,100000)<beta_lo<beta_hi
    # bQ(cusp) < beta*+E: r0(P)=0 is incompatible with Q y <= alpha.
    bq_lo=bquadratic(xlo,ahi)
    bq_hi=bquadratic(xhi,alo)
    assert bq_lo<bq_hi<beta_lo+F(11,5000)
    # Constructively isolate the unique solution of both r1 faces, cusp and
    # exact joint budget. b on the r1 face is strictly increasing in x.
    xp_lo,xp_hi=F(23113,100000),F(23115,100000)
    ypl_lo, ypl_hi=F(55565,100000),F(55566,100000)
    yph_lo, yph_hi=F(55571,100000),F(55572,100000)
    assert r1(xp_lo,ypl_lo)>0>r1(xp_lo,ypl_hi)
    assert r1(xp_hi,yph_lo)>0>r1(xp_hi,yph_hi)
    target_lo=2*beta_lo+F(11,5000)-bq_hi
    target_hi=2*beta_hi+F(11,5000)-bq_lo
    assert bquadratic(xp_lo,ypl_lo)<target_lo<target_hi<bquadratic(xp_hi,yph_hi)
    # P is strictly past the r0=r1 intersection, hence r0(P)<0.
    assert xp_lo>xb_hi
    out=io.StringIO(newline=''); writer=csv.writer(out,lineterminator='\n')
    writer.writerow(['case','bernstein_i','bernstein_j','exact_coefficient'])
    writer.writerows(rows)
    raw=out.getvalue().encode()
    return raw,summaries,(alo,ahi,xlo,xhi,xb_lo,xb_hi,yb_lo,yb_hi,beta_lo,beta_hi,xp_lo,xp_hi,ypl_lo,yph_hi,target_lo,target_hi)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--emit',type=Path);ap.add_argument('--verify',type=Path)
    args=ap.parse_args()
    raw,summaries,loc=check()
    if args.emit: args.emit.write_bytes(raw);assert args.emit.read_bytes()==raw
    if args.verify: assert args.verify.read_bytes()==raw
    print('STAGE381B_DOUBLE_R1_AND_Q_CUSP_EXACT_PASS')
    print('model=16_labels_4_independent_residual_channels; parent=Stage380B; frozen_inputs=unchanged')
    print('root_conditions=r1(P)=r1(Q)=0; budget=ACTIVE; yQ=(1+sqrt(13))/8')
    print('global_minimizer=unique_up_to_source_swap, conditional_on_inherited_Stage379_Stage380')
    print('exact_bernstein_sign_cases=4; coefficients=36; unresolved=0')
    for name,lo,hi in summaries:print(f'{name} bernstein_min={lo} bernstein_max={hi}')
    print('alpha_bracket='+','.join(map(str,loc[:2])))
    print('xQ_bracket='+','.join(map(str,loc[2:4])))
    print('beta_root_x_bracket='+','.join(map(str,loc[4:6])))
    print('beta_root_y_bracket='+','.join(map(str,loc[6:8])))
    print('beta_bracket='+','.join(map(str,loc[8:10])))
    print('xP_bracket='+','.join(map(str,loc[10:12])))
    print('yP_bracket='+','.join(map(str,loc[12:14])))
    print('budget_target_P_bracket='+','.join(map(str,loc[14:16])))
    print('certificate_bytes='+str(len(raw))+'; sha256='+sha256(raw).hexdigest())
if __name__=='__main__':main()
