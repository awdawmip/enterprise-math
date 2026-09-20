"""Observer-scoped exact quotients of native-X6 carry-peak automata.

Frozen-law lumping preserves time-resolved HIT/UNKNOWN observations. Atomwise
lumping additionally retains original atom channels. Neither makes erased
spatial data available to arbitrary new operations. Krylov coordinates below
are analytic readouts, possibly signed, NEVER positive BRC branch weights.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from sympy import Matrix as SM

from .brc_transport import Affine, eye
from .brc_control_port import ControlPacket
from .brc_control_mass import ControlMassQuotient
from .brc_weighted_recurrent import finite_recurrent_mass_analysis
from .heartbeat_carry_peak import (CarryPeakAutomaton, verify_peak_automaton,
                                    HIT, UNKNOWN)


def _rat(x):
    if isinstance(x, bool) or not isinstance(x, (int, F)):
        raise TypeError('exact int/Fraction required')
    return F(x)


def _canonical(values):
    ids, out = {}, []
    for x in values:
        if x not in ids:
            ids[x] = len(ids)
        out.append(ids[x])
    return tuple(out)


def _mv(a, v):
    return tuple(sum((x*y for x,y in zip(row,v)), F(0)) for row in a)


def _matrix(rows):
    return tuple(tuple(_rat(x) for x in row) for row in rows)


@dataclass(frozen=True)
class PeakChain:
    """Finite stochastic observation process, not a native spatial codec."""
    kernel: tuple
    colors: tuple[str, ...]
    initial: int = 0
    duration: int = 1
    complete: bool = True
    channels: tuple = ()
    source_digest: str = ''

    def __post_init__(self):
        k = _matrix(self.kernel); n = len(k)
        if not n or any(len(row) != n or min(row) < 0 or sum(row) != 1 for row in k):
            raise ValueError('finite row-stochastic exact kernel required')
        if len(self.colors) != n or any(c not in ('SAFE','HIT','UNKNOWN') for c in self.colors):
            raise ValueError('one valid observation per state required')
        if type(self.initial) is not int or not 0 <= self.initial < n:
            raise ValueError('invalid initial state')
        if type(self.duration) is not int or self.duration < 1:
            raise ValueError('positive fixed arrow duration required')
        if type(self.complete) is not bool:
            raise TypeError('complete must be bool')
        for i,c in enumerate(self.colors):
            if c != 'SAFE' and k[i][i] != 1:
                raise ValueError('observation terminal must be absorbing')
        if self.complete and any(k[i][j] for i,c in enumerate(self.colors) if c=='SAFE'
                                 for j,d in enumerate(self.colors) if d=='UNKNOWN'):
            raise ValueError('complete chain cannot have an unresolved successor')
        ch=[]; seen=set()
        for label, mat in self.channels:
            if not isinstance(label,str) or label in seen:
                raise ValueError('unique string channel labels required')
            seen.add(label); mat=_matrix(mat)
            if len(mat)!=n or any(len(row)!=n or min(row)<0 for row in mat):
                raise ValueError('invalid nonnegative channel matrix')
            ch.append((label,mat))
        if ch and any(sum(m[i][j] for _,m in ch)!=k[i][j] for i in range(n) for j in range(n)):
            raise ValueError('channels must sum exactly to kernel')
        object.__setattr__(self,'kernel',k)
        object.__setattr__(self,'colors',tuple(self.colors))
        object.__setattr__(self,'channels',tuple(ch))


def peak_observation_chain(packet: ControlPacket, automaton: CarryPeakAutomaton) -> PeakChain:
    """Retain the exact automaton; add absorbing observation terminals only."""
    verify_peak_automaton(packet,automaton)
    if automaton.initial_hit:
        return PeakChain(((F(1),),),('HIT',),duration=packet.duration,
                         source_digest=sha256(repr(automaton).encode()).hexdigest())
    n=len(automaton.states); size=n+2
    mats={}
    def put(label,s,t,w):
        if label not in mats: mats[label]=[[F(0)]*size for _ in range(size)]
        mats[label][s][t]+=w
    for e in automaton.edges:
        t=n if e.target==HIT else n+1 if e.target==UNKNOWN else e.target
        put('atom:'+str(e.atom),e.source,t,e.mass)
    put('terminal:HIT',n,n,F(1)); put('terminal:UNKNOWN',n+1,n+1,F(1))
    channels=tuple((key,_matrix(value)) for key,value in sorted(mats.items()))
    k=tuple(tuple(sum(m[i][j] for _,m in channels) for j in range(size)) for i in range(size))
    return PeakChain(k,('SAFE',)*n+('HIT','UNKNOWN'),duration=automaton.duration,
                     complete=automaton.complete,channels=channels,
                     source_digest=sha256(repr(automaton).encode()).hexdigest())


@dataclass(frozen=True)
class PeakQuotient:
    source_digest: str
    mode: str
    labels: tuple[int, ...]
    chain: PeakChain
    refinement_rounds: int
    inherited_mass_certificate: bool


def _rows_into_groups(kernel, labels):
    size=1+max(labels)
    return tuple(tuple(sum((row[j] for j in range(len(labels)) if labels[j]==g),F(0))
                       for g in range(size)) for row in kernel)


def _check_lumping(chain,labels,mode):
    if mode not in ('mass','atoms'):
        raise ValueError('mode must be mass or atoms')
    if len(labels)!=len(chain.colors) or any(type(x) is not int or x<0 for x in labels):
        raise ValueError('nonnegative label per state required')
    labels=_canonical(labels)
    if any(len({chain.colors[i] for i,g in enumerate(labels) if g==a})!=1 for a in set(labels)):
        raise ValueError('cannot merge distinct terminal observations')
    channels=(('mass',chain.kernel),) if mode=='mass' else chain.channels
    if not channels:
        raise ValueError('atomwise certification requires original channel matrices')
    for _,kernel in channels:
        rows=_rows_into_groups(kernel,labels)
        for i in range(len(labels)):
            for j in range(i):
                if labels[i]==labels[j] and rows[i]!=rows[j]:
                    raise ValueError('unsafe future merge at states '+str((i,j)))
    return labels


def compile_peak_quotient(chain: PeakChain, *, mode='mass', initial_labels=None) -> PeakQuotient:
    """Coarsest stable partition refining observations and caller labels.

    'mass' fixes the probability law. 'atoms' preserves original channels and
    permits common channel reweighting; it does not support hidden-state policy.
    """
    if mode not in ('mass','atoms'):
        raise ValueError('mode must be mass or atoms')
    n=len(chain.colors)
    if initial_labels is not None and len(initial_labels)!=n:
        raise ValueError('initial partition length mismatch')
    colors=chain.colors if initial_labels is None else tuple(zip(chain.colors,initial_labels))
    labels=_canonical(colors)
    channels=(('mass',chain.kernel),) if mode=='mass' else chain.channels
    if not channels: raise ValueError('no original atom channels available')
    rounds=0
    while True:
        rows=[_rows_into_groups(m,labels) for _,m in channels]
        fresh=_canonical((labels[i],tuple(r[i] for r in rows)) for i in range(n))
        rounds+=1
        if fresh==labels: break
        labels=fresh
    _check_lumping(chain,labels,mode)
    representatives=tuple(labels.index(i) for i in range(1+max(labels)))
    rows=_rows_into_groups(chain.kernel,labels)
    kernel=tuple(rows[i] for i in representatives)
    # Real reuse of the inherited mass certificate. Identity effects here are
    # observation-transport placeholders, not substitutes for spatial actions.
    identity=Affine.identity(6)
    packet=ControlPacket.from_edges(n,0,chain.duration,
        ((i,j,w,identity,1) for i,row in enumerate(chain.kernel) for j,w in enumerate(row) if w))
    inherited=ControlMassQuotient.compile(packet,labels)
    if inherited.quotient_mass_matrix!=kernel:
        raise ArithmeticError('inherited mass quotient mismatch')
    qchannels=()
    if mode=='atoms':
        qchannels=tuple((key,tuple(_rows_into_groups(m,labels)[i] for i in representatives))
                        for key,m in chain.channels)
    q=PeakChain(kernel,tuple(chain.colors[i] for i in representatives),labels[chain.initial],
                chain.duration,chain.complete,qchannels,sha256(repr(chain).encode()).hexdigest())
    return PeakQuotient(sha256(repr(chain).encode()).hexdigest(),mode,labels,q,rounds,True)


def verify_peak_quotient(chain: PeakChain, certificate: PeakQuotient) -> bool:
    if certificate.source_digest!=sha256(repr(chain).encode()).hexdigest():
        raise ValueError('source law changed; recertification required')
    labels=_check_lumping(chain,certificate.labels,certificate.mode)
    reps=tuple(labels.index(i) for i in range(1+max(labels)))
    rows=_rows_into_groups(chain.kernel,labels)
    q=certificate.chain
    expected_channels=()
    if certificate.mode=='atoms':
        expected_channels=tuple((key,tuple(_rows_into_groups(m,labels)[i] for i in reps))
                                for key,m in chain.channels)
    if (q.kernel!=tuple(rows[i] for i in reps) or
        q.colors!=tuple(chain.colors[i] for i in reps) or
        q.initial!=labels[chain.initial] or q.duration!=chain.duration or
        q.complete!=chain.complete or q.channels!=expected_channels):
        raise ValueError('quotient payload mismatch')
    return True


def passage_prefix(chain: PeakChain, steps: int, *, target='HIT') -> tuple[F, ...]:
    if type(steps) is not int or steps<0: raise ValueError('nonnegative horizon required')
    if target not in ('HIT','UNKNOWN'): raise ValueError('invalid target')
    n=len(chain.kernel); mass=[F(0)]*n; mass[chain.initial]=F(1)
    out=[]
    for _ in range(steps+1):
        out.append(sum(mass[i] for i,c in enumerate(chain.colors) if c==target))
        for i,c in enumerate(chain.colors):
            if c!='SAFE': mass[i]=F(0)
        mass=[sum((mass[i]*chain.kernel[i][j] for i in range(n)),F(0)) for j in range(n)]
    return tuple(out)


@dataclass(frozen=True)
class PassageLaw:
    probability: tuple[F, ...]
    first_time_mass: tuple[F, ...]
    conditional_time: tuple[F | None, ...]
    useful_states: int


def passage_law(chain: PeakChain, *, target='HIT', z=F(1)) -> PassageLaw:
    """For z=1, h=P(hit), m=E[arrow_count;hit]. For other z only h is PGF."""
    z=_rat(z)
    if z<0 or target not in ('HIT','UNKNOWN'): raise ValueError('invalid PGF/target')
    n=len(chain.kernel)
    targets={i for i,c in enumerate(chain.colors) if c==target}
    useful=set(targets); pending=list(targets)
    while pending:
        j=pending.pop()
        for i in range(n):
            if chain.colors[i]=='SAFE' and chain.kernel[i][j] and i not in useful:
                useful.add(i); pending.append(i)
    keep=tuple(i for i in sorted(useful) if chain.colors[i]=='SAFE')
    h=[F(i in targets) for i in range(n)]; m=[F(0)]*n
    if keep:
        q=tuple(tuple(z*chain.kernel[i][j] for j in keep) for i in keep)
        b=tuple(z*sum((chain.kernel[i][j] for j in targets),F(0)) for i in keep)
        analysis=finite_recurrent_mass_analysis(q)
        if not analysis.stable or not analysis.verify_stable_certificate():
            raise ValueError('first-passage generating value not certified finite')
        local_h=_mv(analysis.star,b)
        local_m=_mv(analysis.star,local_h)
        for i,a,bv in zip(keep,local_h,local_m): h[i]=a; m[i]=bv
    conditional=tuple(m[i]/h[i] if h[i] and z==1 else None for i in range(n))
    return PassageLaw(tuple(h),tuple(m),conditional,len(keep))


def condition_on_hit(chain: PeakChain) -> tuple[PeakChain, tuple[int, ...]]:
    """Doob h transform: diagnostic conditional law, never changed original law."""
    if not chain.complete:
        raise ValueError('complete automaton required; UNKNOWN is not actual failure')
    h=passage_law(chain).probability
    if h[chain.initial]==0: raise ValueError('cannot condition on zero-probability event')
    keep=tuple(i for i,v in enumerate(h) if v>0)
    index={i:j for j,i in enumerate(keep)}
    k=tuple(tuple(chain.kernel[i][j]*h[j]/h[i] for j in keep) for i in keep)
    channels=tuple((label,tuple(tuple(mat[i][j]*h[j]/h[i] for j in keep) for i in keep))
                   for label,mat in chain.channels)
    return PeakChain(k,tuple(chain.colors[i] for i in keep),index[chain.initial],
                     chain.duration,True,channels,sha256(repr(chain).encode()).hexdigest()),keep


def _fractions(mat):
    return tuple(tuple(F(int(x.p),int(x.q)) for x in row) for row in mat.tolist())


@dataclass(frozen=True)
class FirstPassageModel:
    """Exact Krylov readout. Coordinates/matrix may be signed, not BRC mass."""
    source_digest: str
    safe_indices: tuple[int, ...]
    basis: tuple
    transition: tuple
    output: tuple[F, ...]
    rank: int
    initial_safe_row: int | None
    initial_hit: bool

    def coefficient(self, time: int) -> F:
        if type(time) is not int or time<0: raise ValueError('nonnegative time required')
        if time==0: return F(self.initial_hit)
        if self.initial_hit or self.initial_safe_row is None or not self.rank: return F(0)
        v=self.output
        for _ in range(time-1): v=_mv(self.transition,v)
        return sum((a*b for a,b in zip(self.basis[self.initial_safe_row],v)),F(0))


def compile_first_passage_model(chain: PeakChain) -> FirstPassageModel:
    """Exact observable subspace span{b,Qb,...}; not a positive-state quotient.

    It is complete for first-hit-time law at this threshold and frozen kernel,
    not arbitrary rewards, new thresholds, or chosen atom sequences.
    """
    if not chain.complete: raise ValueError('complete model required')
    safe=tuple(i for i,c in enumerate(chain.colors) if c=='SAFE')
    q=SM([[chain.kernel[i][j] for j in safe] for i in safe])
    b=SM([sum((chain.kernel[i][j] for j,c in enumerate(chain.colors) if c=='HIT'),F(0)) for i in safe])
    columns=[]; v=b
    for _ in range(len(safe)):
        trial=SM.hstack(*(columns+[v]))
        if trial.rank()==len(columns): break
        columns.append(v); v=q*v
    d=len(columns)
    if d:
        basis=SM.hstack(*columns)
        trans= basis.gauss_jordan_solve(q*basis)[0]
        output=basis.gauss_jordan_solve(b)[0]
        if q*basis!=basis*trans or basis*output!=b:
            raise ArithmeticError('Krylov closure certificate failed')
        vb,vt,vo=_fractions(basis),_fractions(trans),tuple(F(int(x.p),int(x.q)) for x in output)
    else:
        vb=tuple(() for _ in safe); vt=(); vo=()
    return FirstPassageModel(sha256(repr(chain).encode()).hexdigest(),safe,vb,vt,vo,d,
                            safe.index(chain.initial) if chain.initial in safe else None,
                            chain.colors[chain.initial]=='HIT')


def distinguishing_first_time(model: FirstPassageModel, left: int, right: int):
    """First separating time, or None proving same all-time first-hit law.

    left/right are rows in safe_indices, not arbitrary spatial Cell addresses.
    """
    n=len(model.safe_indices)
    if any(type(i) is not int or not 0<=i<n for i in (left,right)):
        raise ValueError('safe row index out of range')
    for j in range(model.rank):
        if model.basis[left][j]!=model.basis[right][j]: return j+1
    return None


def killed_debt_risk_timing(continuation, threshold: int) -> dict:
    """Exact risk and conditional timing for stopped symmetric U/V only.

    Original probabilities are c/2, c/2, 1-c. The conditional kernel is a
    diagnostic of paths that eventually hit +/-R, not a proposed new dynamics.
    Units are monitored arrows, not physically calibrated seconds.
    """
    from .heartbeat_carry_peak import killed_symmetric_debt_tail
    c=_rat(continuation)
    if not 0<=c<=1 or type(threshold) is not int or threshold<0:
        raise ValueError('c in [0,1] and nonnegative integer threshold required')
    risk=killed_symmetric_debt_tail(c,threshold)
    if threshold==0:
        return {'risk':risk,'conditional_steps':F(0),'outward_given_hit':()}
    if c==0:
        return {'risk':risk,'conditional_steps':None,'outward_given_hit':()}
    x=1/c; t=[F(1),x]; derivative=[F(0),F(1)]
    for j in range(1,threshold):
        t.append(2*x*t[j]-t[j-1])
        derivative.append(2*t[j]+2*x*derivative[j]-derivative[j-1])
    outward=(F(1),)+tuple(c*t[j+1]/(2*t[j]) for j in range(1,threshold))
    return {'risk':risk,'conditional_steps':x*derivative[threshold]/t[threshold],
            'outward_given_hit':outward}
