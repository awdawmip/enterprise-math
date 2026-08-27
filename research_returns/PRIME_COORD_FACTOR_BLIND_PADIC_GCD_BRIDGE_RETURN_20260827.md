# Prime Coordinate Blind p-adic-to-GCD Bridge — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE`  
Publication-ID: `TP2-7B0534E09E4286CB5B6E`  
Researcher-ID: `EM-PCF4-F9AD88`  
Claim-ID: `chatgpt-pcf4-20260827-1718`  
Execution record: `ER-35E187B7C5FE5046F8F1`

## 1. Frozen verdict

`GCD_EXTRACTOR_PROVED`

Hard target `BLIND_PADIC_GCD_BRIDGE_PROVED_REFUTED_OR_EXACTLY_OBSTRUCTED` is met at research-return strength.

There is an explicit factor-blind integer kernel and deterministic public seed policy which, for every semiprime

\[
N=pq,\qquad p<q
\]

with distinct odd primes, returns a proper factor from `N` alone.  The case `p=3` is removed by the public precheck `gcd(N,6)`; the load-bearing theorem therefore assumes `3<p<q`.

**Important boundary.** This is an exact extraction theorem, not a factoring-speedup theorem.  The elementary exact implementation has support cost polynomial in the smaller factor `p`, hence exponential in the input bit length on balanced semiprimes.  No polynomial-time, sub-square-root, or novelty claim is made.

## 2. N-only construction

Use the frozen Enterprise integer kernel

\[
\boxed{
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s}.
}
\]

Define the candidate residue

\[
\boxed{G_N(s)=A_s.}
\]

Only `gcd(G_N(s),N)` is observed; equivalently `A_s mod N` may be taken after exact integer construction.  No `p`, `q`, factor-labelled coordinate, CRT idempotent, factor-derived phase or prime scan is an input.

### Deterministic seed/stopping policy

1. Compute `d=gcd(N,6)`.  If `1<d<N`, return `d`.
2. Probe public dyadic seeds
   \[
   s=1,2,4,8,\ldots
   \]
   up to a bit-length-only cap.  At each seed compute `g=gcd(A_s,N)`.
3. If `1<g<N`, return `g`.
4. If the first non-unit response is `g=N`, set
   \[
   t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor
   =\left\lfloor\frac{\operatorname{isqrt}(N)}3\right\rfloor
   \]
   and probe `t,t+1`; return the first proper gcd.
5. On the stated semiprime domain one of these probes is proved to return a proper factor, so the failure branch is unreachable.

The candidate side receives only `N` and this public schedule.

## 3. Exact local valuation law

Let `r>3` be prime and `0<=s<r`.  Since `3s<3r<r^2`, Legendre's factorial formula gives

\[
\begin{aligned}
v_r(A_s)
&=v_r((2s)!)+v_r((3s)!)-5v_r(s!)\\
&=\left\lfloor\frac{2s}{r}\right\rfloor
 +\left\lfloor\frac{3s}{r}\right\rfloor.
\end{aligned}
\tag{V}
\]

Thus, while `s<r`, the first local divisibility wall is exactly `3s>r` (equality is impossible for a prime `r>3`).  This is the N-only asymmetry source.

CRT-wise, for `N=pq`, the kernel state is read as

\[
A_s\pmod N\longleftrightarrow
(A_s\bmod p,\ A_s\bmod q).
\]

The three relevant states are therefore

- `(nonzero,nonzero)` — nowhere vanishing, gcd `1`;
- `(0,nonzero)` — asymmetric, gcd `p`;
- `(0,0)` — synchronized, gcd `N`.

No factor-labelled constructor is used to obtain these states.

## 4. Dyadic collision theorem

Assume `3<p<q` and let

\[
j_*=\min\{j\ge0:3\cdot2^j>p\},\qquad s_*=2^{j_*}.
\]

Because `p>3` is prime, equality with a multiple of `3` is impossible.  Minimality gives

\[
3s_*/2<p<3s_*<2p,
\qquad
s_*<\frac{2p}{3}<p.
\tag{D1}
\]

For every earlier dyadic seed `s<s_*`, `3s<p<q`, so neither hidden prime divides `A_s`; hence the observed gcd is `1`.

At `s=s_*`, equation `(V)` gives `v_p(A_s)>=1`.  Since `s_*<p<q`, the same valuation law applies at `q`:

- if `q>3s_*`, then `v_q(A_s)=0`, so
  \[
  \boxed{\gcd(A_{s_*},N)=p};
  \]
- if `q<3s_*`, then `v_q(A_s)>=1`, so
  \[
  \boxed{\gcd(A_{s_*},N)=N}.
  \]

The second case is the complete synchronization set at the first collision.  By `(D1)` it implies

\[
\boxed{q<2p}.
\tag{SYNC}
\]

So a synchronized dyadic response is not a dead end: it proves a strong balance condition which makes the public square-root fallback exact.

## 5. Exact synchronization-breaking fallback

Assume the synchronized case, hence `q<2p`, and put

\[
t=\left\lfloor\frac{\sqrt{pq}}3\right\rfloor.
\]

Because `p<\sqrt{pq}<q`, exactly one of the following holds.

### Case A: `3t>p`

Then

\[
p<3t<\sqrt{pq}<q.
\]

Also `t<p` because `q<2p` gives

\[
t+1<\frac{\sqrt2}{3}p+1<p
\]

for every `p>=5`.  Hence `(V)` applies at both factors and gives

\[
\boxed{\gcd(A_t,N)=p}.
\]

### Case B: `3t<p`

Now `3(t+1)>\sqrt{pq}>p`.  It remains to prove `3(t+1)<q`.

The number `3(t+1)` is the least multiple of `3` strictly above `sqrt(pq)`.  Since `q>3` is prime:

- if `q≡1 (mod 3)`, then `q-1` is a multiple of `3`; distinct odd primes give `p<=q-2`, and
  \[
  \sqrt{pq}\le\sqrt{q(q-2)}<q-1;
  \]
- if `q≡2 (mod 3)`, then `q-2` is a multiple of `3`; `p=q-2` would make `p>3` divisible by `3`, impossible, so `p<=q-4`, and
  \[
  \sqrt{pq}\le\sqrt{q(q-4)}<q-2.
  \]

Therefore in either residue class the least multiple of `3` above `sqrt(pq)` is still below `q`.  Thus

\[
p<3(t+1)<q,
\]

and, since `t+1<p`, equation `(V)` yields

\[
\boxed{\gcd(A_{t+1},N)=p}.
\]

Hence the two public fallback seeds `t,t+1` deterministically break every synchronized dyadic response.

## 6. Main theorem

### Theorem — factor-blind Enterprise-kernel splitter

Let `N=pq` with distinct odd primes `p<q`.  Apply the public algorithm of Section 2.

- If `p=3`, the precheck `gcd(N,6)` returns `3`.
- If `p>3`, all dyadic probes before `j_*` return `1`.
- The first non-unit dyadic probe returns either `p` or `N`.
- If it returns `N`, the fallback probes `floor(sqrt(N)/3)` and its successor contain a guaranteed proper split.

Therefore the algorithm terminates with

\[
\boxed{1<g<N,\qquad g\mid N}
\]

for every distinct odd semiprime `N`, using only `N` and public parameters.

The success probability is exactly `1` on the theorem domain.

## 7. Deterministic seed bound and complete response set

At the first dyadic collision,

\[
s_*<\frac{2p}{3}.
\]

Thus the number of gcd probes before the first non-unit response is `O(log p)`, and a bit-length-only cap `O(log N)` is sufficient.

The response set on the theorem domain is exact:

1. `p=3`: public small-prime precheck returns `3`;
2. `j<j_*`: `gcd(A_{2^j},N)=1`;
3. `j=j_*` and `q>3s_*`: proper factor `p`;
4. `j=j_*` and `q<3s_*`: synchronized value `N`, necessarily with `q<2p`;
5. synchronized case: one of `t,t+1` returns `p`.

There is no residual nowhere-vanishing or doubly-vanishing failure set on distinct odd semiprimes.

## 8. Complexity and non-speedup boundary

The exact recurrence

\[
\boxed{
A_{k+1}
=A_k\,
\frac{6(2k+1)(3k+1)(3k+2)}{(k+1)^3}
}
\tag{R}
\]

uses an exact integer division at every step; it never performs an invalid division in `Z/NZ`.

Stirling gives

\[
A_s=\Theta(108^s s^{-3/2}),
\]

so `A_s` has `Theta(s)` bits.  A simple exact recurrence implementation up to seed `s` uses `s` steps, `O(s)`-bit live integers, and a conservative schoolbook bit-cost `O(s^2 log s)` with `O(s)` bits of kernel memory.  The dyadic indices are geometric, and the largest theorem-forced index is `O(p)`, so the elementary implementation is bounded by

\[
O(p^2\log p)
\]

bit operations plus `O(log p)` gcd probes.  On balanced semiprimes `p=Theta(sqrt(N))`, this is exponential in the input bit length `n=ceil(log_2 N)`.

Accordingly:

`GCD_EXTRACTOR_PROVED != FACTORIZATION_SPEEDUP_PROVED`.

The theorem replaces candidate-prime scanning by an exact kernel-support/valuation wall, but the present construction does not prove a better asymptotic factoring complexity.  PCF2 should benchmark it against factorial-product, trial-division, product-tree and faster classical baselines before any algorithmic significance is inferred.

## 9. Independence from the unproved all-prime supercongruence

The predecessor half-coupling work studies

\[
S_p=\sum_{n=0}^{p-1}(6n+1)A_n216^{-n}
\]

and its conjectural all-prime mod-`p^3` fingerprint.  That stronger congruence is **not used** in this proof.

The present bridge uses only:

- the frozen exact integer kernel `A_s`;
- elementary prime valuations of factorials;
- exact integer recurrence `(R)`;
- integer square root and gcd.

Thus the factor extraction theorem remains valid even if the stronger weighted all-prime congruence is later refuted.

## 10. Two independent exact checkers

Candidate-side checker A:

- `scripts/check_pcf4_blind_padic_gcd_bridge.py`
- direct exact `math.comb` construction of `A_s`.

Candidate-side checker B:

- `scripts/check_pcf4_blind_padic_gcd_bridge_independent.py`
- independent exact recurrence `(R)` with divisibility assertions.

Neither candidate extractor receives hidden factors.

Authoring-time external-oracle regression over every pair of distinct odd primes below `300`:

- semiprime cases: `1830`;
- direct checker failures: `0`;
- recurrence checker failures: `0`;
- cross-implementation mismatches: `0`;
- synchronized cases requiring fallback: `400`;
- maximum recorded candidate trace length: `10`.

These finite checks are regression evidence only; theorem closure is supplied by Sections 3–6.

Machine-readable evidence:

- `research_artifacts/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE/evidence_bundle.json`
- authoring SHA256: `6a97596a98d5a44866069726de2c81ef7c3d22898e9db61800c7173290f8359a`.

## 11. Source/dependency pins

- current publication taskbook blob: `sha1:1b7c1988d59492f709e4afc0755a3c1300289cf1`;
- generation-1 taskbook blob: `sha1:f1cce110096911438d5633a0cb9a1b4350c2a7d1`;
- PCF1 accepted input audit result: `RR-B8D8679EB033E990E825`;
- PCF1 return blob: `sha1:650a01f59534f2652b033873cc7c4dcd8038723a`;
- frozen blind p-adic task source commit: `8e8ec2fde8adeb4c75580075d63ac76adc562536`.

PCF1's constructor boundary is respected: no factor-labelled data enter the candidate path.

## 12. Remaining boundary and Driver recommendation

The exact missing interface `N_ONLY_ASYMMETRY_GENERATOR` is now instantiated at theorem level by the valuation wall of `A_s`.

What remains open is **complexity compression**, not existence of an N-only splitter:

> Can the same hidden-prime valuation wall be detected or compressed in time polynomial in `log N`, or at least below the strongest relevant classical factorization baseline, without materializing an `A_s` whose index is `Theta(p)`?

Recommended control-plane disposition:

1. accept this result only as `EXACT_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM`;
2. feed the sealed algorithm to PCF2 for adversarial benchmarking against classical factorial/product-tree/Strassen-style baselines;
3. let PCF3 analyze the hidden-factor separation spectrum of the kernel wall;
4. do not promote a factoring-speedup theorem from this result alone.

No Foundation, physics, or canonical prime-coordinate promotion is requested.
