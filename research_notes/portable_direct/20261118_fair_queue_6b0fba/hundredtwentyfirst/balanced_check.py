"""Balanced semiprimes: exact original Hart scores over each complete integer shell."""
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from math import isqrt


def cube_floor(n):
    high = 1 << ((n.bit_length() + 2) // 3)
    low = 0
    while low + 1 < high:
        mid = (low + high) // 2
        if mid**3 <= n:
            low = mid
        else:
            high = mid
    return high if high**3 <= n else low


def is_prime(n):
    return n > 1 and all(n % j for j in range(2, isqrt(n) + 1))


def prime_interval(lo, hi, limit=None):
    out = []
    for x in range(lo | 1, hi + 1, 2):
        if is_prime(x):
            out.append(x)
            if limit is not None and len(out) == limit:
                break
    return out


def primes_in_box(P, limit=None):
    return (prime_interval(P, 21 * P // 20, limit),
            prime_interval((11 * P + 9) // 10, 23 * P // 20, limit))


def scaled_phase(N, bits):
    s = 1 << bits
    return cube_floor(27 * N * s**3) % s


def longest(N, window=None):
    k0 = cube_floor(N - 1) + 1
    k1 = cube_floor(8 * N)
    if window is not None:
        k1 = min(k1, k0 + window - 1)
    best = size = 0
    start = None
    for k in range(k0, k1 + 1):
        four_nk = 4 * N * k
        # The same ceiling for square and nonsquare products.
        floor = isqrt(four_nk)
        x = floor + int(floor * floor != four_nk)
        ok = 10 * (x*x - four_nk) <= 3 * (2*x - 1)
        size = size + 1 if ok else 0
        if size > best:
            best = size
            start = k - size + 1
    return best, start, (k0, k1)


def check_witness(N, size, start, shell):
    if not size:
        return
    def score(k):
        x = isqrt(4 * N * k - 1) + 1
        return Fraction(x*x - 4*N*k, 2*x-1)
    boundary = Fraction(3, 10)
    assert all(score(k) <= boundary for k in range(start, start + size))
    if start > shell[0]:
        assert score(start - 1) > boundary
    if start+size <= shell[1]:
        assert score(start + size) > boundary


def box(P):
    left, right = primes_in_box(P)
    hist, phase_hist = Counter(), [0] * 16
    digest = hashlib.sha256()
    examples = {}
    scans = 0
    sum_powers = [0] * 3
    for p in left:
        for q in right:
            N = p*q
            phase = scaled_phase(N, 28)
            L, start, shell = longest(N)
            check_witness(N, L, start, shell)
            idx = phase >> 24
            phase_hist[idx] += 1
            hist[L] += 1
            scans += shell[1]-shell[0]+1
            for i, w in enumerate((1, 4, 6)):
                sum_powers[i] += L**w
            item = (p, q, phase, L, start, shell)
            for key, measure in [('longest', -L), ('shortest', L)]:
                if key not in examples or measure < examples[key][0]:
                    examples[key] = (measure, item)
            digest.update(f'{p},{q},{phase},{L},{start}\n'.encode())
    return {"P":P, "prime_counts":[len(left),len(right)], "pairs":len(left)*len(right),
            "full_shell_multiplier_visits":scans, "L_histogram":sorted(hist.items()),
            "16_equal_phase_bins":phase_hist, "power_sums_L_1_4_6":sum_powers,
            "extremizers_p_q_phase28_L_start_shell":{k:v[1] for k,v in examples.items()},
            "ordered_rows_sha256":digest.hexdigest()}


def large_examples():
    # Fixed lexicographic candidates, used only for finite existence witnesses.
    P = 1 << 27
    left,right=primes_in_box(P,128)
    s = 1 << 42
    pool=[]
    for p in left:
        for q in right:
            pool.append((scaled_phase(p*q,42),p,q))
    def edge_example(rows):
        def rank(row):
            _,p,q=row
            return (-longest(p*q, 1024)[0],p,q)
        return min(rows,key=rank)
    schedules=(
        ('phase_near_zero', edge_example(row for row in pool if row[0] < s//128)),
        ('phase_near_middle', min(pool,key=lambda row:abs(2*row[0]-s))),
        ('phase_near_one',edge_example(row for row in pool if row[0] >= s-s//128)))

    result=[]
    for name,(phase,p,q) in schedules:
        n=p*q
        L,start,shell=longest(n)
        check_witness(n,L,start,shell)
        result.append({"type":name,"p":p,"q":q,"N":n,"shell":shell,
                       "floor_phase_times_2pow42":phase,"L":L,"first_start":start})
    return {"P":P,"candidate_pairs":len(pool),"selection":"first 128 primes per interval; at each outer 1/128 phase bin maximize the first 1024-point run, break ties by (p,q); middle chosen nearest phase 1/2",
            "full_scans":result}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick",action="store_true",help="run the smallest complete box only")
    args=parser.parse_args()
    out={"score_threshold":"3/10","factor_box":["[P,21P/20]","[11P/10,23P/20]"],
         "semiprime_sampling":"all named pairs with equal weight in each complete box",
         "full_boxes":[box(P) for P in ([1000] if args.quick else [1000,5000,20000])]}
    if not args.quick:
        out["larger_balanced_witnesses"]=large_examples()
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
