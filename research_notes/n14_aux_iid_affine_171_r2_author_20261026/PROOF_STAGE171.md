# Stage171: exact full-real minimax stopping interval (external N14 ternary IID)

**Scientific status, 2026-10-26:** AUTHOR_EXACT, author-side exact rational proof and two computational structures; no native Enterprise Math CLAIM, no independent Research Driver review/admission, no Lean checker and no P000-native claim.

## 1. Sources, scope and precise statement

Read source pins: GLOBAL_KNOWLEDGE_V1 canonical main df7e8fb68cec1d6f5925f8947a36d9c5c04eee65 (both entry files, P000 and ACTIVE worldview); Enterprise Math main c69f657436d0dd0b5ad9ed848f055da9e5eb7c2f (docs/PORTABLE_RESEARCH_PROTOCOL.md). The *distinct immutable scientific predecessor* is Stage170, commit 12755060786f7ef9b6657c3ea7d014d271bcb87b, under research_notes/n14_aux_iid_affine_170_r2_author_20261026/, including dual171.json. Prior Stage170 author endpoint, not an independent mathematical admission, is the inherited input.

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) be IID laws on three labeled outcomes. Allow **all randomized decisions on complete ordered histories**, with stop time tau at most 14 and terminal verdict P or Q. Define eP=P(verdict Q), eQ=Q(verdict P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=inf{max(tP,tQ):eP<=alpha,eQ<=alpha}.

Let

    alpha170 = 126062165849964145105/361441878574651932672
    V170     = 4191196473918241372757/361441878574651932672
    K171     = 378837/1529
    L171     = 1128472/4587
    H171     = 332293501648867121767/1807757198084800512
    S171     = K171+L171 = 2264983/4587
    width171 = 12351453125/274532676868767744
    alpha171 = 882435274780741015735/2530093150022563528704
    V171     = 4191188444229937372757/361441878574651932672

**Theorem:** For *every real* delta with 0<=delta<=width171, including irrational delta,

    V14(alpha170+delta) = V170 - S171*delta.

For any alpha>alpha171, the same supporting affine line H171-S171*alpha is strictly below V14(alpha); this does not assert the value function ends there.

## 2. Bellman lower bound and exhaustive domain

For an ordered prefix with n observations, a zeros and b ones, let s=(n,a,b). The exact Q/P *prefix* likelihood ratio is ell(s)=2^(a+b)/3^a. Thus a count-state suffix dynamic program can represent every ordered history's conditional objective without assuming count-state-only policies.

At n=14, h(s)=min{K171*ell(s),L171}; before n=14,

    h(s) = min{ K171*ell(s), L171,
                1+sum(i=0..2) P_i*h(s+symbol_i) }.

These options mean stop with verdict P (penalty K171 under Q), stop with verdict Q (penalty L171 under P), or continue (one time unit under P). Backwards induction over each *individual ordered history* yields H171=h(0,0,0)<=tP+K171*eQ+L171*eP. Since K171,L171>0, V14(alpha)>=H171-(K171+L171)*alpha.

An exhaustive exact rational scan covers sum(n=0..14)binom(n+2,2)=680 states, all admissible P/Q/continue actions and all reachable count coordinates. It returns precisely 1,238 strictly positive nonwinning gaps (minimum 3442966771823/94671649898496); no negative gaps; exact root H171; and **exactly two ties**:
R=(10,0,1), verdict Q / continue;
U=(12,4,3), verdict Q / continue.
This finite exhaustive verification is confined to the declared N14 IID object, not a universal statement about native Cell dynamics.

## 3. Attaining the bound for all real parameters

At R stop Q with probability r, else continue; at U stop Q with probability u, else continue; at all other states take the unique Bellman minimizing action. If an ordered path hits R at step 10, it has 0 zeros; it can acquire at most two zeros before step 12, whereas U needs four. Therefore **no path can reach both tie states**. Each coin affects a disjoint set of labeled first-hit prefixes, so M(r,u)=(eP,eQ,tP,tQ) is exactly affine in r,u with zero ru coefficient.

Two distinct exact algorithms were actually run on the four deterministic coin corners (0,0),(0,1),(1,0),(1,1): (i) Fraction conditional suffix DP; (ii) unmerged full-ordered-prefix DFS with integer P step numerators (3,1,20)/24 and Q numerators (1,1,10)/12. All four coordinates agree exactly at all four corners; both terminal masses are exactly 1; mixed vector M11-M10-M01+M00 is (0,0,0,0). Ordered DFS visits respectively 321361,290341,321121,290101 nodes, total 1,222,924.

First-hit evidence:
R: 10 labeled prefixes, P mass 9765625/120932352, Q mass 9765625/60466176.
U: 5170 labeled prefixes, P mass 8078125/220150628352, Q mass 8078125/139314069504.

Setting D=eP-eQ=0 in the exact affine vector determines uniquely

    r(u) = 1284898704522779/1689088000000000
           - (641597/3694880000)*u.

Both r(0),r(1) lie in [0,1], hence r(u) is a legal probability at every real u in [0,1]. The exact four-corner certificate verifies:

u=0: eP=eQ=alpha170 and tP=V170;
u=1: eP=eQ=alpha171 and tP=V171.

At these endpoints the P-time advantage is respectively

    (tP-tQ)_0 = 134198175358476229825/361441878574651932672 > 0;
    (tP-tQ)_1 = 939402695545477608775/2530093150022563528704 > 0.

All observers are affine along u, so tP>=tQ for every real u in [0,1]. Common error increases strictly by width171; P-time decreases by exactly S171*width171. At both endpoints, tP+K171*eQ+L171*eP=H171; equality persists by affinity at *every* real interpolation point. The policy therefore attains the universal lower bound throughout the stated interval. This proves the theorem without grid sampling.

## 4. Strict right-support boundary

The finite-horizon, finite-alphabet full-history randomized-policy observer set is compact, so each feasible alpha admits a minimizer. Equality V14(alpha)=H171-S171*alpha would require simultaneously tP>=tQ, eP=eQ=alpha (K171,L171 positive), and no positive-reach suboptimal Bellman actions. Every alphabet event has positive P and Q probability, so the only randomized choices can occur at R and U. Any history-dependent coins at a fixed tie count-state have identical likelihood ratio and conditional suffix laws; first-hit P-mass-weighted averaging reduces them to one effective r and one effective u without changing any of eP,eQ,tP,tQ. Their first-hit cones are disjoint, so no interaction survives. Balance uniquely enforces the displayed r(u), with legal u<=1; common error is increasing in u and cannot exceed alpha171. Hence equality for alpha>alpha171 is impossible. The line is strictly *unattained*, not a global strict-convexity assertion.

## 5. Exact evidence, BRC scope and research authority

Evidence: executable standard-library Fraction verifier VERIFY_STAGE171.py, computed certificate171.json, stdout run171.log; next dual scan SCAN_STAGE172.py, dual172.json, scan172.log. Both scripts preserve model scope and report exact rational, not floating-point, quantities. Full executed source and original logs are also in the supplied portable evidence package. Under the BRC provenance discipline we retain distinct positive P/Q branch masses and full ordered first-hit paths; no negative-mass or phase cancellation is claimed. No BRC-native operator was executed, and no native X6 embedding, third-coordinate semantics or preservation-of-operations map has been proved; external auxiliary results are *not* P000 six-dimensional Cell theorems.

Connected identity was read as GitHub login awdawmip with EM repo push access. Native em_control_tasks returned CONTROL_QUOTA. Native em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Thus active Task owner is UNKNOWN; there is no native session, CLAIM, Source Result, Driver acceptance, or Foundation promotion.

Next independent mathematical unit: Stage172 exact dual candidate along dK=-1, dL=-10592/12501, with R Q/C and new Y=(5,4,1) P/C ties. Derive the full-ordered-history R/Y four-corner primal interval or a rational obstruction. See NEXT_TASK_PACKET_172.md and dual172.json.