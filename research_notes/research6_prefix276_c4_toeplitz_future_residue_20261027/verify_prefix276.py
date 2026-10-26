"""PREFIX-276 exact typed C4 path-pair BRC observer check (author-side).

No ordinary propagator, numerical trigonometry, or float arithmetic is used.
This executes the documented Stage50 path-pair character law independently;
it does NOT import the original Stage46/Stage50 package or run a native H_n law.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import json

ZERO=(F(0), F(0)); ONE=(F(1), F(0)); II=(F(0), F(1))
C4=(ONE,II,(F(-1),F(0)),(F(0),F(-1)))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def scale(x,s): return (x[0]*s,x[1]*s)
def mod2(x): return x[0]*x[0]+x[1]*x[1]
def fmt(x): return str(x[0]) if x[1]==0 else f'{x[0]}+({x[1]})i'

@dataclass(frozen=True)
class Path:
    source_load: int
    weight: F
    phase: int

    def __post_init__(self):
        assert self.weight>0 and 0<=self.phase<4

    @property
    def amplitude(self):
        return scale(C4[self.phase],self.weight)


def normalization(paths):
    assert len({p.source_load for p in paths}) == len(paths)
    return sum((p.weight*p.weight for p in paths),F(0))


def brc_moment(paths, r):
    """c_r = (sum_{k} conjugate(a[k+r])*a[k])/Z.

    Every summand is a labeled ordered pair. The C4 character and weight
    multiplication occur before summation; positive mass is never substituted
    for a signed/complex amplitude.
    """
    assert isinstance(r,int) and r>=0
    indexed={p.source_load:p for p in paths}
    total=ZERO
    for p in paths:
        q=indexed.get(p.source_load+r)
        if q is not None:
            total=add(total,mul(conj(q.amplitude),p.amplitude))
    return scale(total,F(1)/normalization(paths))


def p_external(paths,r,p):
    assert 0<=p<4
    ch=mul(C4[p],brc_moment(paths,r))
    return F(5,18)*(1-ch[0])


def rational_family(t):
    """All rational t: (a, -i, c), a>0,c<=0, normalized by exact Z."""
    t=F(t)
    a=F(2)/(1+t*t)
    c=-(t-1)*(t-1)/(1+t*t)
    ans=[Path(0,a,0),Path(1,F(1),3)]
    if c:
        ans.append(Path(2,-c,2))
    return ans


def disk_certificate(c1,c2):
    center=mul(c1,c1)
    radius=F(1)-mod2(c1)
    lhs=mod2(sub(c2,center))
    rhs=radius*radius
    assert radius>=0 and lhs<=rhs
    return {'center':fmt(center),'radius':str(radius),'lhs_squared':str(lhs),'rhs_squared':str(rhs)}


def run():
    a=rational_family(F(1))
    b=rational_family(F(0))
    assert [p.source_load for p in a]==[0,1]
    assert [p.source_load for p in b]==[0,1,2]
    assert normalization(a)==2
    assert normalization(b)==6
    assert brc_moment(a,1)==(F(0),F(1,2))
    assert brc_moment(b,1)==(F(0),F(1,2))
    assert brc_moment(a,2)==ZERO
    assert brc_moment(b,2)==(F(-1,3),F(0))
    assert brc_moment(a,0)==brc_moment(b,0)==ONE
    first_a=[p_external(a,1,p) for p in range(4)]
    first_b=[p_external(b,1,p) for p in range(4)]
    next_a=[p_external(a,2,p) for p in range(4)]
    next_b=[p_external(b,2,p) for p in range(4)]
    assert first_a==first_b==[F(5,18),F(5,12),F(5,18),F(5,36)]
    assert next_a==[F(5,18)]*4
    assert next_b==[F(10,27),F(5,18),F(5,27),F(5,18)]
    da=disk_certificate(brc_moment(a,1),brc_moment(a,2))
    db=disk_certificate(brc_moment(b,1),brc_moment(b,2))
    assert da['lhs_squared']=='1/16' and db['lhs_squared']=='1/144'
    tested=set()
    samples=[F(n,d) for d in range(1,8) for n in range(-9,10)]
    for t in samples:
        ps=rational_family(t)
        c1=brc_moment(ps,1)
        c2=brc_moment(ps,2)
        assert c1==(F(0),F(1,2))
        assert c2==(F(-(t-1)*(t-1)/((1+t*t)*(t*t-2*t+3))),F(0))
        disk_certificate(c1,c2)
        # Check four C4 detector settings against ordered pair chi at r=0,1,2.
        for r in (0,1,2):
            for ph in range(4):
                y=p_external(ps,r,ph)
                assert F(0)<=y<=F(5,9)
        tested.add(t)
    # Infinitely many rational parameters are certified analytically by a
    # nonconstant rational function; only these finite tests are executed.
    infinite_witnesses=[brc_moment(rational_family(F(1,n)),2) for n in range(2,13)]
    assert len(set(infinite_witnesses))==11
    # Moment identity has full BRC provenance: each entry is a source-load pair.
    payload={
        'status':'PREFIX276_EXACT_TYPED_C4_BRC_CHECK_PASS',
        'semantics':'independent rational C4 ordered source-load-pair observer from Stage50; no native H_n or original Stage46 source package run',
        'rational_parameters_tested':len(tested),
        'c1_for_both':fmt(brc_moment(a,1)),
        'c2_A':fmt(brc_moment(a,2)),
        'c2_B':fmt(brc_moment(b,2)),
        'norms':{'A':str(normalization(a)),'B':str(normalization(b))},
        'disk_A':da,'disk_B':db,
        'r1_C4_A_B':[str(z) for z in first_a],
        'r2_C4_A':[str(z) for z in next_a],
        'r2_C4_B':[str(z) for z in next_b],
        'distinct_c2_1_over_n_witnesses':len(set(infinite_witnesses))
    }
    return payload

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
