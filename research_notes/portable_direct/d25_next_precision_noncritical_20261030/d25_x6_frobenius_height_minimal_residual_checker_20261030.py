#!/usr/bin/env python3
"""Author exact integer check of the declared finite X6 candidate, not native dynamics.

No external package, network or hidden Source input.  The six-coordinate charts
are explicit finite models; P000/time/source scope is handled in the proof.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from json import dumps
from pathlib import Path


def count_formula(p, L, e):
    n = L - e
    assert n >= 1 and p % 2 and p >= 3
    layers = []
    for t in range((n - 1) // p + 1):
        m = n - p * t
        images = (p - 1) * p ** max(m - 2, 0)
        per_image = p ** (L - t - 1 - max(m - 2, 0))
        layers.append(dict(t=t, m=m, image_count=images,
                           sources_per_image=per_image))
    zero_size = p ** (L - (n + p - 1) // p)
    return layers, zero_size, 1 + sum(s['image_count'] for s in layers), max(1, n - 1)


def valuation(x, p, maximum):
    if x == 0:
        return maximum
    t = 0
    while x % p == 0:
        x //= p
        t += 1
    return t


def check_case(p, L, e):
    N = p ** L
    n = L - e
    low = p ** n
    layers, zero_size, number_images, min_k = count_formula(p, L, e)

    observed = defaultdict(list)
    for h in range(N):
        H = pow(h, p, low)
        observed[H].append(h)
    assert len(observed) == number_images, ('image count', p, L, e)
    assert len(observed[0]) == zero_size, ('zero mass', p, L, e)
    assert sum(map(len, observed.values())) == N
    expected_distribution = Counter({zero_size: 1})
    for layer in layers:
        t, m, I, F = (layer[x] for x in ('t','m','image_count','sources_per_image'))
        hits = [(H, hs) for H, hs in observed.items() if H != 0 and valuation(H,p,n) == p*t]
        assert len(hits) == I, ('layer image count', p, L, e, t, len(hits), I)
        assert all(len(hs) == F for H,hs in hits), ('fiber weight', p,L,e,t)
        expected_distribution[F] += I
    assert Counter(map(len, observed.values())) == +expected_distribution
    assert sum(a*b for a,b in expected_distribution.items()) == N

    ks = []
    for k in range(L+1):
        stride = p**k
        ok = all(pow((h+stride)%N,p,low) == pow(h,p,low) for h in range(N))
        ks.append(k if ok else None)
        assert ok == (k>=min_k), ('minimal height congruence',p,L,e,k,ok,min_k)

    # Ensure the all-future signature is exactly the two-readout (q,H) signature,
    # checked by actual six-coordinate dynamics on several independent source rows.
    checked_rows = 0
    checked_transitions = 0
    for qbase in [0, 1, low-1, N-1]:
        q0 = (qbase % N, (2*qbase+1)%N, (3*qbase+2)%N, (4*qbase+3)%N, (5*qbase+4)%N)
        seen_after_one = defaultdict(set)
        for h in range(N):
            z = tuple((q+h)%N for q in q0) + (h,)
            def observe(x): return tuple((x[i]-x[5])%N for i in range(5))
            def advance(x): return ((x[0]+p**e*pow(x[5],p,N))%N,) + x[1:]
            assert observe(z) == q0
            H = pow(h,p,low)
            orig_h = z[5]
            for step in range(1,5):
                z = advance(z)
                assert z[5] == orig_h
                out = observe(z)
                assert out[0] == (q0[0] + step*p**e*H)%N
                assert out[1:] == q0[1:]
                checked_transitions += 1
                if step == 1: seen_after_one[H].add(out)
            checked_rows += 1
        assert len(seen_after_one)==number_images
        assert all(len(v)==1 for v in seen_after_one.values())

    witness = None
    if min_k>0:
        k = min_k-1
        stride = p**k
        for h in range(N):
            left = pow(h,p,low)
            right = pow((h+stride)%N,p,low)
            if left != right:
                witness={'k_too_small':k, 'h':h, 'h_prime':(h+stride)%N,
                         'q0':0, 'next_q1':(p**e*left)%N,
                         'next_q1_prime':(p**e*right)%N}
                break
        assert witness is not None
    return dict(p=p,L=L,e=e,n=n, modulus=N, image_count=number_images,
                min_congruence_depth=min_k, layer_spectrum=layers,
                zero_fiber_size=zero_size,
                fiber_size_counts=dict(sorted(expected_distribution.items())),
                source_rows=checked_rows, actual_updates=checked_transitions,
                insufficient_depth_witness=witness)


def main():
    configurations=[]
    for p,max_L in [(3,7),(5,5),(7,4),(11,3)]:
        for L in range(2,max_L+1):
            for e in range(1,L):
                configurations.append(check_case(p,L,e))
    assert len(configurations)==sum(m*(m-1)//2 for m in [7,5,4,3])
    assert sum(c['source_rows'] for c in configurations)>10000
    output = {'schema':'D25_X6_FROBENIUS_HEIGHT_INTEGER_CERT_V1',
              'status':'AUTHOR_EXACT_CHECKED_NOT_NATIVE',
              'scope':'Declared polynomial finite ring candidate, entire height set for each checked parameter',
              'pass':True, 'num_configurations':len(configurations),
              'source_rows':sum(c['source_rows'] for c in configurations),
              'actual_six_coordinate_updates':sum(c['actual_updates'] for c in configurations),
              'cases':configurations}
    dest=Path(__file__).with_name('d25_x6_frobenius_height_minimal_residual_author_check_20261030.json')
    dest.write_text(dumps(output,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('PASS configs=',len(configurations),'source_rows=',output['source_rows'],
          'updates=',output['actual_six_coordinate_updates'],'sha256_json=',sha256(dest.read_bytes()).hexdigest())
    for p,L,e in [(3,5,1),(5,4,1),(3,3,1)]:
        c=next(x for x in configurations if x['p']==p and x['L']==L and x['e']==e)
        print('sample',p,L,e,'J',c['image_count'],'k*',c['min_congruence_depth'],
              'weights',c['fiber_size_counts'])

if __name__=='__main__': main()
