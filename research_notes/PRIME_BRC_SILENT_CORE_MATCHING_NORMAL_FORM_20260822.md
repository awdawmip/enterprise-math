# Prime-BRC Silent-Core Matching Normal Form

Status: `OWNER-LOCAL L3 RESEARCH NOTE / PROVED ELEMENTARY REFINEMENT / NOT LEGENDRE`
Date: `2026-08-22`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Depends on: `PRIME_BRC_POLARITY_SILENT_SEMIPRIME_CORE_20260822.md`

## 1. Stronger cofactor range

For `k>=10`, an anchor-surviving polarity-silent composite has already been proved to be

\[
n=pq,\qquad k/2<p\le k<q.
\]

Because `q>k`, each of the two half basins contains at most one multiple of `q`.  Silence `chi_q=0` therefore forces one strict-interior `q`-multiple on each side of `M`.  They are consecutive multiples, separated by exactly `q`.

The largest possible distance between two strict square-basin states is

\[
(U-1)-(L+1)=2k-1.
\]

Hence

\[
\boxed{k<q\le2k-1.}
\]

So the ambiguity core lives in the exact bilinear rectangle

\[
\boxed{
(p,q)\in
\bigl(\mathbb P\cap(k/2,k]\bigr)
\times
\bigl(\mathbb P\cap(k,2k)\bigr).
}
\]

## 2. Matching theorem

No two silent semiprimes can share the same least prime `p`; this is the fixed-p theorem from the parent note.

No two can share the same cofactor prime `q` either.

Indeed, if `pq` and `p'q` were two silent states for the same `q>k`, the condition `chi_q=0` says that these are exactly the unique `q`-multiple on each side of `M`.  Hence the multipliers are consecutive:

\[
|p-p'|=1.
\]

But `p,p'>k/2>=5` are odd primes.  Two odd primes cannot differ by one.  Contradiction.

Therefore the silent core is a partial bipartite matching:

\[
\boxed{
\mathcal S_k
\subset
P_-(k)\times P_+(k),
}
\]

where

\[
P_-(k)=\mathbb P\cap(k/2,k],
\qquad
P_+(k)=\mathbb P\cap(k,2k),
\]

and both coordinate projections are injective.

Consequently

\[
\boxed{
|\mathcal S_k|
\le
\min\bigl(\pi(k)-\pi(k/2),\ \pi(2k-1)-\pi(k)\bigr).
}
\]

This is still only an ambiguity budget; it does not control non-silent composites.

## 3. Deterministic q_* candidate for each p

Fix a possible silent least prime

\[
k/2<p\le k,
\]

with `p` transverse to `M` and `chi_p=0`.

Write

\[
k=p+t,
\qquad
t(t+1)=hp+s,
\qquad
Q=\lfloor M/p\rfloor.
\]

Let the common directional carry bit be

\[
c=b_-=b_+\in\{0,1\}.
\]

The parent fixed-p theorem proves that the entire shell contains at most one silent semiprime.  In fact it selects one deterministic *integer candidate* before primality is tested.

### c=0 — two p-hits

The only cofactor values are

\[
Q,\quad Q+1.
\]

Since a silent cofactor prime is `>k>=10`, it is odd.  Therefore

\[
\boxed{
q_*=\begin{cases}
Q,&Q\text{ odd},\\
Q+1,&Q\text{ even}.
\end{cases}}
\]

The side is lower when `Q` is odd and upper when `Q` is even.

### c=1 — four p-hits

The cofactor values are

\[
Q-1,Q,Q+1,Q+2.
\]

If `Q` is odd, the only possible prime pair is `Q,Q+2`, but the parent theorem proves `Q` cannot be silent.  Thus only `Q+2` survives.

If `Q` is even, the only possible prime pair is `Q-1,Q+1`, but the parent theorem proves `Q+1` cannot be silent.  Thus only `Q-1` survives.

Hence

\[
\boxed{
q_*=\begin{cases}
Q+2,&Q\text{ odd},\\
Q-1,&Q\text{ even}.
\end{cases}}
\]

The side is upper when `Q` is odd and lower when `Q` is even.

Therefore one possible silent `p` branch has the normal form

\[
\boxed{
p\longmapsto q_*(k,p)\longmapsto
\{\text{accept as silent iff }q_*\text{ prime and }\chi_{q_*}=0\}.}
\]

The ambiguity is a **binary gate**, not a residual cofactor interval.

## 4. BRC interpretation

The polarity-only no-resurrection failure is now sharply typed:

\[
\text{prime and silent composite share empty proper-divisor polarity}
\]

but

\[
\boxed{
\text{silent composite ambiguity}
=
\text{sparse partial matching of deterministic one-candidate p branches}.
}
\]

Thus the information debt left by dropping all zero-polarity divisor detail is not an arbitrary factor tree.  For `k>=10` it is at most one bit of unresolved acceptance per high least-prime branch.

This suggests the next research discriminator:

> can one add one independent multiplicative/signed observable that rejects every edge of this silent matching, while preserving the already-exact non-silent BRC structure?

Quadratic characters at anchor moduli are one candidate, but they must be audited against the possibility that they merely restate CRT data.  Any successful refinement must actually distinguish the deterministic `p -> q_*` silent edges from prime empty-signature states.

## 5. Replay surface

- `src/enterprise_math/prime_brc_silent_matching.py`
- `tests/test_prime_brc_silent_matching.py`

No claim of Legendre, Oppermann, or a new prime-distribution theorem is made.
