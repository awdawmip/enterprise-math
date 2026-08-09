# Legendre Pressure Test — Supplement 16

Status: `ACTIVE RESEARCH NOTE`  
Scope: stable-range disjointness of lower-band quotient-root channels  
Depends on: P017 L051 and canonical P018-T110–T113  
Discipline: this note does **not** prove Legendre's conjecture. It sharpens L051 by elementary integer inequalities. No asymptotic prime-distribution theorem is used.

## 1. L051 is uniform but not stable-range sharp

For a lower-band prime `p^2<2k`, write

\[
j_p=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right),
\qquad C_p(k)=\{j_p,j_p+1\}.
\]

L051 proves that every target root belongs to at most two candidate pairs. Finite pressure tests show the double overlaps are only a small-root phenomenon. The last one occurs at

\[
k=14,\qquad p=2,\ q=3,
\]

where

\[
C_2(14)=\{9,10\},\qquad C_3(14)=\{8,9\}.
\]

From `k=15` onward the candidate pairs are pairwise disjoint. The next theorem proves this exactly.

## 2. L052 — Stable lower-band root channels are disjoint

Status: `PROVED`.

For every `k>=15` and every pair of distinct lower-band primes `p<q`,

\[
\boxed{j_p\ge j_q+2.}
\]

Therefore

\[
\boxed{C_p(k)\cap C_q(k)=\varnothing.}
\]

Equivalently, every descended root index receives at most one lower-band least-prime shell channel. The threshold is sharp because of the `k=14` example.

## 3. Setup

Fix `p<q` and put `u=j_q`. By definition,

\[
qu^2\le k^2.
\]

It is enough to prove

\[
p(u+2)^2\le k^2,
\]

because then `(u+2)^2<=floor(k^2/p)` and `j_p>=u+2=j_q+2`.

## 4. Uniform case q>=13

The lower-band condition `q^2<2k` gives `q^4<4k^2`.

For `q>=13`,

\[
q^3>4(2q-3)^2.
\]

Writing `q=13+h`, `h>=0`,

\[
q^3-4(2q-3)^2=h^3+23h^2+139h+81>0.
\]

Hence

\[
q(2q-3)^2<k^2,
\]

so `u=j_q>=2q-3`. Since `p<q` are primes and `q` is odd, `p<=q-2`, hence `u>=2p+1`. Also `q-p>=2`. Therefore

\[
\begin{aligned}
qu^2-p(u+2)^2
&=(q-p)u^2-4pu-4p\\
&\ge2u^2-4pu-4p\\
&=2(u^2-2pu-2p)>0,
\end{aligned}
\]

because `u>=2p+1`. Thus

\[
p(u+2)^2<qu^2\le k^2.
\]

## 5. Small cases

Only `q=3,5,7,11` remain.

### q=11

Lower band forces `k>=61`; since `11*18^2<61^2`, `u>=18`. The worst `p=7` gives

\[
11u^2-7(u+2)^2=4u^2-28u-28>0.
\]

### q=7

Here `k>=25`, and `7*9^2<25^2`, so `u>=9`. The worst `p=5` is immediate for `u>=11`; for `u=9`, `5*11^2=605<625<=k^2`; for `u=10`, the definition of `u` forces `k>=27`, and `5*12^2=720<729<=k^2`.

### q=5

The theorem assumes `k>=15`; `5*6^2<15^2`, so `u>=6`. The worst `p=3` is immediate for `u>=7`; when `u=6`, `3*8^2=192<225<=k^2`.

### q=3

Then `p=2`. For `k>=15`, `3*8^2<15^2`, so `u>=8`. If `u>=9`, `3u^2-2(u+2)^2=u^2-8u-8>0`. If `u=8`, then `k^2<3*9^2=243`; with `k>=15` this forces `k=15`, and `2*10^2<225=k^2`.

Thus L052 holds in all cases. ∎

## 6. Sharpness

At `k=14`,

\[
j_2=R_2(98)=9,\qquad j_3=R_2(65)=8,
\]

so root `9` belongs to both candidate pairs. Hence the uniform threshold cannot be reduced below `15`.

## 7. Structural consequence

L051 gave constant cross-shell multiplicity. L052 removes even that factor in the stable range:

\[
\boxed{
\text{for }k\ge15,
\quad
\text{one descended root scale}
\longleftarrow
\text{at most one lower-band least-prime shell}.
}
\]

The root coordinate can therefore act as a nonoverlapping shell label before T113 even selects the actual branch.

## 8. Exact windows still matter

Each least prime has the exact open cofactor window

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

L052 eliminates cross-shell root multiplicity, but it does **not** justify replacing these exact subwindows by whole target square basins. That replacement remains too coarse.

## 9. Relation to T113 and mirror gating

T113 gives the statewise switch inside the unique L052 channel:

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
=j_p+\mathbf1[s\ge\tau_p].
\]

For mirror states, `s=k\pm r`; the branch selector becomes a radius half-interval and can be intersected with the existing mirror CRT progression without competing lower-band shell channels at the same root scale.

## 10. Executable validation

`lower_band_root_disjoint_bound(k)` checks L052. Regression tests cover every `15<=k<1000`, selected large roots through `k=200000`, pairwise endpoint separation, and the sharp `k=14,p=2,q=3` witness.

Finite tests audit implementation only; the proof is the integer argument above.

## 11. Next target

For `k>=15`, lower-band cross-shell root collisions are gone. The next question is whether the exact `p`-rough subwindow inside each unique descended root channel has a recursive composite capacity genuinely smaller than ordinary Buchstab bookkeeping.

The hardest surviving branch is expected to be singleton small-prime support with one large prime tail; that parity-sensitive hard core should be isolated explicitly rather than hidden inside a general recursion.
