# R5: a nine-dimensional physical 15-edge chamber and an eight-dimensional 14-edge boundary facet

Date: 2026-11-10 Asia/Shanghai. Status: AUTHOR EXACT-RATIONAL PROOF / INDEPENDENT MATHEMATICAL REVIEW PENDING. **Frozen science unchanged:** GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.

## Precise inputs and provenance

Re-use the seven-likelihood-ratio P/Q–BRC auxiliary model with likelihood ratios `(1/10,1/2,3/4,1,5/4,3/2,19/10)` and the 14-coordinate lawful FULL_HIST source / seedless-F target physical pair of immutable PR #1902 `684ded4d951a0f1b8d314a421b29c39dd1afee64`. The center `p0`, rational physical mass/capacity/stop-time maps, and eight directions `P` are re-derived in `FIBER_CERTIFICATE.py`. The latter is the RREF nullspace basis columns numbered `(0,1,2,4,5,6,7,8)` of the five equalities, exactly as in PR #1923 and immutable PR #1927 `602a8349cb777d9afab1ca8e2822718a05394726`. Preserve the original global/EM scientific pins, P000 and owner/source firewall. The seven likelihood-ratio labels do **not** denote the six P000 native spatial axes.

From PR #1927, author-side exact finite checking proves that every eight-dimensional real `t` with `||t||_infty<rho_*=23/17050000` has a strictly positive 15-edge Blackwell coupling and none with 14 or fewer edges. Its proof enumerates all `binom(20,4)=4845` candidate 14-edge supports after ten dual-forced positive edges. At the corner `t_*=(0,0,0,-rho_*,rho_*,0,0,-rho_*)` it constructs 14 positive edges and excludes all `binom(20,3)=1140` candidate 13-edge supports. These are **inherited exact-source dependencies**, not new findings in this note. Their author-side proof remains pending independent scientific review.

## New Lemma — genuine BRC observer-fiber residual

Write `J_c` for the 5x14 physical equality Jacobian, `J_b` for the 21x14 Blackwell mass/moment right-hand-side Jacobian and `P` for the 14x8 frozen tangent chart. Set
```text
K=(-98800,-98800,-98800,-33345,264290,-33345,591026,
      0,0,0,0,0,0,0).
```
Exact rational differentiation establishes
```text
J_c*K=0 (5 rows),  J_b*K=0 (21 rows),
rank([P|K])=9,    rank(J_b*P)=8.
```
Consequently the complete five-equality physical affine space is nine-dimensional and the Blackwell statistical observer has an exact one-dimensional invisible flow fiber. For arbitrary real `s,t`,
```text
b(p0+P*t+s*K) = b(p0+P*t).
```
The claim is explicitly about this particular 21-component observer and preserved stopping-time maps; it retains the physical flow/provenance coordinate `s` rather than identifying it with zero.

## NEW Theorem 1 — a nine-dimensional real neighborhood where every point needs 15 edges

Set
```text
rho=23/34100000,
sigma=6177/612560000000,
p(t,s)=p0+P*t+s*K.
```
For **all real** `|t_k|<=rho` (eight coordinates) and `|s|<=sigma`, all five physical equalities and all 26 source/target capacity inequalities hold. Every such physical pair admits an exact Blackwell coupling with exactly 15 positive edges; no coupling with <=14 positive edges exists. Since `rank([P|K])=9`, the open interior is a genuinely **nine-dimensional region of lawful physical strategies with exactly 15-edge minimum support**, projecting onto the previously verified eight-dimensional statistical chamber.

Proof of continuum physical capacity: all slack functions are affine; write `S=J_slack P` and `k=J_slack K`. For each slack `i`,
```text
slack_i(t,s) >= slack_i(0) - rho * sum_k |S[i,k]| - sigma*|k[i]|.
```
For the center's structural zero-slack indices `(4,15,23)`, all relevant derivatives vanish. All remaining 23 exact rational lower bounds are nonnegative. The active bound is source slack index 2 with residual `6177/6200000`, derivative `|k[2]|=98800`, giving precisely `sigma=6177/612560000000`. Source `FIBER_CERTIFICATE.py` checks each inequality with exact rationals. Because `J_b K=0`, every 15-edge existence/exclusion certificate from immutable PR #1927 applies without change at every `s`.

## NEW Theorem 2 — an eight-dimensional physical facet of exactly 14-edge strategies

Let `t_*` be the exact 14-edge corner above and set
```text
delta = 63/151745000,
sigma_face = 2961/585640859375,
q_4/80 - q_5 + 13*q_8/4 = 0,   ||q||_infty <= delta,
p_face(q,s)=p0+P*(t_*+q)+s*K, |s|<=sigma_face.
```
Coordinates on the `q` equation are one-based. Its left-hand side is the exact gradient of `mu_1` at `t_*`; `mu_1(t_*+q)=0`. Every such pair is physically lawful. The explicit PR #1927 15-edge affine basis has weight `E_(1,3)=mu_1=0` and the other fourteen weights strictly positive on this small face. By exact 1,140-case 13-edge exclusions and their positive cofactor separation in the `q` neighborhood, its **minimum support is 14**. The eight-dimensional physical facet consists of the seven-dimensional `q` hyperplane and the independent `K` fiber.

Proof of capacity: the zero slack indices at the center of this face are `(4,15,19,23)`; their `K` derivatives vanish, while slack 19's `q` derivative is the displayed `mu_1` gradient and therefore also vanishes on the facet. Every other slack obeys the exact lower bound
```text
slack_i(p_face)>=slack_i(p(t_*))-
     delta*sum_k|S[i,k]|-sigma_face*|k[i]| >= 0.
```
The displayed `sigma_face` is half the smallest positive remaining-slack-over-fiber-derivative ratio and the exact verifier checks it. Independent local exact cofactor enumeration recorded **1,031** 14-edge spans passing through `t_*` (all enforce `mu_1=0`), **3,814** remaining 14-edge spans excluded, and **all 1,140** <=13-edge candidates excluded. The positive guaranteed `q`-separation radius for the excluded spans is `49948501046391/3920403670319950000`, greater than `delta`.

## Evidence and outstanding work

`FIBER_CERTIFICATE.py` is a self-contained SymPy `Matrix` / Python `Fraction` exact-rational verifier of all new 9D kernel/rank and 26-capacity assertions; `FIBER_CERTIFICATE_OUTPUT.txt` reproduces the actually executed local rational validation of the same formulas. Predecessor finite 4,845/1,140 support exclusion is in immutable PR #1927. The supplementary local independent `VERIFY_FACET.py`/ `EXACT_FACET_OUTPUT.txt` were executed to inspect 1,031+3,814+1,140 spans; formal independently reviewed mathematical admission is still pending.

One observed reproducibility defect: PR #1927 `FACE_TRANSITION.py` references variables `model["EB"]` and `model["DeltaB"]`, while `VERIFY_SHARP.py` defines `eb` and `db`. Do not represent its current published facet verifier as successfully executed until repaired; independent local calculations above were used instead. This new proof/article is a non-operational, author-side scientific artifact and grants no formal R5 Owner, CLAIM, Result/Review admission, or Foundation promotion.

**Next independent study:** Solve the *maximal* one-dimensional fiber over each eight-dimensional `t` by intersecting the exact 26 affine physical half-spaces. The resulting interval endpoints `s_-(t),s_+(t)` are rational piecewise-affine functions; classify their active capacities and relation to the 14/15-edge marginal stratification without collapsing BRC flow residuals.
