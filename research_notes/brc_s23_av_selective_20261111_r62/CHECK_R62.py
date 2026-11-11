"""R62 exact sparse latest-source stability certificate.
All numeric reasoning uses Python integers/Fraction; no floating point.
Relative observer x=0; source ages positive, history boundaries {z theta}.
"""
from fractions import Fraction as F
from bisect import bisect_right
import json, random

PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'
p=262204504569236716045286
q=10**24

def label_of_age(theta, m, age):
    phases=sorted(((z*theta)%1,z) for z in range(m))
    loc=(-age*theta)%1
    v=bisect_right(phases,(loc,m))-1
    if v<0: v=len(phases)-1
    return phases[v][1]

def latest_vector(theta,m,ages):
    v=[None]*m
    phases=sorted(((z*theta)%1,z) for z in range(m))
    for r in sorted(ages):
        loc=(-r*theta)%1
        pos=bisect_right(phases,(loc,m))-1
        if pos<0:pos=m-1
        z=phases[pos][1]
        if v[z] is None:v[z]=r
    return v

def history_strict_certificate(p,q,m):
    # Order among {z theta}, z=0..m-1, including the circle origin.
    return all(min((d*p)%q, q-((d*p)%q))>d for d in range(1,m))

def noncollision(p,q,r,h):
    # f(theta) = -(r+h)theta; across [p/q,(p+1)/q]
    d=-(r+h)
    v0=d*p; v1=d*(p+1)
    # exact equality at an endpoint is rejected (except identically zero).
    if d==0: return True
    if v0%q==0 or v1%q==0: return False
    return v0//q == v1//q

def certificate(p,q,m,ages,z):
    """Sufficient full-interval certificate for newest age at original label z.

    If returns success, all theta in [p/q,(p+1)/q] yield the same
    youngest source age. Only the candidate and more-recent sources
    are involved; older sources need not have stable phase membership.
    """
    if not history_strict_certificate(p,q,m):return None
    if not (0<p<p+1<q):return None
    mid=F(2*p+1,2*q)
    ages=sorted(set(ages))
    phase_labels=sorted(((h*mid)%1,h) for h in range(m))
    i=next(i for i,(_,h) in enumerate(phase_labels) if h==z)
    next_h=phase_labels[(i+1)%m][1]
    # special m=1 (all phases have label 0, no crossings)
    if m==1:return {'label':z,'age':ages[0] if ages else None,'inspected':0,'boundary_checks':0}
    candidate=latest_vector(mid,m,ages)[z]
    relevant=[r for r in ages if candidate is None or r<=candidate]
    for r in relevant:
        if not noncollision(p,q,r,z) or not noncollision(p,q,r,next_h):return None
    return {'label':z,'age':candidate,'inspected':len(relevant),
            'boundary_checks':2*len(relevant),'unexamined_older':len(ages)-len(relevant)}


def check_witness():
    age=q
    thetas=[F(4*p+1,4*q),F(4*p+3,4*q)]
    labels=[latest_vector(t,2,[1,age]) for t in thetas]
    assert labels==[[None,1],[age,1]],labels
    cert=certificate(p,q,2,[1,age],1)
    assert cert is not None and cert['age']==1 and cert['inspected']==1 and cert['unexamined_older']==1,cert
    # Age-q collision with at least one of the arcs; cannot certify entire vector
    assert not noncollision(p,q,age,0)
    return {'theta1':str(thetas[0]),'theta2':str(thetas[1]),
        'vectors':labels,'label_one_certificate':cert,
        'high_age_is_undetermined':not noncollision(p,q,age,0)}

def check_random():
    rng=random.Random(20261111)
    cases=0; certified=0; endpoint_crosschecks=0; total_skipped=0; all_status=0
    # Exact small tests: first certify history, then run oracle at 5 parameter points
    for _ in range(500):
        m=rng.randrange(1,10)
        qq=1000003
        pp=rng.randrange(qq//7, 6*qq//7)
        ages=sorted(rng.sample(range(1,101),rng.randrange(1,23)))
        if not history_strict_certificate(pp,qq,m):continue
        cases+=1
        fractions=[F(pp,qq),F(4*pp+1,4*qq),F(2*pp+1,2*qq),F(4*pp+3,4*qq),F(pp+1,qq)]
        for z in range(m):
            all_status+=1
            c=certificate(pp,qq,m,ages,z)
            if c is not None:
                certified+=1
                total_skipped+=c.get('unexamined_older',0)
                for t in fractions:
                    assert latest_vector(t,m,ages)[z]==c['age'],(pp,qq,m,ages,z,c,t)
                    endpoint_crosschecks+=1
    return dict(cases=cases,queries=all_status,certified=certified,independent_queries=endpoint_crosschecks,older_sources_skipped=total_skipped)

def check_near_crossing():
    rng=random.Random(621155)
    queries=0; certificates=0; rejected=0; oracles=0; endpoint_disagreements=0
    for k in range(1000):
        qq=257
        pp=rng.randrange(2,qq-2)
        m=rng.randrange(2,7)
        ages=rng.sample(range(1,121), rng.randrange(2,15))
        if not history_strict_certificate(pp,qq,m):continue
        endpoints=[latest_vector(F(pp,qq),m,ages),latest_vector(F(pp+1,qq),m,ages)]
        for z in range(m):
            queries+=1
            if endpoints[0][z]!=endpoints[1][z]:endpoint_disagreements+=1
            c=certificate(pp,qq,m,ages,z)
            if c is None:
                rejected+=1
                continue
            certificates+=1
            for den,n in [(1,0),(4,1),(2,1),(4,3),(1,1)]:
                t=F(pp*den+n,qq*den)
                assert latest_vector(t,m,ages)[z]==c['age']
                oracles+=1
    assert rejected and endpoint_disagreements and certificates
    return dict(queries=queries,certified=certificates,rejected=rejected,
                divergent_endpoint_queries=endpoint_disagreements,independent_oracles=oracles)

def check_anchor_rotation():
    # A change of anchor rotates every keyed phase by the same amount.
    # Hence the cyclic time-stamped source order is unchanged.
    rng=random.Random(20261112)
    comparisons=0
    for trial in range(120):
        qq=1000003
        pp=rng.randrange(1,qq)
        theta=F(pp,qq)
        origin=(10**70)*rng.randrange(1,10)
        timestamps=sorted(rng.sample(range(-100,101),rng.randrange(5,60)))
        timestamps=[origin+t for t in timestamps]
        a=origin+rng.randrange(-100,101)
        aa=origin+10**30+rng.randrange(-100,101)
        def order(anchor):
            return sorted(timestamps,key=lambda t:(((t-anchor)*theta)%1,t))
        left=order(a);right=order(aa)
        assert any(left[i:]+left[:i]==right for i in range(len(left))), (trial, left,right)
        # Explicitly test translated phase identity at each source.
        delta=((a-aa)*theta)%1
        for t in timestamps:
            assert ((t-aa)*theta)%1==((((t-a)*theta)%1)+delta)%1
            comparisons+=1
    return {'cases':120,'phase_identity_checks':comparisons,
            'max_absolute_offset_digits':71,'cyclic_order_matches':120}

def check_frozen():
    m=128;H=225
    assert history_strict_certificate(p,q,m)
    ages=list(range(1,H+1))
    certificates=[certificate(p,q,m,ages,z) for z in range(m)]
    hit=[c for c in certificates if c is not None]
    visits=0
    endpoints=[latest_vector(F(p,q),m,ages),latest_vector(F(p+1,q),m,ages)]
    for z,c in enumerate(certificates):
        if c is not None:
            assert endpoints[0][z]==c['age']
            assert endpoints[1][z]==c['age']
            visits+=2
    # Full index order certification over E=[-H..-1]+[0..m-1].
    E=set(range(-H,0))|set(range(m))
    D={u-v for u in E for v in E if u!=v}
    minimum=min(min((d*p)%q,q-((d*p)%q))-abs(d) for d in D)
    assert len(D)==704 and minimum>0
    return dict(m=m,H=H,total_labels=m,certified_labels=len(hit),
        certified_label_endpoint_oracles=visits,source_bound_checks=sum(c['boundary_checks'] for c in hit),
        older_sources_skipped=sum(c['unexamined_older'] for c in hit),
        phase_order_difference_count=len(D),phase_order_min_margin=minimum,
        sparse_labels=[certificate(p,q,m,ages,z) for z in (0,31,127)])

if __name__=='__main__':
    result={'scientific_pin':PIN,'claim':'R62-x-aware-newest-source-certificate',
           'witness':check_witness(),'random':check_random(),'near_crossing':check_near_crossing(),'anchor':check_anchor_rotation(),'frozen':check_frozen(),
           'math_semantics':'Exact rational endpoints and 3 interior samples; witness exact; finite tests do not prove general theorem.'}
    print(json.dumps(result,ensure_ascii=False,indent=2,default=str))
