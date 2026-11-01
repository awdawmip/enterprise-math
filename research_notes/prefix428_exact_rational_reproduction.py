#!/usr/bin/env python3
"""PREFIX-428 exact rational bounds; full parameter-rectangle analytic enclosures."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
beta=F(1,10**6);rho=F(1,1000);lo=F(999,1000);hi=F(1001,1000)
Dlo=F(17,5000);Dhi=F(7,2000);Mlo=F(23,1000);Mhi=F(1,40)
checks=[]
def test(label,condition):
    assert condition,label
    checks.append(label)
test('sqrt lower',lo**2<1-beta-beta**2)
test('sqrt upper',hi**2>1+beta)
Jlo=7-5*(1+beta)+F(39,2)*(2-beta)+4*lo
Jhi=7-5*(1-beta)+F(39,2)*(2+beta)+4*hi
test('negative J lower',Jlo>F(67,10)**2)
test('negative J upper',Jhi<F(671,100)**2)
test('positive J upper',7-5*(1-beta)+F(39,2)*(2+beta)-4*lo<F(37004025,10**6))
test('w bound',1+beta-beta**2>=1)
test('plateau J lower',45-F(49,2)*beta>F(67,10)**2)
test('plateau J upper',45+4*beta<F(671,100)**2)
test('D lower',F(372)/(16000*F(671,100))>Dlo)
test('D upper',(372+427*beta)/(16000*F(67,10))<Dhi)
test('M lower',(1287-705*beta)/(8000*F(671,100))>Mlo)
test('M upper',(1287+61*beta)/(8000*F(67,10))<Mhi)
Cup=1024000*(45+4*beta)*F(671,100)/(F(372)**2)
Clo=1024000*(45-F(49,2)*beta)*F(67,10)/((372+427*beta)**2)
test('C range',2100<Clo<Cup<2235)
tmax=F(1,6800)
test('t bound',beta/(2*Dlo)==tmax)
lbound=16*F(671,100)*rho*tmax/(Dlo*(1-tmax**2))
test('lambda upper',lbound<F(1,200))
test('disk radial strict',8*F(67,10)-F(1,200)*48>32*rho)
test('support r derivative',-5+2*F(1001,999)+rho*(72+F(36,200))<0)
test('support s derivative',F(39,2)-2*F(1,999)-F(709,64*200)-rho*(24+F(12,200))>19)
test('positive phase separation',F(37004025,10**6)+8*rho*F(61,10)+16*rho**2<F(37053,1000))
test('negative phase separation',45+4*beta-8*rho*F(67,10)+16*rho**2+2235*beta**2<F(44947,1000))
test('joint observer strict',Mlo-F(53,8)*beta-beta>2*rho+rho**2)
rem=F(2235)*(Dhi**2+5*Mhi**2)/(4*Dlo**4)
test('quartic remainder',rem<14*10**9)
print('PREFIX428_RATIONAL_CERTIFICATE_PASS',len(checks))
for name in checks:print('PASS',name)
print('uniform quartic coefficient upper rational:',rem)
with localcontext() as c:
    c.prec=45
    for e in [Decimal(0),Decimal('0.000001')]:
        w=(1+e-e**2).sqrt();J=41-Decimal(49)*e/2+4*w
        h=J.sqrt();g=4+59*e+368*w;T=1226-705*e+61*w
        D=g/(16000*h);M=T/(8000*h);C=Decimal('0.004')*h/D**2
        print('epsilon',e,'C',C,'cubic',-C*M/D**2)
