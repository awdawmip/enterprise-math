# Stage120 — exact affine optimum after J saturation

**Status:** AUTHOR_EXACT_COMPUTATION_ASSISTED_PROOF. The result concerns the external finite iid problem only; it is neither a native Enterprise Math/P000 X6 theorem nor an admitted Result or independent Driver review.

## Exact setting and statement

For all randomized stopping/decision policies on the **full ordered ternary history** of at most 14 iid observations, let
P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf[max(tP,tQ):eP<=alpha,eQ<=alpha]. The inherited, author-verified Stage119 endpoint is

\[
\alpha_{119}=\frac{900390183707375071351}{2592933255351443128320},\quad
V_{119}=\frac{132634859722005927805223}{10371733021405772513280}.
\]

Put

\[
K_{120}=\frac{1527132609}{1903099},\quad
L_{120}=\frac{1463947128}{1903099},\quad
S_{120}=K_{120}+L_{120}=\frac{2991079737}{1903099}.
\]

**Theorem (finite exact, author proof).** For every REAL delta in

\[
0\le\delta\le \eta_{120}
=\frac{1266642955256352447367}{77958194918387612186050560}
\]

we have

\[
\boxed{V_{14}(\alpha_{119}+\delta)=V_{119}-S_{120}\delta.}
\]

The exact new endpoint is

\[
\boxed{\alpha_{120}=\frac{2573764724900518487425}{7411551152237344456704}},\qquad
\boxed{V_{120}=\frac{378361860665073597077285}{29646204608949377826816}}.
\]

This supporting affine line is **right-sharp**: equality on that same line is impossible for any alpha>alpha120.

## Global dual bound: all literal ordered histories

At count state s=(n,a,b), the exact likelihood ratio is R=Q(prefix)/P(prefix)=2^(a+b)/3^a, where a is the number of symbol 0, b the number of symbol 1. Define H(s) backwards as the minimum of

\[
K R\quad(\mathrm{stop\ and\ declare\ P}),\qquad
L\quad(\mathrm{stop\ and\ declare\ Q}),\qquad
1+\tfrac18H(n+1,a+1,b)+\tfrac1{24}H(n+1,a,b+1)+\tfrac56H(n+1,a,b)
\]

(the continuation option exists only for n<14). There are precisely 680 count states, 1,240 comparisons against selected actions, 1,238 strictly positive nonchosen gaps, and **zero negative gaps**. Exactly TWO states have two minimizing actions:

* D=(9,1,2): declare Q / continue.
* A=(9,3,0): declare P / continue.

The least positive gap is 76168651372577/4909786414055424 and

\[
H(0)=\frac{29115372702587876388649105}{52126377513908875296768}
=V_{119}+S_{120}\alpha_{119}.
\]

For a literal ordered prefix, the conditional iid suffix laws and the prefix likelihood ratio depend on its count state only. Induction on **each full ordered prefix**, not on a restricted count-policy class, gives

\[
H(0)\le t_P+L e_P+K e_Q
\le\max(t_P,t_Q)+S\alpha
\]

for every admissible policy. Therefore V14(alpha)>=H(0)-S alpha.

## Constructive primal family and provenance

At D, declare Q with probability w and continue otherwise. At A, declare P with probability y and continue otherwise. At every other count state use its unique Bellman minimizer. Their actual first-hit ordered-prefix cones are disjoint: both have depth 9 and incompatible a,b. Positive-rational BRC-style carrying of full ordered words yields:

| state | ordered first-hit words | total P mass | total Q mass |
|---|---:|---:|---:|
| D=(9,1,2) | 172 | 671875/53747712 | 671875/20155392 |
| A=(9,3,0) | 84 | 109375/1990656 | 109375/6718464 |

Because no history reaches both sites, the root four-observer vector M=(eP,eQ,tP,tQ) is exactly affine:
M(w,y)=M00+w dD+y dA, where

\[
M_{00}=(608646052236273911/1752976676930715648,\quad
13933675187525/40122452017152,\quad
2803540112797487261/219122084616339456,\quad
40658886091241/3343537668096).
\]

\[
d_D=(593265625/5283615080448,\,
-430671875/5015306502144,\,
-34607609375/1981355655168,\,
-17355203125/417942208512).
\]

\[
d_A=(-1921609375/7925422620672,\,
259765625/835884417024,\,
-20758609375/330225942528,\,
-1476453125/69657034752).
\]

Exact equality eP=eQ forces

\[
\boxed{w(y)=\frac{376517470455067}{1042086080000000}
+\frac{6494178}{2326085}y}.
\]

**New structural boundary:** D's Q-stop probability reaches 1 FIRST, while A still mixes. Specifically,

\[
\boxed{y_*=\frac{665568609544933}{2909391744000000}<1},
\quad 0\le y\le y_*,\quad w(0)=w_{119},\quad w(y_*)=1.
\]

The exact balanced error and P-mean time on this entire real parameter interval are

\[
e_P=e_Q=\alpha_{119}+\frac{\eta_{120}}{y_*}y,\qquad
t_P=V_{119}-S_{120}\frac{\eta_{120}}{y_*}y.
\]

The exact time dominance margins at the two endpoints are
1333129085804580517835/2074346604281154502656 and
19225817524111600585621/29646204608949377826816, both >0; their interpolation stays >0. Thus tP=max(tP,tQ). Every action has Bellman-minimal cost, the dual lower bound is attained, and the theorem holds for **every real** delta in the displayed interval.

## Right-edge sharpness

All finite ordered-history randomized policies form a compact product of finite simplexes. If the same support equality held at some alpha>alpha120, positivity of K,L would force both errors to equal alpha, and all chosen positive-prefix-mass actions to be Bellman minimizers. Outside D and A their minimizing actions are unique. Within each tie-state fiber arbitrary word-dependent mixed decisions may be collapsed only for the **four declared observers**, because the iid suffix moments and likelihood ratio agree at that count state. The disjoint first-hit cones eliminate mixed products.

Therefore every equality-attaining policy is observer-equivalent to w,y in [0,1] with w(y) as above. Since w(y)<=1 and its slope is positive, y<=y_*, while its balanced alpha is strictly increasing in y. Hence alpha<=alpha120, contradiction. There is no unjustified claim about the next support segment.

## Exact execution evidence and scope

A local exact Fraction bottom-up Bellman checker ran to completion for all 680 states, 1,238 positive nonchosen action gaps and all four tie-state corners; its own ordered-word integer DFS visited 893725/888685/885985/880945 prefixes at (w,y)=(0,0)/(0,1)/(1,0)/(1,1), matching all four root moments EXACTLY and proving the mixed difference zero. A separately written independent recursive-Bellman + integer ordered-prefix DFS program, importing nothing from the primary verifier, passed on 680 states, all four exact corner moments, the two first-hit counts/masses, y_* and endpoint. Both checkers executed locally, not on GitHub. Executed local source SHA-256: primary 84f1c5b2925b0a1f0a724c53b11491f416aa4aae9bf58979d65b736c74bda76d, independent 98e92b5634b74cb9eb00926faed553029a34f1db0985fff55b701c9a13e75671. The accompanying portable checker is a source-equivalent reproducibility aid; GitHub storage/readback is not itself runtime execution.

BRC usage is actual positive rational ordered-path/multiplicity/provenance preservation, with a proved **iid and four-observer-specific** quotient. It is not BRC–Shor, and no native six-axis state/readout/operation-preserving bridge has been proved. P000 and ACTIVE worldview were read but not modified.

### Source pins, authority, next task

Global canonical snapshot: awdawmip/chatgpt-global-knowledge main@c6d252e7e402c453dd0eb291d80b0a8a7e8f6821 (P000 canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc); EM starting read: main@a0f54b76491aedcde1405c39ad0df86a3ccda6ab. Prior author source: research_notes/n14_aux_iid_affine_118_119_20261026/PROOF_STAGE118_119.md at that EM ref.

GitHub authenticated login: awdawmip; native task inventory failed CONTROL_QUOTA and own session registration was denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false); therefore live Owner, formal CLAIM, native Result and Driver review remain **unverified/ungranted**. This is ordinary author research provenance, not a native session/Result.

A separate exact affine gap sweep along the A tie with D strictly declaring Q yielded Stage121 dual candidate K=320913819/414584, L=37979256/51823, new tie G=(13,6,4), Q-stop/continue, plus A P-stop/continue. Full 680-state candidate Bellman recheck has 1,238 strictly positive gaps, minimum 110828719979/9903529525248. This is a DUAL CANDIDATE only; its primal interval is open. See NEXT_TASK_PACKET_121.md.
