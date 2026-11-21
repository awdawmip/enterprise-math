"""Exact parity cuts from unions of parallel fibers and type equations.

The integer proof uses only point-cover and prescribed type-count equations.
For a union H of fibers and v in {0,1}^4, let U = H intersect free.
If |U| + sum_t v_t n_t is odd, every integer exact cover satisfies
sum_C ( (|C intersect U| + v_type(C)) mod 2 ) x_C >= 1.
"""
from fractions import Fraction
from itertools import product
from math import lcm

TYPES=((9,557),(10,744),(11,936),(11,944))
COUNTS=(2,5,2,1)
POINTS=list(product(range(5),repeat=3))
FORMS=[(0,0,1)]+[(0,1,a) for a in range(5)]+[(1,a,b) for a in range(5) for b in range(5)]
FIBERS=[[sum(1<<p for p,x in enumerate(POINTS) if sum(a*b for a,b in zip(f,x))%5==v) for v in range(5)] for f in FORMS]
PATTERNS=[[((p&j).bit_count()&1) for p in range(32)] for j in range(32)]
TYPE_BITS=list(product(range(2),repeat=4))

def subset(f,j,free):
    return sum(FIBERS[f][a] for a in range(5) if j>>a&1)&free

def pattern(m,f):
    return sum(((m&h).bit_count()%2)<<a for a,h in enumerate(FIBERS[f]))

def coefficient(m,t,cut):
    U,v=cut
    return ((m&U).bit_count()+v[t])%2

def all_inequalities(free):
    for f in range(31):
        for j in range(32):
            U=subset(f,j,free)
            for v in TYPE_BITS:
                if (U.bit_count()+sum(a*b for a,b in zip(v,COUNTS)))%2:
                    yield f,j,U,v

def exact_family(weights,free):
    """Check the entire family using a single common integer denominator."""
    q=1
    for r in weights:q=lcm(q,r['denominator'])
    totals=[0]*4;coverage=[0]*125
    aggregate=[[[0]*32 for t in TYPES] for f in FORMS]
    for r in weights:
        m=int(r['mask']);t=TYPES.index((r['size'],r['cost']))
        w=r['numerator']*(q//r['denominator'])
        assert w>0 and not m&~free and m.bit_count()==r['size']
        totals[t]+=w
        for p in range(125):
            if m>>p&1:coverage[p]+=w
        for f in range(31):aggregate[f][t][pattern(m,f)]+=w
    assert totals==[q*n for n in COUNTS]
    assert coverage==[q if free>>p&1 else 0 for p in range(125)]
    best=None;violations=[];count=0
    for f in range(31):
        for j in range(32):
            U=subset(f,j,free)
            odd=[sum(w for p,w in enumerate(aggregate[f][t]) if PATTERNS[j][p]) for t in range(4)]
            for v in TYPE_BITS:
                if (U.bit_count()+sum(a*b for a,b in zip(v,COUNTS)))%2==0:continue
                value=sum(totals[t]-odd[t] if v[t] else odd[t] for t in range(4))
                row=(value,f,j,U,v)
                if best is None or row<best:best=row
                count+=1
                if value<q:violations.append(row)
    def describe(row):
        val,f,j,U,v=row
        return {'form':FORMS[f],'levels':[a for a in range(5) if j>>a&1],
                'subset_mask':str(U),'subset_size':U.bit_count(),
                'type_parities':v,'lhs':str(Fraction(val,q)),'lhs_float':val/q}
    return {'tested':count,'minimum':describe(best),'violations':[describe(x) for x in violations],
            'exact_feasible':not violations,'common_denominator':str(q)}
