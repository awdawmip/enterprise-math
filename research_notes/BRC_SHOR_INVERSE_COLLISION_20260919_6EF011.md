# BRC/Shor: pair-count readout and inverse collision order

Progress-Event-ID: `brc-shor-inverse-collision-20260919-6EF011`
Researcher-ID: `EM-DIRECT-6EF011`
Research-Activity-ID: `RA-6EF011C2E75C4A799606AFEA`
Session: `chat-local-brc-shor-6ef011c2e75c4a799606afeaed1dc416` (locally assigned, not authenticated platform identity).
Status: `ELEMENTARY_DERIVATION / FINITE_REFERENCE_CHECK / RESEARCH_DIRECTION / NOT_PROMOTED`.
User question: 综合现在已有的成果 brc模拟shor算法有没有新的思路.
Read snapshots: GLOBAL_KNOWLEDGE `af67de93c661143349855d0af555327bcfb4da67`; EM `d20fbca83ae79b354a9ce2b0659477065a83993b`.
No formal Task-ID, CLAIM, independent review, Working Truth, Foundation promotion, production modification, or asymptotic speedup.

## Existing interfaces actually applied

At the EM read snapshot:
- `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json` and `definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md`: positive branch alternatives add counts; serial composition multiplies counts. REUSE_APPLIED, not source executable execution. A coefficient 2 here denotes two unit branches, not a single branch of weight 2 when dominant single-path mass matters.
- `docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md`: q(x)=q(y) implies equality of the declared future observation. REUSE_APPLIED to retaining modular residue and, only when needed, exponent difference. Different residues may still be distinguished by remaining modular products and must not be collapsed to one total.
- `research_notes/NUMBER_FIELD_DEFECT_SYNTHESIS_20260919_AD0416.md`: preserve exact identity, common depth, remainder, phase and merging multiplicities. Finite carry control does not bound total state/communication cost. Reciprocal shell intersections and Hecke multiplicities remain different typed objects.
- `tool_invocation_policy.json`: this is a domain specialization and research candidate, not a new general-purpose admitted tool family. Positive BRC still does not implement general complex-amplitude cancellation.

## 1. Full Shor output as a positive pair histogram plus a character

Let N>=3, 1<a<N, gcd(a,N)=1, Q=2^m>=N^2, f(x)=a^x mod N, and r=ord_N(a). The candidate computation below never receives r or factors of N.

For 0<=d<Q define
C(d)=#{(x,y):0<=x,y<Q, f(x)=f(y), x-y=d mod Q}.

For the usual Fourier readout of the modular-exponentiation state, without conditioning on the second register,
P(k)=Q^(-2) sum_d C(d) exp(2*pi*i*k*d/Q).

Proof: expand the squared amplitude separately within each equal-f(x) fiber and sum over the discarded second register. Counts are nonnegative integers; phase remains an explicit separate character observer. This does not replace complex amplitudes with positive probabilities. Fourier invertibility makes the full C vector complete for all P(k); this statement gives no efficient compression.

In the group algebra of units modulo N, write [u][v]=[uv mod N], let g_j=a^(2^j) mod N, and impose z^Q=1. Then
C(z) = coeff_[1] product_(j=0)^(m-1) (2[1]+z^(2^j)[g_j]+z^(-2^j)[g_j^(-1)]).

The three terms collect bit pairs (0,0)/(1,1), (1,0), (0,1), respectively. All g_j are obtained by repeated squaring, and modular inverses require no factorization. This is a combinatorial identity, not a native-force or physical-triad assertion.

For checking only, the unfolded pair count at difference d is (Q-|d|)*1_(r divides d), -Q<d<Q. An implementation using this formula with precomputed r is not an order-finding algorithm.

## 2. Stronger narrow observer: one collision mass determines r

Define
K_Q = sum_u n_u^2 = #{(x,y):f(x)=f(y)} = sum_d C(d) = Q^2 P(0),
where n_u is the size of the modular-output fiber. This is the second moment of FIBER OCCUPANCY. The second moment of the original unit branch weights is merely Q and is not K_Q.

Write Q=q*r+s, 0<=s<r. Since powers of a form one r-cycle, r-s occupied fibers have size q and s have size q+1. Hence
K_Q=(r-s)q^2+s(q+1)^2=(Q^2+s(r-s))/r.
Consequently
0 <= r-Q^2/K_Q = r*s(r-s)/(Q^2+s(r-s)) <= r^3/(4Q^2) < 1/2,
since r<N and Q>=N^2. Therefore
r = nearest_integer(Q^2/K_Q).

Exact integer readout is (2*Q*Q+K_Q)//(2*K_Q). No floating-point calculation is needed. For N=21,a=2,Q=512, K_Q=43692 and Q^2/K_Q=6-2/10923, giving r=6. The standard gcd extraction then gives gcd(8-1,21)=7 and gcd(8+1,21)=3 in this example; arbitrary bases may need retry.

Setting z=1 gives a strictly positive coefficient problem:
K_Q = coeff_[1] product_j (2[1]+[g_j]+[g_j^(-1)]).
For this one observer the exponent-difference coordinate is safely forgettable, because future factors act only on the modular residue. No general phase cancellation theorem has been invoked.

This basic counting/rounding derivation is not asserted to be globally novel. Its research value here is the observer-specific reduction of the user's BRC/Shor objective.

## 3. Reference implementation and honest cost

A minimal executable version uses only Python standard-library arithmetic:

```python
from collections import defaultdict
from math import gcd

def collision_order(N, a):
    if N < 3 or not 1 < a < N or gcd(a, N) != 1:
        raise ValueError('require a unit a modulo N')
    m = (N*N - 1).bit_length()
    Q = 1 << m
    counts, g = {1: 1}, a
    for _ in range(m):
        nxt = defaultdict(int)
        inverse = pow(g, -1, N)
        for u, c in counts.items():
            nxt[u] += 2*c
            nxt[u*g % N] += c
            nxt[u*inverse % N] += c
        counts, g = dict(nxt), g*g % N
    K = counts[1]
    return (2*Q*Q+K)//(2*K), K, len(counts)
```

This naive implementation explicitly reaches all r subgroup residues. Its count-update complexity is O(m*r), ignoring bit-operation factors, and its explicit residue width is r. Even the final support size already reveals r. It is a correctness reference, NOT an efficient classical factoring algorithm or an advantage over orbit traversal. The full (residue,difference) version reaches O(Q) states. Polynomial size of the product expression does not imply polynomial cost of coefficient extraction.

The important next question is whether the single unit coefficient can be computed or rigorously enclosed without enumerating the r-cycle. A certified [K_-,K_+] suffices when [Q^2/K_+,Q^2/K_-] lies inside one nearest-integer cell. Bounding it that tightly without already knowing the order is the unresolved algorithmic unit.

Approximating P(0) needs absolute accuracy on the order of 1/r^2 to distinguish neighboring orders. Storing that precision takes O(log r) bits, but obtaining it is not free. Naive independent Bernoulli estimation at P(0) about 1/r has variance about 1/(r*T) and thus a sample requirement of order r^3 for that precision. Exact single-output strong simulation is not the same capability as efficient approximate sampling.

## 4. Scoped obstruction and alternate continuation

For h(t)=1_(a^t=1), the r-by-r matrix H_ij=h(i+j), 0<=i,j<r, is a permutation matrix and has rank r. Any finite-dimensional linear realization reproducing this complete all-time return sequence therefore has dimension at least r. This is NOT a lower bound on every classical factoring algorithm, symbolic representation, finite-block coefficient method, approximate sampler, or physical model. It discourages demanding a constant-state port signature for every possible future return observation.

For full Shor sampling, keep C(d) or an adequate phase-aware conditional observer. Low-bit marginal identity, b mod 2^j:
Pr(k mod 2^j=b)=(Q*2^j)^(-1) sum_t C(t*Q/2^j) exp(2*pi*i*b*t/2^j).
It was checked against the full finite distribution. Semiclassical QFT and adaptive readout are established prior art, not discoveries here. The unresolved cost stays in the modular correlations.

A multibase extension uses Phi(v)=product_i a_i^(v_i) mod N, L=ker(Phi), and its character/dual-lattice observer. This is a possible bridge to exact remainder/phase geometry, not an identification of ordinary reciprocal shells with the Fourier dual, nor a deduction from six native spatial axes. Regev's multidimensional quantum factoring is a comparison baseline, not a classical solution supplied by BRC.

## 5. Actual local checks

`pair_histogram_check.py` independently constructs modular-value fibers, exact ordered-pair histograms and per-fiber Fourier probabilities. The candidate receives only N,a,m; a separate order routine is used solely for comparison. All eight exact histogram and collision-order checks passed:

|N|a|Q|r recovered|K_Q|peak collision residues|
|--:|--:|--:|--:|--:|--:|
|15|2|256|4|16384|4|
|21|2|512|6|43692|6|
|21|4|512|3|87382|3|
|33|5|2048|10|419432|10|
|35|2|2048|12|349528|12|
|55|2|4096|20|838864|20|
|77|2|8192|30|2236964|30|
|77|4|8192|15|4473926|15|

Maximum floating full-readout discrepancy: 2.7755575615628914e-17. Maximum checked low-bit marginal discrepancy: 1.5543122344752192e-15. Integer histograms and recovered orders were compared exactly; FFT comparisons are only numerical checks. The identical-positive-mass/opposite-Hadamard-output witness also passed.

No blind large-instance or asymptotic benchmark, independent implementation review, Lean proof, EM source suite, activity guard execution, or runtime integration is claimed. Original detailed code/results are delivered locally; the embedded minimal algorithm above preserves an executable EM continuation point.

## External primary comparison sources

- Shor, arXiv:quant-ph/9508027, polynomial-time quantum factoring/order finding.
- Griffiths and Niu, arXiv:quant-ph/9511007, semiclassical Fourier transform.
- Browne, arXiv:quant-ph/0612021, classical semiclassical-QFT simulation and its input-state limitations.
- Wang, Hill and Hollenberg, arXiv:1501.07644, matrix-product-state Shor simulation with order-dependent resources.
- Regev, arXiv:2308.06572, multidimensional quantum factoring; Pilatte, arXiv:2404.16450, unconditional correctness results.

## Next smallest unit

Develop one observer-specific non-enumerative method or rigorously certified enclosure for the unit coefficient above, with explicit input-bit, precision and retained-state costs. Do not inject r, factors, orbit labels, unknown discrete logarithms, or factor-based CRT data. Compare against ordinary orbit/order algorithms and an existing tensor-network baseline; include orders with nontrivial odd components. A proved obstruction for a precisely declared compression family is a useful result, not a global impossibility claim.
