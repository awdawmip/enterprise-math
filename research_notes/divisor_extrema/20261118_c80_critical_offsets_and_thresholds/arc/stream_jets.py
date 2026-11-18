"""Implicit Taylor coefficients using a single directed-interval expression graph.
The kth unknowns enter through the same base Jacobian at every k."""
from fractions import Fraction as F
from rational_interval_high import box

def solve_series(m,y,u,n):
    nodes=[]
    class Node:
        def __init__(self,op,parents=(),value=None):
            self.op,self.parents,self.value=op,parents,value
            self.c=[box(0)]*(n+1)
            nodes.append(self)
        def __add__(self,r):
            return Node('add',(self,node(r)))
        __radd__=__add__
        def __sub__(self,r):
            return Node('sub',(self,node(r)))
        def __rsub__(self,r):
            return node(r)-self
        def __mul__(self,r):
            return Node('mul',(self,node(r)))
        __rmul__=__mul__
        def __truediv__(self,r):
            return Node('div',(self,node(r)))
        def __pow__(self,p):
            return Node('pow',(self,),F(p))
        def update(self,k):
            op=self.op
            if op=='input':
                return
            if op=='constant':
                self.c[k]=self.value if k==0 else box(0)
                return
            a=self.parents[0].c
            if op=='pow':
                e=self.value
                if k==0:
                    v=a[0]
                    if e.denominator==4:
                        v=v.sqrt().sqrt()
                    elif e.denominator!=1:
                        raise ValueError(e)
                    q=v**e.numerator
                else:
                    q=sum((((e+1)*j-k)*a[j]*self.c[k-j] for j in range(1,k+1)),box(0))/(k*a[0])
            else:
                b=self.parents[1].c
                if op=='add':
                    q=a[k]+b[k]
                elif op=='sub':
                    q=a[k]-b[k]
                elif op=='mul':
                    q=sum((a[j]*b[k-j] for j in range(k+1)),box(0))
                elif op=='div':
                    q=(a[k]-sum((b[j]*self.c[k-j] for j in range(1,k+1)),box(0)))/b[0]
            self.c[k]=q
    def node(a):
        return a if isinstance(a,Node) else Node('constant',value=box(a))
    def fields(x,y):
        a=4*x**F(15,4)
        d=4*(y/x)**F(9,4)
        b=F(7,16)*a**5
        ell=F(7,16)*d**5
        center=x**9/((1+112*x**15)*y**12)
        signed=b*ell*(1-a)*(1-d)/(y**F(3,4)*(1+b*d)*(a+b*d))
        return center,signed
    M,Y,U=[Node('input') for _ in range(3)]
    left=fields(1-M,Y)
    right=fields(U,U-M)
    eq=[a-b for a,b in zip(left,right)]
    M.c[0],Y.c[0],U.c[0]=m,y,u
    def eval_at(k,mm,yy,uu):
        M.c[k],Y.c[k],U.c[k]=box(mm),box(yy),box(uu)
        for v in nodes:
            v.update(k)
        return [r.c[k] for r in eq]
    eval_at(0,m,y,u)
    a=eval_at(1,0,1,0)
    b=eval_at(1,0,0,1)
    det=a[0]*b[1]-a[1]*b[0]
    for k in range(1,n+1):
        mm=int(k==1)
        q,r=eval_at(k,mm,0,0)
        yy=(b[0]*r-b[1]*q)/det
        uu=(a[1]*q-a[0]*r)/det
        eval_at(k,mm,yy,uu)
    return M.c,Y.c,U.c
