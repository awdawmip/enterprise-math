# Enterprise Math R5 — Exact all-real ingress-projection no-go

Date: 2026-11-01 (Asia/Shanghai). Author-side portable research; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is an auxiliary finite P/Q stopping-model result, not a theorem about native X6, the HEARTBEAT_WORLD, or empirical physics.

## Immutable sources and permissions

Global Knowledge canonical `main@ae1c9380c450555df6302dfe5ad4d58c053e9196`; Enterprise Math canonical `main@9412897fb2b8e77bb30ee26391fb65edaba2a8fd`. Read the global bootstrap/manual, ACTIVE worldview, project P000 and joint-observer-preservation and heartbeat contracts, current project `AGENTS.md`, the autonomous and portable research protocols, and the predecessor source at immutable author commit `2c74c9ed4995eeb87bf3f1d46c25847904884a11` (`research_notes/brc_r5_route_ingress_projection_20261101_t0140/{RESEARCH.md,VERIFY.py,NEXT_TASK.md}`). P000/ACTIVE worldview remain untouched. Identity is the present research author; GitHub connector login `awdawmip` identifies repository access, **not** a native researcher session. This turn's native status gave `research_authority_granted=false`, `executor_binding_configured=false`, `CODE_REVIEW_REQUIRED`, active job quota 5/5; bounded owner query returned `CONTROL_QUOTA`. No current owner, CLAIM, Result or Driver admission was authenticated.

## Carrier, observers and precise question

Reuse the predecessor's 12 *route-labelled* terminal Q masses in the order `(A,D,Y,C,DH,YH,LD,LY,LC,L4D,L4Y,L4C)`; recover P masses with per-leaf likelihood ratios `(1,1/2,3/2,1,1/4,2,1,1,1,1,1,1)`. Each of the two hidden origins starts with P=Q mass 1/2. Origin parameters are `(alpha0,kappa0)=(1/4,3/4)` and `(alpha1,kappa1)=(1/5,1/6)`, both with theta=11/2. Source i continuing at A produces D,Y,C with respective Q fractions `alpha_i,alpha_i,1-2alpha_i`. D CONTINUE sends 2/3 to DH and 1/3 to L; Y CONTINUE sends 1/2 to YH and 1/2 to L; C reaches L with probability kappa_i. Shared LR action L can only see the *common* time-likelihood key, not ingress. FULL has six binary action keys per source `(A,D,Y,LD,LY,LC)`, hence 4096 deterministic corners; LR has four common keys `(A,D,Y,L)`, hence 16. Every trajectory visits each action key at most once.

Preserve labelled flows to compute `x=Q(DH)`, `u=Q(YH)`, `t=T_Q`, `y=Q(L4D)+Q(L4Y)+Q(L4C)`, `c=Q(LC)`. The question is, **for which real q** are the FULL and seedless LR convex hulls of the four-coordinate readout `V_q=(x,u,t,y+q*c)` equal, and does the LR image have affine rank four? Projecting to `V_q` intentionally erases ingress detail for this finite observer only; the full route-labelled positive-rational carrier remains available for future observations. BRC use: exact positive branch masses, labelled ports and the observer/kernel audit, not native BRC arithmetic or X6 realization. Signed support coefficients are dual tests, not negative physical probabilities.

## Theorem (complete real-q classification)

For **every real q**, the LR four-coordinate observation convex hull has affine dimension **four**, and

`conv(V_q(FULL)) != conv(V_q(LR))`.

Consequently **no real q** in this one-parameter ingress-sensitive projection family can solve the mother problem requiring full four-dimensional convex-hull equality plus unequal actual real behavioral images.

### Exact rank witness

In the lexicographic LR bit order `(A,D,Y,L)`, take indices `(0,9,10,13,14)`. The 4×4 determinant of differences of these five observed vertices, with vertex 0 as base, equals

`8019/5120000 != 0` **for every real q**.

Indeed each row has first three coordinates independent of q and a last coordinate affine in q. Thus the determinant is affine in q; its exact values at q=0 and q=1 both equal `8019/5120000`. This proves rank four for the entire real line, including potential singular projection parameters.

### Three exhaustive parametric separating certificates

Write `s=y+q*c`. Each row below gives `H_q(x,u,t,s) <= b(q)` for **every LR deterministic vertex** on the stated interval. Its specified FULL deterministic witness has positive slack `H_q(V_q)-b(q)`. The bit strings are in per-source order `(A,D,Y,LD,LY,LC)`, first source followed by second.

| Region | LR-valid score `H_q` | `b(q)` | FULL bits | Exact positive slack |
| --- | --- | --- | --- | --- |
| **A:** `q <= 99/118` | `-21x -61u -19t +118s` | `-19` | `111111000000` | `11/2` |
| **B:** `99/118 <= q <= 2772/2413` | `(-891+684q)x+(-5544+5510q)u-342qt+1782s` | `-342q` | `111110000000` | `(3034q-1881)/8`, at the left endpoint `9801/118>0` |
| **C:** `q >= 2772/2413` | `(3360-3040q)x+(4480-3040q)u+(-2240+1520q)t+2240s` | `-5012+3933q` | `101010111110` | `171q`, at the right endpoint `24948/127>0` |

These regions cover `R` without gaps. For each certificate, the listed LR face indices are, respectively, `A:(0,9,11,13)`, `B:(0,8,11,15)`, `C:(8,10,11,15)`; their LR slacks vanish identically for all q. For any one of the other 16 LR vertices, the slack is **affine in q**, because the coefficient of `s` in each H is constant and all other readout coordinates are independent of q. Accordingly: in region A, its slope is nonnegative and its value at q=99/118 is nonpositive; in region B, its values at *both* endpoints are nonpositive; in region C, its slope is nonpositive and its value at q=2772/2413 is nonpositive. These are finitely many exact rational inequalities, independently checked for all 16 LR corners in `VERIFY.py`. No finite grid extrapolation occurs.

By construction, the three FULL witnesses yield the displayed strictly positive real-q slacks. Each is a feasible FULL corner; the LR hull lies in the corresponding closed halfspace. Therefore the two convex hulls are different for all q. Because each action key occurs at most once per trajectory, the observation is multi-affine in the local behavioral probabilities. Every real behavioral observation is a convex combination of deterministic corners; linear support on the LR behavioral set is therefore bounded by its 16 deterministic corners. This proves the theorem for **all real behavioral policies**, not just pure strategies.

## Verification and limits

`VERIFY.py` uses only Python 3 standard-library `fractions.Fraction`. The executed source verifies all 4096 FULL and 16 LR terminal mass P/Q normalizations, three all-real interval support certificates (symbolic affine slopes/endpoint tests for every LR vertex), exact FULL bits and their symbolic positive gaps, four symbolic LR face identities per certificate, and the all-real constant nonzero minor (q=0,1,2 arithmetic regression). Actual output is `EXACT_OUTPUT.txt`; terminal marker `PASS_EXACT_R5_INGRESS_Q_ALL_REAL_NO_GO`.

This completes the parameter question posed in the predecessor's `NEXT_TASK.md`. No claim is made about the full family of ingress-dependent terminal Bernoulli responses, the equality/inequality of actual real behavioral sets at a different four-observer readout, or native X6 correspondence. Independent mathematical review and native registration remain open.

## Next precise unit

This readout family is fully excluded. Preserve all 12 port-labelled masses, and study *two* independent ingress contrasts, e.g. `s_{q,r}=Q(L4D)+Q(L4Y)+Q(L4C)+qQ(LC)+rQ(LD)` or a different path-derived fourth observer. Before any new parameter search, determine exact affine rank of the five/six-dimensional joint carrier and identify which parameterized observer kernels preserve the 3D LR-hull fibers. Seek either an all-parameter separating certificate or exact <=5-LR-vertex convex combinations for all FULL vertices together with rank four. Only after four-hull equality consider semialgebraic nonmembership of the actual real LR behavioral image. An independent reviewer should first rerun the present `VERIFY.py` and adversarially check the three interval end points and rank minor.
