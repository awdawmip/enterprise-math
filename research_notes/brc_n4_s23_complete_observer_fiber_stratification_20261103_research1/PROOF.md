# BRC N=4 / S23: complete classification of every eleven-parameter observation fiber

**Date:** 2026-11-03 (Asia/Shanghai). **Status:** author-side analytic theorem, executed exact-rational checks, independent review pending. **Frozen scientific input:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Predecessor:** `96ae516a9b179c30bbd57247b26449a8a192b416:research_notes/brc_n4_s23_observer_fiber_four_flat_20261103_research1/PROOF.md`. This extends one certified four-dimensional fiber to every point of the original eleven-dimensional cube.

## 1. Original source-labeled model

For `z=(z0,...,z10) in [0,1]^11`, set

```
A=[0,0,0,1,1,1]; B=[2,2,3,2,2,4]; C=[5,6,7,8,9,10].
M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
   [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].
R(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
R_i(z)=R(z[A_i],z[B_i],z[C_i]).
P_i(z)=sum_j (M[i,j]/20) R_j(z).
```

All six source labels and four outcomes are retained. The six-row source mixer has determinant `1/50` and inverse (componentwise on outcome vectors):

```
R0=11P0-10P1; R1=10P1-9P0; R2=P2;
R3=(9P3-5P4)/4; R4=(5P4-P3)/4; R5=P5.
```

Thus equality of full ordered observations `P(z)=P(z')` is equivalent to equality of every labeled raw source `R_i(z)=R_i(z')`.

## 2. Complete fiber classification theorem

Let the Boolean flags at the **given** parameter point be

```
l0=[z0=1], l1=[z1=1], u2=[z2=1], u3=[z3=1], u4=[z4=1].
```

Define the set `I(z)` of inactive indices by the following exact rules:

- `2 in I` iff `l0 AND l1`; `3 in I` iff `l0`; `4 in I` iff `l1`.
- For each `i=0,...,5`, `C_i in I` iff `z[A_i]=1 OR z[B_i]=1`.
- Neither 0 nor 1 belongs to `I`.

Then for **every** real `z in [0,1]^11`,

```
P^{-1}(P(z)) = { z' in [0,1]^11 : z'_j=z_j for all j not in I(z) }.
```

The coordinates indexed by `I(z)` vary freely and independently over the *entire* interval `[0,1]`. Hence each fiber is a coordinate-aligned cube of exactly

```
d(z) = [l0 AND l1]+[l0]+[l1]
     +2[l0 OR u2]+[l0 OR u3]+2[l1 OR u2]+[l1 OR u4].
```

### Proof (necessity and sufficiency)

The first entry of each `R(a,b,c)` identifies `a`, so `z0,z1` are recovered. Whenever `a<1`, its second entry identifies `b=R[1]/(1-a)`. Rows 0,1,3,4 share `z2`, which is therefore identified if at least one of `z0,z1` is below one. Row 2 identifies `z3` iff `z0<1`; row 5 identifies `z4` iff `z1<1`. Finally, in each row with `a<1,b<1` the third entry identifies its unique last-coordinate `c=R[2]/((1-a)(1-b))`. Thus all indices *outside* `I(z)` are necessarily fixed on the fiber, with every division performed only at positive denominator.

Conversely, keep these recovered indices fixed and change the coordinates inside `I(z)` arbitrarily. For a row with `a=1`, `R=(1,0,0,0)` independently of `b,c`; otherwise its `b` was recovered and remains fixed. If `b=1`, `R=(a,1-a,0,0)` independently of `c`; otherwise `c` was recovered. Every raw labeled row therefore remains fixed, and so does the invertible mixed observation `P`. This proves both inclusions and independent freedom. QED.

## 3. Complete dimension spectrum and two missing dimensions

The five flags yield exactly 32 signatures. Formula above reduces to:

| Flag regime | Dimension | Number of flag signatures |
|---|---|---:|
| `l0=l1=0,u2=0` | `u3+u4` | 4 |
| `l0=l1=0,u2=1` | `4+u3+u4` | 4 |
| `l0=1,l1=0` | `4+2u2+u4` | 8 |
| `l0=0,l1=1` | `4+2u2+u3` | 8 |
| `l0=l1=1` | `9` | 8 |

Counting signatures by dimension gives `{0:1, 1:2, 2:1, 4:5, 5:6, 6:5, 7:4, 9:8}`. The **complete attainable spectrum** is

```
{0,1,2,4,5,6,7,9}.
```

**Fiber dimensions 3 and 8 are impossible** in this frozen model. Generic parameters with `z0,z1,z2,z3,z4<1` have a singleton observation fiber. The maximum dimension 9 occurs precisely when `z0=z1=1`; the full observation then assigns probability one to the first outcome at every source, independent of the other nine parameters. The counts describe upstream equality-signatures, not volumes or frequencies of real input points.

At the predecessor's `z*=(1/3,5/6,1,1/2,1/2;1/3,1/2,1,1/2,1/3,1/3)`, flags are `(0,0,1,0,0)`; the theorem recovers `I(z*)={5,6,8,9}` and dimension 4 exactly.

## 4. Source-label-preserving canonical representative

Define `c(z)` by setting to zero precisely the inactive coordinates indexed by `I(z)`. Then

```
P(c(z))=P(z); I(c(z))=I(z); c(c(z))=c(z)
```

for all real `z`. In the only situation where resetting an inactive `b` could change a Boolean `b=1` flag, all sources of that `b` already have `a=1`, so every dependent `c` was also inactive. Therefore the inactive-index set itself remains unchanged.

For every **fixed** stochastic decoder `D` with source output rows `Q_{D,i}` independent of `z`, the exact maximum total-variation risk

```
L_D(z)=max_i TV(P_i(z),Q_{D,i})
```

satisfies `L_D(c(z))=L_D(z)`; the same holds for any minimum over a fixed decoder bank, or any functional factoring only through the six labeled source observations.

This is a certified *readout* quotient only. The original latent causal coordinates and branch provenance remain relevant for downstream interventions. For example, if `z0=1`, changing latent `z3` has no current readout effect, but resetting `z0<1` can reactivate it. No Heartbeat-native dynamics, physical model, or X6 world-state equivalence is asserted.

## 5. Executed verification and next unresolved mathematical unit

Adjacent `VERIFY.py` ran with Python `fractions.Fraction`. Its exact checks include all 32 flags, **5,209** corner equalities of the certified rectangular fibers, 32 interior fiber tests, **168** one-coordinate discriminating tests of identified indices, 32 block-inverse checks, all free-index sets and signature counts. Full machine evidence is `RUN_EVIDENCE.json`. The theorem's universal real-domain quantifier is supplied by the symbolic inverse and zero-factor proof above; the finite tests validate its reproducible implementation.

**Reuse:** The original typed BRC six-labeled-source observer, its `1/50` mixer inverse and the predecessor's observer-fiber theorem are reused directly. No new decoder-bank risk bound or formal checker result is claimed.

**Next:** Apply these observation representatives to the joint optimization of three free decoder kernels over S18, J, F5, C6, two-parameter T and the inherited 2/3 witness. Seek a shared exact `3/5` feasible construction or a certified finite infeasibility argument; preserve provenance if a later intervention uses presently inactive branches.
