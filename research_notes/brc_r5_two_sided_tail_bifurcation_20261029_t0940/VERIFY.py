#!/usr/bin/env python3
"""Exact Fractions verifier of the R5 signed source-tail bifurcation theorem.

Mathematical universal real-parameter claim is certified by affine vertex
reductions in the companion proof. Grid checks below are regressions only.
"""
from fractions import Fraction as F
from itertools import product

S=(F(1,2),F(1),F(3,2),F(5,2))
SRC=('A','B')
MU={'A':(F(7,50),F(11,75),F(1,2),F(16,75)),
    'B':(F(17,200),F(23,150),F(3,5),F(97,600))}
NU={('A','L'):(F(1,2),F(1,6),F(1,4),F(1,12)),
    ('B','L'):(F(5,12),F(1,3),F(1,6),F(1,12)),
    ('A','R'):(F(17,100),F(23,75),F(1,5),F(97,300)),
    ('B','R'):(F(31,120),F(5,18),F(1,15),F(143,360))}
EA=(F(1,8),F(1,4),F(3,8),F(1,4))
EB=(F(5,32),F(3,16),F(13,32),F(1,4))
Q={'A':F(1,4),'B':F(1,4)}
V={i:Q[i]*MU[i][1]*NU[i,'L'][2] for i in SRC}
W={i:Q[i]*MU[i][2]*NU[i,'R'][2] for i in SRC}
X={i:V[i]+W[i] for i in SRC}
TRIANGLE_VERTICES=((F(-1),F(3,32)),(F(-1),F(1,8)),
                   (F(0),F(1,8)),(F(1),F(1,8)),(F(1),F(5,32)))

def eta(i,u):
    return EA if i=='A' else tuple((1-u)*a+u*b for a,b in zip(EA,EB))

def local(t,s,theta):
    return t*theta+min(F(0),F(2)-2*s)

def d_merged(i,u,theta):
    stop=local(3,S[2],theta)
    return sum((z*local(4,s,theta) for z,s in zip(eta(i,u),S)),F(0))-stop

def upstream_margins(i,u,theta,gl,gr):
    """Stop-minus-continue at L/R and root, for arbitrary merged path coins."""
    m={}
    for d,g,k in (('L',gl,1),('R',gr,2)):
        cont=sum((z*((local(3,s,theta)+g*d_merged(i,u,theta))
                    if j==2 else local(3,s,theta))
                  for j,(z,s) in enumerate(zip(NU[i,d],S))),F(0))
        m[d]=(local(2,S[k],theta),cont)
    root_cont=sum((z*(m['L'][1] if j==1 else m['R'][1] if j==2
                      else local(2,s,theta))
                   for j,(z,s) in enumerate(zip(MU[i],S))),F(0))
    return (m['L'][0]-m['L'][1],m['R'][0]-m['R'][1],
            local(1,S[2],theta)-root_cont)

def terminal_lr(u,theta,root,left,right,merge):
    """Full terminal (time, signature) Q masses for a seedless LR policy."""
    z={}
    def add(t,s,m): z[t,s]=z.get((t,s),F(0))+m
    add(1,S[0],F(1,2)); add(1,S[2],(1-root)/2)
    for i in SRC:
        for k,s in enumerate(S):
            m=root*Q[i]*MU[i][k]
            if k not in (1,2):add(2,s,m)
            else:
                d='L' if k==1 else 'R'; gate=left if k==1 else right
                add(2,s,m*(1-gate))
                for j,ss in enumerate(S):
                    n=m*gate*NU[i,d][j]
                    if j!=2:add(3,ss,n)
                    else:
                        add(3,ss,n*(1-merge))
                        for kk,sv in enumerate(S):
                            add(4,sv,n*merge*eta(i,u)[kk])
    return z

def terminal_full(u,which):
    """Root and both time-2 paths continue; exactly origin 'which' continues at merge."""
    z={}
    def add(t,s,m): z[t,s]=z.get((t,s),F(0))+m
    add(1,S[0],F(1,2))
    for i in SRC:
        for k,s in enumerate(S):
            m=Q[i]*MU[i][k]
            if k not in (1,2):add(2,s,m)
            else:
                d='L' if k==1 else 'R'
                for j,ss in enumerate(S):
                    n=m*NU[i,d][j]
                    if j!=2 or i!=which:add(3,ss,n)
                    else:
                        for kk,sv in enumerate(S): add(4,sv,n*eta(i,u)[kk])
    return z

def obs(z):
    q=sum((m for (t,s),m in z.items() if s>1),F(0))
    b=sum((s*m for (t,s),m in z.items() if s>1),F(0))
    return (1-b,q,sum((t*s*m for (t,s),m in z.items()),F(0)),
            sum((t*m for (t,s),m in z.items()),F(0)))

def objective(z,theta):
    return F(2)+sum((m*local(t,s,theta) for (t,s),m in z.items()),F(0))

def predicted_values(u,theta):
    v0=F(2429,1800)+F(37,20)*theta
    da=X['A']*(theta-F(1,8))
    db=X['B']*(theta-(F(1,8)+u/F(32)))
    full=v0+min(F(0),da)+min(F(0),db)
    lr=v0+min(F(0),da+db)
    return full,lr

def check():
    assert X=={'A':F(41,1200),'B':F(59,3600)}
    assert V['A']*W['B']-V['B']*W['A']==-F(49,720000)
    for i in SRC:
        for row,parent in ((MU[i],F(3,2)),(NU[i,'L'],F(1)),
                           (NU[i,'R'],F(3,2))):
            assert all(v>0 for v in row)
            assert sum(row)==1 and sum((a*s for a,s in zip(row,S)),F(0))==parent
        for u in (F(-1),F(0),F(1)):
            row=eta(i,u)
            assert all(v>0 for v in row)
            assert sum(row)==1 and sum((a*s for a,s in zip(row,S)),F(0))==F(3,2)
    minima={}
    for i in SRC:
        vals=[upstream_margins(i,u,theta,gl,gr)
              for u,theta in TRIANGLE_VERTICES
              for gl,gr in product((F(0),F(1)),repeat=2)]
        minima[i]=tuple(min(row[k] for row in vals) for k in range(3))
        assert all(m>0 for m in minima[i])
    assert minima=={'A':(F(43,128),F(3,400),F(353,9600)),
                    'B':(F(25,96),F(49,480),F(431,14400))}
    print('TWO_TRIANGLE_CORNER_MINIMA',minima)
    assert X['B']/(32*sum(X.values()))==F(59,5824)
    assert X['A']*X['B']/(32*sum(X.values()))==F(2419,6988800)
    print('theta_star(u)=1/8+(59/5824)*u')
    print('maximum_signed_gap(u)=(2419/6988800)*abs(u)')
    params=(F(-1),F(-3,4),F(-1,2),F(-1,5),F(0),
            F(1,5),F(1,2),F(3,4),F(1))
    checked=0
    for u in params:
        IA=F(1,8); IB=IA+u/F(32)
        for j in range(17):
            theta=min(IA,IB)+F(j,16)*abs(IB-IA)
            full,lr=predicted_values(u,theta)
            lr_exact=min(objective(terminal_lr(u,theta,*coins),theta)
                         for coins in product((F(0),F(1)),repeat=4))
            assert lr==lr_exact
            assert full<=lr
            if u<0: f=objective(terminal_full(u,'A'),theta)
            elif u>0: f=objective(terminal_full(u,'B'),theta)
            else: f=objective(terminal_lr(u,theta,F(1),F(1),F(1),F(0)),theta)
            assert f==full
            da=theta-IA; db=theta-IB
            assert lr-full==min(X['A']*abs(da),X['B']*abs(db))
            checked+=1
        theta_star=IA+F(59,5824)*u
        fa,lr=predicted_values(u,theta_star)
        assert lr-fa==abs(u)*F(2419,6988800)
        if u<0:
            o=obs(terminal_full(u,'A'))
            assert o==(F(2783,6400),F(6847,28800),F(1831,800),F(2261,1200))
        elif u>0:
            o=obs(terminal_full(u,'B'))
            assert o==((F(98908)-177*u)/F(230400),
                       (F(28156)+59*u)/F(115200),
                       F(5429,2400),F(6719,3600))
        else:
            o=obs(terminal_lr(u,theta_star,F(1),F(1),F(1),F(0)))
        assert F(2)*o[0]+F(2)*o[1]+theta_star*o[3]==fa
    print('EXACT_MODEL_AND_POLICY_REGRESSIONS',checked,'each with 16 LR deterministic policies')
    print('STRICT_POSITIVE_Q_AND_P_KERNELS_FOR_ALL_REAL_u_IN_[-1,1]')
    print('PASS_EXACT_R5_TWO_SIDED_TAIL_BIFURCATION')

if __name__=='__main__':check()
