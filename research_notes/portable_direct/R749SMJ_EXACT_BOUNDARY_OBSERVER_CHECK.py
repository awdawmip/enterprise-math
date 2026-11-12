from fractions import Fraction as Q
from itertools import product
import json

SOURCE = tuple(product((1, -1), repeat=3))
OUTPUT = SOURCE
GRID = (Q(-1), Q(-1,2), Q(0), Q(1,2), Q(1))

def F(z, o, alpha, beta, gamma):
    x,y,t=z; u,v,w=o
    return (2+alpha*u*x)*(2+beta*v*(y if u==1 else t))*(2+gamma*w*y*t)/Q(64)

def P(z, o, alpha, beta, gamma):
    x,y,t=z; u,v,w=o
    return (2+gamma*w*y*t)*sum(
       (2+i*x)*(1+alpha*u*i)*(2+beta*v*(y if i==1 else t))
       for i in (1,-1)
    )/Q(128)

def phi(z):
    x,y,t=z
    return y+t+2*x*(y-t)

def psi(z):
    x,y,t=z
    return y+t-2*x*(y-t)

def prior(z,source,sgn):
    return (1+sgn*Q(source(z),8))/8

def push(K, weights, a,b,c):
    return tuple(sum(K(z,o,a,b,c)*weights(z) for z in SOURCE) for o in OUTPUT)

def tv(xs,ys):
    return sum(abs(x-y) for x,y in zip(xs,ys))/2

def witness_tv(K, source, a,b,c):
    return tv(push(K,lambda z:prior(z,source,+1),a,b,c),
              push(K,lambda z:prior(z,source,-1),a,b,c))

def mu_y(z):return (1+Q(z[1],2))/8

def mu_t(z):return (1+Q(z[2],2))/8

def run():
    checks=0
    strict=0
    for a,b,c in product(GRID,repeat=3):
        for kernel in (F,P):
            for z in SOURCE:
                vec=[kernel(z,o,a,b,c) for o in OUTPUT]
                assert min(vec)>=0 and sum(vec)==1
                checks+=1
        for o in OUTPUT:
            u,v,w=o
            assert sum(F(z,o,a,b,c)*phi(z) for z in SOURCE)==b*v*(2*(1+a)+(1-a)*c*w)/4
            assert sum(P(z,o,a,b,c)*phi(z) for z in SOURCE)==b*v
            assert sum(F(z,o,a,b,c)*psi(z) for z in SOURCE)==b*v*(2*(1-a)+(1+a)*c*w)/4
            assert sum(P(z,o,a,b,c)*psi(z) for z in SOURCE)==b*c*v*w/2
        for source in (phi,psi):
            for sg in (-1,1):
                masses=[prior(z,source,sg) for z in SOURCE]
                assert sum(masses)==1 and min(masses)>=Q(1,16)
        fv=witness_tv(F,phi,a,b,c)
        pv=witness_tv(P,phi,a,b,c)
        fvp=witness_tv(F,psi,a,b,c)
        pvp=witness_tv(P,psi,a,b,c)
        assert fv==abs(b)*max(2*(1+a),(1-a)*abs(c))/32
        assert pv==abs(b)/8
        assert fvp==abs(b)*max(2*(1-a),(1+a)*abs(c))/32
        assert pvp==abs(b*c)/16
        assert tv(push(F,mu_y,a,b,c),push(F,mu_t,a,b,c))==abs(b)/8
        assert tv(push(P,mu_y,a,b,c),push(P,mu_t,a,b,c))==abs(a*b)/8
        if a==1 or b==0:
            for z,o in product(SOURCE,OUTPUT):
                assert F(z,o,a,b,c)==P(z,o,a,b,c)
        if a<1 and b!=0:
            assert pv>fv
            if a>-1:
                assert abs(b)/8>abs(a*b)/8
            else:
                assert fvp>pvp
                assert fv==abs(b*c)/16 and fvp==abs(b)/8
                assert (pv-fv)/2==abs(b)*(2-abs(c))/32
                assert (fvp-pvp)/2==abs(b)*(2-abs(c))/32
            strict+=1
    return {
      'status':'PASS', 'arithmetic':'Python Fraction exact',
      'parameter_triples':len(GRID)**3,
      'kernel_stochastic_columns':checks,
      'source_output_contrast_equalities':len(GRID)**3*len(OUTPUT)*4,
      'positive_prior_pairs':'phi, psi',
      'strict_noncomparability_grid_cases':strict,
      'claim':'all-alpha four Walsh contrasts; three total-variation witness families; A=-1 two-sided exact deficiency lower bound; equality a=1 or b=0',
      'universal_proof':'algebraic Walsh orthogonality in companion note; grid is a regression test'
    }

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
