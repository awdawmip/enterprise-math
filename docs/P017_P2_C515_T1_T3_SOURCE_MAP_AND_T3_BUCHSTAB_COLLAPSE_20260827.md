# P017 — c=103/20 T1–T3 Source Map and Exact T3 Buchstab-Shell Collapse

Status: `PROVED_WIP SOURCE-MAPPED + EXACT T3 COLLAPSE / T1-T2 REMAIN / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Primary source: Iwaniec–Laborde, *P2 in short intervals* (1981), equation (3), Lemma 2, and the p.53 W1 lower bound.

Purpose: pin the exact T1–T3 source ranges for the finite-oriented full-basin packet

\[
a=6,\qquad b=\frac{93}{20},\qquad c=\frac{103}{20},\qquad d=\frac59,
\]

and remove T3 from the upper-sieve/bilinear hard frontier by an exact least-prime/Buchstab-shell identity.

---

## 1. Parameters and notation

Put

\[
\Delta=2c-b-1=\frac{93}{20},
\qquad
U=\frac{b+1}{2a}=\frac{113}{240}.
\]

At the Tier-A full-basin scale let

\[
W=K_0+1,
\qquad
D=W^{10/9},
\qquad
z=D^{1/6}=W^{5/27}.
\]

The source weight is

\[
W(\mathcal A)=S(\mathcal A,z)-\frac{1}{\Delta}(T_1+T_2+T_3+T_4).
\]

The already-frozen T4 term is separate. This note concerns T1–T3.

---

## 2. Exact source map for T1–T3

Equation (3) gives

\[
\boxed{
T_1
=(c-b)
\sum_{D^{1/6}\le p<D^{b/6}}
S(\mathcal A_p,z).
}
\]

For the c=103/20 packet,

\[
c-b=\frac12,
\qquad
\frac b6=\frac{31}{40},
\]

so

\[
\boxed{
T_1
=\frac12
\sum_{D^{1/6}\le p<D^{31/40}}
S(\mathcal A_p,z).
}
\tag{T1}
\]

In the W-variable,

\[
D^{1/6}=W^{5/27},
\qquad
D^{31/40}=W^{31/36}.
\]

The second source term is

\[
\boxed{
T_2
=6\int_{1/6}^{113/240}
\left(
\sum_{D^s\le p<D^{113/240-s}}
S(\mathcal A_p,D^s)
\right)ds.
}
\tag{T2}
\]

The inner prime interval is nonempty only for

\[
s<\frac{113}{480}.
\]

Therefore all T2 external primes lie in

\[
D^{1/6}\le p<D^{73/240},
\]

or, in W-coordinates,

\[
\boxed{
W^{5/27}\le p<W^{73/216}.
}
\tag{T2-range}
\]

The third source term is

\[
\boxed{
T_3
=\sum_{D^{1/6}\le p<D^{113/240}}
\left(
\frac{113}{20}-12\frac{\log p}{\log D}
\right)
S(\mathcal A_p,p).
}
\tag{T3}
\]

The terminal T3 endpoint is

\[
D^{113/240}=W^{113/216}.
\]

These are direct transcriptions/specializations of source equation (3); they do not rely on reconstructing the p.53 integrals backwards.

---

## 3. T3 is a least-prime shell, not an independent sieve remainder

Assume the sequence weights are nonnegative. Let

\[
R(t)=S(\mathcal A,t).
\]

For a prime `p`, the quantity

\[
S(\mathcal A_p,p)
\]

counts exactly those states whose least prime factor is `p` (with the usual sieve convention that `P(p)` contains primes strictly below `p`). Thus the T3 shells are pairwise disjoint.

Let

\[
z\le p_1<p_2<\cdots<p_m<P,
\qquad
P=D^{113/240},
\]

be the primes in the T3 range, and put

\[
R_i=R(p_i),
\qquad
R_{m+1}=R(P).
\]

Then exactly

\[
S(\mathcal A_{p_i},p_i)=R_i-R_{i+1}.
\tag{B1}
\]

Define

\[
\psi(t)=\frac{113}{20}-12\frac{\log t}{\log D}.
\]

Since

\[
P=D^{113/240},
\]

we have

\[
\psi(P)=0.
\]

Discrete Abel summation applied to (B1) gives

\[
\boxed{
\begin{aligned}
R(z)-\frac{T_3}{\Delta}
={}&
\left(1-\frac{\psi(p_1)}{\Delta}\right)R_1\\
&+\sum_{i=2}^{m}
\frac{\psi(p_{i-1})-\psi(p_i)}{\Delta}R_i
+\frac{\psi(p_m)}{\Delta}R_{m+1}.
\end{aligned}
}
\tag{B2}
\]

Every coefficient on the right is nonnegative, because `psi` is decreasing.

Also `p_1>=z`, so

\[
\psi(p_1)\le\psi(z)
=\frac{113}{20}-2
=\frac{73}{20}.
\]

As

\[
\Delta=\frac{93}{20},
\]

we get

\[
1-\frac{\psi(p_1)}{\Delta}
\ge
1-\frac{73}{93}
=\frac{20}{93}
=\frac1\Delta.
\]

Therefore

\[
\boxed{
S(\mathcal A,z)-\frac{T_3}{\Delta}
\ge
\frac1\Delta S(\mathcal A,z).
}
\tag{B3}
\]

This is exact and uses no upper linear sieve, no factorable decomposition, no Fourier expansion, and no exponential-sum estimate.

---

## 4. What is gained and what is not

The previous bookkeeping treated T3 as another upper-sieve prime-lift family. That is unnecessary.

T3 should now be removed from the independent analytic hard frontier. If only the coarse bound (B3) is used, the already-proved base lower-Rosser carry cost

\[
\frac{|R_0^-|}{L}<\frac{29}{20000}
\]

is multiplied by `1/Delta=20/93`, giving the effective coarse base-carry cost

\[
\boxed{
\frac{20}{93}\frac{29}{20000}
=\frac{29}{93000}
<0.000312.
}
\tag{B4}
\]

However, the source-main coefficient `0.00449 L` for c=103/20 already includes the *full* refined T3 main contribution. Therefore one may **not** simply replace the old base error by (B4) and add the numerical difference to the previous `0.00179 L` source-scale budget.

To preserve the source-main efficiency, future work should consume the entire positive Abel expansion (B2), lower-bounding the nested rough counts `R_i`, instead of retaining only its first term.

Thus the current split is:

- T3 upper-sieve/bilinear remainder: **removed**;
- T3 finite main recovery: transferred to a positive nested rough-count problem;
- T1 and T2: still live.

---

## 5. T1 and T2 route diagnosis

A T4-style absolute finite-state treatment does not extend over all T1–T2.

For T1, at the low-prime endpoint `p=z`, the inner upper-sieve parameter is

\[
\frac{\log(D/p)}{\log z}=5,
\]

so the Rosser support is macroscopically large. At the high endpoint `p=D^{31/40}`, the inner level is only

\[
D/p=D^{9/40}=W^{1/4},
\]

which is exactly the small finite scale already seen in T4. Hence T1 naturally splits into a low-p analytic sector and a high-p finite-support tail.

For T2, the external-prime range is only

\[
W^{5/27}\le p<W^{73/216},
\]

but the moving cutoff `D^s` reaches well above `z`; its low-s sector still has a large Rosser support. T2 therefore also needs either a shell/Buchstab recombination or a support-sensitive analytic treatment; naive absolute support is not competitive.

The next valid targets are:

1. retain the full positive T3 Abel expansion while finite-normalizing its nested rough counts;
2. split T1 at a prime threshold where the upper Rosser support becomes a finite activation-threshold family;
3. test whether T2 can be rewritten jointly with T1 through a second Buchstab/ordered-two-prime shell before invoking any generic bilinear theorem.

No finite P2 theorem or all-K claim is made here.
