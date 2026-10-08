"""U10: uncached trail communication and work-clock observers of U9.

These are candidate algorithms/comparison observers, NOT native force, energy,
physical time or a complete distributed implementation. Existing BRC is pinned.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
import hashlib, importlib.util, sys

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'local_latent.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261008_cell_u9_local_latent_4b7e62'/'local_latent.py'
raw=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='67408af5b977bed7295f7225cdd3f550c41b9729':
    raise RuntimeError('U9 source pin mismatch')
spec=importlib.util.spec_from_file_location('u10_pinned_u9',SRC)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
r,u=m.r,m.u
ZERO,ONE=r.brc.CWM_ZERO,r.brc.CWM_ONE


def distance(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def slots(s):
    """Occurrence-local encoding. Pointer names are identities, not hashes.

    A slot stores its next port, predecessor/successor occurrence identifiers.
    It does not store a remote word value or equality certificate at its head.
    End sentinels are explicit. Inputs remain immutable during a comparison.
    """
    out={}
    for i,j,wa,wb in s.links:
        for side,word in enumerate((wa,wb)):
            z=s.cells[(i,j)[side]]
            for k in range(len(word)+1):
                key=(i,j,side,k)
                datum=(None if k==len(word) else word[k],
                       None if k==0 else (i,j,side,k-1),
                       None if k==len(word) else (i,j,side,k+1))
                out[key]=(z,datum)
                if k<len(word): z=r.advance(z,word[k])
    return out


def header(s):
    return (s.cells,s.tree(),s.length(),
            tuple((i,j,len(a),len(b),m.endpoint(s.cells[i],a)) for i,j,a,b in s.links))


def local_view(s,center,radius):
    if radius<0: raise ValueError('negative radius')
    return tuple(sorted((key,z,datum) for key,(z,datum) in slots(s).items()
                        if distance(z,center)<=radius))


def distant_pair(radius):
    """Same original four actors, same headers; only a remote detour differs."""
    if type(radius) is not int or radius<0:raise ValueError('integer radius required')
    z=r.ZERO;e1=r.direction(0);e2=r.direction(2)
    cells=(z,e1,tuple(x+y for x,y in zip(e1,e2)),e2)
    h=radius+2
    w=(4,)*h+(6,7)+(5,)*h
    v=(4,)*h+(7,6)+(5,)*h
    table={(0,1):((0,),w),(1,2):(w,(3,)),(2,3):((1,),())}
    p=m.make(cells,table)
    table2=dict(table);table2[1,2]=(v,(3,));q=m.make(cells,table2)
    m.validate(p);m.validate(q)
    return p,q,h


def compare_trails(s,first=(0,1,1),second=(1,2,0)):
    """Execute a read/one-edge-hop comparison plus an explicit return trace.

    One forward tick reads the two co-located next symbols and traverses their
    shared edge. A deciding tick reads the mismatch/end; the return token then
    retraces every shared edge. This conservative protocol need not be fastest.
    No native update or tree slide is committed by this function.
    """
    data=slots(s)
    i,j,side=first;a,b,other=second
    origin=s.cells[(i,j)[side]]
    if origin!=s.cells[(a,b)[other]]:raise ValueError('common starting Cell required')
    z=origin;prefix=[];trace=[];budget=ONE;unit=r.edge(1);k=0
    while True:
        x,dx=data[i,j,side,k];y,dy=data[a,b,other,k]
        if x!=z or y!=z:raise AssertionError('nonlocal cursor read')
        p,q=dx[0],dy[0]
        if p!=q or p is None:
            equal=(p is None and q is None)
            trace.append(('DECIDE',z,k,p,q,equal))
            budget=r.serial(budget,unit)
            break
        zz=r.advance(z,p)
        trace.append(('READ_HOP',z,zz,k,p))
        budget=r.serial(budget,unit)
        prefix.append(p);z=zz;k+=1
    for p in reversed(prefix):
        zz=r.advance(z,p^1)
        trace.append(('RETURN',z,zz,p^1))
        budget=r.serial(budget,unit);z=zz
    if z!=origin:raise AssertionError('acknowledgement did not return')
    return {'equal':equal,'matched_edges':k,'ticks':len(trace),
            'trace':trace,'positive_trace_weight':budget}


def normalized(values):
    total=r.total(values)
    if total.total<=0:raise ValueError('empty normalizer')
    norm=r.edge(1/total.total)
    return tuple(r.serial(v,norm) for v in values)


def corrected_decision(weights,delta,c_old,c_new):
    """Target m/c at completion times, for externally fixed state work c.

    Only nonnegative BRC powers and positive observer normalization are used.
    This CHANGES the completion kernel; it is not passive relabelling of time.
    """
    if c_old<=0 or c_new<=0:raise ValueError('positive work needed')
    small=weights.power(abs(delta))
    yes,no=(small,ONE) if delta>=0 else (ONE,small)
    return normalized((r.serial(yes,r.edge(c_old)),r.serial(no,r.edge(c_new))))


def clock_lift(kernel,cost):
    """Phase chain with last-committed-state readout held until final tick.

    kernel[i][j] is a positive CWM transition weight, interpreted by total.
    No intermediate material motion is assumed. Each cost[i] is a fixed integer.
    """
    if len(kernel)!=len(cost) or any(type(c) is not int or c<1 for c in cost):
        raise ValueError('one positive integer work count per state')
    out={}
    for i,row in enumerate(kernel):
        if r.total(row.values()).total!=1:raise ValueError('row not normalized')
        for k in range(cost[i]):
            out[i,k]=({(i,k+1):r.edge(1)} if k+1<cost[i]
                       else {(j,0):w for j,w in row.items()})
    return out


def push(kernel,law):
    out={}
    for key,w in law.items():
        for dest,v in kernel[key].items():
            out[dest]=r.merge(out.get(dest,ZERO),r.serial(w,v))
    return out


def phase_invariant(masses,cost):
    denominator=r.total(r.serial(w,r.edge(c)) for w,c in zip(masses,cost)).total
    norm=r.edge(1/denominator)
    return {(i,k):r.serial(w,norm) for i,(w,c) in enumerate(zip(masses,cost)) for k in range(c)}


def group_phases(law):
    out={}
    for (i,k),w in law.items():out[i]=r.merge(out.get(i,ZERO),w)
    return out


def tail_bounds(B,lam=Q(1,48),tilt=Q(2)):
    """Whole-space U9 N=4 bounds, not finite simulation of the target law.

    The denominator uses its known original-square L=3..5 exact population.
    The numerator allows all overlaps/collisions: 16 trees and six free legs.
    Returns separate completion-clock and c=2L+1 work-clock tail bounds.
    """
    if type(B) is not int or B<0 or not 1<tilt<1/(12*lam):
        raise ValueError('positive exponential-moment range')
    w=m.Weights(lam)
    groups={L:r.total(w.power(L) for _ in range(count)) for L,count in ((3,32),(4,192),(5,6624))}
    lower=r.total(groups.values())
    work_lower=r.total(r.serial(v,r.edge(2*L+1)) for L,v in groups.items())
    rho=12*lam*tilt
    r.CALLS['one_state_recurrent_cwm']+=1
    geom=r.brc.one_state_recurrent_cwm([lam*tilt]*12)
    closure=r.edge(geom.total_mass_closure)
    z=ONE
    for _ in range(6):z=r.serial(z,closure)
    upper=r.total(z for _ in range(16))
    # Sum L*(tilt*lambda)^L for six independent legs.
    first=r.serial(r.serial(r.edge(rho),closure),closure)
    moment=first
    for _ in range(5):moment=r.serial(moment,closure)
    derivative=r.total(moment for _ in range(6*16))
    weighted_upper=r.total((upper,derivative,derivative))
    discount=ONE;unit=r.edge(1/tilt)
    for _ in range(B+1):discount=r.serial(discount,unit)
    norm=r.edge(1/lower.total)
    plain=r.serial(r.serial(upper,discount),norm).total
    work=r.serial(r.serial(weighted_upper,discount),r.edge(1/work_lower.total)).total
    return {'B':B,'lambda':lam,'tilt':tilt,'Z_lower':lower.total,'Z_work_lower':work_lower.total,
            'tilted_partition_upper':upper.total,
            'tilted_work_partition_upper':weighted_upper.total,
            'completion_tail_upper':min(Q(1),plain),'work_tail_upper':min(Q(1),work)}



def jet_product(a,b):
    """Positive marked-path product: choose one marker in either factor.

    First coordinate counts ordinary histories; second counts histories with
    one distinguished edge occurrence. This is a typed first-moment extension.
    """
    return (r.serial(a[0],b[0]),r.merge(r.serial(a[1],b[0]),r.serial(a[0],b[1])))


def marked_link(overlap,L,v):
    ordinary=overlap.k(L,v)
    marked=r.total(overlap.g(n,v) for n in range(L+1)
                   for split in range(n+1) for distinguished_edge in range(n))
    a=L+1;rho=overlap.rho;closure=overlap.closure
    first=overlap.series.depth(a)
    # Exact unrestricted tail of n(n+1)*rho^n, written positively.
    term0=r.serial(r.edge(a*(a+1)),closure)
    term1=r.serial(r.serial(r.edge((2*a+1)*rho),closure),closure)
    term2=r.serial(r.serial(r.serial(r.edge(rho*(1+rho)),closure),closure),closure)
    mtail=r.serial(first,r.total((term0,term1,term2))).total
    return {'lower':(ordinary,marked),
            'upper':(r.merge(ordinary,r.edge(overlap.tail(L))),r.merge(marked,r.edge(mtail))),
            'marked_tail_upper':mtail}


def work_score(cells,overlap,L=20):
    """Conditional mean c=2L_total+1 with certified infinite-path bounds.

    Not a physical duration. Source identity/tree and mark provenance remain
    in the retained records/grammar; the mean is only a declared observation.
    """
    u.validate_cells(cells);N=len(cells)
    from itertools import combinations
    links={e:marked_link(overlap,L,u.difference(cells[e[0]],cells[e[1]]))
           for e in combinations(range(N),2)}
    rows=[]
    for tree in u.trees(N):
        low=high=(ONE,ZERO)
        for edge in tree:
            low=jet_product(low,links[edge]['lower']);high=jet_product(high,links[edge]['upper'])
        rows.append({'tree':tree,'lower':low,'upper':high})
    lo=tuple(r.total(row['lower'][j] for row in rows) for j in range(2))
    hi=tuple(r.total(row['upper'][j] for row in rows) for j in range(2))
    if lo[0].total==0:raise ValueError('insufficient prefix for this requested configuration')
    interval=(1+2*lo[1].total/hi[0].total,1+2*hi[1].total/lo[0].total)
    return {'cells':cells,'link_depth':L,'links':links,'trees':rows,
            'lower':lo,'upper':hi,'conditional_work_interval':interval}


def encode(x):
    return m.encode(x)
