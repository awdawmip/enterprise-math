# Stage152 — all-real exact affine optimality for ternary iid N=14

**Research status:** AUTHOR_EXACT / SOURCE_ONLY / NOT_ADMITTED. There is no native execution claim, independent Research Driver review, or Foundation acceptance. The model here is an external finite iid auxiliary sequential-decision model, not P000 native-X6 or Heartbeat dynamics.

## Immutable scientific inputs

GLOBAL_KNOWLEDGE_V1 canonical main at 43639a1bd021e9c6e90e699fbb7b5021855fbef7; Enterprise Math canonical main at e5f859b01b76e84cb6b68b899cbe7d6390eb5b83. The P000 startup projection's canonical blob is 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc and exactly matched the canonical original at this fixed global snapshot. ACTIVE worldview and current portable research protocol were inspected. Stage151 source theorem is at research_notes/n14_aux_iid_affine_151_20261026/PROOF_STAGE151.md at the frozen Enterprise Math commit.

## Model and exact theorem

Consider the ternary iid distributions
\[
P=(1/8,1/24,5/6),\qquad Q=(1/12,1/12,5/6)
\]
and horizon \(N=14\). Policies are allowed to randomize at every **complete ordered history**, choosing to stop/decide P, stop/decide Q, or continue when not terminal. Define
\[
e_P=P(\mathrm{decide}\ Q),\quad e_Q=Q(\mathrm{decide}\ P),\quad
t_P=E_P\tau,\quad t_Q=E_Q\tau,
\]
and \(V_{14}(\alpha)=\min_{e_P,e_Q\le\alpha}\max(t_P,t_Q)\).

The Stage151 author frontier is
\[
\alpha_{151}={18373001785623238325\over52808422392537808896},
\qquad V_{151}={318746112099955105013\over26404211196268904448}.
\]
Define
\[
\eta_{152}={6360587975\over206282899970850816},
\quad\alpha_{152}={18373003413933759925\over52808422392537808896},
\quad V_{152}={318745538371909741813\over26404211196268904448}.
\]

**Theorem (complete real interval, not just rational samples):** For every real \(0\le\delta\le\eta_{152}\),
\[
\boxed{V_{14}(\alpha_{151}+\delta)
=V_{151}-{25612859168\over36346217}\delta.}
\]
The displayed support line is **strictly below** \(V_{14}(\alpha)\) for every \(\alpha>\alpha_{152}\) (right-sharpness). No claim about the next affine segment is made.

## Exact Bellman certificate: all ordered histories

At a count state \(s=(n,a,b)\), any ordered prefix with these counts satisfies
\[
Q(h)/P(h)=2^{a+b}/3^a.
\]
For \(K=12844717560/36346217>0\) and \(L=12768141608/36346217>0\), recursively define
\[
H(s)=\min\left\{
K\frac{2^{a+b}}{3^a},\quad L,\quad
1+\sum_{i=0}^2P_i H(s+e_i)
\right\};
\]
at depth 14 omit continuation. The three terms are P-stop, Q-stop and continue. Suffix laws and prefix likelihood ratios depend only on counts, so backward Bellman induction bounds **all policies on complete ordered histories**, not just count-based policies:
\[
\tag{LB}
H(0,0,0)\le t_P+L e_P+K e_Q
\le\max(t_P,t_Q)+(K+L)\alpha.
\]

Exact Fraction arithmetic on every one of the **680** count states obtains
\[
H(0,0,0)={341463027624594134301829727\over1327376472826305935572992}
\]
and **exactly two** Bellman ties, both Q-stop / continue:
\[
B=(11,0,1),\qquad W=(8,3,3).
\]
There are exactly **1,238 strictly positive** nonminimum action gaps, minimum
\[
204027667/1130512733568>0;
\]
zero negative gaps. Thus every support-attaining policy can use nontrivial choices only at B and W.

## Exact labeled first-hit provenance and four observers

At B let \(b\in[0,1]\) be the probability of Q-stop, otherwise continue. At W let \(w\in[0,1]\) be the probability of Q-stop, otherwise continue. At every other reached state take its uniquely minimizing action. W is at depth 8 and has three symbol-0 occurrences, whereas B is at depth 11 and has zero; symbol counts never decrease. Hence W cannot be an ancestor of B, and B cannot be an ancestor of W by depth. Their **genuine ordered-history first-hit cones are disjoint**.

A literal integer-weight DFS (P symbol weights \((3,1,20)/24\), Q weights \((1,1,10)/12\)) finds:
\[
B:\ 11\ \text{first-hit histories},\quad
(P\text{-mass},Q\text{-mass})=
(107421875/1451188224,\ 107421875/725594112);
\]
\[
W:\ 224\ \text{first-hit histories},\quad
(P\text{-mass},Q\text{-mass})=
(175/7962624,\ 175/3359232).
\]

For the four-vector \(M=(e_P,e_Q,t_P,t_Q)\), exact arithmetic gives
\[
\boxed{M(b,w)=M_{00}+b\,d_B+w\,d_W}
\]
with
\[
\begin{split}
M_{00}={}&(1212592135672539235/3505953353861431296,\\
&224492569856365/641959232274432,\\
&5330367237943930717/438244169232678912,\\
&70007401392629/5944066965504),\\
d_B={}&(4619140625/2229025112064,\;-751953125/417942208512,\\
&-25673828125/278628139008,\;-17939453125/104485552128),\\
d_W={}&(16372475/56358560858112,\;-1952125/10030613004288,\\
&-78138725/2348273369088,\;-19052425/278628139008).
\end{split}
\]
All four deterministic corners were calculated by (1) a backward exact-Fraction observer recurrence and independently by (2) an integer-weight DFS on literal ordered histories. The four DFS visit totals for \((b,w)=(0,0),(0,1),(1,0),(1,1)\) are respectively
\(496174,475342,496042,475210\).
Every observer coordinate agrees between the methods. The four-vector mixed corner term \(M(1,1)-M(1,0)-M(0,1)+M(0,0)\) equals exactly \((0,0,0,0)\), as expected from the incomparable labeled cones.

## Complete real primal segment and endpoint

The equation \(e_P=e_Q\) is exactly
\[
\boxed{b(w)=
{8061971501813291\over8143872000000000}
-{797257531\over6362400000000}\,w.}
\]
Throughout every real \(0\le w\le1\) the probability is strictly between zero and one; \(w\) is also legal. Thus this is a real continuum of admissible randomized policies.

At \(w=0\), direct computation (not assumed from Stage151) recovers
\[
e_P=e_Q=\alpha_{151},\quad
t_P=V_{151},\quad
t_P-t_Q={36759675262851533665\over79212633588806713344}>0.
\]
At \(w=1\),
\[
e_P=e_Q=\alpha_{152},\quad
t_P=V_{152},\quad
t_P-t_Q={12253888791127786955\over26404211196268904448}>0.
\]
The common error rises strictly by \(\eta_{152}>0\), and every observer and both time differences depend affinely on \(w\). Hence \(t_P>t_Q\) and both errors are equal along the **entire real interval**. At both endpoints exact arithmetic checks
\[
t_P+L e_P+K e_Q=H(0,0,0).
\]
By affine interpolation this equality holds for every real intermediate coin; the explicit policies attain the Bellman lower bound (LB). The exact slope is \(K+L=25612859168/36346217\). This proves the stated value function and endpoint.

## Sharpness of this supporting line

The finite complete-ordered-history behavioral-policy space is compact; all observers are continuous polynomials in finitely many coin variables, and the constrained optimum is attained. If the same support line were optimal for some \(\alpha>\alpha_{152}\), because \(K,L>0\), equality in (LB) would require (i) both errors exactly \(\alpha\) and (ii) every reached prefix use only Bellman-minimizing actions. All nontied states have a unique action. Distinct first-hit ordered prefixes with the same tied count state have identical conditional suffix law and the same Q/P prefix-likelihood ratio, so their possibly history-dependent randomizations can be replaced by one **P-mass-weighted effective coin** without changing any of the four observers. Because B/W cones are incomparable, all support-attaining four-vectors lie in the displayed \(M(b,w)\) square. Equal errors force the displayed \(b(w)\). On the feasible square, this relation permits \(0\le w\le1\) and the maximal common error is \(\alpha_{152}\), contradiction. Thus the supporting affine line is **right-sharp**, not necessarily the value function to its right.

## Verification, research attribution, and next task

The companion Python 3 standard-library replayer implements the 680-state exact Bellman recursion, all 1,238 positive gap checks, genuine complete-history integer-weight DFS on all four corners, an independently structured backward Fraction observer recurrence, exact first-hit P/Q masses, no mixed term, error balancing, positive time dominance, dual equalities and both exact endpoints. It **passed** in this run with no floating-point arithmetic. The proof uses exhaustive finite rational arithmetic for its explicit coefficients, and mathematical arguments for validity over all real coins and all ordered-history policies. This remains **author-level** mathematical evidence; the methods share the model and are not a clean-blind Driver review or a formal proof-assistant certificate.

The BRC-inspired observer audit retains positive branch weights and ordered path identity. Signed changes in error/time are **observer differences**, not negative primitive BRC mass. Neither the external statistical model nor this auxiliary finite rational proof supplies a native typed-X6 embedding or residual-faithfulness theorem for P000.

Actual GitHub principal is awdawmip with push rights, but the native owner listing failed with CONTROL_QUOTA; own researcher session registration returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Active owner, valid native CLAIM, formal Source Result and independent Driver acceptance remain **unknown/unverified**. The branch artifact is source-only author evidence and does not take over any active Task.

**Stage153 open:** keeping B's Q/continue tie and treating W at Q-stop saturation, find the earliest legal dual gap closure, recalculate the complete exact Bellman action table, and then inspect all new tied-state *ordered* first-hit cones; prove the next real interval or produce an exact obstruction. Retain P000 and the native X6/triadic/provenance invariants as ontology, without claiming a bridge from this external model.
