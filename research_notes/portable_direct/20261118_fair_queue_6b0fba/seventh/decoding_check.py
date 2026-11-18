"""Replay a positive BRC projection of the all-zero native prefix. No ideal Fourier run."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from random import Random

CORE_SHA = "7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26"


class Digits:
    def __init__(self, core):
        assert hashlib.sha256(core.read_bytes()).hexdigest() == CORE_SHA
        spec = importlib.util.spec_from_file_location("frozen_weighted_core", core)
        mod = importlib.util.module_from_spec(spec)
        import sys
        sys.modules[spec.name] = mod
        spec.loader.exec_module(mod)
        # The frozen sparse-modular proof, Lemma 1, numbers output states 8+2s+c.
        edges = (8, 10, 10, 9, 10, 9, 9, 11)
        graph = [[int(i < 8 and j == edges[i]) for j in range(12)] for i in range(12)]
        output = mod.recurrent_mass_power(graph, 1)
        self.table = []
        for row in output[:8]:
            assert sum(x != 0 for x in row) == 1
            code = row.index(1) - 8
            self.table.append((code >> 1, code & 1))
        self.cells = 0

    def bit_add(self, a, b, width):
        result = carry = 0
        for i in range(width):
            code = (((a >> i) & 1) << 2) | (((b >> i) & 1) << 1) | carry
            bit, carry = self.table[code]
            result |= bit << i
        self.cells += width
        return result, carry

    def add(self, a, b):
        result, carry = self.bit_add(a, b, max(a.bit_length(), b.bit_length(), 1)+1)
        assert not carry
        return result

    def sub_or_none(self, a, b):
        width = max(a.bit_length(), b.bit_length(), 1) + 1
        u, first = self.bit_add(a, (~b) & ((1 << width)-1), width)
        result, second = self.bit_add(u, 1, width)
        return result if first or second else None

    def distance(self, a, b):
        z = self.sub_or_none(a,b)
        return self.sub_or_none(b,a) if z is None else z

    def mul(self, a, b):
        out = 0
        for j in range(b.bit_length()):
            if (b >> j) & 1:
                out = self.add(out, a << j)
        return out

    def div(self, a, b):
        assert b > 0
        q = r = 0
        for j in reversed(range(a.bit_length())):
            r = (r << 1) | ((a >> j) & 1)
            candidate = self.sub_or_none(r, b)
            q = (q << 1) | (candidate is not None)
            if candidate is not None:
                r = candidate
        return q, r

    def mm(self, a, b, N):
        return self.div(self.mul(a,b), N)[1]

    def power(self, a, j, N):
        out = 1
        while j:
            if j & 1:
                out = self.mm(out,a,N)
            j >>= 1
            if j:
                a = self.mm(a,a,N)
        return out

    def gcd(self, a, b):
        while b:
            a, b = b, self.div(a,b)[1]
        return a


def model(k, Q, h):
    q,u = h.div(Q,k)
    return h.add(h.mul(k,h.mul(q,q)), h.mul(u,h.add(q << 1,1)))


def certify(h, N, a, b, candidate):
    if h.power(b,candidate,N) != 1:
        return None
    rem = candidate
    j = 2
    divisors = []
    while h.mul(j,j) <= rem:
        quotient,remainder = h.div(rem,j)
        if remainder==0:
            divisors.append(j)
            while remainder==0:
                rem = quotient
                quotient,remainder = h.div(rem,j)
        j += 1
    if rem>1:
        divisors.append(rem)
    for prime in divisors:
        exponent,remainder = h.div(candidate,prime)
        assert remainder==0
        if h.power(b,exponent,N)==1:
            return None
    c = h.power(a,candidate,N)
    k, prev = 0, None
    while c != 1:
        prev = c
        c = h.mm(c,c,N)
        k += 1
        assert k <= (N-1).bit_length()-1
    factor = None
    if prev is not None:
        g = h.gcd(N,h.sub_or_none(prev,1))
        if 1 < g < N:
            factor=g
    return candidate << k, factor


def check_case(h, N, a, s, R, T, seed):
    before=h.cells; n=(N-1).bit_length(); L=n+(n+s-1)//s; m=L-n+1; Q=1<<m
    assert R<=Q//2 and h.gcd(a,N)==1
    b=a
    for _ in range(n-1):
        b=h.mm(b,b,N)
    # Source recurrence on the actual all-zero path: identity feedback; complete
    # rows are integer multiples of e0 with a common denominator at each level.
    counts={1:1}
    mult=[b]
    for _ in range(m-1):
        mult.append(h.mm(mult[-1],mult[-1],N))
    for perm in reversed(mult):
        nxt=dict(counts)
        for z,c in counts.items():
            target=h.mm(perm,z,N)
            nxt[target]=h.add(nxt.get(target,0),c)
        counts=nxt
    direct=0
    for v in counts.values():
        direct=h.add(direct,h.mul(v,v))
    # Bounded comparison of all address pairs, factored by their true endpoint.
    labels=[h.power(b,j,N) for j in range(Q)]
    histogram={}
    for z in labels:
        histogram[z]=h.add(histogram.get(z,0),1)
    assert histogram==counts
    corr=0
    for z in labels:
        corr=h.add(corr,histogram[z])
    assert corr==direct
    rng=Random(seed)
    observed=0
    for _ in range(T):
        j=rng.getrandbits(m); k=rng.getrandbits(m)
        observed=h.add(observed,int(labels[j]==labels[k]))
    # Only the hit count, public sample size and parameter bound reach the decoder.
    def decode(hits, attempts):
        scores=[]
        for odd in range(1,R+1,2):
            scores.append((h.distance(hits << (2*m),h.mul(attempts,model(odd,Q,h))),odd))
        return min(scores)[1]
    exact=decode(direct,1<<(2*m)); inferred=decode(observed,T)
    result=certify(h,N,a,b,inferred)
    assert result is not None and inferred==exact
    return dict(N=N,a=a,s=s,L=L,m=m,Q=Q,R=R,collision_numerator=direct,denominator=1<<(2*m),
                trials=T,seed=seed,hits=observed,odd=inferred,order=result[0],factor=result[1],
                adder_cells=h.cells-before)


def hidden_odd_pair(h):
    N=631
    out=[]
    for a,d in ((3,315),(27,105)):
        b=a
        for _ in range((N-1).bit_length()-1):
            b=h.mm(b,b,N)
        result=certify(h,N,a,b,d)
        assert result is not None and result[0]==d<<1
        for s in (2,4):
            n=(N-1).bit_length()
            m=1+(n+s-1)//s
            Q=1<<m
            # No address collision implies the two arms have disjoint work support at every prefix.
            assert len({h.power(b,j,N) for j in range(Q)})==Q and d>=Q
            out.append(dict(N=N,a=a,order=result[0],odd=d,s=s,m=m,distinct=Q))
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--core",type=Path,default=Path("src/enterprise_math/brc_weighted_recurrent.py"))
    parser.add_argument("--record",type=Path)
    args=parser.parse_args()
    h=Digits(args.core);rows=[]
    for N,a,R in ((21,2,3),(341,2,7)):
        for s in (1,2,4):
            rows.append(check_case(h,N,a,s,R,4096,7319+s))
    summary={"core_sha256":CORE_SHA,"projection_trials":rows,"blind_prefix_pairs":hidden_odd_pair(h)}
    # Same Bernoulli outcome in every trial, with correct marginal but maximal dependence.
    Q,R=64,5
    endpoints=[min((h.distance(bit << 12,model(k,Q,h)),k) for k in (1,3,5))[1] for bit in (0,1)]
    assert endpoints==[5,1]
    summary["cloned_bit_selected_candidates"]=endpoints
    print(json.dumps(summary,indent=2))
    if args.record:
        args.record.write_text(json.dumps(summary,indent=2)+"\n")


if __name__=="__main__":
    main()
