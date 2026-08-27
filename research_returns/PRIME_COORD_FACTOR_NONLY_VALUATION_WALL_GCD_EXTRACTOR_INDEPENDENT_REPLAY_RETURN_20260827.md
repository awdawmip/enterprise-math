# Prime Coordinate N-only Valuation-Wall GCD Extractor — Independent Replay Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`  
Publication-ID: `TP2-DF186CDB4959BEA10875`  
Researcher-ID: `EM-PCF4R-6D96F8`  
Claim-ID: `chatgpt-pcf4r-20260827-1932`  
Execution record: `ER-27AB495541F655BAA420`  
Claim base: `839224dfac59072ecc7c6c027b30b906f5ee24f4`

## 1. Frozen verdict

`N_ONLY_GCD_EXTRACTOR_VERIFIED`

Hard target
`N_ONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENTLY_RECONSTRUCTED_AND_VERIFIED_OR_NARROWED_OR_REFUTED`
is met at exact theorem / task-return strength on the promised domain

\[
N=pq,\qquad 3<p<q,
\]

with distinct odd primes.

The construction receives only `N`, public constants, and public seed indices.
It uses no hidden factor, factor-labelled coordinate, prime scan, CRT idempotent,
or factor-derived phase.

**Boundary:** this is not a factorization-speedup theorem. The current kernel
construction is square-root scale in `N`, hence exponential in input bit length.

## 2. Exact local wall

Define

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s}.
\]

For prime `r>3` and `0<=s<r`, Legendre's formula gives

\[
\boxed{
v_r(A_s)=
\left\lfloor\frac{2s}{r}\right\rfloor+
\left\lfloor\frac{3s}{r}\right\rfloor
}.
\]

Indeed `r>=5` and `3s<=3r-3<r^2`, so no higher `r`-power contributes,
while `v_r(s!)=0`.

Hence, in this local range,

\[
\boxed{r\mid A_s\iff 3s\ge r}.
\]

Since `r>3` is prime, equality `3s=r` never occurs; `>=` and `>` are
equivalent at the threshold.

## 3. First dyadic nonunit theorem

Probe the public dyadic seeds

\[
s=1,2,4,8,\ldots
\]

and let `s_*` be the first seed with `gcd(A_s,N) != 1`.

Equivalently, `s_*` is the least power of two with `3s_*>=p`.
Its predecessor satisfies `3s_*/2<p`, so

\[
s_*<\frac{2p}{3}<p<q.
\]

Thus the local wall applies at both factors. At `s_*`, `p|A_{s_*}`.
Therefore

\[
\boxed{\gcd(A_{s_*},N)\in\{p,N\}}.
\]

The response cannot be `q`: the smaller factor's wall is reached first.

If the response is `p`, extraction is complete.

If the response is `N`, then `q|A_{s_*}`, so `q<=3s_*`; combining this
with dyadic minimality gives

\[
\boxed{q\le3s_*<2p}.
\]

Thus synchronization forces `q<2p`.

A purely public cap exists: if `L=N.bit_length()`, then `j=0,...,L-1`
contains the first nonunit dyadic seed, because `s_*<p<N<2^L`.

## 4. Exact synchronized fallback

Assume synchronization, so `q<2p`, and set

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor
=\left\lfloor\frac{\operatorname{isqrt}(N)}{3}\right\rfloor.
\]

Since `p<sqrt(N)<q` and `q<2p`,

\[
\sqrt N<\sqrt2\,p<\frac{3p}{2},
\]

so `t<p/2`; as `p` is odd, `t+1<p`. Both fallback seeds are below both
hidden primes, so the local wall still applies.

Also

\[
3t\le\sqrt N<q,
\]

hence `q` does not divide `A_t`.

If `3t>=p`, then `p|A_t` and

\[
\boxed{\gcd(A_t,N)=p}.
\]

Otherwise `3t<p<sqrt(N)<3t+3`, so

\[
p\in\{3t+1,3t+2\}.
\]

Then `p|A_{t+1}`. Because distinct odd primes have gap at least two,
and `3t+3>3` is divisible by `3`, both possibilities force

\[
q\ge3t+4>3(t+1).
\]

Hence `q` does not divide `A_{t+1}` and

\[
\boxed{\gcd(A_{t+1},N)=p}.
\]

Therefore one of the two public seeds `t,t+1` deterministically breaks
every synchronized dyadic response.

## 5. N-only algorithm

For promised input `N=pq`, `3<p<q`:

1. Let `L=N.bit_length()`.
2. For `j=0,...,L-1`, set `s=2^j` and compute `g=gcd(A_s,N)`.
3. If `1<g<N`, return `g`.
4. If `g=1`, continue.
5. If `g=N`, set `t=isqrt(N)//3`.
6. Probe `A_t`, then `A_{t+1}`, returning the first proper gcd.

Sections 3--4 prove that the failure branch is unreachable on the theorem
domain.

## 6. Exact recurrence and modular constructor

The integer kernel satisfies

\[
\boxed{
A_{s+1}(s+1)^3
=
6(2s+1)(3s+1)(3s+2)A_s,
\qquad A_0=1.
}
\]

Phase A additionally proves a constructor strengthening not needed by the
supplemental exact-integer implementation: every queried seed before
termination satisfies `s<p`. Hence `s!` is a unit modulo `N` and

\[
\boxed{
A_s\bmod N=
(2s)!(3s)!(s!)^{-5}\pmod N
}
\]

is valid in `Z/NZ`.

This keeps all live arithmetic at `O(log N)` bits. The independent checker
cross-checks this modular constructor and the modularized recurrence against
direct exact-binomial evaluation on bounded cases.

## 7. Complexity and memory

Let `L=ceil(log2 N)`.

The first dyadic nonunit satisfies

\[
s_*<2p/3<2\sqrt N/3.
\]

If each public dyadic seed is recomputed from scratch, the total seed length is
still geometric and therefore `O(p)`. The synchronized fallback costs another
`O(p)` modular-factorial steps because `t+1<p`.

Using schoolbook `L`-bit modular multiplication/reduction, a conservative
bound is

\[
\boxed{O(\sqrt N\,L^2)}
\]

bit operations, with `O(L)` streaming working memory, plus `O(L)` gcd/inverse
operations of lower aggregate order at this precision.

In terms of input bit length this is

\[
2^{L/2}\operatorname{poly}(L).
\]

Therefore:

`N_ONLY_GCD_EXTRACTOR_VERIFIED != FACTORIZATION_SPEEDUP_PROVED`.

The open algorithmic residue is complexity compression of the valuation-wall
support, not existence of an N-only splitter on the promised semiprime domain.

## 8. Phase-A independent regression

Phase-A proof and checker were frozen before opening the originating duplicate
execution's return or scripts.

Checker:

`scripts/check_prime_coord_factor_nonly_valuation_wall_gcd_extractor_replay.py`

Frozen command:

`python scripts/check_prime_coord_factor_nonly_valuation_wall_gcd_extractor_replay.py --prime-limit 2000`

Exact report:

- primes: `301`;
- distinct odd semiprimes: `45,150`;
- dyadic direct splits: `35,181`;
- synchronized/fallback splits: `9,969`;
- failures: `0`;
- local valuation-wall checks: `277,045`;
- recurrence/direct-constructor cross-checks: `166`;
- maximum returned seed in this range: `666`.

Finite regression is only a consistency guard. Universality is supplied by the
proof.

Phase-A artifact:

`research_artifacts/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY/PHASE_A_BLIND_RECONSTRUCTION.md`

Phase-A freeze head:

`f6f12c64d6d251631fa098f260e96d6d7127f253`.

### Independence disclosure

Before CLAIM, the scheduler reconciliation surface already exposed the
candidate's high-level shape and the headline synchronization inequality
`q<2p`. No duplicate-execution return, detailed derivation, script, or branch
was read before Phase-A freeze. The derivation and checker were independently
authored. This is recorded explicitly rather than overstating epistemic
blindness.

## 9. Phase-B comparison

After Phase-A freeze, Draft PR #715 was unsealed as supplemental evidence.

The two derivations agree on all load-bearing interfaces:

- the local valuation wall;
- the first dyadic alternative;
- synchronization `q<2p`;
- the two-seed square-root fallback;
- N-only constructor admissibility;
- independence from the conjectural weighted all-prime supercongruence.

No counterexample or endpoint mismatch was found.

There are two useful independent differences:

1. Phase A proves the `3t<p` fallback case through
   `p in {3t+1,3t+2}` and the odd-prime gap, rather than the supplemental
   `q mod 3` case split.
2. Phase A identifies the modular-unit constructor above, reducing the
   conservative live-integer cost from the supplemental exact-integer
   `O(p^2 log p)` bound to a square-root-scale modular
   `O(sqrt(N) L^2)` bound.

The supplemental execution remains non-authoritative for its parent claim race;
it is evidence for comparison, not execution authority for this replay.

Phase-B artifact:

`research_artifacts/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY/PHASE_B_COMPARISON_AND_DEDUP.md`

## 10. Current-tool dedup

At claim base `main@839224dfac59072ecc7c6c027b30b906f5ee24f4`, the
canonical scripts surface contains current PCF/half-coupling checkers but no
canonical N-only valuation-wall gcd extractor. Repository search found no
canonical method duplicate.

The only exact method match located is the explicitly non-authoritative
supplemental Draft PR #715. Its code is not silently promoted or copied into
canonical authority. This replay retains its independently authored modular
checker.

## 11. Frozen evidence

Machine-readable evidence:

`research_artifacts/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY/evidence_bundle.json`

Key Phase-A pins:

- derivation blob: `25c4a8c5ebf95fb896a61bf17c367e3e632a9cac`;
- derivation SHA256:
  `0c9ecb8b9911a82458362198ef698d99c52ccca842e9b935f5dba1f90a0fb7bc`;
- checker blob: `6d8c4d73c52c5ae27c0ce974d845dc16fe8e4701`;
- checker SHA256:
  `5d61d0236b7f891151a83f9b216ad7e28547695dd9671c3fb33302b4686a30cf`.

## 12. Driver recommendation

Recommended disposition:

`ACCEPT / EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM`.

What is closed by this task:

- exact local factorial valuation wall;
- deterministic first-dyadic alternative;
- synchronization endpoint;
- deterministic N-only two-seed fallback;
- modular constructor admissibility;
- exact recurrence;
- theorem-level semiprime splitting on `3<p<q`.

What remains open:

`COMPLEXITY_COMPRESSION_OF_THETA(p)_SCALE_VALUATION_WALL`.

A successor is justified only if it attacks the support/time complexity, or
benchmarks this sealed extractor against appropriate classical baselines. A
successor should not merely repeat larger finite semiprime scans.

No Foundation mutation, Working Truth grant, tool-family promotion, or prime
coordinate canonicalization is requested.
