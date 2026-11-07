#!/usr/bin/env python3
"""Stage346-B rigorous Fraction/Bernstein proof checker (typed 16-tag auxiliary BRC observer).

No Monte Carlo or floating point is used. The two CSV certificates describe complete
rational quadtree coverings, and are regenerated and compared byte-for-byte.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from pathlib import Path
import hashlib, csv
import sympy as S

HERE=Path(__file__).resolve().parent
Q=F(21,4000)  # .00525
E=F(7,5000)  # .0014
R=(F(445,2000),F(473,2000),F(21,40),F(63,100))
LOW_SPLIT=F(531,1000)
CUTOFF=F(3149,100000)  # c>0.03149 on the low-y strip at b<=Q
W=(1,3,3,1); M=(61,21,9,9)
COEFS=((1,-3,3,-1),(0,3,-6,3),(0,0,3,-3),(0,0,0,1))
POLYS={mask:tuple(sum(COEFS[k][i] for k in range(4) if (mask>>k)&1) for i in range(4)) for mask in range(1,16)}

def B(k,z):return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y):return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def D(a,z):return F(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))
def c(x,y):return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

def val(coeffs,z):return sum(t*z**i for i,t in enumerate(coeffs))
def bernstein_controls(coeffs,u,v):
    def der(z):return sum(i*t*z**(i-1) for i,t in enumerate(coeffs) if i)
    return (val(coeffs,u),val(coeffs,u)+(v-u)*der(u)/3,val(coeffs,v)-(v-u)*der(v)/3,val(coeffs,v))

@lru_cache(None)
def bezier_lower(mask,u,v):return min(bernstein_controls(POLYS[mask],u,v))
@lru_cache(None)
def lower_box(mask,a,b_,c_,d):
    mass=sum(W[k]*M[k] for k in range(4) if (mask>>k)&1)
    return F(5,16)*((4*bezier_lower(mask,a,b_)+bezier_lower(mask,c_,d))/5-F(mass,160))
def best(a,b_,c_,d):return max((lower_box(s,a,b_,c_,d),s) for s in range(1,16))

# Entire low-y strip is below y-dagger, hence its 16 tagged signs are fixed;
# c(x,y)=K+(-189x+186x^2-61x^3)/256+(3y^2-2y^3)/128.
CX=(F(0),-F(189,256),F(186,256),-F(61,256))
CY=(F(0),F(0),F(3,128),-F(1,64))
K=c(F(23,100),F(53,100))-val(CX,F(23,100))-val(CY,F(53,100))
assert K+val(CX,F(233,1000))+val(CY,F(528,1000))==c(F(233,1000),F(528,1000))

def lower_audit(a,b_,c_,d):
    return K+min(bernstein_controls(CX,a,b_))+min(bernstein_controls(CY,c_,d))

FIELDS=['path','depth','kind','mask','lb_num','lb_den','xlo_num','xlo_den','xhi_num','xhi_den','ylo_num','ylo_den','yhi_num','yhi_den']

def generate_global():
    leaves=[]
    def recur(a,b_,c_,d,depth,path):
        if a>=R[0] and b_<=R[1] and c_>=R[2] and d<=R[3]:
            leaves.append((path,depth,'INNER',0,F(0),a,b_,c_,d));return
        lb,mask=best(a,b_,c_,d)
        if lb>Q:
            leaves.append((path,depth,'HIGH_B',mask,lb,a,b_,c_,d));return
        assert depth<21,('global unresolved',path,depth)
        xm=(a+b_)/2;ym=(c_+d)/2
        for j,(aa,bb,cc,dd) in enumerate(((a,xm,c_,ym),(xm,b_,c_,ym),(a,xm,ym,d),(xm,b_,ym,d))):
            recur(aa,bb,cc,dd,depth+1,path+str(j))
    recur(F(0),F(1),F(0),F(1),0,'')
    return leaves

def generate_low_strip():
    leaves=[]
    def recur(a,b_,c_,d,depth,path):
        lb,mask=best(a,b_,c_,d)
        if lb>Q:
            leaves.append((path,depth,'HIGH_B',mask,lb,a,b_,c_,d));return
        cl=lower_audit(a,b_,c_,d)
        if cl>CUTOFF:
            leaves.append((path,depth,'HIGH_C',0,cl,a,b_,c_,d));return
        assert depth<23,('strip unresolved',path,depth,lb,cl)
        xm=(a+b_)/2;ym=(c_+d)/2
        for j,(aa,bb,cc,dd) in enumerate(((a,xm,c_,ym),(xm,b_,c_,ym),(a,xm,ym,d),(xm,b_,ym,d))):
            recur(aa,bb,cc,dd,depth+1,path+str(j))
    recur(R[0],R[1],R[2],LOW_SPLIT,0,'')
    return leaves

def line(row):
    path,depth,kind,mask,lb,a,b_,c_,d=row
    return [path,depth,kind,mask,lb.numerator,lb.denominator,*[v for t in (a,b_,c_,d) for v in (t.numerator,t.denominator)]]

def verify_csv(fname,leaves,area):
    path=HERE/fname
    with path.open(newline='',encoding='utf-8') as f:
        reader=csv.reader(f);hd=next(reader);rows=list(reader)
    assert hd==FIELDS
    assert rows==[list(map(str,line(z))) for z in leaves]
    paths={z[0] for z in leaves}
    assert len(paths)==len(leaves)
    assert sum((z[6]-z[5])*(z[8]-z[7]) for z in leaves)==area
    for s in paths:
        for i in range(1,len(s)):assert s[:i] not in paths
    def full(s):
        if s in paths:return
        assert any(p.startswith(s) for p in paths)
        for j in '0123':full(s+j)
    full('')
    for _,_,kind,mask,lb,a,b_,c_,d in leaves:
        if kind=='HIGH_B':assert lb==lower_box(mask,a,b_,c_,d)>Q
        elif kind=='HIGH_C':assert lb==lower_audit(a,b_,c_,d)>CUTOFF
        else:assert kind=='INNER' and a>=R[0] and b_<=R[1] and c_>=R[2] and d<=R[3]
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tagged_signs():
    z=S.symbols('z')
    targets=[('x1',R[0],R[1],F(1,4),'-+++'),('x3',R[0],R[1],F(3,4),'--++'),('y1',R[2],R[3],F(1,4),'++--'),('y3',R[2],R[3],F(3,4),'--*+')]
    for name,u,v,a,word in targets:
        for k in range(4):
            if word[k]=='*':continue
            atom=S.Rational(a.numerator,a.denominator)**k*(1-S.Rational(a.numerator,a.denominator))**(3-k)-z**k*(1-z)**(3-k)
            poly=S.Poly(atom,z)
            coeffs=tuple(F(poly.nth(i)) for i in range(4))
            vals=bernstein_controls(coeffs,u,v)
            assert (min(vals)>0) if word[k]=='+' else (max(vals)<0),(name,k,vals)
    assert S.factor(S.Rational(9,64)-z*z*(1-z))==(4*z-3)*(16*z*z-4*z-3)/64
    x,y=S.symbols('x y')
    def atom(a,k,v):return a**k*(1-a)**(3-k)-v**k*(1-v)**(3-k)
    for sg,expected in [('+',3*y*(1-y)/64),('-',3*y*(18-25*y)/256)]:
        signs=['-+++','--++','++--','--'+sg+'+']
        expr=0
        for v,a,factor,sign in ((x,S.Rational(1,4),63,signs[0]),(x,S.Rational(3,4),1,signs[1]),(y,S.Rational(1,4),9,signs[2]),(y,S.Rational(3,4),7,signs[3])):
            expr+=factor*S.Rational(1,2)*sum(W[k]*(1 if sign[k]=='+' else -1)*atom(a,k,v) for k in range(4))
        expr=S.expand(expr/256)
        assert S.simplify(S.diff(expr,x)+(1-x)*(189-183*x)/256)==0
        assert S.simplify(S.diff(expr,y)-expected)==0
        if sg=='+':
            assert S.simplify(expr-(S.Rational(K.numerator,K.denominator)+sum(S.Rational(q.numerator,q.denominator)*x**i for i,q in enumerate(CX))+sum(S.Rational(q.numerator,q.denominator)*y**i for i,q in enumerate(CY))))==0
    return True

def exact_inequalities():
    x0,x1,y0,y1=R
    assert r(2,x0,y0)>0
    p=lambda x:(1-x)*(189-183*x)/256
    assert p(x1)>F(43,100)
    assert 13>F(18,5)**2 # y_dagger > 23/40
    q_high=lambda y:3*y*(18-25*y)/256
    assert 0<q_high(y1)<q_high(F(23,40))<F(1,40)
    ratio_low=F(3,256)*4*(1-2*x0)/(2*LOW_SPLIT-1)
    ratio_high=F(1,40)*4*(1-2*x0)/(2*F(23,40)-1)
    assert ratio_low<F(42,100)<F(43,100)<p(x1)
    assert ratio_high==F(37,100)<F(43,100)<p(x1)
    assert r(3,x1,F(610,1000))<0 and r(1,x1,F(610,1000))<0
    f=lambda z:z*(2-3*z)/(1-z)**2
    assert f(F(231085,10**6))<f(F(3,5))
    assert r(0,F(228,1000),F(3,5))<0
    assert f(F(228,1000))<f(y1)
    N=lambda x:4*(1-x)*(1-3*x)
    g=lambda y:(1-y)*(3*y-1)
    assert 0<N(x1) and N(x0)/g(y0)<5
    xl=F(1133,5000);xh=F(567,2500)
    assert r(3,xl,F(616,1000))<0<r(3,xl,F(617,1000))
    assert r(3,xh,F(616,1000))<0<r(3,xh,F(617,1000))
    assert r(0,xl,F(617,1000))>0 and r(0,xh,F(616,1000))<0
    assert 2*(1-xh)**2>7*(1-F(616,1000))**2
    assert 2*xh**2<7*F(616,1000)**2
    assert 4*xh*(2-3*xh)<14*F(618,1000)*(2-3*F(618,1000))
    # Narrow q* isolator on Y0(x): each endpoint has rational Y0-root brackets.
    qxl=F(2310839408,10**10);qxh=F(2310839409,10**10)
    yll=F(5555088575,10**10);ylh=F(5555088580,10**10)
    yhl=F(5555088565,10**10);yhh=F(5555088570,10**10)
    assert r(0,qxl,yll)>0>r(0,qxl,ylh)
    assert r(1,qxl,yll)<0
    assert r(0,qxh,yhl)>0>r(0,qxh,yhh)
    assert r(1,qxh,yhh)>0
    # Implicit Y0 is decreasing; r1 on it is strictly increasing (proven in text).
    qyl=F(555508855,10**9); qyh=F(555508860,10**9)
    assert r(0,qxh,qyl)>0 and r(0,qxl,qyh)<0
    beta_lo=F(15,16)*r(2,qxl,qyl)
    beta_up=F(15,16)*r(2,qxh,qyh)
    assert beta_lo<beta_up and beta_up+E<Q
    # q_E is strictly between .2353 and .2355, in the y<.570 arc.
    xa=F(2353,10000);ya=F(5684,10000);yb=F(5685,10000)
    assert r(1,xa,ya)>0>r(1,xa,yb)
    assert F(15,16)*r(2,xa,yb)<beta_lo+E
    xb=F(2355,10000); ylo=F(569,1000); yhi=F(5691,10000)
    assert r(1,xb,ylo)>0>r(1,xb,yhi)
    assert F(15,16)*r(2,xb,ylo)>beta_up+E
    # At s0=.0012, the existing right branch already beats the low-y certificate cutoff;
    # for s>=s0, strictly decreasing candidate c makes the same barrier valid.
    s0=F(3,2500)
    xoldlo=F(234719,10**6); xoldhi=F(234722,10**6)
    yoldlo=F(566715,10**6);yoldhi=F(566719,10**6)
    yhi_oldlo=F(566723,10**6);yhi_oldhi=F(566725,10**6)
    assert r(1,xoldlo,yoldlo)>0>r(1,xoldlo,yoldhi)
    assert F(15,16)*r(2,xoldlo,yoldhi)<beta_lo+s0
    assert r(1,xoldhi,yhi_oldlo)>0>r(1,xoldhi,yhi_oldhi)
    assert F(15,16)*r(2,xoldhi,yhi_oldlo)>beta_up+s0
    assert c(xoldlo,yhi_oldhi)<CUTOFF
    assert c(xa,yhi)<CUTOFF # stronger E-endpoint sanity; only s0 bound is needed
    return beta_lo,beta_up,ratio_low,ratio_high

def curvature_certificate():
    xa,xb,ya,yb=F(231,1000),F(236,1000),F(555,1000),F(570,1000)
    N=lambda x:4*(1-x)*(1-3*x)
    g=lambda y:(1-y)*(3*y-1)
    yp_min=N(xb)/g(yb);yp_max=N(xa)/g(ya)
    yl=F(29,10);yu=F(33,10)
    assert yl<yp_min and yp_max<yu
    H_upper=4*(6*xb-4)+(6*yb-4)*yl**2
    H_lower=4*(6*xa-4)+(6*ya-4)*yu**2
    # Y''=H/g, g positive; account for sign of H
    ypp_upper=H_upper/g(yb)
    ypp_lower=H_lower/g(ya)
    assert ypp_lower<ypp_upper<0
    # b'', b', c', c'' from exact formula; elementary monotonicity in box.
    bpp_upper=F(3,16)*(4*(2-6*xa)+(2-6*ya)*yl**2+yb*(2-3*yb)*ypp_upper)
    bp_upper=F(3,16)*(4*xb*(2-3*xb)+ya*(2-3*ya)*yu)
    p=lambda x:(1-x)*(189-183*x)/256
    cp_upper=-p(xb)+F(3,256)*yu
    cpp_upper=(372-366*xa)/256
    assert bpp_upper<0 and 0<bp_upper and cp_upper<0 and cpp_upper>0
    # exact quantitative negative curvature
    bound=cpp_upper*bp_upper+cp_upper*(-bpp_upper) # c''b' - c'b'', upper for c'<0, b''<0
    assert bound<0
    # Verify positivity b' at every parameter from monotone positivity of x(2-3x),y(2-3y),Y'
    assert xa>0 and xb<F(1,3) and ya>0 and yb<F(2,3)
    return (yp_min,yp_max,ypp_lower,ypp_upper,bpp_upper,bp_upper,cp_upper,cpp_upper,bound)

def main():
    global_leaves=generate_global();strip_leaves=generate_low_strip()
    sha_global=verify_csv('CERTIFICATE_STAGE346B_GLOBAL.csv',global_leaves,F(1))
    sha_strip=verify_csv('CERTIFICATE_STAGE346B_LOW_STRIP.csv',strip_leaves,(R[1]-R[0])*(LOW_SPLIT-R[2]))
    assert tagged_signs()
    beta_lo,beta_up,rl,rh=exact_inequalities()
    curv=curvature_certificate()
    print('GLOBAL_KNOWLEDGE_V1_FROZEN_MAIN=b33cf2f18b4fbfd428312f384310cb2601c68a79')
    print('ENTERPRISE_MATH_MAIN_FROZEN=ce7279d4cafc8d7ddb4a65d75c33e8c40849428c')
    print('P000_SOURCE_BLOB=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc')
    for name,leaves,sha in [('GLOBAL',global_leaves,sha_global),('LOW_STRIP',strip_leaves,sha_strip)]:
        cnt=Counter(z[2] for z in leaves)
        print(f'{name}_CERTIFICATE_LEAVES={len(leaves)} COUNTS={dict(cnt)} DEPTH={max(z[1] for z in leaves)} SHA256={sha}')
    print('Q='+str(Q)+' E='+str(E)+' R='+repr(tuple(map(str,R))))
    print('BETA_INTERVAL='+str(beta_lo)+' .. '+str(beta_up))
    print('DESCENT_RATIOS='+str(rl)+' / '+str(rh))
    print('CURVATURE_BOUNDS='+repr(tuple(map(str,curv))))
    print('STAGE346B_GLOBAL_E_0p0014_WITH_LOW_STRIP_AUDIT_BARRIER_EXACT_PASS')
if __name__=='__main__':main()
