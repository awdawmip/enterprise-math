#!/usr/bin/env python3
"""Independent stdlib verifier for RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE.

No third-party packages are required. The verifier reconstructs hidden semiprime
labels by factoring public N values internally. It never serializes factors.
"""

from __future__ import annotations
import argparse
import functools
import hashlib
import json
import math
import statistics
from pathlib import Path

TASK_ID = "RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE"
P_THRESH = [0,1/256,1/64,1/16,1/4,1/2,3/4,0.9,0.97,0.995,1.0000000001]
Q_THRESH = [1,1.005,1.03,1.1,4/3,2,4,16,64,256,float("inf")]
T_THRESH = [0,1e-6,1e-4,1e-3,1e-2,0.05,0.2,1,4,16,float("inf")]
RES_MODS = [3,5,7,11,13,17,19,23,29,31]
LOCAL_QR_MODS = [8,9,5,7,11,13]
PERIODIC_QR_MODS = [8,9,5,7,11]
QR = {m:{(x*x)%m for x in range(m)} for m in set(LOCAL_QR_MODS+PERIODIC_QR_MODS)}
MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

def isprime64(n:int)->bool:
    if n < 2:
        return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0:
            return n == p
    d = n-1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in MR_BASES:
        if a % n == 0:
            continue
        x = pow(a,d,n)
        if x in (1,n-1):
            continue
        for _ in range(s-1):
            x = (x*x) % n
            if x == n-1:
                break
        else:
            return False
    return True

def brent_factor(n:int)->int:
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    for c0 in range(1,80):
        y = 2+c0
        c = c0
        m = 128
        g = r = qacc = 1
        ys = x = 0
        while g == 1:
            x = y
            for _ in range(r):
                y = (y*y+c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m,r-k)):
                    y = (y*y+c) % n
                    qacc = (qacc * abs(x-y)) % n
                g = math.gcd(qacc,n)
                k += m
            r *= 2
            if r > (1<<22):
                break
        if g == n:
            while True:
                ys = (ys*ys+c) % n
                g = math.gcd(abs(x-ys),n)
                if g > 1:
                    break
        if 1 < g < n:
            return g
    raise RuntimeError(f"deterministic rho failed for {n}")

def factor_semiprime(n:int)->tuple[int,int]:
    if isprime64(n):
        raise AssertionError(f"corpus row is prime, not semiprime: {n}")
    d = brent_factor(n)
    p,q = sorted((d,n//d))
    assert p*q == n and isprime64(p) and isprime64(q), (n,p,q)
    return p,q

def bucket(v:float, th:list[float])->int:
    for i in range(len(th)-1):
        if th[i] <= v < th[i+1]:
            return i
    return len(th)-2

def features(N:int)->list[float]:
    s = math.isqrt(N)
    c = s if s*s == N else s+1
    a = N-s*s
    b = c*c-N
    L = 2*s+1
    D = b-a
    mant = N/(1 << (N.bit_length()-1)) - 1.0
    out = [float(N.bit_length()), mant, a/L, D/L, b/L]
    for m in RES_MODS:
        out += [(N%m)/m, (c%m)/m]
    pass_all = []
    pass_frac = []
    for t in range(64):
        z = (c+t)*(c+t)-N
        hits = sum((z%m) in QR[m] for m in LOCAL_QR_MODS)
        pass_frac.append(hits/len(LOCAL_QR_MODS))
        if hits == len(LOCAL_QR_MODS):
            pass_all.append(t)
    out += [
        len(pass_all)/64,
        (pass_all[0]/64 if pass_all else 1.0),
        statistics.mean(pass_frac),
        statistics.pstdev(pass_frac),
        max(pass_frac),
    ]
    assert len(out) == 30
    return out

def hidden_labels(N:int,p:int,q:int)->dict[str,int|float]:
    c = math.isqrt(N)
    if c*c < N: c += 1
    A = (p+q)//2
    B = (q-p)//2
    T = A-c
    b = c*c-N
    assert B*B == b + T*(2*c+T)
    assert p == c+T-B and q == c+T+B
    return {
        "p_bucket":bucket(p/c,P_THRESH),
        "q_bucket":bucket(q/c,Q_THRESH),
        "t_bucket":bucket(T/c,T_THRESH),
        "T":T,
    }

def split_expected(N:int)->str:
    v = int(hashlib.sha256(f"SMSB1|20260829|{N}".encode()).hexdigest()[:8],16) % 10
    return "train" if v <= 5 else ("tune" if v <= 7 else "heldout")

def knn_orders(train:list[tuple[list[float],int]], testX:list[list[float]], k:int=15)->list[list[int]]:
    nfeat = len(train[0][0])
    means = [sum(row[0][j] for row in train)/len(train) for j in range(nfeat)]
    stds = []
    for j in range(nfeat):
        var = sum((row[0][j]-means[j])**2 for row in train)/len(train)
        stds.append(math.sqrt(var) if var > 0 else 1.0)
    ztr = [([(x[j]-means[j])/stds[j] for j in range(nfeat)], y) for x,y in train]
    out = []
    for x in testX:
        zx = [(x[j]-means[j])/stds[j] for j in range(nfeat)]
        ds = []
        for i,(z,y) in enumerate(ztr):
            d2 = sum((a-b)*(a-b) for a,b in zip(zx,z))
            ds.append((d2,i,y))
        ds.sort(key=lambda a:(a[0],a[1]))
        neigh = ds[:k]
        votes = [0.0]*10
        zero = [row for row in neigh if row[0] == 0.0]
        if zero:
            for _,_,y in zero:
                votes[y] += 1.0
        else:
            for d2,_,y in neigh:
                votes[y] += 1.0/math.sqrt(d2)
        out.append(sorted(range(10), key=lambda cls:(-votes[cls],cls)))
    return out

def rank_metrics(orders:list[list[int]], truth:list[int])->dict[str,float|int]:
    ranks = [order.index(y)+1 for order,y in zip(orders,truth)]
    def cov(k): return sum(r<=k for r in ranks)/len(ranks)
    return {
        "n":len(ranks),
        "top1":cov(1),
        "top2":cov(2),
        "top3":cov(3),
        "top5":cov(5),
        "k_at_99":next(k for k in range(1,11) if cov(k)>=0.99),
        "k_at_999":next(k for k in range(1,11) if cov(k)>=0.999),
    }

def iroot3(x:int)->int:
    r = int(round(x**(1/3)))
    while (r+1)**3 <= x: r += 1
    while r**3 > x: r -= 1
    return r

def make_lehmer_pi(limit:int=100_000):
    sieve = bytearray(b"\x01")*(limit+1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2,math.isqrt(limit)+1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = b"\x00"*(((limit-i*i)//i)+1)
    primes = [i for i in range(2,limit+1) if sieve[i]]
    piv = [0]*(limit+1)
    c = 0
    for i in range(limit+1):
        if sieve[i]: c += 1
        piv[i] = c
    @functools.lru_cache(maxsize=None)
    def phi(x:int,s:int)->int:
        if s == 0: return x
        if s == 1: return x-x//2
        return phi(x,s-1)-phi(x//primes[s-1],s-1)
    @functools.lru_cache(maxsize=None)
    def pi(x:int)->int:
        if x < limit:
            return piv[x]
        a = pi(math.isqrt(math.isqrt(x)))
        b = pi(math.isqrt(x))
        c3 = pi(iroot3(x))
        res = phi(x,a) + ((b+a-2)*(b-a+1))//2
        for i in range(a,b):
            w = x//primes[i]
            res -= pi(w)
            if i < c3:
                lim = pi(math.isqrt(w))
                for j in range(i,lim):
                    res -= pi(w//primes[j])-j
        return res
    return pi

def prime_bucket_bounds(c:int,k:int)->tuple[int,int]:
    lo = max(2, math.ceil(P_THRESH[k]*c))
    hi = min(c, math.ceil(P_THRESH[k+1]*c)-1)
    return lo,hi

def eval_stratum(N:int,p:int,q:int)->str:
    if q/p <= 1.02:
        return "near_twin"
    lam = math.log2(q/p)/N.bit_length()
    if lam < 0.10: return "balanced"
    if lam < 0.45: return "moderate"
    return "strong"

def assert_close(a:float,b:float,tol:float=1e-10):
    assert abs(a-b) <= tol*max(1.0,abs(a),abs(b)), (a,b)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, default=Path(__file__).with_name("public_corpus_manifest.json"))
    ap.add_argument("--summary", type=Path, default=Path(__file__).with_name("result_summary.json"))
    ap.add_argument("--full-search", action="store_true", help="also recompute the slower exact prime-count search audit")
    args = ap.parse_args()
    man = json.loads(args.manifest.read_text())
    summ = json.loads(args.summary.read_text())
    assert man["task_id"] == TASK_ID == summ["task_id"]
    code_to_split = {"R":"train","U":"tune","H":"heldout"}
    pN, cN, codes = [], [], ""
    for sh in man["shards"]:
        sp = args.manifest.with_name(sh["path"])
        sd = json.loads(sp.read_text())
        assert sd["schema"] == "SMSB1_FACTOR_BLIND_CORPUS_SHARD_V1"
        assert sd["bit_length"] == sh["bit_length"]
        assert len(sd["primary_N"]) == sh["primary_cases"] == 160
        assert len(sd["challenge_N"]) == sh["challenge_cases"] == 120
        assert len(sd["primary_split_codes"]) == 160
        assert all(int(n).bit_length()==sd["bit_length"] for n in sd["primary_N"]+sd["challenge_N"])
        pN += [int(n) for n in sd["primary_N"]]
        cN += [int(n) for n in sd["challenge_N"]]
        codes += sd["primary_split_codes"]
    assert len(pN)==len(codes)==800 and len(cN)==600
    primary = [{"case_id":f"P{i:04d}","suite":"primary","split":code_to_split[codes[i]],"N":N,"bit_length":N.bit_length()} for i,N in enumerate(pN)]
    challenge = [{"case_id":f"C{i:04d}","suite":"challenge","split":"heldout_challenge","N":N,"bit_length":N.bit_length()} for i,N in enumerate(cN)]
    rows = primary + challenge
    assert len(rows) == 1400
    counts = {s:sum(r["split"]==s for r in primary) for s in ("train","tune","heldout")}
    assert counts == {"train":510,"tune":137,"heldout":153}
    assert all(r["split"]==split_expected(r["N"]) for r in primary)
    assert all(r["split"]=="heldout_challenge" for r in challenge)
    for band in (24,32,40,48,64):
        assert sum(r["bit_length"]==band for r in primary)==160
        assert sum(r["bit_length"]==band for r in challenge)==120

    # Reconstruct only verifier-side hidden labels.
    hidden = {}
    needed = [r for r in primary if r["split"]=="train"] + challenge
    for r in needed:
        N = int(r["N"])
        p,q = factor_semiprime(N)
        hidden[r["case_id"]] = (p,q,hidden_labels(N,p,q))
        assert N.bit_length() == r["bit_length"]

    # Exact fixed-period residue no-go verification on every challenge row.
    M = math.lcm(*PERIODIC_QR_MODS)
    assert M == 27720
    positive_T = 0
    for r in challenge:
        N = int(r["N"])
        p,q,h = hidden[r["case_id"]]
        T = int(h["T"])
        c = math.isqrt(N) + (math.isqrt(N)**2 < N)
        zT = (c+T)*(c+T)-N
        assert math.isqrt(zT)**2 == zT
        assert all((zT%m) in QR[m] for m in PERIODIC_QR_MODS)
        if T >= M:
            positive_T += 1
            z2 = (c+T-M)*(c+T-M)-N
            assert all((z2%m) in QR[m] for m in PERIODIC_QR_MODS)
            for m in PERIODIC_QR_MODS:
                assert z2 % m == zT % m
    assert positive_T > 300

    # Independent KNN: train only primary/train; evaluate only challenge.
    trainX = [(features(int(r["N"])), hidden[r["case_id"]][2]) for r in primary if r["split"]=="train"]
    testX = [features(int(r["N"])) for r in challenge]
    computed = {}
    order_cache = {}
    for target in ("p_bucket","q_bucket","t_bucket"):
        train = [(x,int(h[target])) for x,h in trainX]
        truth = [int(hidden[r["case_id"]][2][target]) for r in challenge]
        orders = knn_orders(train,testX,15)
        order_cache[target] = orders
        met = rank_metrics(orders,truth)
        computed[target] = met
        expected = summ["independent_stdlib_knn15"][target]
        assert met["k_at_99"] == 10 and met["k_at_999"] == 10
        for key in ("top1","top2","top3","top5"):
            assert_close(met[key],expected[key],1e-12)
        assert met["n"] == expected["n"] == 600

    # Exact coarse-public-fingerprint collisions with far hidden p-buckets.
    def coarse_fp(N:int):
        s=math.isqrt(N); c=s+(s*s<N)
        a=N-s*s; L=2*s+1
        full=0
        for t in range(64):
            z=(c+t)*(c+t)-N
            if all((z%m) in QR[m] for m in LOCAL_QR_MODS):
                full += 1
        return (N.bit_length(), math.floor(32*(a/L)), N%105, full)
    for row in summ["adversarial_coarse_fingerprint_collisions"]:
        n1,n2=int(row["N1"]),int(row["N2"])
        r1=next(r for r in challenge if int(r["N"])==n1)
        r2=next(r for r in challenge if int(r["N"])==n2)
        assert coarse_fp(n1)==coarse_fp(n2)==tuple(row["fingerprint"])
        g=abs(hidden[r1["case_id"]][2]["p_bucket"]-hidden[r2["case_id"]][2]["p_bucket"])
        assert g == row["gap"] and g >= 5

    if not args.full_search:
        print(json.dumps({
            "task_id":TASK_ID,
            "verdict":"PASS",
            "mode":"CORE_INDEPENDENT",
            "public_rows":len(rows),
            "verified_semiprimes":len(needed),
            "periodic_no_go_period":M,
            "independent_knn":computed,
            "adversarial_collisions_verified":len(summ["adversarial_coarse_fingerprint_collisions"]),
            "private_factors_serialized":False,
        },indent=2))
        return

    # Factor-blind search wrapper on 64-bit challenge: KNN bucket order -> exact prime divisibility candidates.
    pi = make_lehmer_pi()
    costs = []
    challenge64 = [(i,r) for i,r in enumerate(challenge) if r["bit_length"]==64]
    for idx,r in challenge64:
        N=int(r["N"]); p,q,h=hidden[r["case_id"]]
        c=math.isqrt(N)+(math.isqrt(N)**2<N)
        true=int(h["p_bucket"])
        cost=0
        for k in order_cache["p_bucket"][idx]:
            lo,hi=prime_bucket_bounds(c,k)
            if k==true:
                cost += pi(p)-pi(lo-1)
                break
            if hi>=lo:
                cost += pi(hi)-pi(lo-1)
        base=pi(p)
        costs.append((eval_stratum(N,p,q),cost,base,cost/base))
    for strat,expected in summ["search_wrapper_knn15_p_bucket_64bit"]["by_stratum"].items():
        part=[x for x in costs if x[0]==strat]
        ratios=[x[3] for x in part]
        got={
            "n":len(part),
            "median_ratio_vs_ascending_prime_scan":statistics.median(ratios),
            "mean_ratio_vs_ascending_prime_scan":statistics.mean(ratios),
            "total_cost_ratio_vs_ascending_prime_scan":sum(x[1] for x in part)/sum(x[2] for x in part),
            "min_ratio":min(ratios),
            "max_ratio":max(ratios),
        }
        assert got["n"]==expected["n"]
        for key in got:
            if key!="n": assert_close(got[key],expected[key],1e-9)
    # Kill conditions: generalized strata do not support a stable search bridge.
    bys=summ["search_wrapper_knn15_p_bucket_64bit"]["by_stratum"]
    assert bys["balanced"]["total_cost_ratio_vs_ascending_prime_scan"] > 1.0
    assert bys["moderate"]["total_cost_ratio_vs_ascending_prime_scan"] > 4.0
    assert bys["strong"]["total_cost_ratio_vs_ascending_prime_scan"] > 100.0
    # Near-twin positive signal is not S2 because Fermat T=0 is the stronger matched baseline.
    nt=[r for r in challenge64 if eval_stratum(int(r[1]["N"]), *hidden[r[1]["case_id"]][:2])=="near_twin"]
    assert all(hidden[r["case_id"]][2]["T"]==0 for _,r in nt)

    print(json.dumps({
        "task_id":TASK_ID,
        "verdict":"PASS",
        "public_rows":len(rows),
        "verified_semiprimes":len(needed),
        "periodic_no_go_period":M,
        "independent_knn":computed,
        "search_kill":{"balanced_gt_1":True,"moderate_gt_4":True,"strong_gt_100":True},
        "private_factors_serialized":False,
    },indent=2))

if __name__ == "__main__":
    main()
