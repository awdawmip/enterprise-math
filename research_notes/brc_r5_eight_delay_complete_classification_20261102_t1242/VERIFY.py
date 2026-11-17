"""Exact author-side checks for R5 eight-delay exposed-face classification.
All-real result is proved algebraically in RESEARCH.md; these are finite regression checks.
Uses only Python standard library Fraction.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

SOURCES = ('C', 'I', 'BJ', 'IJ')
MASS = {'C': F(1, 4), 'I': F(1, 4), 'BJ': F(1, 8), 'IJ': F(1, 8)}
M = sum(MASS.values())
assert M == F(3, 4)


def observe(policy, p, q):
    x, jb, ji, kc, ki, kb, kj = map(F, policy)
    choices = dict(zip(SOURCES, (kc, ki, kb, kj)))

    def per_law(delay, terminal_p):
        a = F(1, 2) * x  # I-stop answers P at t=1
        t = F(1, 2) * x
        k_mass = {'C': F(1, 4), 'I': (1-x)/4}
        for name, mass, stop in (
            ('BJ', F(1, 4), jb),
            ('IJ', (1-x)/4, ji),
        ):
            a += mass*stop + mass*(1-stop)/2*terminal_p
            t += 2*mass*stop + 3*mass*(1-stop)/2
            k_mass[name] = mass*(1-stop)/2
        for name in SOURCES:
            mass = k_mass[name]
            stop = choices[name]
            a += mass*(stop+(1-stop)/2)
            t += mass*(3*stop+(4+delay[name])*(1-stop))
        return a, t

    ep,tp = per_law(p, F(3,5))
    q_answer_p,tq = per_law(q, F(2,5))
    return ep,1-q_answer_p,tp,tq


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def lr_policy(x,y,z):
    return (x,y,y,z,z,z,z)


def weighted(d):
    return sum(MASS[s]*d[s] for s in SOURCES)/M


def witness(s):
    return (0,0,0,*(int(name == s) for name in SOURCES))


def markovize(f,p,q):
    x,jb,ji,kc,ki,kb,kj = map(F,f)
    mass_j = (2-x)/4
    y = (F(1,4)*jb + (1-x)/4*ji)/mass_j
    mass_k = {'C':F(1,4), 'I':(1-x)/4,
              'BJ':(1-jb)/8, 'IJ':(1-x)*(1-ji)/8}
    total = sum(mass_k.values())
    z = sum(mass_k[s]*k for s,k in zip(SOURCES,(kc,ki,kb,kj)))/total
    return lr_policy(x,y,z)


def verify():
    count=0
    p={s:F(v) for s,v in zip(SOURCES, (F(1,4),F(1,2),F(2,3),F(1,3)))}
    q={s:F(1,3) for s in SOURCES}
    full=list(product((0,1),repeat=7))
    lr=[lr_policy(*b) for b in product((0,1),repeat=3)]
    L=[observe(b,p,q) for b in lr]
    E=[v[0]+v[1] for v in L]
    assert E == [F(21,20),F(21,20),F(1),F(1),F(41,40),F(41,40),F(1),F(1)]
    count+=1
    U0,U1=L[:2]
    pbar,qbar=weighted(p),weighted(q)
    assert pbar==F(5,12) and qbar==F(1,3)
    assert U0 == (F(21,40),F(21,40),F(65,16),F(4))
    assert U1 == (F(9,10),F(3,20),F(3),F(3))
    count+=2
    for s in SOURCES:
        ws=observe(witness(s),p,q)
        interpolated=tuple(U0[i]+MASS[s]/M*(U1[i]-U0[i]) for i in range(4))
        assert tuple(ws[i]-interpolated[i] for i in range(4)) == (
            F(0),F(0),MASS[s]*(pbar-p[s]),MASS[s]*(qbar-q[s]))
        count+=1
    W=observe(witness('C'),p,q)
    assert W==(F(13,20),F(2,5),F(15,4),F(11,3))
    normal=(F(400)+2*(1+pbar),F(400),F(1),F(0))
    scores=[dot(normal,v) for v in L]
    assert max(scores)==scores[0]==scores[1]==F(8511,20)
    assert dot(normal,W)-max(scores)==F(1,24)
    assert sum(abs(t) for t in normal)==F(4823,6)
    assert (dot(normal,W)-max(scores))/sum(abs(t) for t in normal)==F(1,19292)
    count+=5

    # Test every signed face-normal choice for all sources and both time laws
    # at each of 50 independently generated exact-rational parameter octuples.
    rng=Random(202611021242)
    cases=50
    for case in range(cases):
        ds=[]
        for law in range(2):
            ds.append({s:F(rng.randint(1,23),rng.randint(24,37)) for s in SOURCES})
        pp,qq=ds
        l=[observe(b,pp,qq) for b in lr]
        means=(weighted(pp),weighted(qq))
        for j,d in enumerate(ds):
            mean=means[j]
            for s in SOURCES:
                w=observe(witness(s),pp,qq)
                inter=tuple(l[0][i]+MASS[s]/M*(l[1][i]-l[0][i]) for i in range(4))
                assert (w[2+j]-inter[2+j])==MASS[s]*(mean-d[s])
                count+=1
                if mean==d[s]:
                    continue
                sign=F(1) if mean>d[s] else F(-1)
                n=(F(400)+sign*2*(1+mean),F(400),
                   sign if j==0 else F(0),sign if j==1 else F(0))
                vals=[dot(n,v) for v in l]
                assert max(vals)==vals[0]==vals[1]
                assert dot(n,w)-max(vals)==MASS[s]*abs(mean-d[s])
                assert sum(abs(t) for t in n)<=805
                count+=3

    # Noncorner real-behaviour regression when P and Q delays are source-independent.
    # The algebraic key-flow argument in RESEARCH.md proves this for every real policy.
    cases_markov=100
    for c in range(cases_markov):
        f=tuple(F(rng.randint(0,13),13) for _ in range(7))
        pp={s:F(3,7) for s in SOURCES}
        qq={s:F(4,9) for s in SOURCES}
        mapped=markovize(f,pp,qq)
        assert all(F(0)<=t<=F(1) for t in mapped)
        assert observe(f,pp,qq)==observe(mapped,pp,qq)
        count+=2

    print('frozen_input_global=main@a01383f825ef9d43b4b754254303298c64041568')
    print('frozen_input_enterprise=main@86149263e38c22292c9def1e0f69092efa1be77e')
    print('answer_lr_face_sums='+str(E))
    print('positive_example_p='+str(tuple(p[s] for s in SOURCES)))
    print('positive_example_q='+str(tuple(q[s] for s in SOURCES)))
    print('weighted_p='+str(pbar)+' weighted_q='+str(qbar))
    print('LR_face_U0='+str(U0))
    print('LR_face_U1='+str(U1))
    print('FULL_single_C='+str(W))
    print('support_normal='+str(normal))
    print('LR_support='+str(max(scores)))
    print('FULL_witness_gap=1/24')
    print('witness_Linf_distance_lower_bound=1/19292')
    print('general_Linf_Hausdorff_lower_bound=maximum(P_range,Q_range)/12880')
    print('sampled_parameter_octuples='+str(cases))
    print('sampled_source_facet_checks='+str(cases*8))
    print('sampled_real_policy_markovization_checks='+str(cases_markov))
    print('exact_assertion_count='+str(count))
    print('PASS_EXACT_R5_EIGHT_SOURCE_FIBER_GLOBAL_CLASSIFICATION')


if __name__=='__main__':
    verify()
