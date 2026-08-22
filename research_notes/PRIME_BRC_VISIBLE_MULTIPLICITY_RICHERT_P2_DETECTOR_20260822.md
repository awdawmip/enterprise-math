# Prime-BRC Visible-Multiplicity Richert P2 Detector

Status: `OWNER_LOCAL_L3_RESEARCH / PROVED_CONDITIONAL_ON_DECLARED_RICHERT_INPUT`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Date: `2026-08-22`
Branch: `research/prime-brc-stage-a`

## 1. Scope

This note isolates a minimal Prime-BRC carrier that can be coupled to the Richert weight used in the current consecutive-square P3 route. It does **not** prove Legendre's conjecture and does not claim a new asymptotic P2 theorem. Its purpose is to classify a square-basin-specific P3-to-P2 detector and the exact new switched incidence term it creates.

Let the square basin be

\[
I_k=\{n:k^2<n<(k+1)^2\}.
\]

Use a roughness threshold `z>2`, the Richert upper cutoff `y`, and the standard square-removal condition that excludes `p^2|n` for primes `z<=p<y` in the retained weighted set. Let

\[
\lambda=0.83
\]

be the declared Richert base credit from the current P3 parameter choice.

## 2. Visible multiplicity carrier

Define

\[
V_k(n)=\sum_{\substack{p\le k\\p\text{ prime}}}v_p(n).
\]

Thus `V_k(n)` counts all prime-factor occurrences at scale `<=k`, with multiplicity.

For theorem semantics only the capped four-state carrier is needed:

\[
\widehat V_k(n)=\min(V_k(n),3)\in\{0,1,2,3\}.
\]

Interpretation in the square basin:

- prime: `V=0`;
- semiprime `n=pq` with `p<=k<q`: `V=1`;
- large-tail squarefree triprime `n=pqr` with `p,q<=k<r`: `V=2`;
- fully `k`-smooth triprime, including repeated-prime types that survive the square-removal gate: `V=3`.

At most one prime-factor occurrence of any basin state can exceed `k`: two factors `>k` would have product at least `(k+1)^2`, outside the open basin.

## 3. Prime-BRC weight

Define

\[
\boxed{
 w_\star(n)=w_R(n)-\frac{\lambda}{2}\bigl(V_k(n)-1\bigr)
}
\]

or, for purely finite-state classification, replace `V_k` by `min(V_k,3)` once the ordinary Richert nonpositivity for `Omega>=4` is invoked.

The branch cost is therefore

\[
\boxed{c_\star=\lambda/2=0.415.}
\]

It has the exact low-depth behavior:

- prime: receives bonus `+lambda/2`;
- semiprime: unchanged;
- visible multiplicity 2: pays `lambda/2`;
- visible multiplicity at least 3: pays at least `lambda`.

## 4. P2 detector theorem

Assume the declared Richert facts used by the current P3 proof:

1. `w_R(n)<=lambda` for every retained rough state;
2. states with `Omega(n)>=4` are already nonpositive under the P3 Richert criterion;
3. for a squarefree large-tail triprime
   \[
   n=pqr,\qquad p\le q\le r,\qquad pq<r,
   \]
   one has the sharper bound
   \[
   w_R(n)<\lambda/2.
   \]

Then

\[
\boxed{w_\star(n)>0\Longrightarrow\Omega(n)\le2.}
\]

### Proof

If `Omega(n)>=4`, at most one factor occurrence can exceed `k`, hence `V_k(n)>=3`. The new penalty is nonnegative (indeed at least `lambda`) and cannot restore positivity to a state already nonpositive under the Richert P3 criterion.

Now let `Omega(n)=3`.

If `V_k(n)>=3`, the Prime-BRC penalty is at least `lambda`, while `w_R(n)<=lambda`; hence `w_star(n)<=0`.

The only remaining case is `V_k(n)=2`, so exactly one factor occurrence exceeds `k`. In the retained square-removal universe this is the squarefree large-tail triprime case. The sharper A-type bound gives

\[
w_R(n)<\lambda/2,
\]

while the new penalty equals exactly `lambda/2`. Thus again `w_star(n)<0`.

Therefore positive modified weight is possible only when `Omega(n)<=2`. ∎

## 5. Why the large-tail triprime bound is lambda/2

Write the Richert deduction for a visible prime `p` as

\[
\delta(p)=\max\left(0,1-\frac{\log p}{\log y}\right).
\]

For a squarefree A-type triprime `p q r` with `pq<r`, one has `pq<sqrt(n)` and hence, at the declared parameter `k_2=3.17`,

\[
\delta(p)+\delta(q)>2-\frac{k_2}{2}=0.415=\lambda/2.
\]

Therefore

\[
w_R(n)=\lambda-\delta(p)-\delta(q)<\lambda/2.
\]

## 6. Minimax optimality of the uniform branch cost

Consider the restricted class of modifications

\[
w_c(n)=w_R(n)-c\,(V_k(n)-1)
\]

with one uniform nonnegative cost `c` per visible occurrence beyond the first.

A fully smooth squarefree triprime may have all three factors at or above `y`, in which case `w_R=lambda` and `V_k-1=2`. Any uniform detector that forces all such triprimes nonpositive must satisfy

\[
\lambda-2c\le0,
\]

hence

\[
\boxed{c\ge\lambda/2.}
\]

Section 4 shows `c=lambda/2` suffices. Therefore

\[
\boxed{c_\star=\lambda/2}
\]

is minimax-optimal inside this uniform linear branch-cost class.

## 7. Aggregate linearization

The uncapped multiplicity has the exact incidence expansion

\[
V_k(n)=
\sum_{\substack{p\le k\\p\text{ prime}}}
\sum_{j\ge1}\mathbf 1_{p^j\mid n}.
\]

Hence the total new Prime-BRC penalty is linear in ordinary divisibility incidences. The genuinely new first-power range relative to the original Richert weight is the high-prime interval `y<=p<=k`.

For the square-derived cofactor windows, and for every odd sieve modulus `d`, floor-division associativity gives the exact switched identity

\[
\boxed{
A_d^{\rm hi}(k)
=
\sum_{y\le p\le k}O_{pd}(k),
}
\]

where

\[
O_m(k)=H_m(k)-H_{2m}(k)
\]

is the P017 odd/binary-carry hit count.

Thus the extra P2 detector term does not require a new opaque sieve sequence: its divisibility data is an explicit two-parameter sum of the existing square-basin binary-carry family.

## 8. Boundary

This detector targets `P3 -> P2`. It does not solve `P2 -> P1`. The latter remains the genuine parity hard core:

\[
n=pq,\qquad p\le k<q,
\]

where `V_k(n)=1`, so the modified weight deliberately leaves the semiprime untouched.

That is a feature, not a defect: the four-state visible-multiplicity carrier isolates exactly the layer the weighted switching can remove without pretending to solve the final prime/semiprime distinction.
