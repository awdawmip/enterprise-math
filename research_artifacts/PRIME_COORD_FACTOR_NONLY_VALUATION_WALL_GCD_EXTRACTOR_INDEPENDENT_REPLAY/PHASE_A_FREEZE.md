# PCF4R Phase-A Blind-Forward Freeze — N-only Valuation-Wall GCD Extractor

Status: `PHASE_A_FROZEN / POSITIVE UNIVERSAL CANDIDATE / SOURCE_COMPARISON_NOT_YET_OPENED`

Date: `2026-08-27`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Researcher-ID: `EM-PCF4R-D74517`

Claim: `chatgpt-pcf4r-20260827-1927`

## 1. Blind-forward boundary

This freeze was derived before reading the originating non-authoritative duplicate execution, its return, scripts, or discussion.

Allowed Phase-A inputs used:

- the published taskbook;
- accepted parent fixed-public-prefix result only as scope context;
- standard elementary number theory;
- independently authored exact-integer / modular code.

No hidden factor is used by the constructor. Hidden `p,q` appear only in proof-side reasoning and regression oracles.

## 2. Observable and exact recurrence

Let

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s}.
\]

Hence `A_s` is an integer. With `A_0=1`,

\[
\boxed{
A_s
=
A_{s-1}
\frac{6(2s-1)(3s-2)(3s-1)}{s^3}
}\qquad(s\ge1).
\]

For a modulus `N`, whenever `gcd(s,N)=1`, the same identity gives an exact modular update by inverting `s^3 mod N`. The constructor checks `gcd(s,N)` before inversion; a nontrivial denominator gcd is itself already a factor.

## 3. Local valuation wall

Let `r>3` be prime and `0<=s<r`. Since `s<r`, `2s<2r<r^2`, and `3s<3r<r^2`,

\[
v_r(s!)=0,\quad
v_r((2s)!)=\left\lfloor\frac{2s}{r}\right\rfloor,\quad
v_r((3s)!)=\left\lfloor\frac{3s}{r}\right\rfloor .
\]

Therefore

\[
\boxed{
v_r(A_s)
=
\left\lfloor\frac{2s}{r}\right\rfloor
+
\left\lfloor\frac{3s}{r}\right\rfloor
}\qquad(0\le s<r).
\]

In particular,

\[
\boxed{r\mid A_s\iff 3s\ge r}\qquad(0\le s<r),
\]

because `3s<r` forces both floors to vanish, while `3s>=r` makes the second floor positive.

Thus the first local wall is exactly

\[
h_r=\left\lceil\frac r3\right\rceil.
\]

## 4. First dyadic nonunit theorem

Let

\[
N=pq,\qquad 3<p<q
\]

with distinct odd primes. Probe only public dyadic seeds

\[
s=1,2,4,8,\ldots
\]

and stop at the first seed with `gcd(A_s,N)>1`.

### 4.1 The stop exists before `p`

Let `h=ceil(p/3)` and let `d` be the least power of two with `d>=h`. Then `d<2h`.

Since a prime `p>3` is `6k-1` or `6k+1`:

- if `p=6k-1`, then `h=2k` and `2h=4k<6k-1=p`;
- if `p=6k+1`, then `h=2k+1` and `2h=4k+2<6k+1=p`.

Hence

\[
d<p.
\]

The local wall gives `p|A_d`, so the first nonunit dyadic seed `s` satisfies

\[
\boxed{s<p<q}.
\]

Therefore the local valuation law is valid simultaneously for both hidden factors at that first stopping seed.

### 4.2 Exact alternative

At the first nonunit seed, any divisibility by `q` also implies divisibility by `p`, because under `s<p<q` the criterion is exactly `r|A_s iff r<=3s`.

Hence

\[
\boxed{\gcd(A_s,N)\in\{p,N\}}.
\]

If the gcd is `p`, factorization is complete.

If the gcd is `N`, let `u=s/2`. The previous dyadic probe is a unit, so

\[
3u<p.
\]

At the current seed, `q|A_s`, so

\[
q\le3s=6u.
\]

Therefore

\[
\boxed{3u<p<q\le6u}
\]

and in particular

\[
\boxed{q<2p}.
\]

Thus the apparently trivial `gcd=N` branch is a synchronization certificate, not a dead end.

## 5. Synchronized square-root two-seed fallback

Assume the synchronization branch `q<2p`. Put

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor.
\]

Because `N` is not a square,

\[
3t<\sqrt N<3t+3.
\]

Also

\[
p<\sqrt N<q.
\]

The synchronization bound implies

\[
\sqrt N=\sqrt{pq}<\sqrt2\,p<\frac32p,
\]

hence `t<p/2` and therefore

\[
\boxed{t+1<p}
\]

for odd `p>=5`. Thus the local wall is again valid for both factors at `t,t+1`.

Since `3t<sqrt(N)<q`, `q` does not divide `A_t`. Therefore `gcd(A_t,N)` is either `1` or `p`.

- If `p<=3t`, then `gcd(A_t,N)=p`.
- Otherwise `3t<p`. If also `q<=3t+3`, then the two distinct primes `p<q` would both have to lie among `3t+1,3t+2,3t+3`. The last is divisible by `3`, and the first two are consecutive so one is even. Two odd primes greater than `3` cannot occupy those two slots. Contradiction.

Therefore in the second case

\[
3(t+1)<q
\]

while `p<3(t+1)`, and consequently

\[
\gcd(A_{t+1},N)=p.
\]

So the synchronized fallback is exact:

\[
\boxed{
\gcd(A_t,N)=p
\quad\text{or}\quad
\bigl(\gcd(A_t,N)=1\ \text{and}\ \gcd(A_{t+1},N)=p\bigr).
}
\]

## 6. Public N-only stopping rule

Constructor input: only `N`.

1. Stream `A_s mod N` from `s=1` upward using the exact recurrence.
2. At dyadic indices `1,2,4,...`, compute `g=gcd(A_s,N)`.
3. At the first `g>1`:
   - if `1<g<N`, return `g`;
   - if `g=N`, set `t=isqrt(N)//3`, test the already-computed residues at `t` and then `t+1`, and return the first nontrivial gcd.
4. Before each modular inversion of `s^3`, test `gcd(s,N)`; a nontrivial gcd can be returned immediately.

No prime enumeration, primality scan, trial divisor query, or hidden-factor-dependent seed appears in the constructor.

In the theorem path the first dyadic stop has `s<p`, and in the synchronized branch `t+1<p`; hence every denominator actually inverted is a unit modulo `N`.

## 7. Complexity

Let `n=ceil(log2 N)`. The first dyadic stopping seed satisfies

\[
s<p<\sqrt N.
\]

A streaming implementation performs `O(s)` modular recurrence steps. With `M(n)` denoting `n`-bit multiplication cost and extended-gcd inversion bounded by `O(M(n)\log n)`, the bit complexity is

\[
\boxed{O(\sqrt N\,M(n)\log n)}
\]

in the worst case, with `O(n)` working memory if only the current residue and the two public fallback residues are retained.

This is exponential in input bit length (`sqrt(N)=2^{Theta(n)}`) and is not a factoring-speedup theorem. Its value is the exact factor-blind asymmetry mechanism.

## 8. Independent checker freeze

Checker:

`scripts/check_prime_coord_factor_nonly_valuation_wall_replay.py`

SHA-256:

`ad0659389524d0c9c4f4c5c8c6317d881e182f5abf5cdb5d8fbf11526394431a`

Frozen run:

`PASS valuation_checks=76122 recurrence_checks=357 exhaustive_semiprimes=4278 synchronized_cases=928 adversarial_semiprimes=2000 modes=DYADIC:3350,FALLBACK_T:883,FALLBACK_T1:45`

Interpretation:

- `76,122` exact local valuation checks for primes `5<=r<=997`;
- `357` modular-recurrence crosschecks against direct exact `A_s`;
- exhaustive all distinct prime pairs `5<=p<q<=499`: `4,278` semiprimes, zero failures;
- `928` synchronized first-dyadic `gcd=N` cases, all satisfying `q<2p` and the two-seed fallback;
- `2,000` additional deterministic adversarial semiprimes drawn from primes up to `5000`, emphasizing adjacent primes, `q` near `2p`, and highly imbalanced pairs; zero failures.

Finite computation is regression evidence only. The universal claim rests on the proofs above.

## 9. Phase-A freeze verdict

\[
\boxed{\texttt{N_ONLY_GCD_EXTRACTOR_VERIFIED_CANDIDATE}}
\]

at blind-forward Phase-A strength.

This label is intentionally not yet the task-final verdict. Phase B must now compare this derivation against the withheld supplemental execution and run current tool/method dedup before provenance and final return are frozen.
