# P017 — P2 Current-State Synchronization

Status: `OWNER CHECKPOINT / PROVED_WIP + SOURCE-FORMULA CORRECTION + ROOT-EDGE CANDIDATE + RESIDUAL-ENERGY FIXED-POWER COMPRESSION + EXTERNAL-COMPUTATION CONDITIONAL FINITE SPLICE / NOT CANONICAL / NO ALL-K P2 CLAIM`

Originally captured: `2026-08-25T21:34:00+08:00`

Last source-audit/root-edge update: `2026-08-26`

Last residual-energy update: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Authoritative correction note:

`docs/P017_P2_W1_SOURCE_FORMULA_AUDIT_20260826.md`

Preferred current parameter candidate:

`docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`

Residual-energy note:

`docs/P017_P2_RESIDUAL_ENERGY_COMPRESSION_20260826.md`

Exact rational / integer verifiers:

- `experiments/p017_p2_w1_source_formula_audit_20260826.py`;
- `experiments/p017_p2_a6_five_ninth_root_edge_certificate_20260826.py`;
- `experiments/p017_p2_residual_energy_compression_20260826.py`.

## Frozen mathematical state

1. The exact root-normalized detector

   \[
   \omega_K(n)=1-\sum_{p<K+1,\,p\mid n}\nu_p(n)\left(1-\frac{\log p}{\log(K+1)}\right)
   \]

   satisfies

   \[
   \omega_K(n)>0\iff\Omega(n)\le2
   \]

   for every state in the consecutive-square basin.

2. For the P017 binary carry

   \[
   O_m(K)=H_m(K)-H_{2m}(K),
   \]

   the exact bridge

   \[
   O_m(K)-\frac Km=r_K(m)-r_K(2m)
   \]

   reduces the prime-lift carry remainder to the standard Chen short-interval floor remainder.

3. Above the root, odd `O_m` is a Boolean incidence in pairwise-disjoint reciprocal complement windows. Distinct-prime prime-lift collisions factor through one shared small-prime core and one Boolean packet hit. Exact-Mobius top-third and `t=1` collision sectors collapse further; arbitrary Rosser/well-factorable coefficients remain an analytic interface.

4. The additive `O(sqrt(K))` super-root halo has coefficient-uniform bounded L1/L2 discrepancy by the quadratic-excess layer law.

5. On the full live five-ninth super-root strip, the parity-projected centered remainder now has the coefficient-free quadratic-energy compression

   \[
   E_{\rm sharp}(K,D)
   =
   \sum_{\substack{K<m\le D\\m\text{ odd}}}
   \left|O_m(K)-\frac Km\right|^2
   \le
   \frac DK+\frac K2\log\frac DK+K+2.
   \]

   At

   \[
   D=K^{10/9}
   \]

   this gives

   \[
   \boxed{E_{\rm sharp}=K^{1+o(1)}}
   \]

   against the generic level-size envelope `K^(10/9)`, i.e. a definite raw energy saving

   \[
   \boxed{K^{-1/9+o(1)}=X^{-1/18+o(1)}.}
   \]

   The same exponent survives any fixed-height nonnegative smooth parity projection supported in a subinterval of length at most `K`, including the existing fixed-order B-spline baseline. This does **not** yet authorize adding `1/36` to the Lemma-4 amplitude exponent.

6. In the current a6 terminal-prime band

   \[
   p\ge K^{22/27},
   \]

   every distinct-prime collision has

   \[
   P=p_1p_2>K,
   \]

   so the generic collision branch `P<=K` disappears. The surviving small-core packet satisfies

   \[
   \boxed{Q<z^2+1,\qquad z=K^{5/27},}
   \]

   and its shared collision depth satisfies `t^2<Q`. Thus the whole distinct-prime terminal collision carrier is confined to the same `z^2` scale that caps the legal Selberg auxiliary level.

7. The finite side remains conditionally spliced, under the declared conservative public exhaustive-gap premise, through

   \[
   K\le116{,}009{,}280{,}740{,}973{,}308,
   \]

   corresponding to

   \[
   X=K^2\approx1.3458153218\times10^{34}.
   \]

## 2026-08-26 source-formula correction

A direct audit of the unsimplified Iwaniec–Laborde p. 53 `W_1` lower bound found two normalization/transcription errors in the 2026-08-25 `a=4` effectivity packages:

1. after normalizing `F((1-t)/t)=2e^gamma*t/(1-t)`, the source `dt/t` cancels the `t`; the earlier `J_3` formulas retained an extra `1/t`;
2. the source fourth negative integral has a literal leading factor `2`, omitted in the earlier packages.

Consequences:

### Four-sevenths remains valid but with a smaller reserve

For

\[
\theta=\frac{4999}{10000},\qquad D=X^{4/7},\qquad a=4,\quad b=\frac52,\quad c=\frac72,
\]

the corrected source-normalized coefficient satisfies

\[
\boxed{C_1^{(4/7)}>\frac{533}{5000}=0.1066.}
\]

With the unchanged Lemma-6 coefficient

\[
C_2^{(4/7)}=\frac{128}{174790063},
\]

the corrected certified net reserve is

\[
\boxed{
C_1^{(4/7)}-C_2^{(4/7)}
>
\frac{93162463579}{873950315000}
\approx0.1065992677.
}
\]

The former `>0.145713553` reserve is superseded.

### The existing five-ninth `a=4` specialization is not positive

For

\[
D=X^{5/9},\qquad a=4,\quad b=\frac{13}{5},\quad c=\frac{18}{5},
\]

the corrected verifier proves

\[
\boxed{C_1^{(5/9)}<-\frac{3}{2500}.}
\]

Therefore the old `a=4` five-ninth package must not be used as a positive main-term certificate. This invalidates that parameter specialization, not the exponent `d=5/9` under all admissible weights.

Any older owner artifact that independently integrated the same p. 53 unsimplified formula must be re-audited before its numerical positivity margin is consumed downstream.

## 2026-08-26 preferred root-edge candidate

The later `a=6`, `b>=3` Laborde-simplified presentation is not affected by the `a=4` J3/J4 transcription error. Re-optimizing it for exact square-root alignment gives

\[
\boxed{
\theta=\frac{4999}{10000},\quad
D=X^{5/9},\quad
a=6,\quad
b=\frac{22}{5},\quad
c=\frac{27}{5}.
}
\]

Then

\[
D^{c/a}=X^{1/2}
\]

exactly, while

\[
z=X^{5/54},\qquad
D^{b/a}=X^{11/27}<y.
\]

Using the 1981 printed optimum decimals as prefix intervals and exact rational logarithm enclosures, the new verifier proves the source-decimal main coefficient bound

\[
\boxed{G_*>\frac{287}{2500}=0.1148.}
\]

This is not yet a direct independent certificate of the underlying Laborde constants; retrieving those constants from their defining source remains an open provenance gate.

For effectivity, with

\[
\varepsilon=\frac1{200},\qquad
M=X^{31/72},\qquad N=X^{1/8},
\]

the original trivial `(1/2,1/2)` route already satisfies the Lemma-4 conditions with exact margins

\[
A2:\ \frac{3541}{90000},
\qquad
A3:\ \frac{23}{72},
\qquad
A4:\ \frac{1771}{36000}.
\]

The structural one-block savings are

\[
\delta_{\rm diag}=\frac{4891}{180000}\approx0.0271722,
\]

\[
\boxed{
\delta_{\rm off}=\frac{1951}{72000}\approx0.0270972.
}
\]

Thus the refined `(1/14,11/14)` exponent pair is unnecessary here as well. This power saving is materially stronger than the corresponding four-sevenths trivial-pair saving `1073/56000 ~= 0.0191607`.

Because the `a=6` `G_*` and the corrected `a=4` coefficient arise through two different presentations of the source main term, their numerical reserves should be placed on one final-count normalization before claiming a strict main-term dominance. The bilinear exponent comparison is direct.

## 2026-08-26 residual-energy compression

The former hard frontier asked whether exact square geometry removes a definite power from the residual support/energy before generic Chen-Iwaniec constants are paid. At the raw quadratic-energy level the answer is now positive.

For the sharp parity-projected remainder,

\[
E_{\rm sharp}(K,\lfloor K^{10/9}\rfloor)
\le
K^{1/9}+\frac1{18}K\log K+K+2,
\]

so

\[
\boxed{
E_{\rm sharp}=K^{1+o(1)}
}
\]

instead of the generic level-size `K^(10/9)` envelope. The fixed energy gap is `1/9` in `K`, equivalently `1/18` in `X`.

The same exponent persists after a fixed-height nonnegative smoothing supported on length `<=K`: super-root odd multiples are spaced by `2m>2K`, so every modulus still has at most one odd-quotient hit. For the existing order-`p` compact B-spline, the elementary bound `||f||_infty<=p` is enough to retain `K^(1+o(1))` energy.

Separately, the a6 terminal lower-prime exponent `22/27` forces every distinct-prime collision into the `P>K` packet branch and hence into a small core `Q<z^2+1`. This is exactly aligned with the Selberg auxiliary cap `z^2`.

These are square-specific structural reductions. They do not by themselves prove signed cancellation for the factorable bilinear form.

## Effectivity pressure test

Mechanical explicit B-spline/Poisson constant tracking of the generic 1981 proof at the current finite splice is still too expensive: even idealized single-block estimates remain order one before the `O((log MN)^2)` bilinear-form multiplicity is charged.

Therefore the priority remains to exploit the new square-specific compression before paying generic Fourier constants. The preferred path is now:

1. use the `a=6,d=5/9` root-edge package as the finite-oriented baseline;
2. keep the proved `K^{-1/9+o(1)}` raw residual-energy ratio as an independent invariant;
3. isolate a valid Cauchy/duality insertion point for that parity-projected energy, without confusing physical same-radius collisions with the Fourier off-diagonal in Lemma 4;
4. exploit the exact a6 confinement `Q<z^2+1` to remove or finitely control the distinct-prime collision carrier;
5. use adaptive interval-length anchors to strip chosen small-prime factors with zero floor error;
6. invoke the generic trivial-pair bilinear estimate only on the signed residual sector that survives these reductions;
7. recover the Laborde constants directly and unify all main-term normalizations.

## Current hard frontier

The support/energy question itself is no longer open. The live problem is now:

> prove a carry-energy insertion theorem for the factorable signed prime-lift remainder, or identify an exact obstruction showing that the `K^{-1/9}` physical residual-energy saving cannot survive the Lemma-4/Fourier interface; in parallel consume the a6 fact that every distinct-prime terminal collision has small core `Q<z^2+1`.

No all-k consecutive-square P2 theorem is claimed here.
