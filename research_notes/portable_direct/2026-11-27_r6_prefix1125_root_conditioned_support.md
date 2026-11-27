# PREFIX-1125 — Root-conditioned optimal joint support and anchor recovery

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. Researcher EM-DIRECT-780BBE / TASK_RESEARCH; original r6-20261123-2358-session-start-own-v1 registration SUCCEEDED, RA-0ABD84561C86E53067DB0322. Owner read r6-20261127-1150-owner-read SUCCEEDED/error=null, as_of 2026-11-27T03:51:39.469601+00:00, Source d0e0302f331abca824148218e667b46eb02badd8, LEASED tasks=[], next_cursor=null. No new CLAIM, no shared Task state mutation.

## Scope and frozen inputs

Parent PREFIX-1124 17fd6bcf9f871cf9e5d5ea152bccf2999b0f5f29:research_notes/portable_direct/2026-11-27_r6_prefix1124_tangent_joint_observer.md (read full). P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and its joint-observer, X6/time and residual-fidelity companions; ACTIVE worldview, current global entries checked at 77872cc5527194dc7be371a3852953b72cfe2369, portable and continuation protocols applied. Preserve original signed reversal -5, 5q cover, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. Scalar t and the auxiliary two-observer coordinate are spectral readouts, not native dimensions or time. No classical reference or physical residual attribution.

Frozen 8800 certificate 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json SHA256 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9; 9200 root 7c0ecbd38264af8fbee8a352f0b4fa47f62ffc21:research_notes/portable_direct/2026-11-27_r6_prefix1122_root_9200_only.json SHA256 b17b098179d915eabbdefc8f6050a8d401e06731a59e7f130350ce6aaab1948f. Parent archive SHA256 list checked. 8400/8800 original command exits unconfirmed; inherited application conditional.

## 1. Optimal root-conditioned joint-support theorem

Let F(t*)=0 for t* in [x-r,x+r]. Let G be any signed joint observer from PREFIX-1124, for example beta F''+(alpha-c0)F'. On the same carrier retain a joint affine enclosure at x:
(F(x),G(x)) in Z = (f,g)+sum_j [-1,1] (u_j,v_j).
For the shared BRC anchor, coefficients a=a0+sum_j b_j e_j, |e_j|<=1, point-vector columns are (P dot b_j, G_vector dot b_j); include anchor residual, coefficient rounding and certified joint point tail/representation payments as additional columns. If only separate uniform point errors EF,EG are known, (EF,0),(0,EG) are safe columns. This is a containing zonotope, not an assertion that independently chosen coefficients all occur. Preserve the common anchor residual and original signed basis; this observer reduction is only for the root-conditioned G output.

Let D=[fl,fu] x [gl,gu] contain (F',G') throughout the root interval. Integrating from x to t* yields
(F(t*)-F(x),G(t*)-G(x)) in T = conv({+r d,-r d : d corner of D}).
Indeed if the displacement is h, the mean derivative vector is in D; hD lies in the indicated convex hull for |h|<=r. The case h=0 is included. Thus the true observation lies in K=Z+T, on the slice F=0.

For every real s define
U(s)=g-s*f+sum_j |v_j-s*u_j|+r max_{(a,b) corner of D}|b-s*a|.
Then G(t*)<=U(s). More strongly, if the relaxed polygon K intersects F=0, its maximal G on that slice equals min_s U(s). The lower endpoint is minus the same formula with G reflected (g,v_j,gl,gu) -> (-g,-v_j,-gu,-gl).

Proof: U(s) is exactly the support of K in direction (-s,1), by Minkowski additivity and the displayed columns/corners. For a finite polygon (including degenerate segment/point), a maximizer of the vertical slice admits a supporting line with normal (-s,1): equivalently, the upper boundary is a finite concave piecewise linear function of F on its projected interval; a finite one-sided supporting slope exists at endpoints too. If projection is a singleton F=0, s=0 suffices. For the nonempty slice this proves equality. Equivalently this is the exact dual of a finite LP with one equality. The equality refers to the relaxed enclosure, not necessarily to the true BRC parameter set; it is still a rigorous bound on the latter. Empty slice can be detected separately by the projection interval of K.

U is convex piecewise affine. A finite exact minimization suffices: candidate s=0, all v_j/u_j for nonzero u_j, and all intersections of the eight affine corner lines r*(+/-)(b-s*a). If a minimum lies on an unbounded affine ray, an endpoint (or 0 in the globally constant case) attains it. Nonempty slice bounds U below. For n columns there are at most n+29 candidate values (8 choose 2 intersections plus zero), with O(n^2) rational arithmetic operations for simple direct evaluation, excluding actual bit costs and the upstream BRC point construction. For the 6+6 residual/rounding columns and 2 point-error columns, <=43 candidates. A sorted piecewise-linear sweep can reduce arithmetic count further but is not implemented here.

This extends PREFIX-1124: optimizing only derivative cancellation can be suboptimal when anchor point uncertainty is dominant; optimizing the full point+transport support is at least as sharp as ANY fixed s, including its tangent-only coefficient. The theorem handles sign tests directly without dividing by an independent F' box. To test integer relation (q,p,h) at scale L use the two G choices c0=h/q-g0/L and c0=h/q-H0/L from PREFIX-1124 and the restricted spectral root interval derived from rho. A strictly negative upper for the required nonnegative G, or a strictly positive lower for the required nonpositive G, excludes the whole integer relation. No actual new Stage46 candidate sign is claimed this round.

## 2. Exact auxiliary computation

The independent verifier enumerates all vertices of the relaxed Minkowski sum (every zonotope endpoint choice and all signed rectangle corners); a slice extremum at F=0 occurs at a vertex or a segment joining two opposite-sign vertices. It compares this exhaustive result to the exact piecewise-linear support calculation. 120 seeded rational cases, of which 119 feasible, all 119 exactly agree. These are auxiliary certificate-geometry tests, not new native BRC runs.

Discriminating example: Z=(0,1/2)+[-1,1](1,3); D={(-1,-2)}; r=1/10. Tangent-only s=2 cancels derivative transport but returns [-1/2,3/2]; joint-optimal s=3 returns [2/5,3/5] and strictly certifies sign. Directly the root constraint restricts the shared point error to [-1/10,1/10]; both endpoints are attained in the relaxation. This demonstrates why minimizing only transport can miss useful sign evidence.

For the actual inherited 8800/9200 derivative boxes, let -F' in [A,B] with A>0 and G' in [C,D] with C>0. The unique minimax coefficient for transport alone is s=-(C+D)/(A+B), and the exact minimized residual radius is (B*D-A*C)/(A+B), since the extremal residuals D+s*A and C+s*B balance in magnitude (s negative). Outside the negative half-line the error is >=D, so this is global. Exact Fraction verified this is strictly smaller than the ratio-midpoint coefficient from PREFIX-1124; the improvement factor minus one is only 6.976715579169535e-80. Both transfer bounds display 4.616032861171954e-150. This is a useful negative diagnostic: transport-only optimization is already effectively saturated; the remaining worthwhile target is the shared point-vector uncertainty, not further improvement of this term. Full G point evaluation is still missing.

Actual run output:
exact relaxed-polytope checks 119 of 120 feasible instances
example optimized bounds 2/5 3/5 s 3 vs tangent-only [-1/2,3/2]
frozen derivative minimax old/new transfer 4.616032861171954e-150 4.616032861171954e-150
strict improvement True
frozen minimax gain minus 1 6.976715579169535e-80

Verifier dual_support_verify.py SHA256 6a8dea92c832737bdd2309b5653f9fbea7c8b4178364865557151bb839f8ef3f; log 192bd1f58a802aaacdee07b076ae27f90936b08e9bd469ce3983243c6eaf30b0. Parent tangent_result.json derived from frozen inputs by tangent_verify.py; archive contains both and all relevant exact inputs. All parent archive hashes verified.

## 3. N=300 anchor recovery attempt

Executed a modified version of the frozen PREFIX-1124 reconstruction. It prepares an exact anchor packet {cc,rad,inv,eps,dr} immediately after anchor construction; point Horner rewritten as integer-endpoint outward grid. If coefficient interval [al,au]/G and t=[tl,tu]/G, for current [l,u]/G the product endpoints are floor(min(l*tl,l*tu,u*tl,u*tu)/G) and ceil(max(...)/G); add coefficient endpoints. This is rigorous by interval arithmetic induction, includes coefficient rounding, and preserves the existing tail payment and signed anchor dual. Payment serialization is changed to upper integer values on grid 10^140 (rather than unbounded exact fraction strings). No successful full execution or new root output this round.

Actual tool execution timed out, last log:
basis ready
m0 ready
all moments ready
anchor row 8400
anchor row 8800
anchor row 9200
anchor row 9600
No exact anchor packet, exit file, polynomial-ready line or root result generated. Hence no evidence that modified Horner was reached. Previous run had completed anchor construction in its log but not saved exact anchor, so redo of missing packet was justified; this attempt should not be counted as a higher precision certificate. Next engineering step: checkpoint M/obs/eps row-by-row BEFORE the large inverse and the two additional moment anchors, then continue the remaining rows and inverse from exact saved bytes. Separate timing and payment serialization cost; do not repeat failed all-in-one invocation unchanged. Patch details: insert packet serialization before return rounded,r,dual in replay_9600_n300.py; integer-Horner implementation and payment serialization in root_9600_n300_fast.py. Files/log in local execution archive; hashes replay_9600_n300_saved.py a7161688ebf0d65d7e0118467677981fff32cc08f6694ec5636a9520e0ffd375; root_9600_n300_fast.py 14a5bf1fb02e73c54efd8e4e2ef1d2b13821a66e20b5a4567ce1bf8668ec9386; fast.log 618ed2af85b976d058bf84fda739277c402649381395decc0c89ae87923b22be.

## 4. Frontier and next action

Next: persist exact rows of the 9600 N=300 anchor, then obtain actual joint point columns, apply optimal root-conditioned support to both candidate-specific signed inequalities, and use the refined root to close the three PREFIX-1122 candidates. Endpoint frontier remains 35763703231524369452081938126483743402578 exclusive; first possible triple window 6.51851512427e99; first possible sqrt-gap pair window 8.54394814368e104. All inherit prior correspondence and analytic certificates. No new exclusion scale, exact-zero decision, eventual separation or B_fix,odd(32) closure. Independent review and Activity observation audit remain pending.
