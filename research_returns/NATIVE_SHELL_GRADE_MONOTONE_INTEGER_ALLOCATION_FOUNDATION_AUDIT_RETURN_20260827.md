# Native Shell Grade-Monotone Integer Allocation — Foundation Admissibility Audit Return

Status: `FINAL_FROZEN / DERIVED_WEAKER_TORSOR_ALLOCATION / FOUNDATION_UNCHANGED`
Date: `2026-08-27`
Researcher-ID: `EM-EBP2-7D2C2F`
Task: `RS-NATIVE-SHELL-GRADE-MONOTONE-INTEGER-ALLOCATION-FOUNDATION-AUDIT`
Publication: `TP2-C75E6232BAC2565C323D`
Claim: `chatgpt-nsia-20260827-1049`

## 1. Primary verdict

`PRIMARY_VERDICT = DERIVED_WEAKER_TORSOR_ALLOCATION`.

Current P0/P1 semantics do not determine a single frame-independent integer label for every shell state. They do determine, without downstream arithmetic input, the complete six-element native-frame torsor of grade-monotone, gap-free, sector-arc-compatible serializations.

Freeze:

- `POINTWISE_FRAME_INDEPENDENT_INTEGER_LABELING = EXACT_DEFINABILITY_OBSTRUCTION`;
- `GRADE_MONOTONE_GAP_FREE_INTERVAL_STRUCTURE = DERIVED`;
- `GLOBAL_FRAME_TORSOR_OF_SERIALIZATIONS = N0_DEFINABLE_DERIVED`;
- `CHOSEN_FRAME_SERIALIZATION = CONDITIONAL_ON_N1_FRAME_CHOICE`;
- `FRAME_INVARIANT_ORBIT_LABEL_SET = N2_READOUT_DESCENDS`;
- `FOUNDATION_MUTATION = NONE`.

No `5`, `7`, `9`, breaker, Joukowski, hyperbola, prime-saturation, or downstream packet theorem is used in the derivation.

## 2. Typed allocation object

Use the accepted native shell
`A_n={(a,b,c) in N_0^3 : min(a,b,c)=0, a+b+c=n}`, `|A_n|=3n`, transported to the native trace shell by the accepted typed bijection.

Let `G=Sym({1,2,3}) ~= S_3 ~= D_3`. A native frame is an ordered triple `f=(i,j,k)` of the three axes. The six frames form a free transitive `G`-set `F`; choosing one frame is presentation/N1 data.

For fixed `n>=1`, `f=(i,j,k)`, and `0<=t<n`, define three half-open sector blocks:

- `x_(0,t)[i]=n-t`, `x_(0,t)[j]=t`, `x_(0,t)[k]=0`;
- `x_(1,t)[i]=0`, `x_(1,t)[j]=n-t`, `x_(1,t)[k]=t`;
- `x_(2,t)[i]=t`, `x_(2,t)[j]=0`, `x_(2,t)[k]=n-t`.

They are disjoint and cover `A_n`. Put `p_f(x_(b,t))=bn+t`.

Let
`C_n=1+3n(n-1)/2`
and define
`lambda_f(x)=C_n+p_f(x)` for `x in A_n`.

The allocation object is the equivariant family
`Lambda:F x A^+ -> N_{>0}`,
not one primitive pointwise map. Its members are `L={lambda_f:f in F}`.

## 3. Exact grade/gap theorem

For each frame `f`, `p_f:A_n->{0,...,3n-1}` is a bijection, because the three half-open native arcs each contain exactly `n` states and count shared axis-boundary states once.

Also
`C_(n+1)=C_n+3n`.
Hence shell `n` receives exactly
`I_n={C_n,...,C_n+3n-1}`
`={1+3n(n-1)/2,...,3n(n+1)/2}`,
the intervals are consecutive, and `lambda_f:A^+->N_{>0}` is a strictly grade-monotone global bijection.

Conversely, any global bijection to positive integers that places every lower grade before every higher grade must assign exactly these intervals. Thus gap-freeness is forced by global bijection plus strict grade monotonicity; it is not a separate axiom.

## 4. Equivariance and uniqueness up to frame

For `g in G`, acting by coordinate relabeling and by `g.(i,j,k)=(g(i),g(j),g(k))`,
the block formulas give exactly

`p_(g f)(g x)=p_f(x)`,
`lambda_(g f)(g x)=lambda_f(x)`.

The map `f -> lambda_f` is injective already on shell `1`, so `L` is itself a `G`-torsor.

Moreover, for a fixed frame, the following four requirements uniquely force `lambda_f`:

1. global bijection to positive integers;
2. strict grade monotonicity;
3. adjacency/order preservation along the three native sector arcs;
4. cut only at a native axis boundary, with one of the two native orientations.

Therefore the admissible family is exactly the six torsor members, not an arbitrary enumeration class.

## 5. Exact pointwise definability obstruction

No `G`-invariant injective scalar map `ell:A^+->N_{>0}` exists when `G` acts trivially on the scalar codomain.

Take the cyclic relabeling `rho=(123)` and `x=(n,0,0)`. Then `rho x=(0,n,0) != x`. A frame-independent Foundation-definable scalar would satisfy `ell(rho x)=ell(x)`, contradicting injectivity.

Equivalently, on the same N0 shell take frames
`f=(1,2,3)` and `f'=(2,3,1)`. For the same state `x=(n,0,0)`,

`lambda_f(x)=C_n`,
`lambda_(f')(x)=C_n+2n`.

The two framed presentations have the same frame-free Foundation reduct but disagree pointwise. This is an exact NSA-02/NSA-13 obstruction at scalar pointwise strength.

## 6. Orbit-readout descent theorem

If `O subset A_n` is `G`-invariant, define
`L_f(O)={lambda_f(x):x in O}`.
For `f'=g f`,

`L_(f')(O)=L_f(g^-1 O)=L_f(O)`.

Therefore any `G`-invariant native orbit has a frame-independent integer label set/multiset, and every symmetric scalar function of that label multiset also descends.

Freeze:

`G_INVARIANT_NATIVE_ORBIT -> FRAME_INVARIANT_INTEGER_LABEL_SET`.

This is exactly quotient/torsor strength; it does not promote individual labels.

## 7. Balance packet consequence

For even shell `n=2m`, the accepted balance orbit is
`O_m={(m,m,0),(0,m,m),(m,0,m)}`.
In frame `(1,2,3)` its positions are `m,3m,5m`. Since
`C_(2m)=6m^2-3m+1`,
the descended label set is exactly

`{6m^2-2m+1, 6m^2+1, 6m^2+2m+1}`.

Thus the parent result's conditional packet is now an exact torsor-descended N2 set-valued readout. No distinguished physical lane is required.

This task does not promote any downstream divisibility, prime, breaker, or capacity theorem. It only discharges their allocation-semantic dependency when their input is genuinely a `G`-invariant set/multiset/symmetric readout.

## 8. Admissibility and anti-circularity ledger

Native inputs used: shell/address structure, `|A_n|=3n`, three-sector gluing, native axis relabeling, integer coordinates/ticks, and cumulative shell counts.

Typing:

- frame space/allocation torsor/equivariant family: `N0_DEFINABLE_DERIVED`;
- a selected `lambda_f`: `CONDITIONAL_DERIVED` on one N1 frame choice;
- invariant orbit label sets: `READOUT_ONLY` at N2 set/multiset/scalar strength;
- pointwise intrinsic scalar label: `SEMANTIC_MISMATCH`, exactly obstructed.

No downstream arithmetic target is used as premise. The balance packet is evaluated only after the torsor theorem is frozen.

## 9. Weakest extra structure

No additional Foundation axiom is required for the allocation torsor or invariant orbit readouts.

A distinguished pointwise labeling requires exactly one extra datum: one global frame `f in F`, i.e. a starting native axis and an orientation. Its ontology cost is one point of a six-element `D_3` torsor.

Freeze:

`MINIMAL_POINTWISE_EXTRA_STRUCTURE = GLOBAL_NATIVE_FRAME_SELECTOR`.
`ONTOLOGY_COST = ONE_D3_TORSOR_POINT`.

Such a selector is legitimate N1/presentation data. Promoting it to intrinsic N0 would break the admitted native relabeling symmetry and is not justified here.

## 10. Parent consequence map

Before this audit:

`native shell support + OPEN allocation law -> conditional frame-invariant packet`.

After this audit:

`native shell support -> derived allocation torsor -> exact frame-invariant orbit label readouts`.

Hence `B_n=C_n` is the forced shell-interval start in every torsor member; the even C3 balance packet descends exactly; named physical lanes and individual point labels remain non-definable; downstream theorems using only invariant set/multiset/symmetric inputs no longer need an extra allocation axiom at that readout strength.

Foundation remains unchanged.

## 11. Regression certificate

The task-local checker exhausts shells `1<=n<=64`, all six frames, and all six axis permutations:

- shell states checked: `6240`;
- shell/frame bijection checks: `384`;
- equivariance point checks: `224640`;
- even balance-packet/frame checks: `192`.

Finite computation is regression only. The general proof is the exact block decomposition, interval recurrence, and group-equivariance argument above.

## 12. Final freeze

`PRIMARY_VERDICT = DERIVED_WEAKER_TORSOR_ALLOCATION`.
`HARD_TARGET = ACHIEVED_AT_TORSOR/QUOTIENT_STRENGTH`.
`POINTWISE_SINGLE_VALUE = EXACTLY_OBSTRUCTED`.
`FRAME_INVARIANT_ARITHMETIC_DESCENT = PROVED_FOR_G_INVARIANT_ORBITS_AND_SYMMETRIC_READOUTS`.
`FOUNDATION = UNCHANGED`.

Recommended Driver action: accept the torsor result, do not promote a distinguished frame, and audit downstream integrations separately at the exact invariant readout strength they consume.
