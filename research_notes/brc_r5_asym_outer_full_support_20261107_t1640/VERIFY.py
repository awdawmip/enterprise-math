#!/usr/bin/env python3
"""R5 asymmetrical signed-support: exact rational primal/dual certificate."""
from fractions import Fraction as F
def f(x): return F(str(x))
def V(**d):
    return (F(0),)+tuple(f(d.get(k,0)) for k in "gabuvwz")
def plus(*v): return tuple(sum(x[i] for x in v) for i in range(8))
def mul(q,v): return tuple(q*t for t in v)
def minus(v): return mul(-1,v)
def ev(v,x): return v[0]+sum(a*b for a,b in zip(v[1:],x))
g,a,b,u,v,w,z=[V(**{k:1}) for k in "gabuvwz"]
c0=plus(mul(F(13,40),a),mul(F(1,80),b))
c1=plus(mul(F(1,10),a),mul(F(9,40),b))
c2=plus(mul(F(3,40),a),mul(F(21,80),b))
M=[plus(mul(F(509,900),u),mul(F(47,180),z),mul(F(67,162),plus(v,minus(z))),mul(F(1,100),w)),
   plus(c0,minus(u)),mul(F(1,2),plus(g,minus(a))),
   plus(V(),(F(1),)+(F(0),)*7,minus(g),c1,minus(v),mul(F(191,450),plus(u,w)),mul(F(43,90),z),mul(F(14,81),plus(v,minus(z)))),
   mul(F(1,2),plus(g,minus(b))),plus(c2,minus(w)),
   plus(mul(F(1,100),u),mul(F(47,180),z),mul(F(67,162),plus(v,minus(z))),mul(F(509,900),w))]
TP=plus((F(1),)+(F(0),)*7,g,mul(F(3,8),a),mul(F(5,8),b),mul(F(1,2),u),v,mul(F(3,2),w))
TQ=plus((F(1),)+(F(0),)*7,g,mul(F(1,2),a),mul(F(1,2),b),u,v,w)
L=[minus(g),plus(g,(F(-1),)+(F(0),)*7),minus(a),plus(a,minus(g)),minus(b),plus(b,minus(g)),
   minus(u),plus(u,minus(c0)),minus(v),plus(v,minus(c1)),minus(w),plus(w,minus(c2)),
   minus(z),plus(z,minus(mul(F(1,10),a))),plus(z,minus(v)),plus(v,minus(z),minus(mul(F(9,40),b)))]
LR=list(map(f,["1/10","1/2","3/4","1","5/4","3/2","19/10"]))
def S(lam):
    return plus(*[mul(1-(1+lam)*r,m) for r,m in zip(LR,M) if 1-(1+lam)*r>0])
def pt(s): return tuple(map(f,s.split()))
P0=pt("2186/2325 1814/2325 2186/2325 0 2693/9300 0 907/11625")
P1=pt("1 974/1325 1186/1325 0 1457/5300 0 487/6625")
N0=pt("138/155 138/155 138/155 1/25 897/3100 0 69/775")
N1=pt("742/775 742/775 618/775 0 853/3100 0 371/3875")
N2=pt("1 1226/1325 1014/1325 0 1403/5300 0 613/6625")
# Each entry is [lambda, active-slack indices, nonnegative dual y, unrestricted time dual nu_P,nu_Q].
DP=[
("-1/10","5 6 9 10 15","13781/558000 46481/930000 54791/558000 183499/2790000 17537/162000","21007/348750","9403/348750"),
("-351/17291","6 9 10 15","22473/345820 7789/69164 46129/345820 81757/622476","6694/86455","3016/86455"),
("0","1 6 9 10 15","117/10600 3999/53000 1283/10600 7127/53000 247/1800","391/6625","364/6625"),
("351/16589","6 9 10 15","26373/331780 7789/66356 42229/331780 81757/597204","3184/82945","6526/82945"),
("1/10","5 6 9 10 15","13079/558000 332837/2790000 67769/558000 112541/2790000 21983/162000","-43037/348750","81727/348750")]
DN=[
("-1/10","3 5 9 10 15","46481/3720000 136177/11160000 54791/558000 161471/1395000 17537/162000","223471/1395000","-101831/1395000"),
("-26217/398347","3 9 10 15","22473/1593388 41579/398347 60226/398347 423605/3585123","71878/398347","-32852/398347"),
DP[1],DP[2],DP[3],
("1/10","3 6 9 10 15","13079/558000 71257/2790000 67769/558000 41569/310000 21983/162000","11179/174375","2722/58125")]
IP=[("-1/10","-351/17291",P0),("-351/17291","0",P1),("0","351/16589",P1),("351/16589","1/10",P0)]
IN=[("-1/10","-26217/398347",N0),("-26217/398347","-351/17291",N1),
    ("-351/17291","0",N2),("0","351/16589",N2),("351/16589","1/10",N1)]
def verify(e,dual,intervals):
    for x in {q for _,_,q in intervals}:
        assert all(ev(t,x)<=0 for t in L)
        assert ev(TP,x)==f("31/10")+e and ev(TQ,x)==f("31/10")-e
        assert sum(ev(m,x) for m in M)==1
        assert sum(r*ev(m,x) for r,m in zip(LR,M))==1
        G,A,B,U,Ve,W,Z=x
        assert 9*B*Z==4*A*(Ve-Z)
    bounds={}
    for ls,ids,ms,p,q in dual:
        lam=f(ls); ii=list(map(int,ids.split())); mu=list(map(f,ms.split()))
        p,q=f(p),f(q)
        assert len(ii)==len(mu) and all(a>=0 for a in mu)
        c=plus(S(lam),*[mul(-y,L[k]) for y,k in zip(mu,ii)],mul(-p,TP),mul(-q,TQ))
        assert c[1:]==(F(0),)*7,("DUAL_ERROR",e,lam,c)
        bounds[lam]=c[0]+p*(f("31/10")+e)+q*(f("31/10")-e)
        print("EXACT_DUAL",e,lam,"value",bounds[lam],"nonnegative",len(ii),"coefficients",7)
    for ls,rs,x in intervals:
        l,r=f(ls),f(rs)
        assert l<r and (r<=0 or l>=0)
        assert ev(S(l),x)==bounds[l] and ev(S(r),x)==bounds[r]
        intercept=ev(S(f(0)),x)
        slope=(ev(S(r),x)-ev(S(l),x))/(r-l)
        print("PROVEN_ALL_REAL_INTERVAL",e,l,r,"intercept",intercept,"slope",slope)
    assert intervals[0][0]=="-1/10" and intervals[-1][1]=="1/10"
    assert all(a[1]==b[0] for a,b in zip(intervals,intervals[1:]))
print("MODEL_7_VARIABLE_7_STOP_KEYS_FRACTION_EXACT")
verify(f("1/100"),DP,IP)
verify(f("-1/100"),DN,IN)
print("PASS_11_EXACT_DUAL_CERTIFICATES_9_ALL_REAL_INTERVALS_5_SEEDLESS_VERTICES")
print("PASS_ASYMMETRIC_OUTER_SUPPORT_COMPLETE_LAMBDA_INTERVAL")
