"""Positive Euler boundary histories and exact TV inverses for the named RR11 protocol."""
import argparse
from collections import Counter
from decimal import Decimal, ROUND_CEILING, getcontext
from fractions import Fraction as F
from hashlib import sha1
from itertools import product
import json
from pathlib import Path
import sys

PERIOD = 12
UNIFORM = (F(1, 3),) * 3
EDGE = (F(1), F(-1), F(0))
PINS = {
    "research_tasks/RS-EULER-RR-11-ERROR-BUDGET-20261011.md": "cca5b340109b858d30c3184c9358a307379b8eaf",
    "research_notes/chatgpt_direct/20261010_EULER_PASSIVE_SAMPLING_AND_NOISE.md": "bd80290c259cc60995069613a5f4b5f5b41a13d1",
    "research_notes/chatgpt_direct/20261010_EULER_TEMPORAL_APERTURE_AND_IDENTIFIABILITY.md": "b25208a5b812e9345622d88275c806130e628391",
    "research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md": "03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b",
    "src/enterprise_math/brc_weighted.py": "3f205696709e847909958a153f8fe10d3f6b70f0",
    "src/enterprise_math/brc_logarithm.py": "4732e5fc381ce613d240c4381ccbef03c27a69c7",
    "src/enterprise_math/exact_arithmetic.py": "35ea95b0916494b83a92386e3e313928362dd79e",
}


def tv(v):
    assert sum(v) == 0
    return sum(abs(x) for x in v) / 2


def convolution(q, v):
    return tuple(sum(q[b] * v[(j-b) % 3] for b in range(3)) for j in range(3))


def equilibrium(q):
    return sum(x*x for x in q) - q[0]*q[1] - q[1]*q[2] - q[2]*q[0]


def channel_inverse(q, v):
    d = equilibrium(q)
    assert d and sum(v) == 0
    return tuple(x/d for x in convolution((q[0], q[2], q[1]), v))


def geometry_grid():
    grid = invertible = singular = channel_edges = 0
    for a, b in product(range(7), repeat=2):
        if a+b > 6:
            continue
        q = (F(a,6), F(b,6), F(6-a-b,6))
        d = equilibrium(q)
        for ell in range(9):
            lam = F(ell,8)
            grid += 1
            if lam == F(1,2) or d == 0:
                singular += 1
                continue
            h = [(-lam)**r * (1-lam)**(11-r) / ((1-lam)**12-lam**12) for r in range(12)]
            assert all((1-lam)*h[r] + lam*h[(r-1)%12] == int(r == 0) for r in range(12))
            kt = 1/abs(1-2*lam)
            assert sum(map(abs,h)) == kt and abs(sum((-1)**r*x for r,x in enumerate(h))) == kt
            kc = (max(q)-min(q))/d
            for i,j in product(range(3), repeat=2):
                if i == j:
                    continue
                v = tuple(F(int(k==i)-int(k==j)) for k in range(3))
                inv = channel_inverse(q,v)
                assert convolution(q,inv) == v and tv(inv) == kc
                channel_edges += 1
            invertible += 1
    return dict(grid=grid, invertible=invertible, singular=singular, signed_channel_edges=channel_edges)


def pulse_traces():
    # One representative of the archived Q=00 pulse, with its original multiplicities.
    rows = [(1,0,0,0,2),(2,0,0,0,1),(1,0,0,1,1),(0,0,3,0,1),(0,0,3,1,1),
            (1,1,0,0,1),(2,1,0,0,2),(2,1,0,1,1),(0,1,3,0,1),(0,1,3,1,1)]
    traces = []
    for j,s,w,theta,multiplicity in rows:
        F2 = 0
        initial = (j,s,w,theta,F2)
        path = []
        for _ in range(12):
            path.append(j)
            active = w in (0,3) and theta == 0
            if active:
                w = 3-w
            s ^= F2 ^ active
            F2 ^= 1 ^ active
            theta ^= w in (1,3)
            j = (j + (-1)**s) % 3
        assert (j,s,w,theta,F2) == initial
        traces.extend([tuple(path)]*multiplicity)
    assert len(traces) == 12
    return traces


def prepare_rows(X):
    # Equal total weight for each marked time. This convenient subfamily contains the ball.
    weights = [[F(1,36)+4*(x-F(1,3)) for x in row] for row in X]
    assert all(min(row)>=0 and sum(row)==F(1,12) for row in weights)
    return weights


def path_read(kernel, traces, X, lam, offsets):
    weights = prepare_rows(X)
    output = []
    total_paths = branch_contacts = 0
    # Keep all positive source paths; fold equal current labels only after calibration 
    # has been specified as a kernel of that label, common across the named histories.
    for t in range(12):
        ends = [kernel.CWM_ZERO]*3
        for delay,prob in enumerate((1-lam,lam)):
            if not prob:
                continue
            source = [kernel.CWM_ZERO]*3
            for mark,row in enumerate(weights):
                for rotation,w in enumerate(row):
                    if not w:
                        continue
                    mass = kernel.cwm_edge(w/12)
                    for path in traces:
                        j = (rotation+path[(t+delay+11-mark)%12])%3
                        source[j] = kernel.cwm_recoalesce(source[j],mass)
            assert tuple(v.total for v in source) == X[(t+delay)%12]
            for j,record in enumerate(source):
                joint = kernel.cwm_propagate(record,kernel.cwm_edge(prob))
                for b,value in enumerate(offsets[j]):
                    if not value:
                        continue
                    weighted=kernel.cwm_propagate(joint,kernel.cwm_edge(value))
                    receiver=b
                    for _ in range(j or 1):
                        if j:
                            receiver=(receiver+1)%3
                        weighted=kernel.cwm_propagate(weighted,kernel.CWM_ONE)
                    assert receiver == (j+b)%3
                    ends[receiver]=kernel.cwm_recoalesce(ends[receiver],weighted)
                    branch_contacts += j*weighted.count
        assert sum(v.total for v in ends)==1
        output.append(tuple(v.total for v in ends))
        total_paths += sum(v.count for v in ends)
    return output, dict(positive_paths_all_twelve_reads=total_paths,path_contacts_all_twelve_reads=branch_contacts)


def add_noise(X, lam, q):
    return [convolution(q,[(1-lam)*X[t][i]+lam*X[(t+1)%12][i] for i in range(3)]) for t in range(12)]


def distance(a, b):
    return max(tv([x-y for x,y in zip(row,other)]) for row,other in zip(a,b))


def uncertain_cases():
    """Exact perturbation check using a named clean trajectory and its channel rotation."""
    path=pulse_traces()[0]
    X=[tuple(F(j==v) for j in range(3)) for v in path]
    s=F(1,20)
    changed=[tuple((1-s)*a+s*row[(j-1)%3] for j,a in enumerate(row)) for row in X]
    assert distance(X,changed)==s
    q=(F(1,2),F(1,3),F(1,6))
    lam=F(1,3)
    kc,kt=F(4),F(3)
    g=[(-lam)**r*(1-lam)**(11-r)/((1-lam)**12-lam**12) for r in range(12)]
    cases=0
    for a,b in product(range(5),repeat=2):
        if a+b>4:
            continue
        trial_q=(F(a,4),F(b,4),F(4-a-b,4))
        eq=tv([x-y for x,y in zip(trial_q,q)])
        for ell in range(5):
            trial_lam=F(ell,4)
            el=abs(trial_lam-lam)
            actual=add_noise(changed,trial_lam,trial_q)
            reported=[tuple((19*x+u)/20 for x,u in zip(row,UNIFORM)) for row in actual]
            e=distance(actual,reported)
            centered=[channel_inverse(q,[x-u for x,u in zip(row,UNIFORM)]) for row in reported]
            recovered=[tuple(UNIFORM[j]+sum(v*centered[(t+r)%12][j] for r,v in enumerate(g))
                             for j in range(3)) for t in range(12)]
            assert distance(recovered,X)<=s+kc*kt*e+kc*eq+kt*el+2*kc*kt*eq*el
            positive=[]
            for row in recovered:
                clipped=[max(F(0),x) for x in row]
                positive.append(tuple(x/sum(clipped) for x in clipped))
            assert distance(positive,X)<=distance(recovered,X)
            cases+=1
    return cases


def signed_family(direction,scale,alternating):
    return [tuple(u+scale*x*((-1)**t if alternating else 1) for u,x in zip(UNIFORM,direction)) for t in range(12)]


def actual_cases(kernel):
    traces=pulse_traces()
    q=(F(1,2),F(1,3),F(1,6))
    lam=F(1,3)
    local=channel_inverse(q,EDGE)
    kc=tv(local)
    unit=tuple(x/kc for x in local)
    K=kc/abs(1-2*lam)
    radius=F(1,192)
    plus=signed_family(unit,radius,True)
    minus=signed_family(unit,-radius,True)
    yp,steps1=path_read(kernel,traces,plus,lam,[q]*3)
    ym,steps2=path_read(kernel,traces,minus,lam,[q]*3)
    assert yp==add_noise(plus,lam,q) and ym==add_noise(minus,lam,q)
    measured=max(tv([u-v for u,v in zip(a,b)]) for a,b in zip(yp,ym))
    assert 2*radius == K*measured
    assert yp==signed_family(EDGE,radius/K,True)
    collapsed,_=path_read(kernel,traces,plus,F(1,2),[q]*3)
    assert collapsed==[UNIFORM]*12 and add_noise(plus,lam,UNIFORM)==collapsed
    # Two preparations have the same receiver law, but different clean sources.
    delta=F(1,1000)
    strength=(0,-6,6)
    X=signed_family(strength,delta,False)
    uniform_source=[UNIFORM]*12
    plain,steps3=path_read(kernel,traces,X,lam,[q]*3)
    checkerboard=((1,-1,0),(-1,1,0),(0,0,0))
    dependent=[tuple(q[b]+3*delta*checkerboard[j][b] for b in range(3)) for j in range(3)]
    assert [sum(row[b] for row in dependent)/3 for b in range(3)]==list(q)
    mixed,steps4=path_read(kernel,traces,uniform_source,lam,dependent)
    assert all(min(row)>0 and sum(row)==1 for row in dependent)
    assert mixed==plain==signed_family((1,-2,1),delta,False)
    joint_loss=F(1,2)*sum(abs(delta*x) for row in checkerboard for x in row)
    assert joint_loss==tv([x-u for x,u in zip(plain[0],UNIFORM)])
    return dict(q=[str(x) for x in q],lambda_=str(lam),kappa=str(K),tv_channel=str(kc),
                true_source_separation=str(2*radius),receiver_separation=str(measured),
                singular_window_all_uniform=True,singular_offset_all_uniform=True,
                correlation_example=dict(delta=str(delta),source_distance=str(6*delta),
                    output_distance_between_models="0",output_minus_ideal_independent=str(joint_loss)),
                CWM_path_counts=[steps1,steps2,steps3,steps4])


def sample_budget(K,eta,alpha):
    def dec(x):
        return Decimal(x.numerator)/Decimal(x.denominator)
    getcontext().prec=70
    k,e,c=map(dec,(K,eta,alpha))
    b=2*e/k
    one_third=Decimal(1)/3
    lower=(1-2*c)*((1-c)/c).ln()/(2*b*((one_third+b)/(one_third-b)).ln())
    upper=(k/e)**2*(72/c).ln()/2
    return dict(kappa=str(K),error_target=str(eta),failure_probability=str(alpha),
                necessary_total_independent_draws=int(lower.to_integral_value(rounding=ROUND_CEILING)),
                sufficient_independent_draws_per_slot=int(upper.to_integral_value(rounding=ROUND_CEILING)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    args=parser.parse_args()
    for name,expected in PINS.items():
        raw=(args.repo/name).read_bytes()
        assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==expected
    sys.path.insert(0,str(args.repo/'src'))
    from enterprise_math import brc_weighted
    print(json.dumps(dict(task='RS-EULER-RR-11-ERROR-BUDGET-20261011',
        exact_grid=geometry_grid(),fixed_Q_positive_paths=actual_cases(brc_weighted),
        exact_perturbed_protocols_and_probability_projections=uncertain_cases(),
        sample_budget=[sample_budget(k,F(1,300),F(1,20)) for k in (F(1),F(12),F(120))],
        input_git_blobs=PINS),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
