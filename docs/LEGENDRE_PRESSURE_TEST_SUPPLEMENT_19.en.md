# Legendre Pressure Test — Supplement 19

Status: `PROVED RESEARCH NOTE`  
Scope: lower-band exact-window root separation and its realized-shell corollary  
Depends on: P017 L051–L054, P007 quotient-window transport Supplement 01, P023 image-separation Supplement 08, and P018 T113  
Discipline: finite integer inequalities only; no prime-distribution estimate and no claim of a Legendre proof.

## 1. Why L052 should be re-examined

For a lower-band prime `p`, L052 enlarges the possible root output to a two-point candidate set. It proves uniform cross-shell separation only from `k>=15`.

L054 gives more information: after stripping `p`, every possible cofactor lies in the exact raw interval

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right].
\]

The root image of this interval can be much smaller than L052's enlarged candidate pair. For example at `k=14`, the candidate sets for `p=2,3` both contain root 9, but

\[
R_2(W_2(14))=\{9,10\},
\qquad
R_2(W_3(14))=\{8\}.
\]

So the candidate collision is false already at the exact-window level.

## 2. Three different state layers

A semantic distinction is essential.

Define the **exact-window root image**

\[
\boxed{
G_p^{\rm win}(k)=\{R_2(q):q\in W_p(k)\}.
}
\]

A real least-prime shell is smaller. Let

\[
Q_p^{\rm sh}(k)
=
\{n/p:\ k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\}.
\]

Then

\[
Q_p^{\rm sh}(k)\subseteq W_p(k)
\]

because a realized shell cofactor must satisfy the interval constraint **and** the `p`-roughness/admissibility condition. Define its realized root image

\[
\boxed{
G_p^{\rm sh}(k)=\{R_2(q):q\in Q_p^{\rm sh}(k)\}.
}
\]

Therefore

\[
\boxed{
G_p^{\rm sh}(k)\subseteq G_p^{\rm win}(k).
}
\]

The correct hierarchy is thus

\[
\text{candidate root superset}
\supseteq
\text{exact-window root image}
\supseteq
\text{realized shell root image}.
\]

An exact interval is not automatically an actually realized shell.

## 3. L055 — Exact-window lower-band root images are disjoint from k=9 onward

Status: `PROVED`.

Let `k>=9` and let `p<r` be distinct lower-band primes:

\[
p^2<2k,
\qquad
r^2<2k.
\]

Then

\[
\boxed{
G_p^{\rm win}(k)\cap G_r^{\rm win}(k)=\varnothing.
}
\]

Since realized shell images are subsets of exact-window images, the immediate corollary is

\[
\boxed{
G_p^{\rm sh}(k)\cap G_r^{\rm sh}(k)=\varnothing.
}
\]

Thus the retained root coordinate recovers the lower-band least-prime shell label from `k>=9` onward.

## 4. Necessary conditions for an exact-window collision

Assume a common root `s` occurs in the two exact-window images. Then there are

\[
q_p\in W_p(k),
\qquad
q_r\in W_r(k)
\]

with

\[
R_2(q_p)=R_2(q_r)=s.
\]

Because

\[
s^2\le q\le s^2+2s,
\]

the interval endpoints give

\[
\boxed{k^2<p\,s(s+2),}
\tag{A}
\]

\[
\boxed{rs^2\le k^2+2k,}
\tag{B}
\]

\[
\boxed{k^2<r(s+1)^2.}
\tag{C}
\]

Subtracting (A) from (B) in the needed direction yields

\[
\boxed{(r-p)s^2<2ps+2k.}
\tag{D}
\]

These conditions apply to the stronger exact-window collision problem, so any contradiction here automatically excludes realized shell collisions too.

## 5. Every r>=5 is impossible

For `r>=5`, prime spacing gives

\[
r-p\ge2,
\qquad
p\le r-2.
\]

From (C) and

\[
4r\le(r+1)^2
\]

we obtain

\[
\boxed{2k<(r+1)(s+1).}
\tag{E}
\]

Combining (D) and (E),

\[
\boxed{2s^2<(3r-3)s+r+1.}
\tag{F}
\]

For `r>=11`, the lower-band condition and (C) imply

\[
r^3<4(s+1)^2.
\]

This forces

\[
2s\ge3r-1,
\]

which makes the left side of (F) at least the right side, a contradiction.

For `r=7`, (F) gives `s<=9`; then (A) with `p<=5` gives `k<=22`, while lower-band requires `k>=25`.

For `r=5`, (F) gives `s<=6`; then (A) with `p<=3` gives `k<=11`, while lower-band requires `k>=13`.

Hence

\[
\boxed{r\ge5\Longrightarrow\text{no exact-window lower-band root collision}.}
\]

## 6. The only remaining prime pair is (2,3)

For `(p,r)=(2,3)`, (A) and (B) become

\[
\boxed{k^2<2s(s+2),}
\tag{I}
\]

\[
\boxed{3s^2\le k^2+2k.}
\tag{J}
\]

A pure integer comparison excludes `s>=8`. Indeed, (I) gives

\[
7k<10(s+1),
\]

using `98<100`; combining this with (J) gives

\[
47s^2<340s+240,
\]

which fails at `s=8` and thereafter.

Thus `s<=7`, and (I) gives `k<=11`. Under the theorem hypothesis `k>=9`, only `k=9,10,11` remain; direct use of (I) and (J) excludes all three. Therefore L055 holds. ∎

## 7. Sharpness at the realized-shell level

The threshold `k>=9` is sharp even after the `p`-rough realizability filter.

At `k=8`, take

\[
n_2=66=2\cdot33,
\qquad
n_3=75=3\cdot25.
\]

Both lie in the square basin `(64,81)`, and

\[
\operatorname{spf}(66)=2,
\qquad
\operatorname{spf}(75)=3.
\]

Yet

\[
R_2(33)=R_2(25)=5.
\]

Hence

\[
\boxed{5\in G_2^{\rm sh}(8)\cap G_3^{\rm sh}(8).}
\]

So no uniform realized-shell separation theorem can start below 9.

## 8. Exact-window collision need not be realizable

The distinction between the middle and bottom layers is already visible at `k=6`.

The exact windows are

\[
W_2(6)=[19,24],
\qquad
W_3(6)=[13,16].
\]

Thus both exact-window root images contain root 4. But the only `p=3` cofactor in this window with root 4 is `q=16`, corresponding to

\[
3q=48,
\]

and `48` has least prime factor 2. Therefore root 4 is **not** realized by the `p=3` shell.

So `k=6` is an exact-window collision but not a realized-shell collision.

This is the next precision lesson after L052:

\[
\boxed{
\text{exact interval membership}
\neq
\text{admissible/realized state membership}.
}
\]

## 9. Finite regression profiles

The executable checks now keep the two collision profiles separate.

For the exact-window images below 9, the collisions occur at

\[
k=5,6,8.
\]

After the least-prime / `p`-rough realizability filter, the bounded profile becomes

\[
k=5,8.
\]

These finite profiles are regression evidence here. Supplement 20 later upgrades the full-family classification to an ordinary proof.

## 10. Relation to L052

L052 remains a valid stronger-information-poorer statement: it uses the enlarged two-root candidate set and gets uniform separation at 15.

L055 uses the exact quotient windows and proves the stronger arithmetic statement

\[
\text{exact-window separation from }k=9.
\]

The actual shell is a subset, so it inherits the same threshold, while the `k=8` realized witness proves sharpness.

The hierarchy is

\[
\boxed{
\text{candidate superset}
\to
\text{exact-window image}
\to
\text{realized-shell image}.
}
\]

Each arrow adds valid structure and can delete false collisions.

## 11. A2 interpretation

P023-S8 should be applied to the **reachable/admissible** shell state when that state is known. Pairwise disjointness of realized shell images is exactly the zero-repair criterion for deleting the shell label.

For `k>=9`, the root coordinate is sufficient to recover lower-band shell identity. This does not recover the original cofactor or composite state, because the root map remains many-to-one within a shell.

Thus

\[
\boxed{
\text{shell identity retained}
\neq
\text{full state retained}.
}
\]

## 12. Executable specification

- `src/enterprise_math/p017_actual_root_separation.py`
- `tests/test_p017_actual_root_separation.py`
- `experiments/p017_actual_root_separation_probe.py`

The executable layer now exposes both exact-window root images and actually realized least-prime-shell root images. It pins the `k=6` semantic counterexample, the realized sharp witness at `k=8`, and large finite disjointness regressions from `k>=9`.

Historical novelty remains `NOVELTY_UNVERIFIED`. The important project result is the theorem-lifting discipline and the stronger P017 structure exposed by retaining the correct state layer.
