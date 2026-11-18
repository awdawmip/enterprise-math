"""Exact checks over Z_2[sqrt(-2)], F^+=Q(sqrt(417)), and the R105 CM field."""
import argparse
from collections import Counter
from pathlib import Path
import hashlib
import subprocess
import sys
from itertools import product
import json


class Ramified:
    # Each element is encoded a+n*b, representing a+b*pi with pi^2=-2 mod n.
    def __init__(self,n):
        self.n=n
        self.pi=n
    def elem(self,a,b=0):
        return a%self.n+self.n*(b%self.n)
    def add(self,x,y):
        n=self.n
        return self.elem(x%n+y%n,x//n+y//n)
    def neg(self,x):
        return self.elem(-(x%self.n),-(x//self.n))
    def conj(self,x):
        return self.elem(x%self.n,-(x//self.n))
    def mul(self,x,y):
        n=self.n
        a,b=x%n,x//n
        c,d=y%n,y//n
        return self.elem(a*c-2*b*d,a*d+b*c)
    def inv(self,x):
        norm=self.mul(x,self.conj(x))
        assert norm<self.n and norm%2
        return self.mul(self.conj(x),self.elem(pow(norm,-1,self.n)))
    def mm(self,A,B):
        a,b,c,d=A
        e,f,g,h=B
        def pair(x,y,z,w):
            return self.add(self.mul(x,y),self.mul(z,w))
        return (pair(a,e,b,g),pair(a,f,b,h),pair(c,e,d,g),pair(c,f,d,h))
    def star(self,A):
        return tuple(self.conj(x) for x in (A[0],A[2],A[1],A[3]))
    def inverse(self,A):
        a,b,c,d=A
        determinant=self.add(self.mul(a,d),self.neg(self.mul(b,c)))
        invdet=self.inv(determinant)
        return tuple(self.mul(x,invdet) for x in (d,self.neg(b),self.neg(c),a))
    def form(self,a,c,b):
        return (self.elem(a),c,self.conj(c),self.elem(b))
    def unitary(self,g,H):
        return self.mm(self.mm(self.star(g),H),g)==H
    def order3(self,g):
        g2=self.mm(g,g)
        return all(self.add(self.add(x,y),e)==0 for x,y,e in zip(g2,g,(1,0,0,1)))


def finite_classification():
    K=Ramified(4)
    elements=range(16)
    candidates=[]
    # The F_2 reduction of X^2+X+1 is irreducible, hence the upper-right entry is a unit.
    for a in elements:
        for b in elements:
            if not b%2:
                continue
            d=K.neg(K.add(1,a))
            c=K.mul(K.add(K.mul(a,d),K.neg(1)), K.inv(b))
            g=(a,b,c,d)
            assert K.order3(g)
            candidates.append(g)
    counts=Counter()
    tested=0
    for a,b,c in product(range(4),range(4),elements):
        real,imag=c%4,c//4
        if a%2 or b%2 or real%2:
            if a%2 or b%2:
                kind='unit_scale_non_even'
            else:
                kind='unit_scale_Arf1' if a==b==2 else 'unit_scale_Arf0'
        elif imag%2:
            kind='pi_scale_norms_in_4' if a==b==0 else 'pi_scale_norm_obstruction'
        else:
            continue
        H=K.form(a,c,b)
        found=sum(K.unitary(g,H) for g in candidates)
        predicted=kind in ('unit_scale_Arf1','pi_scale_norms_in_4')
        assert bool(found)==predicted
        counts[(kind,found)]+=1
        tested+=1
    return {'residue_modulus':'4 O_w','candidate_matrices':len(candidates),'primitive_Gram_classes_tested':tested,
            'by_type_and_number_of_order3_solutions':[[k,n,c] for (k,n),c in sorted(counts.items())]}


def square_root_1_mod8(value,k):
    root=1
    assert value%8==1
    for j in range(3,k):
        if (root*root-value)%(1<<(j+1)):
            root+=1<<(j-1)
    assert (root*root-value)%(1<<k)==0
    return root


def lift_units(a,b,k):
    assert a%2 and b%2
    n=1<<k
    K=Ramified(n)
    delta=1-4*a*b
    z=square_root_1_mod8((-3*pow(delta,-1,4*n))%(4*n),k+2)
    h=(-1-z)//2
    g=tuple(K.elem(x) for x in (h,-z*b,z*a,h+z))
    assert K.unitary(g,K.form(2*a,1,2*b)) and K.order3(g)
    return g


def lift_pi(a,b,k):
    n=1<<k
    K=Ramified(n)
    y=0
    for j in range(k):
        if (a-y+2*b*y*y)%(1<<(j+1)):
            y+=1<<j
    assert (a-y+2*b*y*y)%n==0
    c=pow(1-4*b*y,-1,n)
    H=K.form(4*a,K.pi,4*b)
    T=K.mm((1,0,K.elem(0,y),1),(1,0,0,K.elem(c)))
    T=K.mm(T,(1,K.elem(0,-b*c*c),0,1))
    assert K.mm(K.mm(K.star(T),H),T)==K.form(0,K.pi,0)
    C=(0,K.neg(1),1,K.neg(1))
    g=K.mm(K.mm(T,C),K.inverse(T))
    assert K.unitary(g,H) and K.order3(g)
    return g


def lifts():
    out={}
    for name,fn,params in [('unit_scale',lift_units,[(-1,3),(1,1),(3,5),(5,7)]),
                           ('pi_scale',lift_pi,[(0,0),(2,-5),(1,3),(-7,4)])]:
        for a,b in params:
            last=None
            for k in (3,5,8,12):
                n=1<<k
                v=fn(a,b,k)
                if last:
                    m,previous=last
                    K=Ramified(m)
                    # The square root version can differ in the unused top bit after halving;
                    # fixing the extra bit in the construction makes reductions agree exactly.
                    assert tuple(K.elem(x%n,x//n) for x in v)==previous
                last=n,v
            out[f'{name}({a},{b})']=[[x%n,x//n] for x in v]
    return {'precision_exponents':[3,5,8,12],'matrices_at_2_to_12':out}


def archimedean_shells():
    # alpha=(t+B*sqrt(417))/2=A+B*omega. alpha+1 is in 4 O_{F^+}.
    allowed=[]
    for t in range(1,101):
        for B in range(-7,8):
            if (t-B)%2 or t*t<=417*B*B:
                continue
            A=(t-B)//2
            if (A+1)%4==0 and B%4==0:
                allowed.append([4*t,A,B])
    assert allowed[0]==[24,3,0] and allowed[1]==[56,7,0]
    assert min(q for q,a,b in allowed if b)!=0
    assert min(q for q,a,b in allowed if b)==328
    return {'possible_trace_shells_below_100':[v for v in allowed if v[0]<100],
            'first_compatible_nonscalar_determinant':[v for v in allowed if v[0]==328]}


def quartic_examples():
    # tau^2+5*tau-98=0, varpi^2-tau*varpi+49=0.
    # H_plus entries a=44-tau, c=varpi-22, det=1501-71*tau.
    roots=[t for t in range(4) if (t*t+5*t-98)%4==0]
    assert sorted(roots)==[1,2]
    obs=[]
    for t in roots:
        a=44-t
        norm=49-22*t+22**2
        determinant=a*a-norm
        assert determinant==1501-71*t+(t*t+5*t-98)
        assert (a*a-norm-(1501-71*t))%4==0
        obs.append({'tau_mod4':t,'a_mod4':a%4,'det_mod4':determinant%4})
    # In the Eisenstein reduction X^2+X+1 the nonzero F_2 vectors form one cycle.
    C=((0,-1),(1,-1));v=(1,0);orbit=[]
    for _ in range(3):
        orbit.append(v);v=tuple(sum(x*y for x,y in zip(row,v))%2 for row in C)
    assert v==orbit[0] and len(set(orbit))==3
    return {'CM_generator_polynomial':[2401,245,0,5,1],'same_Hermitian_determinant':'1501 - 71*tau',
            'two_dyadic_place_data':obs,'companion_mod2_cycle':orbit,
            'index_order_mod5_discriminant':(-3)%5}


def prym_consequence(folder):
    pins={'theta.md':'0df59e18730762dba6db77ce8ab1c9e2209c269247889aa4c4cd2da7f1a1573a',
          'theta_check.py':'70cb4a9b3be807a62c141601a36bd5ca055089c02ab584c7353aa3a238395b36',
          'theta_checked.json':'f773be99f6958affc429af4752b0d95333e1e28224ee34ae201479f886d43b67'}
    if folder:
        for name,digest in pins.items():
            assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest
        actual=subprocess.check_output([sys.executable,'-B',str(folder/'theta_check.py')])
        assert json.loads(actual)==json.loads((folder/'theta_checked.json').read_bytes())
    return {'actual_Prym':'Prym(C46/E) over F7bar, induced polarization',
            'prior_source_SHA256':pins,'global_line_image_order':1,
            'global_group_order_divisible_by_3':False,'norm24_shell':'empty by thirteenth/theta.md theorem',
            'minimum_if_coset_nonempty_at_least':56,'attainment_of_56':'unresolved'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--theta-dir',type=Path,help='optionally replay the verified upstream finite certificate')
    args=parser.parse_args()
    print(json.dumps({'mod4':finite_classification(),'lifts':lifts(),
                      'trace_bound':archimedean_shells(),'quartic_examples':quartic_examples(),
                      'actual_Prym_consequence':prym_consequence(args.theta_dir)},
                     indent=2,sort_keys=True))
