"""F7 r457: exact Fraction certificate of Ω4 old-axis graph + two mixed witnesses."""
from fractions import Fraction as F
from math import gcd

def check(e):
    a,b=1-e,F(1,2)-e
    V={(x,s*t) for t in (1,2,3) for s in (-1,1)
       for x in range(1,11) if gcd(x,t)==1}
    E={frozenset(((x,t),(y,-t))) for t in (1,2,3)
       for x in range(1,11) for y in range(1,11)
       if (x,t) in V and (y,-t) in V
       and (abs(x-y)==3*t or (t>=2 and x+y==3*t))}
    assert (len(V),len(E))==(44,29)
    adj={p:set() for p in V}
    for edge in E:
        p,q=tuple(edge)
        adj[p].add(q);adj[q].add(p)
    values={}
    marks={(2,1),(1,-1)}
    unseen=set(V)
    npaths=0
    while unseen:
        found={min(unseen)}; stack=list(found)
        while stack:
            for p in adj[stack.pop()]-found:
                found.add(p);stack.append(p)
        unseen-=found
        ends=sorted(p for p in found if len(adj[p])==1)
        assert len(ends)==2
        path=[ends[0]]
        while len(path)<len(found):
            nxt=adj[path[-1]]-set(path)
            assert len(nxt)==1
            path.append(next(iter(nxt)))
        npaths+=1
        if path[-1] in marks: path.reverse()
        if path[0] in marks:
            values[path[0]]=F(0);values[path[1]]=a
            path=path[2:]
        n=len(path)
        if n:
            lo=F(n//2,n)*a; hi=F(n-n//2,n)*a
            for i,p in enumerate(path): values[p]=lo if i%2==0 else hi
    assert npaths==15
    base=sum(t*t for t in values.values())
    assert base==F(67,6)*a*a

    if e<=F(11,20):
        x=F(4,9)*a;y=x-b;c=x+b
        la=F(4,3)*a+6*b;mu=F(2,3)*a+6*b
    else:
        x=(a+b)/2;y=(a-b)/2;c=a/3
        la=a+3*b;mu=F(0)
    values.update({(3,1):x,(6,-1):a-x,(9,1):x,
                   (5,-2):a-y,(1,2):y,(7,-2):a-y,
                   (5,2):c,(1,-2):a-c,(7,2):c})
    assert 0<=x<=a/2 and 0<=c<=a/2 and 0<=y<=a
    assert la>=0 and mu>=0 and x-y>=b and c-x>=b
    assert 6*x-2*a-la+mu==0
    assert 6*y-4*a+la==0
    assert 6*c-2*a-mu==0
    assert la*(x-y-b)==mu*(c-x-b)==0
    assert all(values[p]+values[q]>=a for p,q in map(tuple,E))
    assert min(values.values())>=0
    assert all(values[p]==0 for p in marks)

    def q(pt):
        x,y=pt
        if x==y==0:return F(0)
        if y==0:return F(1)
        return F(1,2)+values[abs(x),y]
    for z in ((-4,0,-1,2),(3,0,3,1)):
        k=z[0]-2*z[1]-z[2]+2*z[3]
        az=(z[0]+k,z[1]+k,z[2]-k,z[3]-k)
        D=q(az[:2])+q(az[2:])-q(z[:2])-q(z[2:])
        assert abs(D)<=e
    en=sum(t*t for t in values.values())
    gap=max(F(0),a+9*b)**2/18
    assert en==base+(a+3*b)**2/6+gap
    return en,gap

if __name__=="__main__":
    for e in (F(1,2),F(21,40),F(13,24),F(11,20),F(9,16),F(4,7)):
        value,gap=check(e)
        print(e,value,gap)
