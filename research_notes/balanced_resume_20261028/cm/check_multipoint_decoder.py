"""Exact finite regressions for the new decoder, not a proof for all primes."""
import json
from math import comb
from pathlib import Path
import sympy as sp


class Field:
    def __init__(self, p, f):
        self.p, self.f, self.e = p, f, len(f)-1
        self.zero = (0,)*self.e
        self.one = self.make([1])
    def make(self, a):
        a = [v % self.p for v in a]+[0]*max(0, self.e-len(a))
        for j in range(len(a)-1, self.e-1, -1):
            for k in range(self.e):
                a[j-self.e+k] = (a[j-self.e+k]-a[j]*self.f[k]) % self.p
        return tuple(a[:self.e])
    def add(self, a, b):
        return tuple((u+v) % self.p for u,v in zip(a,b))
    def neg(self, a):
        return tuple(-v % self.p for v in a)
    def mul(self, a, b):
        out = [0]*(2*self.e-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b): out[i+j] += u*v
        return self.make(out)
    def scale(self, a, n): return tuple(v*n % self.p for v in a)
    def power(self, a, n):
        out = self.one
        while n:
            if n&1: out = self.mul(out,a)
            a = self.mul(a,a); n >>= 1
        return out
    def inv(self,a):
        assert a != self.zero
        return self.power(a, self.p**self.e-2)
    def trace(self,a):
        out=self.zero
        for j in range(self.e): out=self.add(out,self.power(a,self.p**j))
        assert all(v==0 for v in out[1:])
        return out[0]


def decoder(p,a,d):
    x=sp.Symbol('x')
    if a==0: f=[0,1]
    elif a==1: f=[-4 % p,1]
    else:
        factors=sp.factor_list(x**3-6*x*x+9*x-4*a,modulus=p)[1]
        # Largest degree deliberately exercises quadratic as well as cubic fields.
        chosen=max(factors,key=lambda pair:sp.degree(pair[0],x))[0]
        cs=[int(v)%p for v in sp.Poly(chosen,x).all_coeffs()]
        cs=[v*pow(cs[0],-1,p)%p for v in cs]
        f=list(reversed(cs))
    E=Field(p,f); alpha=E.make([0,1]); k4=pow(4,-1,p)
    am3=E.add(alpha,E.make([-3])); deninv=E.inv(am3)
    lam=E.scale(E.mul(E.add(alpha,E.make([-1])),am3),3*k4)
    mu=E.scale(E.add(alpha,E.make([-2])),3*k4)
    nu=E.make([k4]); invlam=E.inv(lam)
    A=[[E.zero for j in range(d)] for k in range(d)]
    A[0][0]=E.one
    for j in range(1,d):
        for k in range(j,d):
            for h,c in [(1,lam),(2,mu),(3,nu)]:
                if k>=h: A[k][j]=E.add(A[k][j],E.mul(c,A[k-h][j-1]))
    def run(q):
        # Truncated Horner evaluation of Q_T(alpha+t), including alpha=0.
        ser=[E.zero for _ in range(d)]
        for c in reversed(q):
            ser=[E.add(E.mul(alpha,ser[k]),ser[k-1] if k else E.make([c])) for k in range(d)]
        R=[]
        for k in range(d):
            b=E.scale(ser[k],24)
            if k: b=E.add(b,E.neg(R[-1]))
            R.append(E.mul(deninv,b))
        ls=[]
        for k in range(d):
            b=R[k]
            for j in range(k): b=E.add(b,E.neg(E.mul(A[k][j],ls[j])))
            ls.append(E.mul(E.power(invlam,k),b))
        return [E.trace(v)*pow(E.e,-1,p)%p for v in ls]
    return run,E.e,f


def main():
    output={'status':'FINITE_EXACT_REGRESSION_ONLY','cases':[],'field_degrees_seen':[],'claims_checked':0}
    degrees=set()
    for p in [13,19,37,43]:
        m=(p-1)//6; N=3*m
        # Single endpoints cover all a and all jets within the original D<=m range.
        for a in range(p):
            run,e,f=decoder(p,a,m); degrees.add(e)
            count=0
            for j in range(p-1):
                if j==N: continue
                q=[0]*(3*j+2)
                u=pow(24*pow(4,j,p),-1,p)
                for s in range(2*j+2):
                    q[j+s]=comb(2*j+1,s)*pow(-3,2*j+1-s,p)*u%p
                central=[v if N<=k<=2*N else 0 for k,v in enumerate(q)]
                outer=[(v-central[k])%p for k,v in enumerate(q)]
                got=[(u+v)%p for u,v in zip(run(central),run(outer))]
                expected=[comb(j,k)*pow(a,j-k,p)%p if k<=j else 0 for k in range(m)]
                assert got==expected,(p,a,j,e,got,expected)
                count+=m
            output['claims_checked']+=count
            output['cases'].append({'p':p,'endpoint':a,'jet_count':m,'extension_degree':e,'modulus_ascending':f,'monomial_scalar_equalities':count})
    output['field_degrees_seen']=sorted(degrees)
    assert degrees=={1,2,3}
    # Each actual multipoint map is concatenation of checked per-point maps;
    # this finite run does not assert universal linear independence from samples.
    output['result']='PASS'
    out=Path(__file__).with_name('multipoint_decoder_check.json')
    out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='cases'},indent=2))


if __name__=='__main__': main()
