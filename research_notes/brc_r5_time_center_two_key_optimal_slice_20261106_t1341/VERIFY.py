from fractions import Fraction as F
from itertools import product

f=lambda p,q=1:F(p,q)
r=f(13,10)
alpha,beta=f(47,180),f(67,162)
V_coeff=(f(13,40)+r*f(1,80), f(1,10)+r*f(9,40), f(3,40)+r*f(21,80))
k=(alpha*f(1,10)+beta*r*f(9,40))/V_coeff[1]
(g,u,X0,X1,X2,h)=(f(91,276),f(35,138),f(637,7360),f(1099,11040),f(497,7360),f(287903,10672000))
u1=r*u
V0,V1,V2=[v*u for v in V_coeff]
J=k*X1
Mminus=(509*X0+9*X2)/900+J
Mplus=(9*X0+509*X2)/900+J
assert u1<=g<=1 and 0<=u<=g and 0<=X0<=V0 and 0<=X1<=V1 and 0<=X2<=V2
assert Mminus==f(29,9)*h
assert Mplus>=f(11,9)*h

M={s:f(0) for s in (f(1,10),f(1,2),f(3,4),f(1),f(5,4),f(3,2),f(19,10))}
M[f(1)]+=1-g
M[f(3,4)]+=(g-u)/2; M[f(5,4)]+=(g-u1)/2
M[f(1,2)]+=V0-X0; M[f(1)]+=V1-X1; M[f(3,2)]+=V2-X2
M[f(1,10)]+=Mminus
M[f(1)]+=f(382,900)*(X0+X2)+X1-2*J
M[f(19,10)]+=Mplus
assert all(m>=0 for m in M.values())
assert sum(M.values())==1 and sum(key*mass for key,mass in M.items())==1
TQ=1+g+(u+u1)/2+X0+X1+X2
TP=1+g+(3*u+5*u1)/8+X0/2+X1+f(3,2)*X2
assert TQ==TP==f(15,8)
for c,d in product((-h,h),repeat=2):
    t={s:f(1,2) for s in M}
    t[f(1,10)]=f(1,2)+(10*c+19*d)/(18*Mminus)
    t[f(19,10)]=f(1,2)-(10*c+d)/(18*Mplus)
    assert all(0<=v<=1 for v in t.values())
    ep=1-sum(s*M[s]*t[s] for s in M)
    eq=sum(M[s]*t[s] for s in M)
    assert ep==f(1,2)+c and eq==f(1,2)+d

lam=(f(41129,1334000),f(78011,667000),f(17899747,209438000),f(9,29))
muq,mup=f(115107,1334000),-f(36989,667000)
assert all(t>=0 for t in lam)
rows=[(-1,r,0,0,0,0),(0,-V_coeff[0],1,0,0,0),(0,-V_coeff[1],0,1,0,0),(0,0,-f(509,900),-k,-f(9,900),f(29,9))]
tqrow=(1,f(1,2)*(1+r),1,1,1,0)
tprow=(1,f(3,8)+f(5,8)*r,f(1,2),1,f(3,2),0)
assert all(sum(lam[i]*f(rows[i][j]) for i in range(4))+muq*f(tqrow[j])+mup*f(tprow[j])==int(j==5) for j in range(6))
assert f(7,8)*(muq+mup)==h
print('PASS_EXACT_R5_TIME_CENTER_TWO_KEY_SLICE_AND_DUAL_OPTIMUM')
print('ratio=',r,'k=',k)
print('g,u0,u1,X0,X1,X2=',g,u,u1,X0,X1,X2)
print('V0,V1,V2=',V0,V1,V2)
print('M_minus,M_plus=',Mminus,Mplus)
print('all_stopped_mass_keys=',','.join(f'{s}:{v}' for s,v in M.items()))
print('fixed_time_TP_TQ=',TP,TQ)
print('max_h=',h,'decimal=',float(h))
print('improvement_over_previous_fourcube_factor=',h*52)
print('dual_lambdas=',','.join(str(x) for x in lam),'dual_mus=',muq,mup)
print('corners_checked=4; universal proof=affine box in (c,d), two-key inversion and dual LP identity')
