"""R72 minimal exact arithmetic reproduction (not the full treap stress test)."""
from fractions import Fraction as Q
from dataclasses import dataclass

def fl(x): return x.numerator // x.denominator
def ce(x): return -fl(-x)
def floors(a,b,L,U):
    ka,kb=fl(a*L),fl(b*L)
    assert fl(a*U)==ka and fl(b*U)==kb
    assert a*L-ka < b*L-kb and a*U-ka < b*U-kb
    return ka,kb

def feasible(I,m,c,n,d):
    # m*theta+c >= 0; n*theta+d < 0, retaining the open upper boundary.
    L,U=I; opL=opU=False
    if m==0:
        if c<0: return None
    elif m>0:
        z=-c/m
        if z>L:L=z;opL=False
    else:
        z=-c/m
        if z<U:U=z;opU=False
    if n==0:
        if d>=0: return None
    elif n>0:
        z=-d/n
        if z<U:U=z;opU=True
        elif z==U:opU=True
    else:
        z=-d/n
        if z>L:L=z;opL=True
        elif z==L:opL=True
    if L>U or (L==U and (opL or opU)):return None
    return (L+U)/2 if L<U else L

def witness(t,j,x,a,b,I):
    L,U=I;ka,kb=floors(a,b,L,U);d=t-j
    lower=min(x+(d-b)*L+kb,x+(d-b)*U+kb)
    upper=max(x+(d-a)*L+ka,x+(d-a)*U+ka)
    for k in range(fl(lower)+1,fl(upper)+1):
        z=feasible(I,Q(d-a),x+ka-k,Q(d-b),x+kb-k)
        if z is not None:
            assert a*z%1 <= (x+d*z)%1 < b*z%1
            return z
    return None

@dataclass(frozen=True)
class Version:
    anchor: Q
    records: tuple
    def change(self,event,add):
        s=set(self.records)
        if add:s.add(event)
        else:s.discard(event)
        return Version(self.anchor,tuple(sorted(s)))
    def classes(self):
        groups={}
        for t,br in self.records:
            groups.setdefault(t*self.anchor.numerator%self.anchor.denominator,[]).append((t,br))
        return groups

def out_group(events,r,anchor,j,x,a,b,I):
    ka,kb=floors(a,b,*I);L,U=I
    lo=min(t for t,_ in events);hi=max(t for t,_ in events)
    base=Q(r,anchor.denominator)+x-j*anchor
    deviations=[(t-j)*(theta-anchor) for t in (lo,hi) for theta in I]
    slo,shi=base+min(deviations),base+max(deviations)
    qlo=min(a*L-ka,a*U-ka);qhi=max(b*L-kb,b*U-kb)
    return ce(slo-qhi)>fl(shi-qlo)

def query(v,j,x,a,b,I):
    for r,group in v.classes().items():
        if out_group(group,r,v.anchor,j,x,a,b,I):continue
        for t,br in group:
            z=witness(t,j,x,a,b,I)
            if z is not None:return 'EXISTS_MEMBER',(t,br),z
    return 'ALL_OUT',None,None

def run():
    a=Version(Q(1,4),tuple())
    history=[a]
    for k in range(1,33):
        for t in (4*k,4*k-1):
            a=a.change((t,str(k)),True);history.append(a)
    I=(Q(1,4)-Q(1,3200),Q(1,4)+Q(1,3200))
    assert len(a.classes())==2
    assert query(a,0,Q(0),1,2,I)[0]=='ALL_OUT'
    old=a
    a=a.change((128,'32'),False)
    assert (128,'32') in old.records and (128,'32') not in a.records
    assert query(a,0,Q(0),1,2,I)[0]=='ALL_OUT'
    a=a.change((4,'same-time-second-branch'),True)
    a=a.change((4,'1'),False)
    assert (4,'same-time-second-branch') in a.records
    assert witness(1,0,Q(0),1,2,(Q(1,4),Q(1,4)))==Q(1,4)
    assert witness(2,0,Q(0),1,2,(Q(1,4),Q(1,4))) is None
    v=Version(Q(1,10),((1,'a'),(9,'a')))
    w=v.change((5,'b'),True)
    J=(Q(99,1000),Q(101,1000))
    assert query(v,0,Q(0),4,6,J)[0]=='ALL_OUT'
    assert query(w,0,Q(0),4,6,J)[0]=='EXISTS_MEMBER'
    print('R72_MIN_PASS',len(history),'two phase groups','strict endpoints','identity preservation','four-extrema witness')

if __name__=='__main__':run()
