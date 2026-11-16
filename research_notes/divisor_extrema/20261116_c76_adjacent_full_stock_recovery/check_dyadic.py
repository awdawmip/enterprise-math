"""Exact 2-adic linear residuals on affine dyadic gap families, with modular units."""
from fractions import Fraction as F
from math import prod
import json


def v2_int(n):
    return (abs(n) & -abs(n)).bit_length()-1


def v2(x):
    return v2_int(x.numerator)-v2_int(x.denominator)


class Units:
    def __init__(self, bits=15):
        self.bits = bits
        self.mod = 1 << bits
        self.period = self.mod//4
        self.odd = [1]
        for i in range(1, self.mod, 2):
            self.odd.append(self.odd[-1]*i % self.mod)
        assert self.odd[-1] == 1
        self.progression = {}
        for k in (1,3,5):
            row = [1]
            for i in range(1,self.period+1):
                row.append(row[-1]*(4*i+k) % self.mod)
            self.progression[k] = row

    def fraction(self, x):
        a,b=x.numerator,x.denominator
        return (a >> v2_int(a))*pow(b >> v2_int(b),-1,self.mod) % self.mod

    def inverse(self, x):
        return pow(x,-1,self.mod)

    def factorial(self, n):
        u=1
        while n:
            u = u*self.odd[((n % self.mod)+1)//2] % self.mod
            n //= 2
        return u

    def oddprod(self, k, n):
        full, rest=divmod(n,self.period)
        row=self.progression[k]
        return pow(row[-1],full,self.mod)*row[rest] % self.mod

    def visible(self,n,s,k):
        a=F((s+k-1)*rising(n+k+1,3*k),28*(4*s+k-1)*rising(s+k,3*k))
        q,r=n+k,s+k-1
        order = v2(a)+2*(n-s) + (q-q.bit_count())-(r-r.bit_count())
        unit = self.fraction(a)*self.factorial(q)*self.inverse(self.factorial(r))
        unit = unit*self.oddprod(k,s-1)*self.inverse(self.oddprod(k,n)) % self.mod
        return a,(order,unit)

    def tail(self,w):
        q=w+1
        order=2*(w-2)+q-q.bit_count()-1
        unit=self.factorial(q)*self.inverse(3)*self.oddprod(1,2)*self.inverse(self.oddprod(1,w)) % self.mod
        return order,unit


def rising(s,k):
    return prod(range(s,s+k))


def derivatives(a,b,W):
    p,q=1/(1+W/2),1/(1+5*W)
    return (1/(1+b*p)-1/(1+b*q),
            -a*(p/(1+a+b*p)-q/(1+a+b*q)),
            a*b*W*(p/(6*(1+b*p)*(1+a+b*p))-q/(F(3,32)*(1+b*q)*(1+a+b*q))))


def evaluate(engine,gaps):
    first,middle,last=gaps
    c,v,w=sum(gaps)+2,middle+last+2,last+2
    a,t=engine.visible(c,v,5)
    b,s=engine.visible(v,w,3)
    linear=derivatives(a,b,F((w+2)*(w+3)*(w+4),840))
    parts=[(v2(d)+o,u*engine.fraction(d)%engine.mod)
           for d,(o,u) in zip(linear,(t,s,engine.tail(w)))]
    low=min(o for o,_ in parts)
    residue=sum(u*(1<<(o-low)) for o,u in parts if o-low < engine.bits) %engine.mod
    if not residue:
        raise ValueError("insufficient modulus at "+str(gaps))
    return [o for o,_ in parts],low+v2_int(residue)


def main():
    engine = Units()
    examples=[]
    for slopes,offsets in [((1,1,1),(0,0,0)),((1,1,1),(-3,1,1)),((1,2,1),(3,4,3)),((3,3,3),(0,0,0)),((1,1,2),(-2,3,0)),((5,5,5),(0,0,0)),((2,2,2),(6,-2,-4)),((3,2,2),(-10,-4,-4))]:
        rows=[]
        for h in (4,5,6,7,8,12,16,24,40,64,100,128):
            gaps=[a*(1 << h)+b for a,b in zip(slopes,offsets)]
            orders,real=evaluate(engine,gaps)
            common=3*min(slopes)*(1 << h)
            rows.append([h,*[o-common for o in orders],real-common])
        examples.append(dict(slopes=slopes,offsets=offsets,rows=rows))
    print(json.dumps(examples,indent=2))

if __name__=='__main__':
    main()
