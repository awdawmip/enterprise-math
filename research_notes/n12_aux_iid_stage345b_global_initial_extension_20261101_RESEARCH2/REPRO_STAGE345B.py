#!/usr/bin/env python3
"""Stage343-B exact rational/Bernstein certificate checker and reproduction.
All conclusions concern the declared tagged auxiliary Bernoulli observer.
Requires Python stdlib + sympy for independent derivative identities only.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from pathlib import Path
import csv, hashlib
import sympy as S

HERE=Path(__file__).resolve().parent
Q=F(501,100000)
E=F(3,2500)  # 0.0012
R=(F(2237,10000),F(235,1000),F(531,1000),F(626,1000))
W=(1,3,3,1); M=(61,21,9,9)
COEFS=((1,-3,3,-1),(0,3,-6,3),(0,0,3,-3),(0,0,0,1)) # weighted w_k B_k polynomials
POLYS={mask:tuple(sum(COEFS[k][i] for k in range(4) if (mask>>k)&1) for i in range(4)) for mask in range(1,16)}

def B(k,z):return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y):return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def D(a,z):return F(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))
def c(x,y):return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

@lru_cache(None)
def bezier_lower(mask,u,v):
    t=POLYS[mask]
    def val(z):return t[0]+z*(t[1]+z*(t[2]+z*t[3]))
    def der(z):return t[1]+z*(2*t[2]+3*t[3]*z)
    return min(val(u),val(u)+(v-u)*der(u)/3,val(v)-(v-u)*der(v)/3,val(v))

@lru_cache(None)
def lower_box(mask,a,b_,c_,d):
    mass=sum(W[k]*M[k] for k in range(4) if (mask>>k)&1)
    return F(5,16)*((4*bezier_lower(mask,a,b_)+bezier_lower(mask,c_,d))/5-F(mass,160))

def best(a,b_,c_,d):return max((lower_box(s,a,b_,c_,d),s) for s in range(1,16))

def generate():
    leaves=[]
    def recur(a,b_,c_,d,depth,path):
        if a>=R[0] and b_<=R[1] and c_>=R[2] and d<=R[3]:
            leaves.append((path,depth,'INNER',0,F(0),a,b_,c_,d));return
        lb,mask=best(a,b_,c_,d)
        if lb>Q:
            leaves.append((path,depth,'HIGH',mask,lb,a,b_,c_,d));return
        assert depth<22, ('certificate_limit',path,depth)
        ab=(a+b_)/2;cd=(c_+d)/2
        for j,(u,v,s,t) in enumerate(((a,ab,c_,cd),(ab,b_,c_,cd),(a,ab,cd,d),(ab,b_,cd,d))):
            recur(u,v,s,t,depth+1,path+str(j))
    recur(F(0),F(1),F(0),F(1),0,'')
    return leaves

def line(row):
    path,depth,kind,mask,lb,a,b_,c_,d=row
    return [path,depth,kind,mask,lb.numerator,lb.denominator,*[v for t in (a,b_,c_,d) for v in (t.numerator,t.denominator)]]

def verify_csv(leaves):
    path=HERE/'CERTIFICATE_STAGE345B.csv'
    with path.open(newline='',encoding='utf-8') as fh:
        reader=csv.reader(fh);hd=next(reader);rows=list(reader)
    assert len(hd)==14
    assert rows==[list(map(str,line(z))) for z in leaves]
    paths={z[0] for z in leaves}
    assert len(paths)==len(leaves)
    assert sum((z[6]-z[5])*(z[8]-z[7]) for z in leaves)==1
    for s in paths:
        for i in range(1,len(s)):
            assert s[:i] not in paths
    def full_tree(s):
        if s in paths:return
        assert any(t.startswith(s) for t in paths)
        for j in '0123':full_tree(s+j)
    full_tree('')
    for _,_,kind,mask,lb,a,b_,c_,d in leaves:
        if kind=='HIGH':assert lb==lower_box(mask,a,b_,c_,d)>Q
        else:assert kind=='INNER' and a>=R[0] and b_<=R[1] and c_>=R[2] and d<=R[3]
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tagged_signs():
    z=S.symbols('z');a_ref=(F(1,4),F(3,4))
    targets=[('x1',R[0],R[1],a_ref[0],'-+++'),('x3',R[0],R[1],a_ref[1],'--++'),('y1',R[2],R[3],a_ref[0],'++--'),('y3',R[2],R[3],a_ref[1],'--*+')]
    def bezier_values(expr,u,v):
        val=S.lambdify(z,expr,'sympy')
        poly=S.Poly(expr,z)
        def ev(t):return F(int(poly.nth(0)),1)+sum(F(int(poly.nth(i)),1)*t**i for i in range(1,4)) if all(x.q==1 for x in poly.all_coeffs()) else F(str(poly.eval(S.Rational(t.numerator,t.denominator))))
        # arbitrary rational coeff, use exact direct SymPy values
        def E(t):return F(poly.eval(S.Rational(t.numerator,t.denominator)))
        dpoly=poly.diff();h=v-u
        return (E(u),E(u)+h*F(dpoly.eval(S.Rational(u.numerator,u.denominator)))/3,E(v)-h*F(dpoly.eval(S.Rational(v.numerator,v.denominator)))/3,E(v))
    for name,u,v,a,word in targets:
        for k in range(4):
            if word[k]=='*':continue
            atom=S.Rational(a.numerator,a.denominator)**k*(1-S.Rational(a.numerator,a.denominator))**(3-k)-z**k*(1-z)**(3-k)
            coefs=bezier_values(atom,u,v)
            assert (min(coefs)>0) if word[k]=='+' else (max(coefs)<0),(name,k,coefs)
    assert S.factor(S.Rational(9,64)-z*z*(1-z))==(4*z-3)*(16*z*z-4*z-3)/64
    # complete sixteen signed contributions, separate the algebraic tag cusp
    x,y=S.symbols('x y')
    def atom(a,k,v):return a**k*(1-a)**(3-k)-v**k*(1-v)**(3-k)
    def grad(sign_y3):
        signs=['-+++','--++','++--','--'+sign_y3+'+']
        exprs=[]
        for (v,a,factor,sig) in ((x,S.Rational(1,4),63,signs[0]),(x,S.Rational(3,4),1,signs[1]),(y,S.Rational(1,4),9,signs[2]),(y,S.Rational(3,4),7,signs[3])):
            exprs.append(factor*S.Rational(1,2)*sum(W[k]*(1 if sig[k]=='+' else -1)*atom(a,k,v) for k in range(4)))
        return S.expand(sum(exprs)/256)
    below=grad('+');above=grad('-')
    px=(1-x)*(189-183*x)/256
    assert S.simplify(S.diff(below,x)+px)==0 and S.simplify(S.diff(above,x)+px)==0
    assert S.simplify(S.diff(below,y)-3*y*(1-y)/64)==0
    assert S.simplify(S.diff(above,y)-3*y*(18-25*y)/256)==0
    return True

def exact_inequalities():
    """All global rectangle/sign and low-budget brackets in exact rationals."""
    x0,x1,y0,y1=R
    assert r(2,x0,y0)>0  # B_2 increasing for every x,y in R
    p=lambda x:(1-x)*(189-183*x)/256
    assert p(x1)>F(43,100)
    cusp_lower=F(23,40)
    assert 13>F(18,5)**2  # y_dagger > 23/40
    q_high=lambda y:3*y*(18-25*y)/256
    assert 0<q_high(y1)<q_high(cusp_lower)<F(1,40)
    ratio_low=F(3,256)*4*(1-2*x0)/(2*y0-1)
    ratio_high=F(1,40)*4*(1-2*x0)/(2*cusp_lower-1)
    assert ratio_low<F(42,100)<F(43,100)<p(x1)
    assert ratio_high<F(37,100)<p(x1)
    # r3 >= 0 implies y > .612 and thus r1 < 0.
    assert r(3,x1,F(612,1000))<0 and r(1,x1,F(612,1000))<0
    f=lambda z:z*(2-3*z)/(1-z)**2
    assert f(x1)<f(y1)
    # Uniform r1-zero implicit slope Y1'<5 in the new rectangle.
    N=lambda x:4*(1-x)*(1-3*x)
    g=lambda y:(1-y)*(3*y-1)
    assert 0<N(x1) and N(x0)/g(y0)<5
    # r0=r3 unique crossing; same independent rational isolator as predecessor.
    xl=F(1133,5000);xh=F(567,2500)
    assert r(3,xl,F(616,1000))<0<r(3,xl,F(617,1000))
    assert r(3,xh,F(616,1000))<0<r(3,xh,F(617,1000))
    # On Y3(x): r3=0, Y3 in (.616,.617). Since r0 decreases in y,
    # r0(xl,Y3(xl)) > r0(xl,.617)>0;
    # r0(xh,Y3(xh)) < r0(xh,.616)<0.
    assert r(0,xl,F(617,1000))>0 and r(0,xh,F(616,1000))<0
    # d=(1,-14) lowers r0, r3, r2 at double zero in this isolating rectangle.
    xmax=xh; ymin=F(616,1000);ymax=F(618,1000)
    assert 2*(1-xmax)**2>7*(1-ymin)**2
    assert 2*xmax**2<7*ymin**2
    assert 4*xmax*(2-3*xmax)<14*ymax*(2-3*ymax)
    # q* bracket is independent of this E and can be checked by signed rational cells.
    qxl=F(231083,10**6);qxh=F(231085,10**6)
    assert r(0,qxl,F(555521,10**6))<0 and r(0,qxl,F(555520,10**6))>0
    assert r(0,qxh,F(555497,10**6))<0 and r(0,qxh,F(555496,10**6))>0
    assert r(1,qxl,F(555520,10**6))<0 and r(1,qxh,F(555497,10**6))>0
    beta_upper=F(15,16)*r(2,qxh,F(555521,10**6))
    assert beta_upper+E<Q
    # right-hand candidate Y1(x1) belongs to (.567,.568), beyond Q by x1.
    xx=x1;ya=F(567,1000);yb=F(568,1000)
    assert r(1,xx,ya)>0>r(1,xx,yb)
    assert r(0,xx,ya)<0 and r(3,xx,yb)<0
    assert F(15,16)*r(2,xx,ya)>Q
    # Positive y-derivative of r2; right endpoint's budget exceeds all s<=E.
    return beta_upper,ratio_low,ratio_high

def curvature_certificate():
    """Uniform exact interval bounds along r1=0, q* <= x <= right E endpoint."""
    xa,xb,ya,yb=F(231,1000),F(235,1000),F(555,1000),F(568,1000)
    N=lambda x:4*(1-x)*(1-3*x)
    g=lambda y:(1-y)*(3*y-1)
    yp_min=N(xb)/g(yb);yp_max=N(xa)/g(ya)
    yl=F(59,20);yu=F(16,5)
    assert yl<yp_min and yp_max<yu
    # Exact Y''=(4(6x-4)+(6Y-4)(Y')**2)/g(Y).
    H_upper=4*(6*xb-4)+(6*yb-4)*yl**2
    H_lower=4*(6*xa-4)+(6*ya-4)*yu**2
    assert H_upper/g(yb)<-51 and H_lower/g(ya)>-59
    # b''<-3, 0<b'<7/20, c'<-39/100, c''<9/8.
    bpp_upper=F(3,16)*(4*(2-6*xa)+(2-6*ya)*yl**2+yb*(2-3*yb)*(-51))
    assert bpp_upper<-3
    bp_upper=F(3,16)*(4*xb*(2-3*xb)+ya*(2-3*ya)*yu)
    assert bp_upper<F(7,20)
    p=lambda x:(1-x)*(189-183*x)/256
    cp_upper=-p(xb)+F(3,256)*yu
    assert cp_upper<-F(39,100)
    cpp_upper=(372-366*xa)/256
    assert cpp_upper<F(9,8)
    N_upper=F(9,8)*F(7,20)-F(39,100)*3
    assert N_upper==-F(621,800)<0
    return (yp_min,yp_max,H_upper/g(yb),H_lower/g(ya),bpp_upper,bp_upper,cp_upper,cpp_upper,N_upper)

def main():
    leaves=generate();sha=verify_csv(leaves);kinds=Counter(z[2] for z in leaves)
    assert len(leaves)==424 and kinds=={'HIGH':272,'INNER':152} and max(z[1] for z in leaves)==12
    assert tagged_signs()
    beta_upper,rl,rh=exact_inequalities()
    curv=curvature_certificate()
    print('GLOBAL_KNOWLEDGE_MAIN_PIN=9037e30aaa0d5c085d9700f1eb924e29496aecf1')
    print('ENTERPRISE_MATH_MAIN_PIN=4d349d63a10612d9e196f49791bd5946c6dd9bba')
    print('P000_SOURCE_BLOB=bcc2590d3168a28f72e8b9f0f9b1f76faadcd488')
    print('STAGE344_FRONTIER=50b38a08dfeb2a74064723ed0d5f59c3c2e4048c')
    print(f'CERTIFICATE_LEAVES={len(leaves)} HIGH={kinds["HIGH"]} INNER={kinds["INNER"]} MAX_DEPTH={max(z[1] for z in leaves)} AREA=1')
    print('CERTIFICATE_SHA256='+sha)
    print('BETA_UPPER='+str(beta_upper)+' E='+str(E)+' Q='+str(Q))
    print('DESCENT_RATIOS='+str(rl)+' / '+str(rh))
    print('CURVATURE_BOUNDS='+repr(tuple(map(str,curv))))
    print('STAGE345B_GLOBAL_E_0p0012_EXACT_BERNSTEIN_AND_CURVATURE_PASS')
if __name__=='__main__':main()
