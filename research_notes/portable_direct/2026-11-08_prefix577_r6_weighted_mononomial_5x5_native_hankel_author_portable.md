# PREFIX-577 / BRC-X6 — exact 25-family monomial-weight first-gate observer ranks

**2026-11-08 / AUTHOR-PROVED / NATIVE EXACT INTEGER-MODULAR-CHECKED / UNREVIEWED / NOT_ADMITTED.**

**Frozen science input** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Starting at original native port 9 of the 96-port, 576-action (six separately labeled actions per port) frozen X6 system, sample each action uniformly until the **first gated action**. Keep all native six axes, path labels, gate events and provenance in the underlying carrier. Observe the scalar `W=a U+b V` with U and V accumulated fifth/sixth-axis rewards, first-gate time T. For nonnegative integer a,b and an indeterminate L define `F_(a,b)(z,L)=E_9[z^T L^(aU+bV)]=F(z,L^a,L^b)`. The original model has nonnegative reward exponents.

## Exact theorem on all 25 weight pairs

For **all** `(a,b) in {0,1,2,3,4}^2`, the reduced denominator degree of `F_(a,b)` over Q(L), equivalently the minimal passive scalar sequence Hankel rank, is

```
d(a,b) = 10, if (a,b)=(0,0);
         24, if precisely one of a,b is zero;
         18, if a=b>0;
         28, if a,b>0 and a != b.
```

Rank matrix (row a, column b):

```
       b=0  1  2  3  4
 a=0   10 24 24 24 24
 a=1   24 18 28 28 28
 a=2   24 28 18 28 28
 a=3   24 28 28 18 28
 a=4   24 28 28 28 18
```

**Upper bounds:** Reuse the independently established exact integer polynomial identity `Q(t,x,y)S(t,x,y)=P(t,x,y)` for this passive gate return observer, with Q degree 28 and P degree <28. Direct exact symbolic gcd(P,Q) yields orders 24 at x=1 (or y=1), 18 along x=y and 10 at x=y=1. Replacing L with L^k for k>0 preserves these identities and upper bounds. Distinct positive exponents use the unmodified upper bound 28. Prior proof and coefficients: [exact generic 28](https://github.com/awdawmip/enterprise-math/blob/a3e9f095d92bd31d2ffcd6b3a40ccb733b137751/research_notes/portable_direct/2026-11-08_prefix577_r6_gate_joint_generic_degree28_exact_author_portable.md) and [exact eight specialization orders](https://github.com/awdawmip/enterprise-math/blob/9ac151648298f5d08b0ad1d2b2d28f4bb7de71cb/research_notes/portable_direct/2026-11-08_prefix577_r6_gate_observer_rank_strata_author_portable.md).

**Sharp lower bounds:** Independent original96 native tagged-action computation of each `s_n(L^a,L^b)` uses all 576 original actions, not a numerical or quotient approximation. At L=2, each expected d×d scalar Hankel matrix `H_d=(s_(i+j))_(0<=i,j<d)` has a nonzero exact determinant modulo the prime 1,000,000,007. This is a characteristic-zero rational-function nonvanishing certificate because a rank <d rational identity would force all such minors to vanish in the original integral series; no division by numerically vanishing factors was used.

Determinants modulo 1000000007, indexed rows a=0,..,4 and columns b=0,..,4:

```
a=0  530286724 205620315  87893233 180057407 212717606
a=1  205620315 648725615 112892214 698244405 137493982
a=2   87893233 112892214 758940315 325877832 705006459
a=3  180057407 698244405 325877832 173083423 923023742
a=4  212717606 137493982 705006459 923023742  14598793
```

Every entry is nonzero modulo the prime and provides the exact minimal d in its row/column.

## Exact BRC native information-loss witness despite rank equality

The full passive joint (U,V) series has scalar Hankel rank 28, and the scalar observer W=U+2V for (a,b)=(1,2) **also has rank 28**. Nevertheless, at **first-gate time T=8**, original 96-port 576-action integer path enumeration gives

```
#(T=8,U=0,V=1) = 320
#(T=8,U=2,V=0) = 1984
W=2 for both; total 2304 of 6^8=1679616 equally weighted native tagged action strings
P(T=8,W=2) = 2304/1679616 = 1/729.
```

The first-gate scalar observer merges these distinct reward outcomes. Consequently **equality of scalar recurrence order is not a certificate of lossless joint observation**, including subsequent operations that may inspect U,V, tag choice, branch identity, port history or individual native-axis reward. The 28-state minimal scalar realization is valid only for the declared passive readout and horizon.

## Reproduction/provenance, limits and next work

The self-contained local zipped author evidence `PREFIX577_R6_WEIGHTED_OBSERVER_5X5_AUTHOR_PORTABLE_20261108.zip` SHA-256 `8720ea909780e51abdf874565a1871b4839b057894f86911b14fd7cf62c13588` retains `verify_weighted_observer_5x5.py`, `WEIGHTED_OBSERVER_5x5_CERTIFICATE.json` (SHA256 `d80a4ab16c9f1475b02636fb362ee67a1a5042830dbd747b2604d00b2caa833c`), full theorem and the frozen kernel. Reexecution verified all 25 determinants and the native 320/1984 collision. **ZIP is a local author artifact; this GitHub note is the published proof, not a claim that local ZIP has been uploaded.**

Retained and not recredited: original 96-port frozen kernel, native 37-state passive quotient, generic degree28, source-specific 24/18/10 specialization lemmas, and previously recorded universal-start rank29/balance-hyperplane author proofs. This work is independent new author-side, finite-domain 25-case classification; the possible all-positive-slope extension remains open. **Next scientific unit:** investigate all nonnegative integer slopes and classify exceptions using exact Q/P factorization, retaining the original joint BRC branch provenance and native observer scope.

The D25 native task remains separately at `HANDOFF_READY / NEEDS_DISPATCH` at the last successful exact Source read, with missing original-class H0/B0 divided-power module, `[X]U mod p^2`, Frobenius direction, normalization eta and native CM experiment NOT_RUN. No current Source task CLAIM/open/checkpoint/Result/review accepted by this author turn. Earlier native Source issued historical researcher identity `EM-ENTERPRISE-301CA6` / activity `RA-E889C3B8461F5844B53CAF15`; private session capability is unavailable for this run, and a previous read-only continuation request `h40-r11-d25-continuation-20261108t1512-v1` remains QUEUED for its original receipt. UR V2 genuine original four-file bundle remains absent in checked local workspace, expected exactly 94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; do not substitute.
