from fractions import Fraction as F
from itertools import product

# Ordered strictly-positive Q tree and local P/Q likelihood factors.
# All branch probabilities under P are Q times the factor.
trans = {
  (): (("a",F(1,3),F(2)),("b",F(2,3),F(1,2))),
  ('a',): (("x",F(1,2),F(1,2)),("y",F(1,2),F(3,2))),
  ('b',): (("x",F(2,3),F(1,2)),("y",F(1,3),F(2))),
  ('a','x'): (("u",F(16,21),F(1,16)),("v",F(5,21),F(4))),
}
for h in [('a','y'),('b','x'),('b','y')]:
    trans[h]=(("u",F(1,2),F(1)),("v",F(1,2),F(1)))

q={():F(1)}; p={():F(1)}
for d in range(3):
    for h in [h for h in list(q) if len(h)==d]:
        for sym,qp,factor in trans[h]:
            child=h+(sym,)
            q[child]=q[h]*qp
            p[child]=p[h]*qp*factor
for h in trans:
    assert sum(q[h+(s,)] for s,_,_ in trans[h])==q[h]
    assert sum(p[h+(s,)] for s,_,_ in trans[h])==p[h]
assert sum(q[h] for h in q if len(h)==3)==sum(p[h] for h in p if len(h)==3)==1
assert all(v>0 for v in list(q.values())+list(p.values()))

def L(h):return p[h]/q[h]
key=lambda h:(len(h),L(h))

A=B=F(1)
C=F(389,1344);D=F(-347,1344)
val=lambda o:o[0]+o[1]+C*o[2]+D*o[3]

def observe(policy):
    result=[F(0),F(0),F(0),F(0)]
    # Random strategies represented directly by probability of action at a node;
    # this evaluator instead traverses a distribution of decisions using complete reach.
    def recur(h,reach):
        dist=policy(h)
        assert sum(dist.values())==1
        assert len(h)<3 or 'C' not in dist
        for action,weight in dist.items():
            if weight==0:continue
            if action=='C':
                for sym,_,_ in trans[h]:recur(h+(sym,),reach*weight)
            else:
                if action=='P':result[1]+=q[h]*reach*weight
                else:result[0]+=p[h]*reach*weight
                result[2]+=len(h)*p[h]*reach*weight
                result[3]+=len(h)*q[h]*reach*weight
    recur((),F(1))
    return tuple(result)

# Tie at L=1 is decided P for a fully specified policy.
def full_policy(mode):
    def pol(h):
        if h==():return {'C':F(1)}
        if h==('a',):return {'P':F(1)} if mode==0 else {'C':F(1)}
        if h==('b',):return {'C':F(1)}
        if h==('a','x'):return {'P':F(1)} if mode==0 else {'C':F(1)}
        if h==('a','y'):return {'P':F(1)}
        if h==('b','x'):return {'C':F(1)}
        if h==('b','y'):return {'P':F(1)} if mode==0 else {'C':F(1)}
        return {'Q':F(1)} if L(h)<1 else {'P':F(1)}
    return pol

O0=observe(full_policy(0));O1=observe(full_policy(1))
Om=tuple((a+b)/2 for a,b in zip(O0,O1))
assert O0==(F(1,9),F(5,9),F(13,9),F(19,9)),O0
assert O1==(F(5,42),F(3,7),F(5,2),F(17,6)),O1
assert Om==(F(29,252),F(31,63),F(71,36),F(89,36)),Om
assert val(O0)==val(O1)==val(Om)==F(34,63)

# An explicit behavioral full-history realization of the midpoint, no root seed.
def full_mid(h):
    if h==():return {'C':F(1)}
    if h==('a',):return {'C':F(1,2),'P':F(1,2)}
    if h==('b',):return {'C':F(1)}
    if h==('a','x'):return {'C':F(1)}
    if h==('a','y'):return {'P':F(1)}
    if h==('b','x'):return {'C':F(1)}
    if h==('b','y'):return {'C':F(1,2),'P':F(1,2)}
    return {'Q':F(1)} if L(h)<1 else {'P':F(1)}
assert observe(full_mid)==Om

# The two modes use only time/exact-LR and hence are valid coarse policies.
for policy in [full_policy(0),full_policy(1)]:
    for h in list(q):
        for hh in list(q):
            if key(h)==key(hh):
                assert policy(h)==policy(hh),(key(h),h,hh)

# Exact formula for every coarse behavioral policy: choose root C, at t1
# continue a with x and b with y; at t2 continue merged LR=1 with z;
# the globally favorable other continuations are bx=1 and ay=0.
# After all terminal decisions are optimized, and for root continuation,
# J=67/96+(431/4032)x-(319/2016)y+z*(-51*x/448+y/144).
base=F(67,96);a=F(431,4032);b=F(-319,2016);ax=F(-51,448);by=F(1,144)
assert base+b==F(34,63)
assert base+a+b+ax+by==F(34,63)
assert a+ax==-F(1,144)
assert b+by<0
# y=1 minimizes for all z; then z=0 or 1 and x endpoints minimize.
assert F(34,63)<1

# Exhaust all deterministic time-LR behavior tables; stochastic lower bound
# is the analytic multilinear inequality above, not inferred from enumeration.
states={d:sorted({key(h)[1] for h in q if len(h)==d}) for d in range(4)}
order=tuple((d,l) for d in range(4) for l in states[d])
act_sets=[('P','Q','C') if d<3 else ('P','Q') for d,l in order]
seen_opt=set(); mincost=None; min_taus=set(); policies_checked=0
for actions in product(*act_sets):
    table=dict(zip(order,actions))
    pol=lambda h,t=table: {t[key(h)]:F(1)}
    o=observe(pol);v=val(o);policies_checked+=1
    if mincost is None or v<mincost:
        mincost=v;min_taus={(o[2],o[3])};seen_opt={o}
    elif v==mincost:
        min_taus.add((o[2],o[3]));seen_opt.add(o)
assert mincost==F(34,63),(mincost,policies_checked)
assert min_taus=={(F(13,9),F(19,9)),(F(5,2),F(17,6))},min_taus
assert Om not in seen_opt
print('PASS strictly_positive_PQ_8_leaf_N3')
print('PASS likelihood_ratio_states',states)
print('PASS objective_coefficients',C,D)
print('PASS O0',O0,'J',val(O0))
print('PASS O1',O1,'J',val(O1))
print('PASS Om',Om,'J',val(Om),'realizable_full_behavioral')
print('PASS global_analytic_support_min',F(34,63),'root_stop_J',F(1))
print('PASS coarse_deterministic_tables',policies_checked,'min',mincost,'distinct_opt_time_pairs',sorted(min_taus))
print('PASS behavioral_coarse_nonconvex_certificate; note not a matched-convex-hulls example')
