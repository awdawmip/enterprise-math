"""Finite field certificate from actual Regina triangulations; polynomial and DVR counts."""
from collections import defaultdict
from functools import cache
from importlib.metadata import version
from itertools import product
from math import gcd
import argparse
import json
from pathlib import Path

import regina


class Ring:
    """(Z/D)[w]/monic polynomial, in coefficient radix D; tables for small finite rings."""
    def __init__(self,D,poly):
        d=len(poly)
        self.size=D**d
        self.D=D
        self.d=d
        powers=[D**i for i in range(d)]
        self.digits=[[i//w%D for w in powers] for i in range(self.size)]
        def encode(z):
            return sum((x%D)*w for x,w in zip(z,powers))
        def mul(a,b):
            z=[0]*(2*d-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):z[i+j]+=x*y
            for m in range(2*d-2,d-1,-1):
                for i,x in enumerate(poly):z[m-d+i]-=x*z[m]
            return encode(z)
        self.add=[[encode([x+y for x,y in zip(a,b)]) for b in self.digits] for a in self.digits]
        self.mul=[[mul(a,b) for b in self.digits] for a in self.digits]
        self.neg=[encode([-x for x in a]) for a in self.digits]
        self.one=(1,0,0,1)

    def mm(self,A,B):
        a,b,c,d=A;x,y,z,w=B
        m=self.mul;s=self.add
        return (s[m[a][x]][m[b][z]],s[m[a][y]][m[b][w]],
                s[m[c][x]][m[d][z]],s[m[c][y]][m[d][w]])

    def det(self,A):
        a,b,c,d=A
        return self.add[self.mul[a][d]][self.neg[self.mul[b][c]]]

    def inverse(self,A):
        a,b,c,d=A
        return d,self.neg[b],self.neg[c],a

    def power(self,A,n):
        if n<0:return self.power(self.inverse(A),-n)
        out=self.one
        while n:
            if n&1:out=self.mm(out,A)
            A=self.mm(A,A);n//=2
        return out


FIELD={2:(2,(0,)),3:(3,(0,)),4:(2,(1,1)),5:(5,(0,)),7:(7,(0,)),8:(2,(1,1,0)),
       9:(3,(1,0)),11:(11,(0,)),13:(13,(0,)),16:(2,(1,1,0,0)),17:(17,(0,))}


@cache
def field(q):
    return Ring(*FIELD[q])


@cache
def matrices(q):
    R=field(q)
    return [a for a in product(range(q),repeat=4) if R.det(a)==1]


def binder(r):
    if r=='S3': tri=regina.Example3.threeSphere()
    elif r=='P5': tri=regina.Example3.poincare()
    else:
        eps=1 if r%6==1 else -1
        tri=regina.Example3.sfsOverSphere(2,1,3,-1,r,(eps-r)//6)
    sig=tri.isoSig()
    tri=regina.Triangulation3.fromIsoSig(sig)
    assert tri.isoSig()==sig and tri.isClosed() and tri.isConnected() and tri.isValid() and tri.isOrientable()
    assert tri.homology().isTrivial()
    gp=tri.group()
    rels=[[(t.generator,t.exponent) for t in gp.relation(i).terms()] for i in range(gp.countRelations())]
    return dict(isosig=sig,tetrahedra=tri.size(),generators=gp.countGenerators(),relators=rels,
                valid_closed_orientable=True,abelianization='0')


def takes(R,rels,A,B,powersA,powersB):
    for w in rels:
        z=R.one
        for g,n in w:
            z=R.mm(z,powersA[n] if g==0 else powersB[n])
        if z!=R.one:return False
    return True


def generate(R,A,B):
    seen={R.one};frontier=[R.one]
    while frontier:
        x=frontier.pop()
        for a in (A,B):
            z=R.mm(x,a)
            if z not in seen:seen.add(z);frontier.append(z)
    return len(seen)


def count_native(r,q,rec):
    R=field(q); mats=matrices(q); rels=rec['relators']
    assert rec['generators']==2
    exps=[{n for w in rels for j,n in w if j==i} for i in range(2)]
    Btable=[(b,{n:R.power(b,n) for n in exps[1]}) for b in mats]
    classes=defaultdict(list)
    for A in mats:
        a,b,c,d=A
        key=('scalar',a) if b==c==0 and a==d else ('trace',R.add[a][d])
        classes[key].append(A)
    total=0;first=None
    for group in classes.values():
        A=group[0];powersA={n:R.power(A,n) for n in exps[0]}
        for B,powersB in Btable:
            if takes(R,rels,A,B,powersA,powersB):
                total+=len(group)
                if first is None and (A!=R.one or B!=R.one):
                    comm=R.mm(R.mm(R.mm(A,B),R.inverse(A)),R.inverse(B))
                    trace_comm=R.add[comm[0]][comm[3]]
                    assert trace_comm!=R.add[1][1]
                    first=dict(A=A,B=B,image_order=generate(R,A,B),commutator_trace=trace_comm)
    p=FIELD[q][0]
    nroots=(gcd(r,q-1)+gcd(r,q+1)-2)//2+int(r%p==0)
    poly=real_cyclo(r)
    def is_root(x):
        v=0
        for coeff in reversed(poly):v=R.add[R.mul[v][x]][coeff%p]
        return v==0
    assert sum(map(is_root,range(q)))==nroots
    assert total==1+nroots*q*(q*q-1),(r,q,total)
    return dict(q=q,hom_count=total,field_trace_roots=nroots,witness=first)


def lift_witness(q,rec,witness):
    p,poly=FIELD[q]
    R=Ring(p*p,poly); F=field(q)
    def reduce(v):
        return sum((x%p)*p**i for i,x in enumerate(R.digits[v]))
    lift=[[y for y in range(R.size) if reduce(y)==x] for x in range(q)]
    def candidates(A):
        return [m for m in product(*(lift[x] for x in A)) if R.det(m)==1]
    aa=candidates(witness['A']); bb=candidates(witness['B'])
    assert len(aa)==len(bb)==q**3
    rels=rec['relators']
    exps=[{n for w in rels for j,n in w if j==i} for i in range(2)]
    bb=[(b,{n:R.power(b,n) for n in exps[1]}) for b in bb]
    count=0;first=None
    for a in aa:
        pa={n:R.power(a,n) for n in exps[0]}
        for b,pb in bb:
            if takes(R,rels,a,b,pa,pb):
                count+=1
                if first is None:first=[a,b]
    assert count==q**3
    return dict(residue_q=q,coefficient_modulus=p*p,polynomial=list(poly)+[1],
                tested=len(aa)*len(bb),actual_native_lifts=count,first=first)


def real_cyclo(r):
    # Coefficients ascending, U_m(X/2)-U_{m-1}(X/2).
    prev=[0];cur=[1]
    for _ in range((r-1)//2):
        nxt=[0]+cur
        for i,b in enumerate(prev):nxt[i]-=b
        prev,cur=cur,nxt
    for i,b in enumerate(prev):cur[i]-=b
    return cur


def dvr(r,e,unit,k):
    # O=Z_r[pi], pi^e=unit*r.  Enumerate O/pi^k by integral pi-coefficient boxes.
    m=(r-1)//2
    mod=[r**max(0,(k-i+e-1)//e) for i in range(e)]
    assert gcd(r,unit)==1
    poly=real_cyclo(r)
    def evaluate(x):
        z=[0]*e
        for c in reversed(poly):
            t=[0]*(2*e-1)
            for i,u in enumerate(z):
                for j,v in enumerate(x):
                    t[i+j]+=u*v
            t[0]+=c
            for n in range(e,2*e-1):
                t[n-e]+=r*unit*t[n]
            z=[t[i]%mod[i] for i in range(e)]
        return not any(z)
    # Every root must have residue trace -2. Independently enumerate the full residue fibre.
    roots=sum(evaluate(t) for t in product(range((-2)%r,mod[0],r),*(range(v) for v in mod[1:])))
    good=any(pow(z,m,r)==((-1)**(m+1)*pow(unit,-1,r))%r for z in range(1,r))
    expected=(r**(k-(k+m-1)//m) if k<=e else
              (m*r**(e-e//m) if e%m==0 and good else 0))
    assert roots==expected,(r,e,unit,k,roots,expected)
    return dict(r=r,e=e,pi_power_over_r=unit,k=k,moduli=mod,trace_roots=roots)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    rs=[5,7,11,13,17]
    bindings={str(r):binder(r) for r in ['S3','P5']+rs}
    assert bindings['P5']['isosig']=='fvPQcdecedekrsnrs'
    assert bindings['S3']['generators']==0
    checks={}
    for r in rs:
        qs=[q for q in FIELD if q<=r]
        if r<=7:qs.extend(q for q in (8,9,11,13) if q>r)
        checks[str(r)]=[count_native(r,q,bindings[str(r)]) for q in sorted(set(qs))]
        minimum=min(row['q'] for row in checks[str(r)] if row['hom_count']>1)
        assert minimum==(r-1 if ((r-1)&(r-2))==0 else r)
    for r in [25,35]:
        bindings[str(r)]=binder(r)
        checks[str(r)]=[count_native(r,q,bindings[str(r)]) for q in (2,3,4,5,7,8,9,11)]
    old=[count_native(5,q,bindings['P5']) for q in (4,5,9)]
    mixed=[lift_witness(q,bindings['P5'],next(z['witness'] for z in old if z['q']==q)) for q in (4,9)]
    ramified=[dvr(r,e,unit,k) for r,e,unit,last in [(5,2,1,5),(7,1,1,4),(7,3,1,5),(7,3,2,5),(11,2,1,4)] for k in range(1,last+1)]
    result=dict(regina=version('regina'),bindings=bindings,native_counts=checks,
                poincare_named_control=old,mixed_characteristic_native=mixed,
                ramified_trace_counts=ramified,real_cyclotomic={r:real_cyclo(r) for r in rs})
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.out:args.out.write_text(text)
    else:print(text,end='')


if __name__=='__main__':
    main()
