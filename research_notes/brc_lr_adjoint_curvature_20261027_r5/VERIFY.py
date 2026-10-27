from fractions import Fraction as F

Y = (F(1, 2), F(1), F(3, 2))
KA = (F(1, 4), F(1, 2), F(1, 4))
KB = (F(1, 8), F(3, 4), F(1, 8))
K = {'a': KA, 'b': KB}
FIRST_CONT = {'a': F(3, 4), 'b': F(1, 4)}
SECOND_CONT = {('a','u'): F(1), ('a','v'): F(1,2),
               ('b','u'): F(1,4), ('b','v'): F(3,4)}


def dot(v,w): return sum((x*y for x,y in zip(v,w)), F(0))
def kernel_mix(weight_a): return tuple(weight_a*x+(1-weight_a)*y for x,y in zip(KA,KB))
def tv(a,b): return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def eval_policy(q1,q2):
    """q1, q2 maps are action probabilities conditional on hidden history."""
    out=[F(0)]*4
    Qtotal = Ptotal = F(0)
    for a in ('a','b'):
        w1=F(1,2)
        c1=q1(a)
        stop1=w1*(1-c1)
        out[1]+=stop1; out[2]+=stop1; out[3]+=stop1
        Qtotal+=stop1; Ptotal+=stop1
        for u in ('u','v'):
            w2=w1*F(1,2)*c1
            c2=q2(a,u)
            stop2=w2*(1-c2)
            out[1]+=stop2; out[2]+=2*stop2; out[3]+=2*stop2
            Qtotal+=stop2; Ptotal+=stop2
            for y,k in zip(Y,K[a]):
                w3=w2*c2*k
                if y<F(1): out[0]+=w3*y
                else: out[1]+=w3
                out[2]+=3*w3*y; out[3]+=3*w3
                Qtotal+=w3; Ptotal+=w3*y
    assert Qtotal==Ptotal==1
    return tuple(out)

full=eval_policy(lambda a: FIRST_CONT[a],lambda a,u: SECOND_CONT[a,u])
bar=eval_policy(lambda a: F(1,2),lambda a,u:F(11,16))
f=tuple(min(y,F(1)) for y in Y)
assert f==(F(1,2), F(1),F(1))
assert sum(KA)==sum(KB)==1
assert dot(Y,KA)==dot(Y,KB)==1
assert tv(KA,KB)==F(1,4)
assert dot(KA,f)==F(7,8)
assert dot(KB,f)==F(15,16)
# At t=2, full alive=1/2, conditional continue=11/16.
# Full continued branch a weight=9/32 and branch b weight=1/16.
d2=F(1,2); c2=F(11,16)
Kfull=kernel_mix(F(9,11)); Kbar=kernel_mix(F(1,2))
assert Kfull==tuple((F(9,11)*x+F(2,11)*y for x,y in zip(KA,KB)))
assert tv(Kfull,Kbar)==F(7,88)
assert dot(Kfull,Y)==dot(Kbar,Y)==1
adjoint=d2*c2*dot(tuple(x-y for x,y in zip(Kfull,Kbar)), f)
assert adjoint==F(-7,1024)
assert (full[0]+full[1])-(bar[0]+bar[1])==adjoint
assert (full[2],full[3])==(bar[2],bar[3])==(F(59,32),F(59,32))
# Three-point residual-affine oscillation of min(y,1) is exactly 1/4.
rho=abs(f[1]-(f[0]+f[2])/2)
assert rho==F(1,4)
assert abs(adjoint)==d2*c2*tv(Kfull,Kbar)*rho
assert abs(adjoint)<=d2*c2*tv(KA,KB)*rho
# One-step instance: full continues a only, projected LR continues half.
short_full=eval_policy(lambda a:F(1),lambda a,u:F(1) if a=='a' else F(0))
short_bar=eval_policy(lambda a:F(1),lambda a,u:F(1,2))
assert (short_full[0]+short_full[1])-(short_bar[0]+short_bar[1])==F(-1,64)
assert abs(F(-1,64))==F(1,2)*tv(KA,kernel_mix(F(1,2)))*rho
print('MODEL strictly positive P/Q tree: 2 x 2 x 3 = 12 leaves')
print('K_A=',KA,'K_B=',KB,'TVdiameter=',tv(KA,KB))
print('FULL=',full)
print('SEEDLESS_LR_PROJECTION=',bar)
print('FULL_MINUS_LR=',tuple(x-y for x,y in zip(full,bar)))
print('SECOND_LAYER_ALIVE=',d2,'CONTINUE=',c2)
print('CONDITIONAL_CONTINUED_K_FULL=',Kfull)
print('CONDITIONAL_CONTINUED_K_LR=',Kbar)
print('ACTUAL_KERNEL_TV=',tv(Kfull,Kbar),'CURVATURE_OSC=',rho)
print('ADJOINT_EXACT=',adjoint,'CURVATURE_BOUND=',d2*c2*tv(Kfull,Kbar)*rho)
print('UNIFORM_DIAMETER_BOUND=',d2*c2*tv(KA,KB)*rho)
print('ONE_STEP_FULL_MINUS_LR_J=',F(-1,64))
print('ALL EXACT CHECKS PASSED')
