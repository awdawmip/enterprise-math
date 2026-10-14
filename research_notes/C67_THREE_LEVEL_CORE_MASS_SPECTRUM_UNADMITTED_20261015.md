# C67 — Exact three-level G0-orbit mass spectrum (UNADMITTED)

**Research status:** author finite GF(2) theorem and two independent-in-code exhaustive checks; UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM. Classical finite 156-integer-edge, 142-exchange-face positive BRC auxiliary model only. Not original C46 exact-observer equivalence and not native six-dimensional X6 Cell mathematics.

**Verified read pins:** GLOBAL_KNOWLEDGE_V1 `main@ae30c62e21132ac89cab0708a8fca475a1159b9e`; Enterprise Math `main@1c2913ac2c3b0412b3aedca30dfa9cf16ac8bee7`. Predecessor C66 draft `0cf78ee2713ec4a45ad55051081fe5e455668aed:research_notes/C66_FULL142_GLOBAL_CORE_MASS_DOMINANCE_UNADMITTED_20261015.md`. Source uses original C66 arrays (32×23 GF(2) pair-gauge A, 32×23 disagreement D) and C65 real 156-old-edge complement.

## New theorem and complete finite orbit spectrum

Write `beta=(1-t)/(1+t)` for `0<t<1`. In the sector `chi_83=chi_96=+1`, each G0 orbit has a 23-bit transversal `z`, a 32-bit discordance mask `delta(z)=D*z`, and `d=popcount(delta)`. The C66 canonical section has second face positive in all 32 ordinary pairs; gauge `g` flips both members of pair i exactly when `(A*g)_i=1`, preserving all 76 noncore faces. Let

`J(z)={i:delta_i(z)=0}`, `Delta(z)=min_g #{i in J(z):(A*g)_i=0}`.

The core-determined 66-face negative count is exactly `w_+(z,g)=d+2 #{i in J(z):(A*g)_i=1}`, so `min_g w_+=d` and `max_g w_+=64-d-2*Delta`. C65's genuine old-edge complement flips all 66 fixed faces and preserves the 76 noncore positive factors, so the paired negative sector has minimum negative count `66-max_g w_+=d+2+2*Delta`. Therefore, including the full, uncancelled positive noncore mass in the comparison,

`max_{c in O_z^-} Q_t(c) / max_{c in O_z^+} Q_t(c) = beta^(2+2*Delta(z))`  (**exact**, all `0<t<1`).

A direct 32-row/23-variable GF(2) elimination proves no word of `Im(A)` has fewer than two zeros, and gives a two-zero word:
`g*=0x55ddbc`, `A*g*=0xbfffbfff`, zero indices `{14,30}` (0-based). Thus `0<=Delta(z)<=2` for EVERY z (restrict this same word to J(z)); for `z=0`, `Delta=2`. The 23D image code rank and D rank both equal 23.

**Exhaustive 2^23 orbit classification (author self-check, exact integers):**

| Delta | Orbitwise max-mass ratio | At t=1/2 | Number of distinct G0 orbits |
|---|---|---|---:|
| 0 | beta^2 | 1/9 | 7,313,074 |
| 1 | beta^4 | 1/81 | 1,042,432 |
| 2 | beta^6 | 1/729 | 33,102 |
| **Total** | | | **8,388,608** |

Two different programs traversed all 8,388,608 z:
A. Build the nine-dimensional kernel of A^T, enumerate 256 odd dependencies v. Delta=0 iff no odd v has v&delta=0; otherwise Delta=1 iff the intersection of all offending v contains a remaining concordant coordinate, else Delta=2.
B. Build a nine-bit parity-check H for Im(A); write h=H*all_ones. For discordant set S, Delta=0 iff h belongs to span of H columns from S; else Delta=1 iff h xor H_i does for some i outside S; otherwise Delta=2. Both full checks gave (7,313,074,1,042,432,33,102). The first count also matches independently inherited C66; the other 1,075,534 are now *completely* classified. Neither check uses floating point.

**New global two-sided mass theorem:** with `W_max,+/- = max Q_t(c)` over all genuinely feasible `chi83=chi96=+1/-1` full-core states,

`beta^6 <= W_max,-(t)/W_max,+(t) <= beta^2`.

C66 proved the upper bound. For the new lower bound, choose the z sector realizing `W_max,+`; its paired negative orbit has maximal mass at least `beta^6` times that positive maximum. In particular at `t=1/2`:

`1/729 <= W_max,-(1/2)/W_max,+(1/2) <= 1/9`.

**Lossless observer reduction limited to these extrema:** let `S_t(z)>0` denote the full 76-face noncore factor constant on G0 and under complement, and `A_z(t)=(1+t)^66*S_t(z)*beta^d(z)`. Then `W_max,+=max_z A_z`, `W_max,-=max_z A_z*beta^(2+2*Delta(z))`. The remaining unresolved exact global value requires `S_t(z)` and cannot be inferred from the three exponent counts alone.

### Exact raw A,D matrices (32 rows, hexadecimal 23-bit masks)

`A=[0x21003,0x620105,0xa0049,0x11,0x2206,0x408a,0x22,0x40c,0x4,0x40030,0x10,0x1080c0,0x840,0x80,0x210300,0xd00,0x100,0x600,0x800,0x413000,0xd000,0x1000,0x6000,0x8000,0x10000,0x180000,0x60000,0x680000,0x620000,0x100000,0x200000,0x400000]`

`D=[0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80,0x100,0x8449,0x4110a,0x4225,0x20886,0x900b0,0x2013,0x20000,0x40000,0x80000,0x7b4013,0x2000,0x4000,0x8000,0x10000,0x400000,0x516000,0x200,0x400,0x800,0x1000,0x300a00,0x200000,0x100000]`

Every bit is GF(2); `(A*g)_i = popcount(A[i]&g)%2` and likewise D. Full portable checkers, unmodified C66 input and individual receipts are packaged as `EM_C67_THREE_LEVEL_BRC_PORTABLE.zip` in the originating ChatGPT run. This note's statement is self-contained for regeneration.

**Boundary:** Existing C65/C66 source is author-only and not Driver admitted. This theorem compares maxima of UNNORMALIZED core-event masses, not total-sector probability or conditional four-residual feedback. C46's precise 2^24 observer/weight contract was NOT retrieved and NO transfer is claimed. No native X6/three-dimensional-slice bridge. Formal Source activity, CLAIM, Result and independent review separately require valid native authority.

**Next unit:** compute/compare the full `S_{1/2}(z)` for maximizing candidate sectors, or prove a rigorous noncore-weight dominance that narrows the global interval; then inspect the exact C46 taskbook for an observer-preserving transfer before making any C46 exponent claim. Retain the independent all-negative-core conditional-feedback question as unsolved.

**Reproducibility:** GF(2) two-zero target solve checks all 0- and 1-error patterns (33 systems), finds `g*`, then enumerates `z=0..2^23-1` in Gray order using D's 23 columns. Algorithms A and B above provide an exact independent arithmetic cross-check of every label; finite exact outputs are author evidence, not independent Driver review.
