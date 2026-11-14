from fractions import Fraction as F

q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
q4=(
    ((F(509,900),F(382,900),F(9,900)), (F(47,180),F(43,90),F(47,180)), (F(9,900),F(382,900),F(509,900))),
    ((F(509,900),F(382,900),F(9,900)), (F(67,162),F(14,81),F(67,162)), (F(9,900),F(382,900),F(509,900))),
)
r2=(F(3,4),F(5,4))
r3=(F(1,2),F(1),F(3,2))
r4=(F(1,10),F(1),F(19,10))
R=sorted(set((F(1),)+r2+r3+r4))
assert len(R)==7
for i in (0,1):
    assert sum(q3[i])==1 and sum(q3[i][j]*r3[j] for j in range(3))==r2[i]
    for j in range(3):
        assert sum(q4[i][j])==1
        assert min(q4[i][j])>0
        assert sum(q4[i][j][k]*r4[k] for k in range(3))==r3[j]

def observe(g,u,x):
    masses={r:F(0) for r in R}
    masses[F(1)]+=1-g
    for i in range(2):
        masses[r2[i]]+=(g-u[i])/2
        for j in range(3):
            b=u[i]*q3[i][j]/2
            assert 0<=x[i][j]<=b
            masses[r3[j]]+=b-x[i][j]
            for k in range(3):
                masses[r4[k]]+=x[i][j]*q4[i][j][k]
    assert sum(masses.values())==1
    assert sum(r*m for r,m in masses.items())==1
    X=[sum((x[i][j] for i in range(2)),F(0)) for j in range(3)]
    TQ=1+g+sum(u)/2+sum(X)
    TP=1+g+(3*u[0]+5*u[1])/8+X[0]/2+X[1]+3*X[2]/2
    ell={r:(m if r<1 else F(0)) for r,m in masses.items()}
    eQ=sum(ell.values())
    eP=1-sum(r*v for r,v in ell.items())
    return masses, (eP,eQ,TP,TQ),X

g=F(1); u=(F(1),F(1))
x=((F(13,80),F(1,40),F(0)),(F(1,80),F(9,40),F(0)))
m,W,X=observe(g,u,x)
assert X==[F(7,40),F(1,4),F(0)]
assert (m[F(3,2)],m[F(1,10)])==(F(27,80),F(1787,9000))
assert W==(F(161801,180000),F(6499,18000),F(267,80),F(137,40))
A=F(1,10); B=F(9,40); alpha=F(47,180); beta=F(67,162)
J_full=alpha*x[0][1]+beta*x[1][1]
J_lr=X[1]*(alpha*A+beta*B)/(A+B)
assert J_full==F(239,2400) and J_lr==F(11,120)
V=(F(27,80),F(13,40),F(27,80))
z=[X[j]/V[j] for j in range(3)]
x_lr=tuple(tuple(u[i]*q3[i][j]/2*z[j] for j in range(3)) for i in range(2))
mlr,Wlr,Xlr=observe(g,u,x_lr)
assert Xlr==X and Wlr[2:]==W[2:]
assert mlr[F(3,2)]==F(27,80)
assert mlr[F(1,10)]==F(6863,36000)
assert mlr[F(1,2)]==F(13,80) and mlr[F(3,4)]==0
full_D=W[0]+W[1]-1
LR_D_max=F(9,10)*mlr[F(1,10)]+F(1,2)*mlr[F(1,2)]
assert (full_D,LR_D_max,full_D-LR_D_max)==(F(5199,20000),F(10113,40000),F(57,8000))
assert full_D>LR_D_max
print('FULL_W=',tuple(map(str,W)))
print('EXTRA_Q_STOP_M_3_OVER_2=',m[F(3,2)])
print('J_FULL=',J_full,'J_LR=',J_lr)
print('FULL_D=',full_D,'LR_MAX_D=',LR_D_max,'GAP=',full_D-LR_D_max)
print('PASS_EXACT_R5_FIVE_OBSERVER_STRICT_SEPARATION')
