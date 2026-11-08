# PREFIX-601-R6 — Twelve-incidence weighted native-BRC phase discriminant

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Native source: `PREFIX565_positive_marginal_certificate.py` (Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`).
Direct predecessor: `2026-11-08_prefix600_r6_sparse_phase_inverse_seven_reward_codec.md`, original frozen kernel recovered at `t_e=1`.

## Question and exact observer

The frozen BRC primitive has 48 native phases (96 phase/branch-bit ports), six labeled original actions, and nine allowed roots. PREFIX-600 proved that its 48-phase adjacency has two 24x24 sign-flip blocks `B=W+UV`, with `W` eight disjoint 3-cycles, 12 native star-edge incidences, six reciprocal incidence pairs, and `VW^{-1}U=2J` for the involution `J` interchanging each pair.

Explore the EXACT **12-parameter deformation of this original native action graph**, assigning each incidence `e=(star,shared edge)` a cross-star weight `t_e>=0`. Keep all native states, native phase/signed tags, action provenance and source, but weight the two cross-star successors at incidence `e` by `t_e`, while its one within-star successor retains weight 1. The original frozen kernel is the section `t_e=1` for every incidence. The observer is the **next native phase marginal**; the proof makes no claim of preserving full seven-reward/branch/action histories under this observer.

Write `D(t)=diag(t_e)` (12x12) and

`B(t)=W+U D(t) V`;  `M(t)=[0 B(t); B(t) 0]` (48x48).

Because the row corresponding to incidence `e` has mass `1+2t_e`, row normalization yields a nonnegative Markov kernel `Q(t)=diag(row_sums(M(t)))^{-1} M(t)` whenever all `t_e>=0`.

## Theorem 1 — exact six-factor discriminant

Let the six two-cycles of `J` be `{e,f}`. For all 12 real, rational or symbolic weights:

```text
det B(t) = product_{ {e,f} in J-pairs } (1-4 t_e t_f)
det M(t) = product_{ {e,f} in J-pairs } (1-4 t_e t_f)^2.
```

In particular, each of the six native shared edges contributes a distinct independent factor; the factor belonging to any selected reciprocal pair is independent of the other ten incidence weights.

**Proof.** The native frozen incidence identity persists because the primitive graph itself is unmodified:

`V W^{-1} U D(t) = 2 J D(t)`.

By Sylvester's determinant identity and `det W=1` (eight 3-cycles),

`det B(t)=det W det(I_12+2JD(t))`.

Order the incidence basis by reciprocal pairs. The corresponding block for `{e,f}` is

```text
H_{ef} = [1    2t_f]
         [2t_e 1   ]
```

and its determinant is `1-4t_e t_f`. Multiplying six blocks proves the first formula. Since `M(t)` has two identical off-diagonal blocks of even size 24, its determinant is `(det B(t))^2`. QED.

## Theorem 2 — exact rank and recoverability transition

Define `k(t)=#{ {e,f}: 4t_e t_f=1 }`. For all 12 scalar weights,

```text
rank B(t)=24-k(t),     rank M(t)=48-2k(t).
```

For nonnegative weights, normalized one-step phase transport `Q(t)` is exactly invertible iff none of the six products equals `1/4`. Its nullity is exactly `2k(t)` otherwise.

**Proof.** Let `H=I+2JD`. The equation `B(t)x=0` is equivalent to `x=-W^{-1}UDz`, with `z=Vx`. Inserting into `z=Vx` gives `Hz=0`. Conversely any `z in ker H` produces the displayed `x`, and `Vx=z`, so these kernel spaces are isomorphic. Each reciprocal pair block has nullity zero when its determinant is nonzero and one when it vanishes. The sign-flip 48-matrix doubles this nullity; positive diagonal row normalization preserves rank. QED.

## Theorem 3 — local exact inverse and linear-cost application

When all `delta_{ef}=1-4t_et_f` are nonzero, the inverse is

```text
B(t)^(-1)= W^(-1)-W^(-1) U D(t) H(t)^(-1) V W^(-1)
H_{ef}^(-1) = (1/delta_ef) [1       -2t_f]
                              [-2t_e   1   ].
```

There are six independent 2x2 solves. Since `W` is a permutation and `U,V` have fixed bounded incidence sparsity, the inverse can be *applied* to a vector with O(24+12) rational operations when exact bit cost is accounted separately. Multiplying the inverse of the row-normalized transition by the row-mass diagonal reconstructs initial phase laws. This recovers PREFIX-600's four-nonzero-per-row inverse at the original `t_e=1` section. Singular weights require retaining an independent lost-phase coordinate rather than using inverse reconstruction.

## A constructive identifiability counterexample (homogeneous t=1/2)

At all `t_e=1/2`, each native phase moves internally with probability `1/2` and to either cross-star successor with probability `1/4`. Precisely `k=6`: `rank M=36`, rather than the original model's `rank M=48`.

Let the positive-signed 24-phase ordering be the one constructed from the original `PHASES` table. Under the uniform baseline `u_i=1/24` define `w` supported at indices 0,1,6,7 with entries `(+1/2,+1/2,-1/2,-1/2)`. These correspond to original phase IDs `(2,3,14,15)`. Direct native incidence calculation yields `w B(1/2)=0`, `sum_i w_i=0`. Thus

`pi^+=u+(1/24)w`, `pi^-=u-(1/24)w`

are distinct, nonnegative, normalized initial laws with **exactly identical next-phase marginals**. At the four differing coordinates, `pi^+` has `(1/16,1/16,1/48,1/48)` and `pi^-` swaps these values. This is an explicit observer-loss witness, not a claim of indistinguishability for the full seven-reward action-aware language.

## Exact verification

The attached short executable certificate imports the verified native PREFIX-565 implementation via PREFIX-600, recomputes the incidence identity, constructs rational weighted 24x24 matrices, verifies their exact block inverses for regular cases and native null vectors for singular cases. An extended independent certificate additionally computes exact rational determinants/ranks of the actual weighted matrix, constructs the two distinct probability laws above, and verifies exact equality of their next-phase marginals.

Executed locally with Python stdlib `fractions.Fraction`: `ALL_CHECKS_PASS`.

| Weight family | det B | rank B | rank M |
|---|---:|---:|---:|
| Original all 1 | 729 | 24 | 48 |
| All 0 | 1 | 24 | 48 |
| Twelve distinct rationals (i+1)/(i+3), i=0..11 | -1094608/4729725 | 24 | 48 |
| One reciprocal pair at (1/2,1/2), others 1 | 0 | 23 | 46 |
| Two reciprocal pairs at (1/4,1), others 1 | 0 | 22 | 44 |
| All 1/2 | 0 | 18 | 36 |

The new statement is a **parameterized native-action-graph model family**, rooted in the original typed BRC `NEXT` source. The frozen original probabilistic law is its all-1 section. The singular strata are candidate experiments for observer identifiability and information-preserving BRC coarse graining; they do not alter P000, the ACTIVE worldview, or the original frozen science pin.

## Next problem

Derive a phase-local repair coordinate for each singular reciprocal shared edge, and determine if a branch-labeled or full-seven-reward observer can identify it. Then measure minimum sufficient nonnegative-state representation and exact bit complexity across the six critical hypersurfaces.

Reuse: `REUSE_EXECUTED` original BRC native graph (PREFIX-565); `COMPOSE_APPLIED` PREFIX-600 incidence decomposition. Formal Result/Review and independent mathematical review remain open.
