"""Exact identities and scoped numerical cross-checks for C84's 1D formula."""
from pathlib import Path
import json
import sympy as s
import mpmath as mp
from one_dimensional import kernel

x,r=s.symbols('x r',positive=True)
checks=[]
def prove(name,lhs,rhs):
    assert s.simplify(lhs-rhs)==0,name
    checks.append({'name':name,'status':'passed','arithmetic':'symbolic exact'})
u=s.atanh(x/r)
R0=u/r;R1=-s.log(1-x*x/(r*r))/2
R2=r*r*R0-x;R3=r*r*R1-x*x/2
S0=x/(2*r*r*(r*r-x*x))+u/(2*r**3);S2=r*r*S0-R0
for n,R in enumerate([R0,R1,R2,R3]):prove('rational_R'+str(n),s.diff(R,x),x**n/(r*r-x*x))
prove('squared_S0',s.diff(S0,x),1/(r*r-x*x)**2)
prove('squared_S2',s.diff(S2,x),x*x/(r*r-x*x)**2)
Lm0=x*s.log(r*r-x*x)+2*r*u-2*x
Lm2=x**3*s.log(r*r-x*x)/3+2*r**3*u/3-2*r*r*x/3-2*x**3/9
Lp0=x*s.log(r*r+x*x)-2*x+2*r*s.atan(x/r)
Lp2=x**3*s.log(r*r+x*x)/3-2*x**3/9+2*r*r*x/3-2*r**3*s.atan(x/r)/3
for name,f,target in [('Lm0',Lm0,s.log(r*r-x*x)),('Lm2',Lm2,x*x*s.log(r*r-x*x)),('Lp0',Lp0,s.log(r*r+x*x)),('Lp2',Lp2,x*x*s.log(r*r+x*x))]:prove(name,s.diff(f,x),target)
A0=x*u-r*R1
A1=(x*x-r*r)*u/2+r*x/2
A2=x**3*u/3-r*(r*r*R1-x*x/2)/3
A3=(x**4-r**4)*u/4+r**3*x/4+r*x**3/12
for n,f in enumerate([A0,A1,A2,A3]):prove('atanh_A'+str(n),s.diff(f,x),x**n*u)
z,d,h,q,Lh,Le,Lratio,Lq=s.symbols('z d h q Lh Le Lratio Lq')
K2=h*(4-(5*z+d)/2)+z*h*h/2-d+q+(3*z/2-4)*Lh-d*Lq+z*Lratio/2
K3=4*h-3*z*h+z*h*h+(z/2-2)*Le
C=4*h-s.Rational(3,2)*(z+d)*h-z*h*h/2-3*d+3*q+(s.Rational(9,2)*z-12)*Lh+(4-z)*Le-3*d*Lq+s.Rational(3,2)*z*Lratio
prove('triangle_parallelogram_combination',3*K2-2*K3,C)
P,K=s.symbols('P K')
Rat=4-2*z-s.Rational(9,2)*d+3*q+K*(-4+s.Rational(5,2)*z+s.Rational(3,2)*d)/P-z*K*K/(2*P*P)
prove('rational_kernel_reduction',C.subs({h:1-K/P,Lh:0,Le:0,Lratio:0,Lq:0}),Rat)
# Endpoint constants: beta integrals on x,y>=0, x+y<=1.
x,y=s.symbols('x y',positive=True)
M0=s.integrate(s.integrate(x*y,(y,0,1-x)),(x,0,1))
Mlog=s.Rational(1,24)*(s.digamma(1)-s.digamma(5))
Mhalf=s.gamma(2)**2*s.gamma(s.Rational(3,2))/s.gamma(s.Rational(11,2))
prove('endpoint_log_coefficient',3*M0,s.Rational(1,8))
prove('endpoint_constant_coefficient',-3*Mlog,s.Rational(25,96))
prove('endpoint_half_power_coefficient',6*Mhalf,s.Rational(32,315))
Ix=s.Rational(1,60)
Ixlog=-s.Rational(137,3600)
prove('endpoint_next_log_coefficient',s.Rational(9,2)*2*Ix+6*Ix+3*M0,s.Rational(3,8))
prove('endpoint_next_constant_coefficient',-(s.Rational(9,2)*2*Ixlog+6*Ixlog+3*Mlog)-3*M0,s.Rational(113,160))
# Primitive evaluation versus direct inner numerical integration, only a cross-check.
mp.mp.dps=45
errors=[]
for A in [mp.mpf(13)/25,mp.mpf(2)/3,mp.mpf(4)/5,mp.mpf(49)/50]:
    lo=2*mp.sqrt(A); split=1+A
    for z in [(2*lo+split)/3,(lo+2*split)/3,(2*split+2)/3,(split+4)/3]:
        q=mp.sqrt(z*z-4*A);b=2-z;D=min(b,q);kk=4*A;c=mp.mpf(9)*z/2-12;e=4-z
        def f(d):
            H=z*z-d*d
            C=4-2*z-mp.mpf(9)*d/2+3*q+kk*(-4+mp.mpf(5)*z/2+mp.mpf(3)*d/2)/H-z*kk*kk/(2*H*H)
            C+=c*mp.log((q*q-d*d)/H)+e*mp.log((8*A-z*z+d*d)/H)-3*d*mp.atanh(d/q)+3*z*mp.atanh(d/z)
            return (b*b-d*d)*C/4
        direct=mp.quad(f,[0,D])
        error=abs(kernel(A,z)-direct)
        assert error<mp.mpf('1e-37'),str(error)
        errors.append(str(error))
checks.append({'name':'elementary_kernel_vs_direct_inner_integral','status':'passed','cases':len(errors),'maximum_absolute_difference':str(max(map(mp.mpf,errors))),'arithmetic':'45-digit exploratory numerical cross-check, not an interval certificate'})
result={'scope':'Symbolic primitive and coefficient identities plus explicitly labelled numerical cross-checks; analytic shape classification and remainder bounds are in FINITE_FORMULA.md.','passed':len(checks),'failed':0,'checks':checks}
Path(__file__).with_name('one_dimensional_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
