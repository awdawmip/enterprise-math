# R5 — Complete classification of the source-compensated two-law J/K family

Date: 2026-11-02 (Asia/Shanghai). Research status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an auxiliary finite-horizon two-law source-labelled BRC stopping model, not a native X6 physical realization.

## Source, scope and exact scientific freeze

Parent goal: construct strictly positive two-law stopping model with equal four-observer convex hulls for FULL history and seedless likelihood-ratio (LR) policies, but different actual real-behavior observer images, ideally of full affine rank four. The exact predecessor is `awdawmip/enterprise-math@d4b832b0a55cc0b92474600879c019d5dc989978:research_notes/brc_r5_compensated_k_delay_fullface_20261102_t1945/RESEARCH.md`, which proved equality of the *entire* maximal `B=3` face under answer/time compensation while giving an off-face support gap. The predecessor's frozen scientific inputs remain global `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Behavioral policy is read separately at current canonical main. P000 and ACTIVE worldview remain unchanged.

## Definition: complete compensated source family

Order the four hidden sources as `C,I,BJ,IJ`. Let `p_s ∈ (1/8,1)` and set `q_s=(8p_s-1)/9`, so that `q_s∈(0,1)` and `9(1+q_s)=8(1+p_s)`. Put `α_s=1+p_s`. Choose `κ,λ>0` with `0<κ α_s<1` and `0<λ α_s<1` for all sources. Set the conditional K answer probabilities under P and Q to `U_s=κ α_s` and `V_s=λ α_s`. The four J answer probabilities `a_B,a_I,b_B,b_I` lie independently in `(0,1)`.

The FULL behavior is `(x,j_B,j_I,k_C,k_I,k_BJ,k_IJ)∈[0,1]^7`; the LR behavior is the restricted real policy `j_B=j_I=y`, `k_C=k_I=k_BJ=k_IJ=z`, with `(x,y,z)∈[0,1]^3`. Define

```
D_B=(1-j_B)/8,            D_I=(1-x)(1-j_I)/8,          D=D_B+D_I,
w=(1/4,(1-x)/4,D_B,D_I),
R=Σ_s α_s w_s (1-k_s),
B=5/2-3x/4+2D.
O=(e_P,e_Q,T_P,T_Q)
 =(1-a_B D_B-a_I D_I-κR,
   b_B D_B+b_I D_I+λR,
   B+R,
   B+(8/9)R).
```

The observer itself recovers `B=-8T_P+9T_Q`, `R=9(T_P-T_Q)` and the corrected source answer masses `A=1-e_P-κR=a_B D_B+a_I D_I`, `C=e_Q-λR=b_B D_B+b_I D_I`. All source masses `w_s` are nonnegative and carry their original path identities until an explicit observer-preserving quotient is proved. The supported claim concerns this precise finite model.

## Main theorem — exact all-real four-observer classification

For every set of **real** natural parameters satisfying the preceding strict inequalities,

```
conv O(FULL) = conv O(LR)
   iff a_B=a_I and b_B=b_I and p_BJ=p_IJ.
```

Whenever those three equalities hold, there is the stronger **actual real-behavior** image identity `O(FULL)=O(LR)`. In every hull-equality instance, the common observer set lies in an affine subspace of dimension at most three. Thus the full compensated family has no full-four-dimensional hull-equal/image-unequal example; the parent four-observer construction question remains open for other time/action mechanisms.

### Proof, part 1: two exact source-J support gaps

Set `s_a=a_B+a_I`, `s_b=b_B+b_I`, and define affine observer functionals

```
F_P=(s_a/4)(B-5/2)-A,
F_Q=(s_b/4)(B-5/2)-C.
```

In original observer coordinates, their signed normals (affine constants omitted) are

```
n_P=(1,0,-2s_a+9κ, 9s_a/4-9κ),
n_Q=(0,-1,-2s_b+9λ, 9s_b/4-9λ).
```

Substitution, with all K behavior eliminated *exactly*, gives

```
F_P= -3s_a x/16 + (a_I-a_B)(D_B-D_I)/2,
F_Q= -3s_b x/16 + (b_I-b_B)(D_B-D_I)/2.
```

Under LR, `D_I=(1-x)D_B`, `0≤D_B≤1/8`. Therefore `F_P≤x(-3s_a+|a_B-a_I|)/16≤0`, with equality at `x=0`. The same argument holds for `F_Q`; both are zero at some LR strategy. Under FULL, `D_B≤1/8`, `D_I≤(1-x)/8≤1/8`, so `F_P≤|a_B-a_I|/16`, attained by `x=0` and selecting precisely one of the two J branches (`(D_B,D_I)=(1/8,0)` or `(0,1/8)`, depending on the sign). Identically for Q. Consequently for **all signed observer normals** specifically displayed here,

```
h_FULL(n_P)-h_LR(n_P)=|a_B-a_I|/16,
h_FULL(n_Q)-h_LR(n_Q)=|b_B-b_I|/16.
```

Hull equality thus forces `a_B=a_I`, `b_B=b_I`. This holds for arbitrary allowed source-specific `p_s` and both compensated K-answer kernels, not merely on the previously studied `B=3` face.

### Proof, part 2: exact remaining BJ/IJ time-source gap

Now let `a_B=a_I=a`, `b_B=b_I=b`, and put `δ=α_BJ-α_IJ=p_BJ-p_IJ`, `c=(α_BJ+α_IJ)/2`. Since `a>0`, the total J-source mass is recovered from the observer as `D=A/a`. Define

```
F_K=R-cD;
n_K=(c/a,0,9(1+cκ/a),-9(1+cκ/a)).
```

The displayed normal implements `F_K` up to its affine constant. Because all `α_s>0`, maximizing `F_K` at fixed upstream behavior sets all K continuation controls to zero (or `z=0` in LR). Put `H=(α_C+α_I)/4` where the `I` subscript here denotes the second K source. Then

```
F_K,maxK=H-α_I x/4 +(δ/2)(D_B-D_I).
```

For FULL, this is at most `H+|δ|/16` and equality is attained at `x=0` with exactly the favorable one of `D_B,D_I` equal to `1/8`. In LR, `D_B-D_I=xD_B` and `D_B≤1/8`, giving

```
F_K,LR ≤ H-α_I x/4+δ xD_B/2
       ≤ H+x(-α_I/4+|δ|/16) ≤ H.
```

The last inequality is strict for positive `x`, since `α_I>1` and `|δ|<1`. LR attains `H` at `x=0,z=0`. Therefore

```
h_FULL(n_K)-h_LR(n_K)=|p_BJ-p_IJ|/16.
```

The necessary third equality follows, with all quantities exact for every real parameter in the declared domain.

### Proof, part 3: source-flow aggregation yields the stronger sufficiency

Assume `a_B=a_I=a`, `b_B=b_I=b`, and `α_BJ=α_IJ=α_J`. For an arbitrary FULL real policy take its `x`, `D=D_B+D_I` and `R`. Since `0≤D≤(2-x)/8`, select the LR J-hazard

```
y=1-8D/(2-x) ∈[0,1].
```

The maximum possible source-weighted continuation is independent of how `D` is split between BJ and IJ:

```
R_max=α_C/4+α_I(1-x)/4+α_J D >0.
```

Nonnegative source masses and K hazards give `0≤R≤R_max`. Set the common LR K-hazard `z=1-R/R_max ∈[0,1]`. Its source flow gives exactly the same `(x,D,R)` and hence exactly the same `O`. The reverse inclusion is immediate because LR is a restriction of FULL. Thus actual real-behavior observer images (and convex hulls) coincide.

Finally, in this equality case, all four observer entries are affine functions of just `(x,D,R)`, so their affine dimension is at most three. This closes the theorem.

## Quantitative separation and fully positive rational witness

Whenever the corresponding gap is nonzero, an actual FULL observer lies at `L∞` distance at least `gap / ||n||_1` from `conv O(LR)`, using the matching displayed normal. For the K normal this statement assumes both J vector equalities, as in part 2.

A strictly positive example with `a_B=a_I=3/5`, `b_B=b_I=2/5`, `p=(1/4,1/3,1/2,2/3)`, `κ=2/5`, `λ=1/3` has the exact K gap `1/96`. The FULL deterministic witness `(x,j_B,j_I;k_C,k_I,k_BJ,k_IJ)=(0,1,0;0,0,0,0)` gives

```
W=(7/12,241/720,173/48,379/108),
n_K=(95/36,0,37/2,-37/2),
||n_K||_1=1427/36,
dist_∞(W,conv O(LR))≥3/11416.
```

The gap and distance are for this model; they are not physical timing or spatial predictions.

## Author-side exact verification and unfinished questions

`VERIFY.py` uses only Python standard-library `fractions.Fraction`, enumerates all 128 FULL and 8 LR deterministic policies for each of seven strictly positive rational parameter sets, and verifies all three support-gap formulas in their applicable regimes. It checks the observer's corrected source-flow invariants and, for two hull-equal cases, constructs exact real LR matches for all 128 FULL corners plus 32 additional non-corner FULL policies per case. The actual captured output reports 2,711 exact assertions and 1,912 source-flow evaluations. The finite tests audit calculations; the universal real classification is established by the algebra above. There is no Lean/formal certificate, independent Driver review, Source-native Result/admission, or claimed native X6 embedding.

The next scientific unit is to change **one actual decision topology feature** that invalidates the current J-source aggregation and the K-source separation simultaneously. A source-conditioned downstream J-time mechanism or an additional interacting merger is a concrete candidate; use the present three support forms as exact diagnostics, then test full signed convex hull equality by rational FULL-vertex primal certificates or Farkas separators before attempting real-image nonmembership. See `NEXT_TASK.md`.

This is a portable GitHub author-side frontier, not a native CLAIM. Authenticated GitHub identity `awdawmip` has push permission; this run's native gateway reported `research_authority_granted=false`, `executor_binding_configured=false`, active control lookup `CONTROL_QUOTA`, and own-session start `STATIC_READONLY_SCOPE_DENIED` without sending the operation. No credentials are stored.
