# N14 auxiliary iid sequential-discrimination model: 66th exact affine interval

**2026-10-24; author-level exact finite-model proof, independent Research Driver unreviewed.** This is a theorem only for the explicitly stated auxiliary iid probability model. It is not a native Heartbeat/X6/BRC dynamical theorem, nor a formally admitted Task Result.

## 1. Model, inherited anchor, precise theorem

At each ordered observation there are three symbols with probability laws
\[
P=(1/8,1/24,5/6),\qquad Q=(1/12,1/12,5/6),\qquad N=14.
\]
Rules may randomize and depend on the complete ordered observation history; they must stop and announce P or Q by observation 14. Define \(e_P=P(\text{announce Q})\), \(e_Q=Q(\text{announce P})\), \(t_P=E_P\tau\), and \(t_Q=E_Q\tau\). Write
\[
V_{14}(\alpha)=\min_{\pi:e_P,e_Q\leq\alpha}\max(t_P,t_Q).
\]

The previously published author-level interval 65 is an inherited dependency: Source immutable commit 9cb91fb9aa846c2eae4ade29a25f12f5abe71c7e, directory research_notes/n14_aux_iid_affine_65_20261024. Its exact anchor and balancing probability at \(B=(12,0,1)\) are
\[
\alpha_{65}=\frac{5171859261098244647}{14900301753911083008},\quad
V_{65}=\frac{12336162058364474269}{931268859619442688},\quad
s_{65}=\frac{26151763070183819}{41779200000000000}.
\]
All inherited deterministic stopping rules are frozen, including \(A_{65}=(9,6,1)\mapsto P\). This author-level proof is conditional on those inherited exact rules and their prior certificate; it does not claim independent mathematical review of interval 65.

Fix
\[
K_{66}=\frac{1627128}{263},\quad
\lambda_Q=K_{66},\quad
\lambda_P=72+\frac89K_{66}=\frac{1465272}{263},\quad
\Gamma_{66}=\lambda_P+\lambda_Q=\frac{3092400}{263},
\]
and \(\eta_{66}=664075/8622859811291136>0\).

**THEOREM (finite auxiliary model).** For **every real** \(\delta\in[0,\eta_{66}]\), including irrational \(\delta\),
\[
\boxed{V_{14}(\alpha_{65}+\delta)=V_{65}-\frac{3092400}{263}\delta.}
\]
The right endpoint is sharp as a supporting-line endpoint:
\[
\boxed{\alpha_{66}=\frac{5171859262245766247}{14900301753911083008}},\qquad
\boxed{V_{14}(\alpha_{66})=\frac{12336161215066994269}{931268859619442688}}.
\]

## 2. Complete Bellman dual, with positive slacks

Write a count state \(z=(n,a,b)\), with \(a,b\) the first two symbol counts and the third count \(n-a-b\). The exact prefix likelihood ratio is
\[
L(z)=\frac{Q(z)}{P(z)}=\frac{2^{a+b}}{3^a}.
\]
For a P-normalized Bellman objective \(t_P+\lambda_Pe_P+\lambda_Qe_Q\), the action costs are
\[
C_P(z)=\lambda_Q L(z),\quad C_Q(z)=\lambda_P,\quad
C_C(z)=1+\sum_{i=0}^2P_iD(z+e_i)\quad(n<14);
\]
continuation is unavailable at \(n=14\), and \(D(z)\) is the minimum of available action costs. Conditional iid suffixes and the likelihood ratio depend only on counts; the Bellman lower bound is valid for arbitrary ordered-history policies, not only count-based policies. This count reduction does **not** permit erasing actual ordered first-stop histories when evaluating risk.

Two author-side exact programs are attached. The primary program evaluates all 680 count states with Python Fraction and all 1,240 alternative-action gaps under the inherited stopping map. There are 1,238 strictly positive gaps, zero negative gaps, and precisely two zero gaps: \(A_{66}=(11,7,2)\), where continue and immediate P tie; and \(B=(12,0,1)\), where continue and immediate Q tie. The smallest positive gap is \(115693/3635712\). A second program directly recomputes the minimum at every state, not merely gaps under the chosen action. Both return
\[
\boxed{D(0,0,0)=\frac{7373790509633184491777}{1800909632940539904}
=V_{65}+\Gamma_{66}\alpha_{65}.}
\]

For any randomized history-dependent policy obeying both error limits,
\[
D(0,0,0)\leq t_P+\lambda_Pe_P+\lambda_Qe_Q
\leq \max(t_P,t_Q)+\Gamma_{66}\alpha.
\]
Therefore \(V_{14}(\alpha)\geq D(0,0,0)-\Gamma_{66}\alpha\) globally.

## 3. Genuine ordered first hits, not nominal multinomial paths

The new tie \(A_{66}=(11,7,2)\) has 1,980 nominal length-11 ordered words. Exactly **1,212 survive the entire inherited stop tree**; the other 768 are cut at the first earlier stop. The complete cut histogram is:

| First earlier stopping state (all announce P) | Number |
|---|---:|
| (6,5,0) | 180 |
| (6,6,0) | 30 |
| (7,5,0) | 90 |
| (8,7,1) | 18 |
| (9,6,1) | 366 |
| (9,7,1) | 84 |
| **Total** | **768** |

Every true arriving word has the same probability under either iid law. Thus
\[
p_A=\frac{2525}{3623878656},\quad q_A=\frac{2525}{15479341056}.
\]
All 12 nominal B histories are true arrivals:
\[
p_B=\frac{48828125}{725594112},\quad
q_B=\frac{48828125}{362797056}.
\]

The old terminal state \((12,7,2)\) has 7,920 nominal histories and 4,570 true first arrivals. Exactly 1,212 of its surviving histories pass through \(A_{66}\). Switching to immediate P at A **truncates** those downstream paths; one cannot count the old and new terminal events as independent. The primary verifier uses the forward first-hit mass recurrence and the second verifier enumerates ordered words and their earliest stops explicitly.

Conditional on *continuation* at A and B, with the inherited downstream deterministic stops, the exact suffix-risk vectors \((e_P,e_Q,t_P,t_Q)\) are
\[
R_A=(41/13824,\;569/576,\;69/64,\;167/144),
\qquad R_B=(63/64,\;1/144,\;9/8,\;13/12).
\]

## 4. Balancing both errors and attaining the lower bound

Let \(u\in[0,1]\) be the immediate-P probability at A and let \(s\) be the immediate-Q probability at B. On a path the first-symbol count \(a\) cannot decrease. Since \(a(A)=7\) and \(a(B)=0\), **no single path reaches both tie states**; all \(us\) coefficients in the four risk functions vanish. The second verifier checks this by an exact four-corner backward evaluation.

Put
\[
X=p_AR_A.e_P=\frac{103525}{50096498540544},\qquad
Y=q_A(1-R_A.e_Q)=\frac{17675}{8916100448256},
\]
\[
E=p_B(1-R_B.e_P)=\frac{48828125}{46438023168},\qquad
H=q_BR_B.e_Q=\frac{48828125}{52242776064}.
\]
Relative to \((u,s)=(0,s_{65})\), the changes are exactly
\[
\Delta e_P=-Xu+E(s-s_{65}),\qquad
\Delta e_Q=Yu-H(s-s_{65}).
\]
Choose
\[
\boxed{h_{66}=\frac{X+Y}{E+H}=\frac{17743983}{8704000000000}},
\qquad s=s_{65}+h_{66}u.
\]
Then the endpoint
\[
s_{66}=\frac{26151848241302219}{41779200000000000}
\]
lies strictly below one and above \(s_{65}>0\); the rule is feasible for every \(u\in[0,1]\). Both errors obey the **exact identities**
\[
e_P=e_Q=\alpha_{65}+\eta_{66}u,\qquad
\eta_{66}=Eh_{66}-X=Y-Hh_{66}
=\frac{664075}{8622859811291136}>0.
\]
Exact forward evaluation yields \(t_P=V_{65}-\Gamma_{66}\eta_{66}u\). Both end margins are strictly positive:
\[
(t_P-t_Q)_{u=0}=\frac{213327829242734891}{413897270941974528}>0,
\]
\[
(t_P-t_Q)_{u=1}=\frac{639982967302999873}{1241691812825923584}>0.
\]
The gap is affine in \(u\), hence stays positive throughout the **entire real interval**. Thus \(t_P=\max(t_P,t_Q)\), all the constructed policies attain the Bellman dual bound, and \(u=\delta/\eta_{66}\) proves the theorem for every real \(\delta\in[0,\eta_{66}]\). The seven rational interpolation points tested by both programs supplement rather than replace this symbolic affine argument.

## 5. Sharp right endpoint

The finite ordered-history randomized decision polytope is compact, so the constrained optimum is attained. Suppose for some \(\alpha>\alpha_{66}\) the **same supporting line** were optimal. Since \(\lambda_P,\lambda_Q>0\), equality in the dual chain would force \(e_P=e_Q=\alpha\) and Bellman-minimizing actions on every positively reached finite history. Every symbol has positive probability under both laws. Because exactly the two tied count states A and B offer alternative minimizing actions, any optimum on the line can randomize only there (apart from zero-probability histories). History-specific probabilities can be averaged at each tied count state because its conditional iid suffix law is history-independent; as already shown, A and B cannot be visited on one path. Thus the two errors must be of the displayed two-parameter form. Equality between them forces \(s=s_{65}+h_{66}u\), and the common error satisfies
\[
\alpha=\alpha_{65}+\eta_{66}u\leq\alpha_{65}+\eta_{66}=\alpha_{66},
\]
a contradiction. Hence the support line cannot extend to the right beyond this sharp endpoint. This does **not** claim a discontinuity in \(V_{14}\).

## 6. Reproduction, provenance and remaining problem

The author-side checker verify_n14_66.py performs exact rational Bellman slacks, forward first-hit/decision-risk accumulation, conditional suffix analysis and seven randomization checkpoints. verify_n14_66_crosscheck.py separately enumerates the ordered words, builds a min-based Bellman recurrence, tests mixed terms at four corners and evaluates backward risk. Both run on Python standard library without network, floating point or Monte Carlo. They share the previously published stopping policy; they are not a clean-independent Driver audit.

The result is an exact finite auxiliary iid model computation, not a formally verified Lean proof, a mathematical admission, or an X6/Heartbeat fidelity bridge. P000 remains untouched. The author-note source publication does not authorize an EM Task CLAIM, freeze a formal Result, or change Foundation truth.

The next *unproved* affine dual candidate is
\[
K_{67}=\frac{1395301593924}{233134355},\qquad
A_{67}=(5,1,3),\quad\text{continue versus immediate Q}.
\]
Interval 67 requires its own first-hit survival audit, downstream truncation, exact balance and supporting-line certificate; a dual tie by itself is insufficient.

**Status:** AUTHOR_EXACT_RATIONAL_PROOF / TWO_AUTHOR_SIDE_REPLAYS_PASS / DRIVER_UNREVIEWED / NATIVE_CORRESPONDENCE_UNPROVED / NATIVE_OWNER_UNVERIFIED.
