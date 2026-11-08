# PREFIX-577 / BRC-X6 — complete integer monomial-slope rank classification

**Date:** 2026-11-08 UTC. **Frozen scientific pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
**Status:** `AUTHOR_PROVED / EXACT_INTEGER_SYMBOLIC_AND_EXHAUSTIVE_MODULAR_CHECKED / UNREVIEWED / NOT_ADMITTED`. This is author portable mathematical evidence, not an admitted canonical Source Task Result, execution checkpoint or independent Driver review.

## Theorem — all nonnegative integer weights, not merely a finite grid

Use the **unchanged original 96-port native BRC-X6 carrier**, its six separately tagged actions at each port (576 actions), all six native spatial rewards, separately typed time, gate events and their original provenance. From native port 9 draw each action uniformly until the first gated action, with time `T` and cumulative fifth/sixth rewards `U,V`. For nonnegative integers `a,b`, declare the passive scalar observation

`F_(a,b)(z,L)=E_9[z^T L^(aU+bV)]=F(z,L^a,L^b)`.

The reduced denominator degree in `z` over `Q(L)` (equivalently the minimal scalar Hankel rank) is **exactly**

```
d(a,b) = 10   if a=b=0
         24   if exactly one of a,b is zero
         18   if a=b>0
         28   if a,b>0 and a != b
```

The 10/24/18 cases are an exact reuse of the prior [symbolic-gcd and native-Hankel rank-strata proof](https://github.com/awdawmip/enterprise-math/blob/9ac151648298f5d08b0ad1d2b2d28f4bb7de71cb/research_notes/portable_direct/2026-11-08_prefix577_r6_gate_observer_rank_strata_author_portable.md), blob `5dee1c7d5ede698d0f958b0c861333f5f1eac2e4`. The **new scientific unit** is the proof for **every** unequal positive `(a,b)`, extending the previous exactly checked 25-family `0<=a,b<=4` result to the infinite domain.

## Proof of the infinite positive off-diagonal case

Let `C(x,y)` be the native 96-state **nongated** action-count matrix weighted by `x^R5 y^R6`, and `g` the native gate-edge count vector. Write `s_n(x,y)=e_9^T C(x,y)^n g`. The inherited [integer-polynomial degree-28 certificate](https://github.com/awdawmip/enterprise-math/blob/a3e9f095d92bd31d2ffcd6b3a40ccb733b137751/research_notes/portable_direct/2026-11-08_prefix577_r6_gate_joint_generic_degree28_exact_author_portable.md) proves over `Z[x,y][[t]]` that `Q(t,x,y) sum_n s_n t^n=P(t,x,y)` with `Q(0)=1, deg_t Q=28, deg_t P<=27`. Hence **d(a,b)<=28** for every `a,b>=0`.

The original native kernel has exactly three gated edges, from ports 7,29,31 to port 9, and their `R5=R6=0`. Each nongated action has `R5+R6<=1`; therefore `s_n` is an integer polynomial of total `x,y` degree at most `n`. Define

`H(x,y)=det(s_(i+j)(x,y))_(0<=i,j<28)`.

Each determinant term has total degree at most `sum_(i=0)^27 (i+pi(i))=756`. Thus `H` is an integer polynomial supported within `{(u,v):u,v>=0,u+v<=756}`. The inherited independent original-96 certificate `H(2,3) mod 1000000007=595325725!=0` proves `H` is not the zero polynomial.

Write any unequal positive `(a,b)=k(A,B)` with `gcd(A,B)=1`. If `max(A,B)>756`, the map `(u,v)->Au+Bv` is **injective on the entire support box**: from `A(u-u')=B(v'-v)` and coprimality, `B|(u-u')`, `A|(v-v')`, while both absolute differences are <=756. Thus `H(L^A,L^B)` remains a nonzero polynomial. This proves rank >=28 for every primitive slope outside the finite square.

The entire remaining finite domain is all **ordered**, coprime, unequal positive pairs with `max(A,B)<=756`, of size

`2 * sum_(m=2)^756 phi(m) = 347574`.

An exact finite-field verifier evaluated `x=2^A, y=2^B` modulo `p=1000000007` at **every one** of these 347574 pairs, constructed the first-gate counts `s_0,...,s_55`, and computed `det H_28 mod p` by Gaussian elimination plus 56-term Berlekamp–Massey order. **Every determinant was nonzero and every BM order exactly 28**; there were zero exceptions. It used a 37-state passive weighted quotient whose bridge back to the unchanged original 96 states was rechecked for all **576 original tagged edges**, with port9->class8, 106 aggregated weighted nongate transitions and exact gate-vector counts. An entirely separate Python computation using the original 96 native states, **not the quotient**, rechecked 100 deterministic boundary and mixed-slope determinants, all identical.

Hence `H(L^A,L^B)` is not identically zero for *every* unequal primitive positive pair. Substituting `L->L^k` preserves polynomial nonzeroness, so `H(L^a,L^b)!=0` for all unequal positive integers. Their minimal scalar Hankel rank is >=28, and the inherited denominator identity bounds it by 28. Thus `d(a,b)=28` universally. The exceptional zero/equal cases, already proved symbolically and with native lower minors, complete the classification.

## Fully reproducible author evidence

The self-contained **15-file** portable research package contains the original frozen native kernel, 576-edge snapshot, 37-state quotient and generic-Q certificates, standalone native-to-quotient bridge verifier, C++ exhaustive modular verifier, **all 347574 ordered pair determinant residues in a CSV**, independent original-96 Python spot-check verifier and its 100 witnesses, complete expanded proof, hash manifest and continuation record.

- Local portable ZIP: `PREFIX577_R6_ALL_NONNEGATIVE_MONOMIAL_SLOPES_AUTHOR_PORTABLE_20261108.zip`, size **2140676 bytes**, SHA-256 `ccfe5091caa33a976f0e363521f867d6f41b9fa354c69781ebb9b890eacef4b1`. This ZIP is an **author local artifact**, not claimed to be uploaded with this GitHub note.
- Complete 347574-pair CSV: SHA-256 `6e93cdd8d6a060a82d5955a3be12670c3ad6301a8c37b1b56a7f07271f5a02a4` (7160458 bytes).
- C++ exact verifier: SHA-256 `555ce0ff8de0e47fe3236bb6462b87dbb2ebd5848154864dc7930d90d9e3f8e0`.
- Independent ZIP extraction and execution: all tests PASS; the C++ verifier reproduced the entire CSV byte for byte, the native 576-edge bridge and 100 native96 spot-checks passed, and all 14 data/proof files matched the manifest SHA-256.
- Sample `(a,b)=(1,2)`: `det H_28=112892214 mod p`; `(a,b)=(755,756)`: `837812010 mod p`; prior original `(x,y)=(2,3)`: `595325725 mod p`.

The result is scoped to the **passive first-gate scalar readout** under uniform tagged-action sampling. Equal rank is not lossless joint observer equivalence: the inherited native `T=8, (U,V)=(0,1)` and `(U,V)=(2,0)` paths both map to `U+2V=2` while preserving distinct counts/provenance. For action-conditioned operations, retain the previous 51-state exact labeled-action interface and the original six-axis carrier.

## Source and research continuity

D25 remains the separate Source scientific target: original-class H0/B0 divided-power, `[X]U mod p^2`, Frobenius direction, normalization and native CM experiment. This note creates no D25 CLAIM, OPEN, Source checkpoint, Result or Review. Historical service-issued `EM-ENTERPRISE-301CA6` and `RA-E889C3B8461F5844B53CAF15` are recorded provenance, not an active session capability. The own-session recovery query currently lacks a valid privately possessed issued session; historical session-start request `h40-r11-self-researcher-session-start-20261108t1954-v1` was successfully reconciled. An original D25 read `h40-r11-d25-continuation-20261108t1512-v1` was most recently `WAITING_RESOURCE`, not grounds to resubmit it. Original UR four-file V2 bundle (94687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) is still unrecovered in the checked workspace. Preserve Source exact seed semantics before any future typed continuation.

**Author provenance:** history `EM-DIRECT-3EE30C`, later historical service issue `EM-ENTERPRISE-301CA6`. **Current claim:** `UNREVIEWED / NOT_ADMITTED`. **No P000/Foundation/Working Truth promotion.**
