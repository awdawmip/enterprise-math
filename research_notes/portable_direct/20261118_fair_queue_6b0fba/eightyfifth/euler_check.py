"""Exact same-world Euler pair law. Pass --repo to a checkout containing the pinned public sources."""
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha1
from itertools import product
import json
from math import isqrt
from pathlib import Path
import sys

PINS = {
    'research_tasks/RS-EULER-RR-07-IDENTIFICATION-20261011.md': '27319d43d0003d348f1f416a131f81d4a42a04fd',
    'research_notes/chatgpt_direct/20261010_EULER_PASSIVE_SAMPLING_AND_NOISE.md': 'bd80290c259cc60995069613a5f4b5f5b41a13d1',
    'research_notes/chatgpt_direct/20261010_EULER_TEMPORAL_APERTURE_AND_IDENTIFIABILITY.md': 'b25208a5b812e9345622d88275c806130e628391',
    'research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md': '03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b',
    'research_notes/chatgpt_direct/20261011_EULER_READOUT_BACKACTION.md': '5e00414f752d97d69cee9bf602fd6b5e50da4b05',
    'src/enterprise_math/brc_weighted.py': '3f205696709e847909958a153f8fe10d3f6b70f0',
    'src/enterprise_math/brc_logarithm.py':'4732e5fc381ce613d240c4381ccbef03c27a69c7',
    'src/enterprise_math/exact_arithmetic.py':'35ea95b0916494b83a92386e3e313928362dd79e',
}

@dataclass(frozen=True)
class Eisenstein:
    a: F
    b: F=F(0)
    def __add__(self,z):
        return Eisenstein(self.a+z.a,self.b+z.b)
    def __sub__(self,z):
        return Eisenstein(self.a-z.a,self.b-z.b)
    def __mul__(self,z):
        return Eisenstein(self.a*z.a-self.b*z.b,self.a*z.b+self.b*z.a-self.b*z.b)
    def conj(self):
        return Eisenstein(self.a-self.b,-self.b)
    def norm2(self):
        return self.a*self.a-self.a*self.b+self.b*self.b
    def __truediv__(self,z):
        p=self*z.conj()
        return Eisenstein(p.a/z.norm2(),p.b/z.norm2())
    def real(self):
        return self.a-self.b/2
    def json(self):
        return [str(self.a),str(self.b)]

one=Eisenstein(F(1))
zero=Eisenstein(F(0))
w=Eisenstein(F(0),F(1))
units=(one,w,w*w)

def sqrtq(x):
    q=F(isqrt(x.numerator),isqrt(x.denominator))
    assert q*q==x
    return q

def gate(atom,cmd):
    j,s,field,writer,theta=atom
    if cmd=='H':
        if writer in (0,3) and theta==0:
            return j,s,field^3,3-writer,theta
    elif cmd=='U':
        return j,s^((field>>1)&1),field^7,writer,theta^int(writer in (1,3))
    elif cmd=='C':
        return (j+(-1)**s)%3,s,field,writer,theta
    elif cmd=='B':
        # Two U1 loops restore the field and flip the probe sheet.
        return j,s^1,field,writer,theta
    else:
        raise ValueError(cmd)
    return atom

def cycle(x):
    for c in 'HUC':
        x=gate(x,c)
    return x

def write(j,a,r):
    # E is a composition of zero, one or two positive contacts in a fixed receiver frame.
    for _ in range((j-a)%3):r=(r+1)%3
    return r

def trajectory():
    x=(0,0,2,0,0)
    states=[x]
    for _ in range(30):states.append(cycle(states[-1]))
    assert states[6]==(1,1,2,0,0) and states[12]==x and len(set(states[:12]))==12
    assert [states[1][0],cycle(gate(x,'B'))[0],states[5][0]]==[1,2,2]
    return [z[0] for z in states]

def model(pi,lam,q):
    u=[[(1-lam)*q[(j-s)%3]+lam*q[(j-(1-s))%3] for j in range(3)] for s in range(2)]
    return [[(1-pi)*u[0][i]*u[0][j]+pi*u[1][i]*u[1][j] for j in range(3)] for i in range(3)]

def actual_pair(brc,traj,pi,lam,q):
    law=[[brc.CWM_ZERO for j in range(3)] for i in range(3)]
    for s,d,e,b,c in product(range(2),range(2),range(2),range(3),range(3)):
        weights=[(1-pi,pi)[s],(1-lam,lam)[d],(1-lam,lam)[e],q[b],q[c]]
        if not all(weights): continue
        i=write(traj[6*(s+d)],0,b)
        j=write(traj[12+6*(s+e)],0,c)
        path=brc.CWM_ONE
        for mass in weights:path=brc.cwm_propagate(path,brc.cwm_edge(mass))
        law[i][j]=brc.cwm_recoalesce(law[i][j],path)
    return [[z.total for z in row] for row in law],sum(z.count for row in law for z in row)

def moments(P):
    M=sum((Eisenstein(sum(P[i]))*units[i] for i in range(3)),zero)
    second=sum((Eisenstein(P[i][j])*units[(i+j)%3] for i,j in product(range(3),repeat=2)),zero)
    conjugate=sum((Eisenstein(P[i][j])*units[(i-j)%3] for i,j in product(range(3),repeat=2)),zero)
    K=second-M*M
    assert conjugate-M*M.conj()==Eisenstein(sqrtq(K.norm2()))
    return M,K

def recover(M,K):
    abs_k=sqrtq(K.norm2())
    Q=(M-K/Eisenstein(abs_k)*M.conj())/(one+w)
    q=[(1+2*(Q*u.conj()).real())/3 for u in units]
    A=(one-w)*Q
    t=2*(M*A.conj()).real()/A.norm2()
    b=sqrtq(t*t+4*abs_k/A.norm2())
    return (1-t/b)/2,(1-b)/2,q

def frozen_three_readers():
    grid=[(F(i,6),F(j,6),F(6-i-j,6))
          for i in range(7) for j in range(7-i)]
    classes={}
    tested=two=three=0
    for src,q in product(grid,repeat=2):
        U=sum((Eisenstein(a)*u for a,u in zip(src,units)),zero)
        Z=sum((Eisenstein(a)*u for a,u in zip(q,units)),zero)
        sums=[F(0)]*3
        second=[F(0)]*3
        diff=[F(0)]*3
        triple=[F(0)]*3
        for j,b,c,e in product(range(3),repeat=4):
            mass=src[j]*q[b]*q[c]*q[e]
            x,y,z=((j+k)%3 for k in (b,c,e))
            sums[x]+=mass;second[(x+y)%3]+=mass
            diff[(x-y)%3]+=mass; triple[(x+y+z)%3]+=mass
        M,T,H,J=[sum((Eisenstein(a)*w for a,w in zip(row,units)),zero)
                 for row in (sums,second,diff,triple)]
        assert (M,T,H,J)==(U*Z,U.conj()*Z*Z,Eisenstein(Z.norm2()),Z*Z*Z)
        if M!=zero:
            assert T/M.conj()*H==J
            two+=1
        if Z!=zero:
            three+=1
            orbit=min(tuple(src[(i-h)%3] for i in range(3))
                      +tuple(q[(i+h)%3] for i in range(3)) for h in range(3))
            key=(M,T,H,J)
            assert classes.setdefault(key,orbit)==orbit
        tested+=1
    return dict(grid_pairs=tested,two_read_generic=two,three_read_nonuniform=three,
                distinct_observable_orbits=len(classes))


def main(repo):
    for name,pin in PINS.items():
        b=(repo/name).read_bytes()
        assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    tr=trajectory()
    count=good=degenerate=tagged=0
    for u,v in product(range(7),repeat=2):
        if u+v>6:continue
        q=[F(u,6),F(v,6),F(6-u-v,6)]
        for i,j in product(range(7),repeat=2):
            pi,lam=F(i,6),F(j,6)
            law=model(pi,lam,q);M,K=moments(law)
            count+=1
            assert K==zero if (pi in (0,1) or lam==F(1,2) or len(set(q))==1) else K!=zero
            if 0<lam<1 and len(set(q))>1:
                e=[]
                for delay in (0,1):
                    probs=[(1-pi)*q[(r-delay)%3]+pi*q[(r-1+delay)%3] for r in range(3)]
                    e.append(sum((Eisenstein(mass)*phase for mass,phase in zip(probs,units)),zero))
                Q=(e[0]+e[1])/(one+w)
                a=(e[0]-e[1])/((one-w)*Q)
                assert a==Eisenstein(1-2*pi)
                assert [(1+2*(Q*u.conj()).real())/3 for u in units]==q
                tagged+=1
            if K==zero:
                degenerate+=1
                means=[sum(r) for r in law]
                assert law==[[x*y for y in means] for x in means]
            else:
                good+=1
                assert recover(M,K)==((1-pi if lam>F(1,2) else pi),min(lam,1-lam),q)
                assert model(1-pi,1-lam,q)==law
    q=[F(1,2),F(1,3),F(1,6)]
    examples=[]
    for pi,lam in [(F(1,4),F(1,4)),(F(3,8),F(0)),(F(1,3),F(1,2)),(F(0),F(1,3))]:
        law,paths=actual_pair(brc,tr,pi,lam,q)
        assert law==model(pi,lam,q) and sum(map(sum,law))==1
        M,K=moments(law)
        examples.append(dict(pi=str(pi),lam=str(lam),paths=paths,pair=[[str(x) for x in r] for r in law],
                             M=M.json(),K=K.json()))
    assert examples[0]['M']==examples[1]['M'] and examples[0]['K']!=examples[1]['K']
    # One labeled read: independent fair source + clock with this alternative calibration
    # versus a perfect match D=S (clock and initial source correlated).
    correlated_q=[F(2,5),F(3,10),F(3,10)]
    independent_q=[F(2,5),F(1,5),F(2,5)]
    tagged_law=[]
    for d in range(2):
        row=[(independent_q[(y-d)%3]+independent_q[(y-1+d)%3])/4 for y in range(3)]
        assert row==[x/2 for x in correlated_q]
        tagged_law.append([str(x) for x in row])
    tv=sum(abs(q[(j-1)%3]-q[(j-2)%3]) for j in range(3))/2
    assert tv==F(1,3)
    return dict(frozen_source_control=frozen_three_readers(),tagged_identifiable=tagged,one_tag_counterexample=tagged_law,period12=tr[:12],half_shift_labels=[tr[0],tr[6]],exact_rational_models=count,
                identifiable=good,degenerate=degenerate,positive_CWM=examples,
                randomized_feedback=dict(total_variation=str(tv),hold_j=tr[1],feedback_j=cycle(gate((0,0,2,0,0),'B'))[0],
                                         mimic_clock_only_at_round5=tr[5]))

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    print(json.dumps(main(ap.parse_args().repo),indent=2,sort_keys=True))
