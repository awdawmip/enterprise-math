# N=14 auxiliary iid sequential discrimination: exact 73rd affine interval

**2026-10-24. Evidence class: author-level exact finite-model proof; independent Research Driver review and native claim are absent.**

## Statement and inherited source

The alphabet is {0,1,2}, with independent observations under
\(P=(1/8,1/24,5/6)\), \(Q=(1/12,1/12,5/6)\), and stopping horizon \(N=14\). Arbitrary randomized policies depending on the entire ordered word are admitted. Set \(e_P=P(\text{decide Q})\), \(e_Q=Q(\text{decide P})\); let \(t_P,t_Q\) denote expected observation counts. Define
\[
V_{14}(\alpha)=\inf_{e_P,e_Q\leq\alpha}\max(t_P,t_Q).
\]
The inherited deterministic stopping tree and terminal likelihood decisions are specified by the immutable 72nd verifier (commit df2fd1ba3a24728e6bb5fc959f602a8b87202623), with one additional immediate-P stop at its endpoint \(A_{72}=(9,4,0)\). In the prior endpoint policy the Q-coin at \(B=(12,0,1)\) has probability
\[
s_{72}=\frac{11935533973576811}{20889600000000000}.
\]
The prior author-checked endpoint is
\[
\alpha_{72}=\frac{2585970549846042247}{7450150876955541504},\qquad
V_{72}=\frac{24569611393219845149}{1862537719238885376}.
\]

**Theorem (within this auxiliary finite model, author proof).** For *every real* \(0\leq\delta\leq\eta_{73}\), including irrational parameters,
\[
\boxed{V_{14}(\alpha_{72}+\delta)
=V_{72}-\Gamma_{73}\delta},\quad
\boxed{\eta_{73}=\frac{13130675}{17245719622582272}},\quad
\boxed{\Gamma_{73}=\frac{4394631492}{525227}}.
\]
Consequently,
\[
\boxed{\alpha_{73}=\frac{2585970555518493847}{7450150876955541504}},\qquad
\boxed{V_{73}=\frac{24569599527714816749}{1862537719238885376}}.
\]
This Bellman supporting line stops being attained past the stated right endpoint.

## Exact full-history Bellman lower bound

For a word of length \(n\) with \(a\) zeros and \(b\) ones, \(Q(w)/P(w)=2^{a+b}/3^a\). At any count state \(x=(n,a,b)\), take
\[
K_{73}=\lambda_Q=\frac{2306549196}{525227},\quad
\lambda_P=72+\frac89 K_{73}=\frac{2088082296}{525227},
\quad\Gamma_{73}=\lambda_P+\lambda_Q.
\]
The P-normalized Bellman alternatives are
\[
C_P=\lambda_Q\frac{2^{a+b}}{3^a},\qquad
C_Q=\lambda_P,\qquad
C_C=1+\sum_{i=0}^{2}P_iD(x+i)\quad(n<14).
\]
Backward minimization is valid for arbitrary ordered-history randomized policies: the conditional suffix law and likelihood ratio depend only on \(x\), while a policy may still use all earlier word information. Both exact rational checkers inspect 680 count states and 1240 nonchosen comparisons, obtaining 1238 strict positive slacks, zero negative slacks and precisely two ties:
\(B=(12,0,1)\), continue / immediate Q, and \(A_{73}=(8,6,1)\), continue / immediate P.
The minimum positive gap equals \(963802307/14521476096\), and
\[
D(0,0,0)=\frac{83941221388756468593095131}{28772208784196530864128}
=V_{72}+\Gamma_{73}\alpha_{72}.
\]
Every admissible policy obeys
\[
D(0,0,0)\le t_P+\lambda_Pe_P+\lambda_Qe_Q
\le \max(t_P,t_Q)+\Gamma_{73}\alpha.
\]
Thus \(V_{14}(\alpha)\ge D(0,0,0)-\Gamma_{73}\alpha\).

## Positive branch history, first hits and truncation

The new site \(A_{73}=(8,6,1)\) has 56 nominal ordered prefixes; **40** survive all earlier stops. Their exact first-hit masses are
\[
p_A=\frac{25}{4718592},\qquad q_A=\frac{25}{26873856}.
\]
At \(B=(12,0,1)\), all 12 nominal words survive, with
\[
p_B=\frac{48828125}{725594112},\qquad
q_B=\frac{48828125}{362797056}.
\]
Conditional *continuation* suffix risks in the old deterministic tree, in the order \((e_P,e_Q,t_P,t_Q)\), are
\[
R_A=\left(\frac{112877}{191102976},\frac{330271}{331776},
\frac{9153341}{7962624},\frac{329321}{248832}\right),\quad
R_B=\left(\frac{63}{64},\frac1{144},\frac98,\frac{13}{12}\right).
\]
Stopping at \(A_{73}\) truncates descendants. Explicit ordered-prefix enumeration gives, respectively, (nominal prefixes, prior-rule live prefixes, live prefixes through \(A_{73}\)):
\[
(9,6,1):(252,180,40),\quad
(9,7,1):(72,40,40),\quad
(11,7,2):(1980,1195,80).
\]
An independent integer prefix-routing audit finds 22 distinct downstream first-stop states visited after \(A_{73}\) and a total of 4280 terminal ordered words through that site (words have varying final lengths). These numbers count provenance, **not** automatically probability mass; the first-hit P/Q masses retain the positive rational branch weights. The ordered sequence must be retained until a proved aggregation.

## Constructive feasibility at every real parameter

At \(A_{73}\), decide P early with probability \(u\in[0,1]\); at \(B\), decide Q early with probability \(s\). A trajectory hitting \(A_{73}\) has already seen six zeros, whereas a trajectory reaching \(B\) has seen none. Therefore the events cannot coexist, and all four risk observables have exactly zero coefficient of \(us\); the separate backward checker verifies the four corner identities.

Define the exact probability changes
\[
X=p_AR_A.e_P=\frac{2821925}{901736973729792},\quad
Y=q_A(1-R_A.e_Q)=\frac{37625}{8916100448256},
\]
\[
E=p_B(1-R_B.e_P)=\frac{48828125}{46438023168},\quad
H=q_BR_B.e_Q=\frac{48828125}{52242776064}.
\]
Relative to the preceding endpoint,
\[
\Delta e_P=-Xu+E(s-s_{72}),\qquad
\Delta e_Q=Yu-H(s-s_{72}).
\]
Balancing both errors requires
\[
s=s_{72}+h_{73}u,\qquad
\boxed{h_{73}=\frac{X+Y}{E+H}
=\frac{64415991}{17408000000000}},
\]
and yields
\[
\Delta e_P=\Delta e_Q=\eta_{73}u,\qquad
\eta_{73}=Eh_{73}-X=Y-Hh_{73}.
\]
The full coin range is valid: \(0<s_{72}<s_{73}<1\), where
\[
s_{73}=\frac{11935611272766011}{20889600000000000}.
\]
At both endpoints the P-expectation is strictly larger than the Q-expectation:
\[
(t_P-t_Q)_{u=0}=\frac{276636241011513187}{465634429809721344}>0,\quad
(t_P-t_Q)_{u=1}=\frac{276634099139617787}{465634429809721344}>0.
\]
Affineness and these two inequalities imply \(t_P>t_Q\) for all real \(u\in[0,1]\). The construction uses only Bellman-minimizing actions at the dual point, so
\[
t_P+\lambda_Pe_P+\lambda_Qe_Q=D(0,0,0),\qquad
t_P=V_{72}-\Gamma_{73}\eta_{73}u.
\]
Taking \(u=\delta/\eta_{73}\) matches the global lower bound for each admissible real \(\delta\), proving the theorem.

## Right-end sharpness and successor

For the finite full-history randomized policy polytope, equality in the supporting line requires both error budgets tight (both multipliers positive), P as worst sample count, and Bellman-optimal action at every reached history. All non-tied decisions are fixed; the only surviving effective randomness is in the two tied sites \(A_{73},B\). Since suffix risks are identical across count-equivalent histories, even word-dependent choices at these two states reduce to their exact weighted effective probabilities \(u,s\). Equality \(e_P=e_Q\) enforces the same linear compensation. Since \(u\le1\), equality is impossible for \(\alpha>\alpha_{73}\). Thus the right endpoint is sharp for this support line.

At the new deterministic-P endpoint, exploratory next-crossing computation gives
\[
K_{74}=\frac{20412}{5},\qquad A_{74}=(12,5,1),
\]
with continue / immediate P as candidate ties. This is **only a dual candidate**, not a proved 74th interval.

## Reproduction, provenance and boundaries

Files verify_n14_73.py and verify_n14_73_crosscheck.py are separate exact-Fraction author checkers: the first performs forward weighted routing, suffix recursion, and Bellman chosen-action gaps; the second independently minimizes the Bellman table, enumerates short ordered words, and computes risks backward. Both were actually executed locally, passed the state/tie, first-hit, endpoint, continuous-affine sample, and four-corner checks. The checkers share the inherited author stop table and are not independent Research Driver review. The path-truncation program provides the complete 22-state integer witness. No formal theorem acceptance, native CLAIM, or faithful native BRC / six-dimensional X6 / Heartbeat dynamics transfer is asserted. The BRC use here is a positive rational ordered-branch provenance carrier, **not** a physical or phase-amplitude model.

Starting Source pin: Enterprise Math main 65f7b285ecf863b65d837b086cfbb91b651dc04a. Prior immutable stop-table source: df2fd1ba3a24728e6bb5fc959f602a8b87202623. Global control read pin: chatgpt-global-knowledge main 67b7a3f8630563826502c31fa22e0c3b58843baf, GLOBAL_KNOWLEDGE_V1. Native dispatch returned CONTROL_QUOTA and native session start returned STATIC_READONLY_SCOPE_DENIED; this author's standalone GitHub activity/Source publication is not a formal task CLAIM.
