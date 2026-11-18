"""EC49DE finite exhaustive test, imports existing canonical VERIFY_EC49DD.py.
Run beside that file: python3 VERIFY_EC49DE_COMPACT.py
"""
from collections import defaultdict
from itertools import product
import VERIFY_EC49DD as E

M = ((-3,3,-3,3,-3,3),(-1,1,-2,2,-1,1),(-2,2,-1,1,-2,2),
     (-3,1,2,-2,-1,3),(-3,2,1,-1,-2,3),(-1,1,2,1,-1,-2))
MOD=1000003

def rank(rows,cols):
    basis={}
    for v in rows:
        w=[int(a)%MOD for a in v]
        for j,b in sorted(basis.items()):
            if w[j]:
                q=w[j];w=[(a-q*c)%MOD for a,c in zip(w,b)]
        j=next((j for j,a in enumerate(w) if a),None)
        if j is None:continue
        w=[a*pow(w[j],-1,MOD)%MOD for a in w]
        basis[j]=w
        for i,b in list(basis.items()):
            if i!=j and b[j]:
                q=b[j];basis[i]=[(a-q*c)%MOD for a,c in zip(b,w)]
        assert len(basis)<=cols
    return len(basis)

def paths(h,s,v):
    d=h-abs(s)-v;assert d>=0
    if s>0 and v>0 and d==0:
        a=(1,)*(2*s);b=(2,)*(2*v);g=(-3,3)
        p=[a+g+b+g*2,a+b+g*3,b+a+g*3,
           (1,2)+(1,)*(2*s-1)+(2,)*(2*v-1)+g*3]
        assert [E.tag(x) for x in p]==[0,2,1,3]
    else:
        base=((1 if s>=0 else -1),)*(2*abs(s))+(-3,3)*d+(2,)*(2*v)
        assert E.tag(base)==0
        p=[base+m for m in M]
        assert [E.tag(x) for x in p]==[0,0,0,2,1,3]
        assert p[1][-1]==1 and p[2][-1]==2
    assert all(len(x)==2*h+6 and E.endpoint(x)==(2*s,2*v,0,0,0,0) for x in p)
    return p

def suffixes(h):
    groups=defaultdict(list)
    for seq in product('abcde',repeat=h):
        q=E.word(''.join(seq));groups[E.endpoint(q)[:2]].append(q)
    return groups

def test():
    assert all(len(x)==6 and E.endpoint(x)==(0,)*6 for x in M)
    all_s={j:suffixes(j) for j in range(1,8)}
    out={};fibers=rows=0
    for h in range(2,8):
        cumulative=defaultdict(list)
        for j in range(1,h+1):
            for d,L in all_s[j].items():cumulative[d].extend(L)
        sums=[0,0]
        for s in range(-h,h+1):
            for v in range(h-abs(s)+1):
                p=paths(h,s,v);d=h-abs(s)-v;fibers+=1
                for z,groups in enumerate((all_s[h],cumulative)):
                    def observations():
                        nonlocal rows
                        for suffix in groups[(-2*s,-2*v)]:
                            tags=[E.tag(x+suffix) for x in p]
                            for t in range(4):
                                rows+=1
                                yield [int(k==t) for k in tags]
                    got=rank(observations(),len(p))
                    want=4 if d==0 else 6 if (z==1 or d%2==0) else 5
                    assert got==want,(h,s,v,z,got,want)
                    sums[z]+=got
        assert sums==[(11*h*h+15*h+8)//2,6*h*h+8*h+4]
        out[h]={'exact':sums[0],'cumulative':sums[1]}
    print({'status':'PASS','all_h':'2..7','fibers':fibers,'rows':rows,
           'complete_operation_words':sum(5**j for j in range(1,8)),'dimensions':out})
if __name__=='__main__':test()
