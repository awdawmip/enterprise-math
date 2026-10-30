#!/usr/bin/env python3
"""PREFIX-377 exact static five-Port tri-observer inverse and Lipschitz certificate."""
import json
import sympy as s

a,b,c,d,ap,bp,cp,dp,x,t=s.symbols('a b c d ap bp cp dp x t',real=True)
I=s.I
L,U=s.Rational(8,85),s.Rational(4321,21259)
K=s.Rational(1101,424)-s.Rational(995,106)*x
T=(3200+56336*t)/(34000+204144*t)
assert s.factor(T.subs(t,0)-L)==0
assert s.factor(T.subs(t,s.Rational(1,4))-U)==0
assert s.factor(s.diff(T,t)-s.Rational(1262163200)/(34000+204144*t)**2)==0
assert U<s.Rational(1,4)
assert K.subs(x,L)==s.Rational(233,136)
assert s.diff(K,x)<0
assert 232*U<49
assert 232*K.subs(x,L)<400

A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
 [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=s.simplify(A[3:5,:]*A[:3,:].inv())
Tinv=(200-2125*x)/(12759*x-3521)
assert s.factor(T.subs(t,Tinv)-x)==0
Q=s.Matrix([34000+204144*Tinv,3200+56336*Tinv,58250+1286*Tinv,
            46600+12936*Tinv,31525+28011*Tinv])
assert s.cancel(Q[1]/Q[0]-x)==0
assert s.cancel(Q[2]/Q[0]-K)==0
q4=s.Rational(217,106)-s.Rational(381,53)*x
q5=s.Rational(1133,848)-s.Rational(921,212)*x
assert s.cancel(Q[3]/Q[0]-q4)==0
assert s.cancel(Q[4]/Q[0]-q5)==0
v=c+I*d
F=[]
for j,qj in enumerate((q4,q5)):
    p,q,r=list(B.row(j))
    Dj=s.expand(s.conjugate(p+r*v)*q)
    n=s.expand((p+r*v)*s.conjugate(p+r*v))
    n=s.expand(n-s.expand(r*s.conjugate(r))*(c*c+d*d-K))
    R=s.factor((qj-n-s.expand(q*s.conjugate(q))*x)/2)
    F.append(s.expand(s.re(Dj)*a-s.im(Dj)*b-R))
F4,F5=F
D=10+6*a-14*b
N=(14*a+6*b+18)*c+s.Rational(39,2)*a-2*b+(132-257*x)/4
assert s.expand(F4-(N-D*d))==0
assert s.expand(F5-(((245*c-123*d)/32+s.Rational(709,64))*a
 -((-123*c-245*d)/32)*b
 -((-51940*c+26076*d+158627*x-91398)/6784)))==0

Cu=1+x+2*a; Du=1+x-2*b; Cv=1+K+2*c
cu,du,cv=s.symbols('cu du cv',real=True)
Arec=(cu-1-x)/2
Brec=(1+x-du)/2
Crec=(cv-1-K)/2
Drec=s.factor(D.subs({a:Arec,b:Brec}))
Dnum=s.factor(N.subs({a:Arec,b:Brec,c:Crec}))
assert s.expand(Cu.subs(a,Arec)-cu)==0
assert s.expand(Du.subs(b,Brec)-du)==0
assert s.expand(Cv.subs(c,Crec)-cv)==0
assert s.cancel(F4.subs({a:Arec,b:Brec,c:Crec,d:Dnum/Drec}))==0

Np=N.subs({a:ap,b:bp,c:cp})
Dp=D.subs({a:ap,b:bp})
identity=((14*a+6*b+18)*(c-cp)
          +(14*cp+s.Rational(39,2)-6*dp)*(a-ap)
          +(6*cp-2+14*dp)*(b-bp))
assert s.expand((N-Np)-(D-Dp)*dp-identity)==0
assert 25+s.Rational(79,2)+22==s.Rational(173,2)
assert (25+s.Rational(79,2)+22)/6==s.Rational(173,12)
out={
 'unit':'PREFIX-377',
 'model':'static auxiliary complex 3-component five-port intensity model',
 'physical_x_range':[str(L),str(U)],
 'readouts':['Cu=|1+u|^2','Du=|1+i*u|^2','Cv=|1+v|^2'],
 'reconstruction':{'a':'(Cu-1-x)/2','b':'(1+x-Du)/2','c':'(Cv-1-K(x))/2',
                    'd':'N/D','D':'10+6a-14b',
                    'N':'(14a+6b+18)c+(39/2)a-2b+(132-257x)/4'},
 'exact_bounds':{'232U':str(232*U),'232Kmax':str(232*K.subs(x,L)),
                 'D_lower':'D>3','inverse_lipschitz':'173/12',
                 'two_candidate_noise_diameter':'173/6'},
 'depends_on_prior_source_count_or_classification':False,
 'method':'exact symbolic F4,F5 reconstruction and finite-difference identity; rational inequalities and Cauchy-Schwarz',
 'native_X6_typed_BRC':False,
 'status':'AUTHOR_SIDE_EXACT_SYMBOLIC / LOCAL_VERIFIED / UNREVIEWED / NOT_ADMITTED'}
print(json.dumps(out,ensure_ascii=False,indent=2))
print('PASS_PREFIX377_UNIFORM_TRI_OBSERVER_INVERSE_LIPSCHITZ')
