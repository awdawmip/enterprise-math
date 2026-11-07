# R5 — Saturated-v six-real-parameter Blackwell lift by a common seedless affine face

Date: 2026-11-08 (Asia/Shanghai). Provenance: author-side mathematical proof and exact rational local execution; independent review and native admission pending. Immediate verified scientific predecessor: `b81bef5b83e0c43d9f40c6e43740c0ae36c8ea19:research_notes/brc_r5_full_source_side_rectangle_20261108_t0240/{RESEARCH.md,VERIFY.py}`. Frozen scientific pins unchanged: global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Source-current normative rules were read separately from these science pins.

## Model and six-parameter theorem

Use the frozen four-stage seven-key P/Q-BRC likelihood carrier
`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)` and flow coordinates
`f=(g,a,b,u,v,w,z)`. A legal FULL_HIST real flow obeys
`0<=a,b<=g<=1`,
`0<=u<=13a/40+b/80`,
`0<=w<=3a/40+21b/80`,
`0<=z<=a/10`,
`0<=v-z<=9b/40`.
The seedless LR condition is `R(f)=9bz-4a(v-z)=0`. The seven Q stopping masses `M_j(f)` and stop times `T_P(f),T_Q(f)` are the affine functions in the copied frozen predecessor `BASE_CERTIFICATES.py`. For a seven-key randomized declaration `d in [0,1]^7`, let
`e_Q=sum M_j(f)d_j`,
`1-e_P=sum r_j M_j(f)d_j`.

**Theorem.** For every real
`0<=s<=g<=1`, `p,q,theta,h in [0,1]`, let
`U=53/160`, `W=33/160`, `u=s U p`, `w=s W q`, `z=s theta/10`, and
`x=(g,s,s/2,u,9s/80+z,w,z)`.
There is a **single legal seedless LR flow** `y=y(g,s,p,q,theta)` and one calibrated nonnegative `7x7` Blackwell Q-mass transport independent of declaration, such that **every** seven-key declaration of both `x` and `x_h=(1-h)x+h y` admits a seedless randomized declaration exactly matching the full four-observer tuple
`(e_P,e_Q,T_P,T_Q)`.

The source `x` covers the entire side capacities `0<=u<=53s/160`, `0<=w<=33s/160` for this scaled `a=s,b=s/2` family and the complete saturated-v interval `0<=z<=s/10`. Its exact structure is
`v-z=9b/40=9s/80`,
`R(x)=(9s/2)(z-s/10)<=0`,
`T_P(x)=1+g+4s/5+u/2+3w/2+z`,
`T_Q(x)=1+g+69s/80+u+w+z`.
At `s=0`, the construction is defined without division and gives the seedless `x=(g,0,0,0,0,0,0)`.

## Complete all-real proof

The immutable predecessor provides for the four indices `ij in {00,10,01,11}` the sources
`c_ij=(1,1,1/2,iU,9/80,jW,0)`, four legal seedless targets `y_ij` in the *common affine face*
`F={legal f: z=a/10, v-z=9b/40}`,
and four explicit rational nonnegative matrices `Q_ij`. For every `i,j,k`,
`sum_k Q_ij[i,k]=M_i(y_ij)`,
`sum_i Q_ij[i,k]=M_k(c_ij)`, and
`sum_i r_i Q_ij[i,k]=r_k M_k(c_ij)`;
also `T_P,T_Q` match on each source-target pair. `BASE_CERTIFICATES.py` is copied from that immutable exact-certificate source and reproduces its four matrices.

Define the legal **seedless positive-z corners**
`c_ij^+=c_ij+(0,0,0,0,1/10,0,1/10)`. Each belongs to `F` and has an identity transport `diag(M(c_ij^+))`. The baseline flows `E_0=(0,0,0,0,0,0,0)` and `E_1=(1,0,0,0,0,0,0)` likewise belong to `F`, are seedless, and have identity transports. Their Q/P stopping measures are normalized.

Set bilinear weights
`lambda_00=(1-p)(1-q)`, `lambda_10=p(1-q)`, `lambda_01=(1-p)q`, `lambda_11=pq`.
All are nonnegative and sum to 1. The following weights are nonnegative and sum exactly to 1:
`1-g`, `g-s`, and, for each `ij`,
`s lambda_ij (1-theta)` and `s lambda_ij theta`.

By direct coordinate comparison the convex combination of the input flows with these weights is *exactly* `x`. Replace every source `c_ij` by its prior target `y_ij`, and retain `E_0,E_1,c_ij^+` as their own targets. Call the resulting combination `y`. Because **every target lies on the same affine seedless face F**, `y` is legal and satisfies `R(y)=0` for all real parameters, including irrational parameters and boundaries. Affineness of both stopping-time functions and the corner stop-time identities prove `(T_P,T_Q)(y)=(T_P,T_Q)(x)`.

Form `Q` using the *identical nonnegative weights* on `diag(M(E_0)),diag(M(E_1)),Q_ij,diag(M(c_ij^+))`. Every Q-mass equation is linear and therefore survives the convex combination:
`sum_k Q[i,k]=M_i(y)`,
`sum_i Q[i,k]=M_k(x)`,
`sum_i r_i Q[i,k]=r_k M_k(x)`.
The affine stopping masses have constant terms, but weights sum to one, so they also interpolate exactly. Set `Q_h=(1-h)Q+h diag(M(y))`. Its rows remain `M(y)` and its calibrated Q/P columns become the masses of `x_h=(1-h)x+h y`. Both time functionals also match.

Normalize every positive row of `Q_h` to `K_h[i,k]=Q_h[i,k]/M_i(y)`; use any stochastic row when `M_i(y)=0`. Then for every real `d in [0,1]^7`, `d'=K_hd` is a declaration in `[0,1]^7` and yields exactly
`sum_i M_i(y)d'_i=sum_k M_k(x_h)d_k` and
`sum_i r_i M_i(y)d'_i=sum_k r_k M_k(x_h)d_k`.
The stop-time identities complete the six-parameter all-real proof.

The construction uses **positive BRC branch mass and explicit seven-key provenance**. Its compression certificate is sufficient for the four stated observers and randomized terminal declaration, with original flow retained as a separate source object.

## New exact interior/capacity witness

For `g=s=p=q=1`, `theta=1/2`, `h=0`, the source and target are
`x=(1,1,1/2,53/160,13/80,33/160,1/20)`,
`y=(39/40,39/40,21/40,207/640,69/320,119/640,39/400)`.
The common times are `(133/40,69/20)`, and source residual is `-9/40`, while `R(y)=0`. Both source side-flow capacities are saturated and `z>0`, in contrast with the immediate predecessor's `z=0,g=s=1` source family.

## Executed verification and limits

`VERIFY.py` imports `BASE_CERTIFICATES.py` to check all four prior full rational matrices, then exactly checks **729** rational cases across `g,s,p,q,theta,h` (3 choices per variable, with `s=0,g/2,g`), the eight flow legality and seedless identities, 7 row masses, 7 Q columns, 7 P-weighted columns, both stopping times, nonnegative matrix entries, and three declarations per case. It executes standard-library Python `Fraction` only. A locally executed reproduction of the frozen predecessor and new checker yielded `PASS_R5_SATURATED_V_SIX_PARAMETER_ALL_REAL_AFFINE_FACE_LIFT`; the captured `EXACT_OUTPUT.txt` is that local reproduction's stdout. The exact all-real conclusion is the algebraic convex proof above plus the four inherited explicit rational corner certificates, not extrapolation from 729 grid points.

The locally executed predecessor file has harmless formatting differences from the verbatim remote `BASE_CERTIFICATES.py`; no byte-identical local/remote execution-source assertion is made. Source readback certifies publication of the independently inspectable verification program, not remote execution.

## Next unit

The present theorem handles the full saturated-v strip for `b=a/2`, while prior R5 work handles another strip at `b=a`. Seek a joint affine-face interpolation bridging intermediate `a/2<b<a`, or test unsaturated `v-z<9b/40` with the same calibrated transport method. Preserve exact S/Q mass formulas and obtain a rational certificate or scoped dual infeasibility witness. Global four-observer FULL_HIST vs seedless LR pointwise equality remains the mother problem.

Native owner/claim check this run: status/task tools returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`, and Site gateway reported `research_authority_granted=false`. Research and publication here are author-side `PORTABLE_ONLY / UNREVIEWED / NOT_ADMITTED`.
