# R5: Five-vertex exposed-facet veto for two ordered LR decisions

Date: 2026-10-29 Asia/Shanghai. Author-side portable mathematical research.
Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.

## Sources and exact scope

Frozen account GLOBAL_KNOWLEDGE_V1 `main@116f066ea7bb9a66d122c63645c7310acc5b89f8`; Enterprise Math `main@9085a8bd7842858d679d29c9305c6993cdcb2fd0`. Read account normative bootstrap/manual, Enterprise Math project/TASK router, P000, ACTIVE worldview, project AGENTS.md, active portable protocol and joint-observer constraint. Scientific predecessor is `research_notes/brc_r5_exposed_simplex_veto_20261029_t1935/RESEARCH.md` at immutable commit `d4784b99d0b2c1684c9994f51fba8fb3ecd492d9`. Native authority read: `research_authority_granted=false`; current owner inventory returned `CONTROL_QUOTA` (5/5 jobs). No formal Source CLAIM, Result or independent review is inferred.

Mathematical scope: an **external finite, two-law, strictly absorbing stop/continue decision tree**, with FULL perfect recall and seedless LR behavioral policies keyed by exact time and likelihood ratio. Observer `O=(e_P,e_Q,T_P,T_Q) in R^4`. No X6 embedding, native physics, BRC-Shor arithmetic, or physical time assertion. BRC provenance discipline: preserve ordered history and source-labeled positive P/Q path masses until the observer-relevant via-key/bypass-key distinction is used; signed differences below are differences of legal observer vectors, never negative probability.

## New theorem: one additional facet vertex does not repair both FULL bypass witnesses

Fix two different time-ordered LR keys `k=(t,r)`, `l=(s,r')`, `t<s`. At both choose action 0 = a fixed absorbing stop/declaration, action 1 = continue; hold all other deterministic LR actions fixed. Let `V_ij` be the four deterministic LR observer vectors for actions `(i,j)` at `(k,l)`, and write

`A=V_00, B=V_01, C=V_10, D=V_11`.

Assume (i) these four vectors are affinely independent, (ii) they are distinct **extreme vertices** of the same three-dimensional exposed face `F` of the complete deterministic LR observer hull `C_LR`, and (iii) `F` has **at most five extreme vertices in total**. Then

`conv(O_FULL) != conv(O_LR)`.

For rational model and rational exposing normal, an explicit **rational all-real LR separating inequality** and a positive L-infinity distance bound can be constructed. In particular, if an interacting two-key candidate truly has equal FULL/LR hulls, every such exposed three-dimensional face must have at least **six** extreme LR vertices.

### Step 1: both bypass vectors are genuine deterministic FULL observations

The fixed-action rectangle has the exact multi-affine form

`O_LR(x,y)=C0+U*x+B0*y+A0*x*y`, `x,y in [0,1]`.

Here the `B0` term comes from histories that reach `l` **without** visiting `k`, while `A0` is the additional action contrast on histories going **via** `k`. Absorbing stop at `k` forbids a via-k visit to `l` under action 0.

FULL remembers whether `k` was visited. With `k=continue`, set the action at `l` to continue on via-k histories and stop on bypass-k histories to obtain

`H1=A+D-B=(1,-1,0,1)` in barycentric coordinates relative to `(A,B,C,D)`.

Reverse the two decisions at `l` to obtain the second legal FULL observer

`H2=C+B-A=(-1,1,1,0)` in the same barycentric system.

Because all four corner points lie on the exposing hyperplane `w·z=h`, so do `H1,H2`. If either is outside `F`, it is outside the entire LR hull.

### Step 2: exact four-case rational separator for a fifth vertex

Let `ell_A,ell_B,ell_C,ell_D` be the affine barycentric coordinate functionals on the three-dimensional affine hull of `F`. Every `ell_i` is nonnegative on the tetrahedron `conv(A,B,C,D)`, and their sum is 1.

When `F` has a fifth vertex `E`, write its barycentric coordinates `(a,b,c,d)`, satisfying `a+b+c+d=1`. Exactly one of the following gives an affine form `L` nonnegative at **all five** vertices and equal to **-1** at one FULL witness:

1. `b>=0`: `L=ell_B`, `L(H1)=-1`.
2. `b<0, c>0`: `L=ell_B-(b/c)ell_C`, `L(E)=0`, `L(H1)=-1`.
3. `b<0, c<=0, a>=0`: `L=ell_A`, `L(H2)=-1`.
4. `b<0, c<=0, a<0`: `d=1-a-b-c>0`; `L=ell_A-(a/d)ell_D`, `L(E)=0`, `L(H2)=-1`.

All coefficients of the `ell_i` in `L` are nonnegative, so the four original corners satisfy `L>=0`. This case partition covers **every real fifth vertex E**; with rational corners and E every coefficient is rational. If there is no fifth vertex, `ell_B` already separates H1.

Thus even one arbitrary extra LR facet vertex cannot simultaneously absorb both legal FULL split observations. This strengthens the previous four-corner simplex veto to **five-vertex facets** without enumerating their faces.

### Step 3: extend a face separator to the complete LR polytope

For rational data, choose a rational affine extension of `L` from `aff(F)` to all of R4. Let `w·z>=h` expose `F`; enumerate all deterministic LR observation vertices outside `F` and set

`M=max(0, max_{q off F}[-L(q)/(w·q-h)])`.

Empty maximum is 0. Every denominator `w·q-h` is strictly positive. The exact rational affine inequality

`Phi(z)=L(z)+M(w·z-h)>=0`

holds for **every** deterministic LR vertex. Seedless LR behavioral outputs are multi-affine convex combinations of deterministic LR outputs (time-labelled keys occur at most once per trajectory), so the inequality holds for **all real** seedless LR policies. The selected FULL witness H satisfies `Phi(H)=-1`. If `n` is the linear normal of `Phi`, the L-infinity observer distance to the LR set is at least `1/||n||_1>0`.

### Step 4: minimum six is sharp as abstract affine geometry

Take observer-coordinates `(x,y,z)` with corners `A=(0,0,0)`, `B=(1,0,0)`, `C=(0,1,0)`, `D=(0,0,1)`. Then `H1=(-1,0,1)`, `H2=(1,1,0)`. All six points `A,B,C,D,H1,H2` are distinct extreme vertices of their 3D convex hull; the two split points are obviously inside this six-vertex hull. Hence the bound of six cannot be increased by affine geometry alone. This is an **abstract exact polyhedral example**, not a two-law stopping realization or a mother counterexample.

For an explicit rational off-face extension example, add `q=(10,0,0,1)` to the 4D LR convex hull with facet `t=0` and its five vertices `A,B,C,D,H1`. The affine rational separator for `H2=(1,1,0,0)` is

`Phi(x,y,z,t)=1-x-y-z+9t >= 0`.

It equals -1 at H2; the L-infinity distance is at least `1/(1+1+1+9)=1/12`. The example is only an exact polyhedral certificate illustration.

## Verification, novelty, limitations

Executed standard-library Python `Fraction` verifier (`VERIFY.py`) exhaustively over **2197** rational fifth-vertex barycentric choices `a,b,c in {-3,-5/2,...,3}`, `d=1-a-b-c`: each of four separator formulas is nonnegative on all five LR vertices and exactly -1 at its chosen FULL witness. Checked six strict vertex-exposing linear witnesses for the sharp abstract example and `M=9` off-face penalty, producing the attached actual `EXACT_OUTPUT.txt`. The **all-real result is proved by the four exhaustive algebraic cases, not inferred from the finite grid**.

This paper supplies a **new conditional structural no-go** relative to R5's preceding four-vertex theorem. It does not classify all exposed faces with six or more LR vertices, does not verify a concrete source-sensitive two-merger stopping model, and does not resolve the mother problem. External novelty priority and native X6 transfer are not claimed. No independent Source reviewer or formal proof assistant checked this result.

## Next exact mathematical unit

In a genuine exact-collision, source-sensitive interacting two-merger DAG, compute all deterministic LR observer vectors. For every exposed 3-face containing a rank-three time-ordered LR rectangle, **discard facets with <=5 extreme vertices** using the explicit rational two-coordinate separator. For any remaining face with >=6 LR vertices, solve the two exact rational convex-combination feasibility systems `H1,H2 in F`. If either fails, return the primal-dual (Farkas) separator; if both pass and ALL signed hull containment passes, then test actual seedless LR real-behavioral nonmembership using semialgebraic equations including zero-flow boundaries. Preserve positive P/Q origin/path masses and both exact LR collision equations throughout.
