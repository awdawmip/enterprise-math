"""Independent P11 audit. No author modules are imported or executed.

Standard Fraction arithmetic; SymPy only checks exact polynomial identities.
All infinite-family arguments are in AUDIT_PROOF.md, not inferred here.
"""
from fractions import Fraction as F
from math import gcd, isqrt, lcm
from functools import reduce
import json
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parent

def enc(v):
    if isinstance(v, F): return str(v)
    if isinstance(v, dict): return {k: enc(x) for k,x in v.items()}
    if isinstance(v, (tuple,list)): return [enc(x) for x in v]
    return v

def square_root(z):
    z=F(z)
    assert z>=0
    a,b=isqrt(z.numerator),isqrt(z.denominator)
    assert a*a==z.numerator and b*b==z.denominator
    return F(a,b)

def rhs(x,a,b): return x*(x-a)*(x-b)

def add(P,Q,a,b):
    if P is None: return Q
    if Q is None: return P
    x,y=P;z,w=Q
    if x==z and y==-w: return None
    slope=(3*x*x-2*(a+b)*x+a*b)/(2*y) if P==Q else (w-y)/(z-x)
    outx=slope*slope+(a+b)-x-z
    outy=slope*(x-outx)-y
    assert outy*outy==rhs(outx,a,b)
    return outx,outy

def multiple(n,P,a,b):
    R=None
    while n:
        if n&1: R=add(R,P,a,b)
        P=add(P,P,a,b);n//=2
    return R

def root_grid(h,d,t,e,discs):
    H=(h-d,h,h+d);T=(t-e,t,t+e)
    cells=[]
    for i,j in [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)]:
        disc=F(discs[(i,j)])
        pair=((H[i]+disc)/2,(H[i]-disc)/2)
        assert pair[0]+pair[1]==H[i]
        assert pair[0]*pair[1]==T[j]
        cells.append({'cell':[i,j],'discriminant':disc,'roots':pair})
    return H,T,cells

def flatten(cells): return [r for c in cells for r in c['roots']]

def primitive(h,d,t,e,discs):
    H,T,cells=root_grid(h,d,t,e,discs)
    roots=flatten(cells);D=lcm(*(r.denominator for r in roots))
    ints=[int(D*r) for r in roots]
    g=reduce(gcd,ints,0);assert g>0
    scale=F(D,g)
    HH,TT,cc=root_grid(scale*h,scale*d,scale*scale*t,scale*scale*e,{k:scale*v for k,v in discs.items()})
    assert all(x.denominator==1 for x in HH+TT+tuple(flatten(cc)))
    assert reduce(gcd,(int(x) for x in flatten(cc)),0)==1
    assert HH[1]-HH[0]==HH[2]-HH[1]>0
    assert TT[1]-TT[0]==TT[2]-TT[1]>0
    return {'lcm':D,'gcd_before':g,'scale':scale,'H':HH,'T':TT,'cells':cc}

def diagonal(n):
    p,q=F(233),F(119);R=p*q
    point=multiple(n,(F(194089),F(69872040)),p*p,q*q)
    xi,eta=point
    T=(p+q)*(xi-R)/(xi+R)
    YY=4*(p+q)*R*eta/(xi+R)**2
    d=YY/(2*T);u=(T+(p*p-q*q)/T)/2;v=(T-(p*p-q*q)/T)/2
    assert d*d+u*u==p*p and d*d+v*v==q*q
    assert 0<abs(d)<q and u*v!=0
    assert (R*((p+q)+T)/((p+q)-T),(p+q)*R*YY/((p+q)-T)**2)==point
    d0,u0,v0=abs(d),abs(u),abs(v)
    k0=2*lcm(d0.denominator,u0.denominator,v0.denominator)
    a,b,c=F(233*k0),F(185*k0),F(119*k0)
    dd,mu,nu=k0*d0,k0*u0,k0*v0
    h=F(0);t=(dd*dd-b*b)/4;e=F(176*57*k0*k0,2)
    discs={(0,0):a,(0,1):b,(0,2):c,(1,0):mu,(1,2):nu,(2,0):a,(2,1):b,(2,2):c}
    HH,TT,cc=root_grid(h,dd,t,e,discs)
    rr=flatten(cc);assert all(r.denominator==1 for r in rr)
    g=reduce(gcd,(int(r) for r in rr),0);assert k0%g==0
    final=primitive(h,dd,t,e,discs)
    assert final['scale']==F(1,g)
    final_scale=F(k0,g)
    assert final['H'][2]/final_scale==d0
    six=(F(176*k0,g),F(57*k0,g),F(185*k0,g),dd/g,mu/g,nu/g)
    assert all(z.denominator==1 for z in six)
    naive_gcd=reduce(gcd,(int(z) for z in six),0)
    return {'n':n,'point':point,'signed_fiber':(d,u,v),'initial_scale':k0,'root_gcd':g,'final_scale':final_scale,'primitive_six':six,'six_coordinate_gcd':naive_gcd,**final}

def offdiagonal(n):
    point=multiple(n,(F(9),F(2112)),F(1945),F(265))
    u,v=point;d=square_root(u);mu=square_root(1945-u);nu=square_root(265-u)
    assert d*mu*nu==abs(v) and 0<d and u<265
    h=132/d;t=((h-d)**2-841)/4;e=F(210)
    discs={(0,0):F(41),(0,1):F(29),(0,2):F(1),(1,0):mu,(1,2):nu,(2,0):F(47),(2,1):F(37),(2,2):F(23)}
    out=primitive(h,d,t,e,discs);assert out['gcd_before']==1
    D=out['lcm'];p,q=d.numerator,d.denominator;r=q*mu;s=q*nu
    assert r.denominator==s.denominator==1 and q%2==1
    if p%2: assert int(r)%4==int(s)%4==0
    else: assert p%4==0 and int(r)%2==int(s)%2==1
    nums=[]
    for z in (41,29,1):nums.extend((132*q*q-p*p+z*p*q,132*q*q-p*p-z*p*q))
    for z in (int(r),int(s)):nums.extend((132*q*q+z*p,132*q*q-z*p))
    for z in (47,37,23):nums.extend((132*q*q+p*p+z*p*q,132*q*q+p*p-z*p*q))
    G=reduce(gcd,nums,0)
    v2=(p&-p).bit_length()-1
    expected_g=gcd(p,33)*(2 if p%2 else (8 if v2==2 else 4))
    assert G==expected_g and D==2*p*q//G
    formula=p*q//gcd(p,132)*(2 if v2>=3 else 1)
    assert D==formula
    # Factor swap preserves the same grid after reversing both rows and root signs.
    swapped={(0,j):discs[(2,j)] for j in (0,1,2)}
    swapped.update({(2,j):discs[(0,j)] for j in (0,1,2)})
    swapped.update({(1,0):mu,(1,2):nu})
    sh,st,sc=root_grid(-h,d,t,e,swapped)
    for old,new in zip(sorted(flatten(root_grid(h,d,t,e,discs)[2])),sorted(-z for z in flatten(sc))):assert old==new
    assert out['H'][2]-out['H'][0]==2*D*d
    assert out['cells'][1]['discriminant']==29*D
    return {'n':n,'point':point,'d':d,'mu':mu,'nu':nu,'h':h,'t':t,'denominator_gcd':G,'denominator_formula':formula,'root_step_ratio':d/29,**out}

def symbolic_checks():
    p,q,x,y=S.symbols('p q x y',nonzero=True)
    a=p+q;R=p*q;f=x*(x-p*p)*(x-q*q)
    T=a*(x-R)/(x+R);YY=4*a*R*y/(x+R)**2
    d=YY/(2*T);U=(T+(p*p-q*q)/T)/2;V=(T-(p*p-q*q)/T)/2
    checks={}
    def zero(label,expr):
        num=S.together(expr).as_numer_denom()[0]
        rem=S.rem(S.Poly(S.expand(num),y),S.Poly(y*y-f,y)).as_expr()
        assert S.factor(rem)==0,label;checks[label]=True
    zero('diagonal_first_quadric',d*d+U*U-p*p)
    zero('diagonal_second_quadric',d*d+V*V-q*q)
    zero('diagonal_inverse_forward_x',R*(a+T)/(a-T)-x)
    zero('diagonal_inverse_forward_y',a*R*YY/(a-T)**2-y)
    zero('quartic_identity',YY*YY-(a*a-T*T)*(T*T-(p-q)**2))
    ss=p*p+q*q;kk=p*p*q*q
    psi3=3*x**4-4*ss*x**3+6*kk*x*x-kk*kk
    zero('division_polynomial',S.diff(f,x)**2-4*f*(3*x-ss)+psi3)
    X=9*x-3*ss;Y=27*y
    zero('short_weierstrass',Y*Y-X**3-27*(3*kk-ss*ss)*X-27*(9*kk*ss-2*ss**3))
    zero('cut_map_same_cubic', (d*U*V)**2-d*d*(d*d-p*p)*(d*d-q*q))
    # Generic chord identity, including a repeated root for a tangent.
    aa,cc,ell,beta,z=S.symbols('A C ell beta z')
    cubic=z*(z-aa)*(z-cc);line=ell*z+beta
    for root in (S.Integer(0),aa,cc):
        assert S.expand((cubic-line*line).subs(z,root)+(ell*root+beta)**2)==0
    checks['offdiagonal_chord_evaluation_for_all_three_roots']=True
    # Direct inherited simultaneous normal form, proved from cell discriminants.
    h,ds,b2,e,K=S.symbols('h ds b2 e K',nonzero=True)
    t=((h-ds)**2-b2)/4
    assert S.expand((h+ds)**2-4*t-b2-4*h*ds)==0
    assert S.expand(h*h-4*(t-e)-(b2-ds*ds+2*h*ds+4*e))==0
    assert S.expand(h*h-4*(t+e)-(b2-ds*ds+2*h*ds-4*e))==0
    checks['normal_form_row_coupling_and_middle_cuts']=True
    return checks

def finite_certificates():
    out={}
    for label,a,b,point,prime in [('diagonal',233**2,119**2,(194089,69872040),5),('offdiagonal',1945,265,(9,2112),11)]:
        x,y=point;disc=a*a*b*b*(a-b)**2
        assert y*y==rhs(x,a,b) and y%prime==0 and disc%prime!=0
        count=1+sum(sum(v*v%prime==rhs(u,a,b)%prime for v in range(prime)) for u in range(prime))
        twice=add(tuple(map(F,point)),tuple(map(F,point)),F(a),F(b))
        out[label]={'prime':prime,'cubic_discriminant_mod_prime':disc%prime,'seed_y_mod_prime':y%prime,'good_reduction_point_count':count,'double':twice}
    assert out['diagonal']['good_reduction_point_count']==8
    candidates={}
    for column,target,pairs in [('left',210,(41,47)),('middle',0,(29,37)),('right',-210,(1,23))]:
        cand=set()
        for eps in (-1,1):
            for eta in (-1,1):
                d=F(eta*pairs[1]-eps*pairs[0],2)
                if d>0:cand.add(d)
        valid=[]
        for d in sorted(cand):
            try:
                mu=square_root(1945-d*d);nu=square_root(265-d*d)
            except AssertionError: continue
            h=132/d;t=((h-d)**2-841)/4
            assert t==target
            valid.append({'d':d,'mu':mu,'nu':nu})
        candidates[column]={'candidates':sorted(cand),'valid':valid}
    assert candidates['left']['valid']==[{'d':F(3),'mu':F(44),'nu':F(16)}]
    assert not candidates['middle']['valid'] and not candidates['right']['valid']
    out['fixed_core_zero_columns']=candidates
    return out

if __name__=='__main__':
    result={'schema':'P11_INDEPENDENT_AUDIT_CHECKS_V1','author_code_imported':False,'finite_checks_are_not_universal_proof':True,'symbolic':symbolic_checks(),'finite_certificates':finite_certificates(),'diagonal':[diagonal(n) for n in range(1,9)],'offdiagonal':[offdiagonal(n) for n in range(1,14,2)]}
    assert len({r['root_step_ratio'] for r in result['offdiagonal']})==7
    assert result['diagonal'][1]['six_coordinate_gcd']==2
    (ROOT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(enc(result),indent=2)+'\n')
    print(json.dumps({'status':'PASS','symbolic_identity_count':len(result['symbolic']),'diagonal_multipliers':list(range(1,9)),'offdiagonal_multipliers':list(range(1,14,2)),'author_code_imported':False,'output':'INDEPENDENT_CHECKS.json'}))
