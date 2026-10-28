"""Exact symbolic certificate check; not an independent review or full all-real proof."""
import sympy as S
a,A,B,U,V,c=S.symbols("a A B U V c",real=True)
b=S.Rational(1,40)
alpha=(S.sqrt(40521)-4)/200
C=(S.sqrt(40521)-131)/80
cp=(259-40*a)/(4*(40*a+23))
eps=(40*a-37)*(259-40*a)/(1920*(40*a+23))
s=(A-a+B-b)/2;t=(A-a+3*(B-b))/4;H=B*c/4
rq=a/6-A*c/6-U/3-V/4
rp=a/6-A*c/6-U/12-V/2
Q2=H-s-rq;Q3=H-rq;Q7=H;P4=rp;P5=t+rp;P6=H-t
p=(c+4)/(23-2*c);q=(3-7*c)/(23-2*c)
r=2*(1+4*c-c*c)/(23-2*c)
u=2*(c*c-2*c+7)/(23-2*c)
L1=(4*a-14*b-3*a*c-(a+3*b)*c*c)/(2*(23-2*c))
assert S.simplify(p*Q2+q*(H-s)+r*P4+u*P5+7*p*(V-B)/4-L1)==0
assert S.simplify(p+q+r+u-1)==0
w1=7*(1-c)/20;w2=(7*c-3)/20;w3=(3*c+1)/10;w4=(7-3*c)/10
L2=(2*a-7*b-(2*a-b)*c)/20
assert S.simplify(w1*Q2+w2*Q3+w3*P4+w4*P5+S.Rational(7,20)*(V-B)-L2)==0
assert S.simplify(w1+w2+w3+w4-1)==0
l1=c/(7-2*c);l2=7*(1-c)/(7-2*c)
l3=2*c*(2-c)/(7-2*c);l4=2*c*c/(7-2*c)
mu=7*c/(4*(7-2*c))
L3=c*(a-(a+3*b)*c)/(2*(7-2*c))
assert S.simplify(l1*Q3+l2*Q7+l3*P4+l4*P5+mu*(V-B)-L3)==0
assert S.simplify(l1+l2+l3+l4-1)==0
R=c*(a+3*b-1)/12
assert S.simplify((1-c/3)*Q7+(c/3)*P6-R-c*(1-A)/12)==0
assert S.simplify(L3.subs(c,cp)-R.subs(c,cp))==0
assert S.simplify(R.subs(c,cp)-eps)==0
assert S.simplify(cp.subs(a,alpha)-C)==0
assert S.simplify(cp.subs(a,1)-S.Rational(73,84))==0
Bs=(a+3*b-1)/3
sub={A:1,B:Bs,U:Bs*(1+cp),V:Bs,c:cp}
assert S.simplify(s.subs(sub)-(1-a)/3)==0
assert S.simplify(t.subs(sub))==0
assert S.simplify(H.subs(sub)-eps)==0
assert S.simplify(rq.subs(sub))==0
assert S.simplify(rp.subs(sub)-eps)==0
assert S.simplify((H-s).subs(sub)-(8000*a*a+320*a-8101)/(640*(40*a+23)))==0
print("PASS_SYMBOLIC_N4_BU_UPPER_CAPACITY_RELEASE")
print("a=1 gives epsilon="+str(S.factor(eps.subs(a,1))))
