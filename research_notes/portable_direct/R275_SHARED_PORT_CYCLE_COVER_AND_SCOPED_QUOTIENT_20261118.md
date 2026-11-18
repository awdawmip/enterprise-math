# R275 — Shared visible-Port cycles: exact cycle-cover determinant, observer quotient, and crossed feedback

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED.
Continuation: R274 at Git commit `f9a93873f1b8d724519434a660f70c91971229b0`.
Scientific input is frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; use canonical WBRC-T30/T31/T32 and the typed, positive-rational, **labeled visible-Port** interface. This is a recurrent Port calculation, not an independent primitive force-balance assertion under P000.

## 1. Signed cycle-cover identity (arbitrary finite graphs)

Let `W` be a finite rational weighted directed graph (entries may be nonnegative) and let `A=I-W`. For each family `F` of pairwise vertex-disjoint directed simple cycles (loops of length 1 included), with `w(F)` the product of its edge weights, the exact identity is

```
det(I-W) = sum_{F vertex-disjoint directed-cycle family} (-1)^{|F|} w(F).
```

Parallel weighted edges are interpreted by expanding each matrix entry into its edge sum. The empty family contributes 1. **Proof:** Expand the determinant by permutations and choose, for every non-fixed point, the `-W_ij` term. A permutation's nontrivial components are disjoint directed cycles; a length-L cycle's permutation sign is `(-1)^(L-1)` while its L selected negative matrix entries give `(-1)^L`, leaving `-1` per cycle. Diagonal fixed points either contribute 1 or one negative self-loop term. This gives the formula without a positivity or stability assumption.

The signed minus signs here are the determinant/inclusion–exclusion algebra; individual BRC edge masses are positive. The full edge labels and provenance are retained before projection.

## 2. A bouquet of complete two-edge cycles has an exact one-scalar hub observer

For labeled visible Ports `0,1,...,k`, `k>=2`, use edges `0->i` of weight `a_i>=0` and `i->0` of weight `b_i>=0`, no other edges. Set `Q_i=a_i*b_i`, `Q=sum_i Q_i<1`.

```
W = [[0, a^T], [b, 0_k]],
det(I-W)=1-Q,
S=(I-W)^(-1),
S_00=1/(1-Q),
S_0i=a_i/(1-Q), S_i0=b_i/(1-Q),
S_ij=delta_ij + b_i*a_j/(1-Q).
```

**Proof:** Schur complement of the identity block `I_k` gives `1-a^T b=1-Q` and the displayed inverse. Equivalently `W` has nonzero eigenvalues `+sqrt(Q),-sqrt(Q)`, so `Q<1` gives strict recurrence stability. Two cycles sharing the hub cannot appear together in a vertex-disjoint cycle cover; there is no `+Q_iQ_j` term in its determinant.

For the **restricted observer language** consisting of `S_00` before and after arbitrary nonnegative self-loop insertions `lambda` at hub 0 with `Q+lambda<1`, the scalar `Q` is a complete and minimal exact signature:

```
S_00(lambda)=1/(1-Q-lambda),  Q=1-1/S_00(0).
```

Thus equal `Q` is precisely observational equivalence for this language. This is a scoped safe quotient only for the stated hub readout and hub-loop contexts, not a replacement for the WBRC-T32 full-port dynamic signature.

## 3. One permitted edge insertion distinguishes equal-Q modules

Take three visible labels 0,1,2, `a_1=a_2=1/4`. Module A has `(b_1,b_2)=(1/4,1/2)`; module B has `(b_1,b_2)=(1/2,1/4)`. Both have `Q=3/16` and `S_00=16/13`, with every row sum below 1.

Insert the **same permitted nonnegative Port edge** of weight `delta=1/8` from 0 to 1 in each module (parallel addition). The new hub sums are

```
Q_A'=7/32,       S_A,00'=32/25,
Q_B'=1/4,        S_B,00'=4/3.
```

Therefore the scalar `Q` loses future-observer information as soon as this explicitly allowed labeled-edge context is added. The missing coordinate here is the effect `delta*b_1`, an actual mixed Port residual. Keeping the full labeled `W_eff` as in WBRC-T32 is safe for unrestricted permitted Port contexts.

## 4. Two individually 13-adically regular cycles create an arbitrary pole together

Set `P=13^t`, `t>=1`, `a_1=a_2=1/4` and `b_1=b_2=2/(1+P)`, with no cross-edges. All four weights are strictly positive and all row sums are below 1. Each complete cycle has

```
Q_i=1/[2(1+P)],
S_00(single cycle)=2(1+P)/(1+2P),
v13(S_00(single cycle))=0.
```

The simultaneous feedback instead yields

```
Q=1/(1+P),   det(I-W)=P/(1+P),
S_00=(1+P)/P,
v13(S_00)=-t,       13^t*S_00=1+P == 1 (mod 13).
```

Hence two individually 13-adically regular *complete* Port cycles share a hub and create an arbitrarily deep collective pole. The result quantifies the joint relation rather than discarding either loop.

## 5. Cross-edges create new cycles and change or remove this resonance

For three distinct visible labels and nonnegative rational edges, define

```
W=[[0,a,c], [b,0,e], [d,f,0]],  rho(W)<1,
D=det(I-W)=1-ab-cd-ef-aed-cfb,
S_00=(1-ef)/D.
```

The three 2-cycles have weights `ab,cd,ef`; the two directed triangles have weights `aed,cfb`. Every two nonempty cycles intersect, so no two-cycle-family product appears. The formula also follows by eliminating Ports 1,2, yielding `W_eff,00=(ab+cd+aed+cfb)/(1-ef)`.

With `a=c=1/4`, `b=d=2/(1+P)`, `e=f=1/8`, all row sums stay below 1 and

```
D=9(7P-1)/[64(1+P)],
S_00=7(1+P)/(7P-1),   v13(S_00)=0, S_00 == 6 (mod 13).
```

A fixed positive cross-edge therefore removes the earlier depth-`t` 13-adic pole. Alternatively, taking `e=f=P/[4(1+P)]` gives

```
D=3P(4+5P)/[16(1+P)^2],
v13(S_00)=-t,   13^t*S_00 == 10 (mod 13).
```

The latter cross context preserves pole depth but changes its normalized residue from 1 to 10. These are exact rational positive recurrent contexts, not numerical approximations.

## 6. Evidence, status and next research unit

A deterministic stdlib `fractions.Fraction` checker independently evaluates each 3×3 determinant by elimination, verifies the inverse cofactor formula, strict row-sum stability, and all valuation/residue identities for `t=1,...,8`. It also verifies the explicit equal-Q/context counterexample. Exact machine result: `PASS`, 24 independent matrix determinant cases plus the labeled-edge witness. Full JSON is reproducible from `R275_shared_port_cycles_checker.py` (stdout); evidence snapshot is `R275_verification.json`.

This proof combines the classical determinant cycle-cover/Schur identities with the concrete WBRC labeled-Port context and a new scoped observer-equivalence/counterexample. No independent reviewer or formal proof checker has yet evaluated it.

**Next:** classify how cross-edge valuation and leading 13-adic coefficients control `D`, including the possibility of additional cancellation at precisely matched scales (continued in R276). Separately test future-operation certificates beyond hub-loop insertion, retaining edge labels, route provenance, and actual BRC restrictions.
