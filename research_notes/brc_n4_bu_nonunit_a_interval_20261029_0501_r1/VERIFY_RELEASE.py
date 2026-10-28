"""Exact BRC N4 BU provenance-bit minimax interval certificate; SymPy required."""
import sympy as S
x,c,A,B,U,V=S.symbols('x c A B U V',real=True)
b=S.Rational(1,40)
C=(S.sqrt(40521)-131)/80
L=1-3*b*C/(4+C)
f=(x+3*b)*c*c+(3*x+8*b)*c+14*b-4*x
assert S.simplify(f.subs({x:L,c:C}))==0
assert S.Rational(3,4)<C<S.Rational(9,10) and S.Rational(1,2)<L<1
s=(A-x+B-b)/2;t=(A-x+3*(B-b))/4;H=B*c/4
q=x/6-A*c/6-U/3-V/4;p=x/6-A*c/6-U/12-V/2
Q2=H-s-q;Q3=H-q;P4=p;P5=t+p;P6=H-t
al=(c+4)/(23-2*c);be=(3-7*c)/(23-2*c)
ga=2*(1+4*c-c*c)/(23-2*c);et=2*(c*c-2*c+7)/(23-2*c)
w=[7*(1-c)/20,(7*c-3)/20,(3*c+1)/10,(7-3*c)/10]
y=[c/(7-2*c),7*(1-c)/(7-2*c),2*c*(2-c)/(7-2*c),2*c*c/(7-2*c)]
z=[c/(4+c),2*(2-c)/(4+c),2*c/(4+c)]
cert=[
 ((al*Q2+be*(H-s)+ga*P4+et*P5+7*al*(V-B)/4),
  (4*x-14*b-3*x*c-(x+3*b)*c*c)/(2*(23-2*c)),[al,be,ga,et]),
 (w[0]*Q2+w[1]*Q3+w[2]*P4+w[3]*P5+S.Rational(7,20)*(V-B),
  (2*x-7*b-(2*x-b)*c)/20,w),
 (y[0]*Q3+y[1]*H+y[2]*P4+y[3]*P5+7*c*(V-B)/(4*(7-2*c)),
  c*(x-(x+3*b)*c)/(2*(7-2*c)),y),
 (z[0]*s+z[1]*H+z[2]*P6,b*c/(4+c),z)]
for lhs,rhs,weights in cert:
    assert S.cancel(lhs-rhs)==0 and S.cancel(sum(weights)-1)==0
assert S.Rational(1767,90160)>b/5
assert S.Rational(3,640)>9*b/49
assert S.simplify((7*x-14*(x+3*b)*c+2*(x+3*b)*c*c).subs(c,S.Rational(3,4)))==-(19*x+225*b)/8
# Sixteen strictly positive leaves: (root,prefix,Q mass,P/Q ratio).
leaves=[]
for root,ps in [('A',[('AU',S.Rational(1,6),[S.Rational(9,10),S.Rational(11,10)]),
                          ('AV',S.Rational(1,3),[S.Rational(1,4)]*2)]),
                ('B',[('BU',S.Rational(1,4),[S.Rational(1,5),S.Rational(9,5)]),
                          ('BV',S.Rational(1,4),[S.Integer(2)]*2)])]:
    for prefix,qmass,ratios in ps:
        for ratio in ratios:
            for _ in range(2): leaves.append((root,prefix,qmass/4,ratio))
assert len(leaves)==16 and sum(v[2] for v in leaves)==1
assert sum(v[2]*v[3] for v in leaves)==1
assert all(v[2]>0 and v[3]>0 for v in leaves)
for aa in [S.Rational(1,2),S.Rational(3,4),S.Rational(19,20),L]:
    cc=C if aa==L else next(v for v in S.solve(f.subs(x,aa),c) if v.is_real and v>0)
    ee=b*cc/(4+cc);AA=aa+3*ee;BB=b-ee;UU=BB*(1+cc)
    assert S.simplify(f.subs({x:aa,c:cc}))==0
    assert 0<BB and AA<=1 and 0<=UU/AA<=1
    for law in ('Q','P'):
        target=[S.Integer(0)]*4;candidate=[S.Integer(0)]*4
        for root,prefix,qmass,ratio in leaves:
            weight=qmass if law=='Q' else qmass*ratio
            rt=aa if root=='A' else b;ct=S.Integer(1) if prefix=='AU' else S.Integer(0)
            target[0]+=weight*(1-rt);target[1]+=weight*rt*(1-ct);target[2]+=weight*rt*ct
            rg=AA if root=='A' else BB
            cg=cc if prefix in ('AU','BU') else (UU/AA if prefix=='AV' else S.Integer(1))
            candidate[0]+=weight*(1-rg);candidate[1]+=weight*rg*(1-cg)
            candidate[3 if prefix=='BU' else 2]+=weight*rg*cg
        wanted=[ee,0,0,-ee] if law=='Q' else [0,0,ee,-ee]
        assert all(S.simplify(u-v-w)==0 for u,v,w in zip(target,candidate,wanted))
print('PASS_EXACT_BU_BIT_NONUNIT_A_INTERVAL; leaf_count=16; algebraic_a_points=4; symbolic_duals=4')
print('alpha=',S.N(L,20),' c_alpha=',S.N(C,20))
