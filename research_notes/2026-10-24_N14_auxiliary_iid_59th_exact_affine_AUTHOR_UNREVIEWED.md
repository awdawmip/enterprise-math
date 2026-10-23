# N=14 auxiliary iid sequential testing: exact 59th optimal affine interval

**2026-10-24 | AUTHOR-LEVEL EXACT FINITE-MODEL PROOF | NOT independently Research Driver reviewed.**

## Exact model, source and inherited frontier

Fixed GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge@bdc4c6b8927afbdf4d031565b3bec53d95936bbc. Initial Enterprise Math Source: awdawmip/enterprise-math@5dbd2586d75f45b06459f1e40ea2f3fbe9072b55. P000 projected canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc was checked against the actual original blob; it is unchanged.

Consider ordered iid symbols under
\[
P=(1/8,1/24,5/6),\qquad Q=(1/12,1/12,5/6),\qquad N=14.
\]
All randomized stopping/decision strategies depending on the **full ordered history** and terminating by N=14 are permitted. Let eP=P(decide Q), eQ=Q(decide P), tP and tQ denote expected sample counts. Define
\[
V_{14}(\alpha)=\inf\{\max(t_P,t_Q):e_P,e_Q\leq\alpha\}.
\]
The inherited author-checked but Driver-unreviewed endpoint is
\[
\alpha_{58}=\frac{1292959797687948215}{3725075438477770752},\quad
V_{58}=\frac{24710844325515742757}{1862537719238885376},\quad
s_{58}=\frac{6490285267896539}{10444800000000000}.
\]
Inherit the complete ordered-history stop tree from the 58th published verifier: all explicit SP/SQ states in the accompanying portable program, especially the fixed immediate-P decision at A58=(10,6,1), plus the exact count-state stop inequalities. These are not substituted by nominal multinomial counts.

## Theorem: closed interval of every real parameter

Define
\[
K_{59}=\frac{57829359672}{5658763},\quad
\lambda_Q=K_{59},\quad
\lambda_P=72+\frac89K_{59}=\frac{51811306200}{5658763},\quad
\Gamma_{59}=\lambda_P+\lambda_Q=\frac{109640665872}{5658763},
\quad \eta_{59}=\frac{707345375}{34491439245164544}.
\]
For **every real** \(0\leq\delta\leq\eta_{59}\), the global optimum of the stated auxiliary finite model satisfies
\[
\boxed{V_{14}(\alpha_{58}+\delta)=V_{58}-\Gamma_{59}\delta.}
\]
Consequently,
\[
\boxed{\alpha_{59}=\frac{1292959874081248715}{3725075438477770752}},\qquad
\boxed{V_{59}=\frac{24710104251021106757}{1862537719238885376}}.
\]
This 59th Bellman supporting line stops being attained immediately beyond its right endpoint; the value function itself does not terminate.

## 1. Exact Bellman dual for unrestricted full-history policies

At count state (n,a,b), a counts symbol 0 and b counts symbol 1. Any ordered history with these counts has \(L=Q(h)/P(h)=2^{a+b}/3^a\). Since the future is iid, the P-unit dual minimum obeys
\[
D(n,a,b)=\min\left\{\lambda_QL,\ \lambda_P,\
1+\sum_{i=0}^{2}P_iD(\mathrm{child}_i(n,a,b))\right\},
\]
with the continuation option absent at n=14. This is an exact dynamic reduction of the **dual** on all full ordered histories, not an assumption that competing primal strategies are Markovian.

The exact rational Bellman sweep enumerates 680 states and 1240 comparisons with the inherited selected action. Among the comparisons, 1238 are strictly positive, none negative, and exactly two are zero:
A59=(6,1,3), continuation vs immediate Q; and B=(12,0,1), continuation vs immediate Q. The smallest positive slack is 54043381/724321664.

The exact root is
\[
D(0,0,0)=
\frac{4177665846687324271885749343}{619979972454905454526464}
=V_{58}+\Gamma_{59}\alpha_{58}.
\]
For **any** randomized history-dependent policy,
\[
D(0,0,0)\leq t_P+\lambda_Pe_P+\lambda_Qe_Q
\leq\max(t_P,t_Q)+\Gamma_{59}\alpha.
\]
Thus the claimed affine expression is a universal lower bound.

## 2. Genuine ordered-history first hits and conditional suffixes

A59=(6,1,3) has 60 nominal ordered prefixes, but 15 stopped earlier: 3 at (3,0,3), 6 at (4,0,3), and 6 at (5,0,3), all with decision Q. **Exactly 45** remain alive on first arrival, with exact P/Q masses
\[
p_A=\frac{125}{442368},\qquad q_A=\frac{125}{82944}.
\]
At B=(12,0,1) all 12 nominal prefixes first arrive, with
\[
p_B=\frac{48828125}{725594112},\qquad
q_B=\frac{48828125}{362797056}.
\]
Conditional continuation suffix risks (eP,eQ,tP,tQ), fully accounting for all later inherited stops, are
\[
\begin{aligned}
c_A&=\left(\frac{452686309}{452984832},\frac{36175}{429981696},
\frac{82013675}{56623104},\frac{45301615}{35831808}\right),\\
c_B&=\left(\frac{63}{64},\frac1{144},\frac98,\frac{13}{12}\right).
\end{aligned}
\]
The new earlier A59 can truncate some later stopping paths. A separate direct ordered-history enumeration finds 1530 genuinely live arrivals under the 58th tree at old Q-stop state (10,4,4), of which **45** pass first through A59. The conditional suffix computation above includes these dependent downstream events; treating raw nominal later-state counts as independent would be invalid. A59 and B have disjoint first-arrival cylinders because a cannot decrease from 1 at A59 to 0 at B.

## 3. Attaining the dual throughout the entire real interval

At A59 immediately decide **Q** with probability \(u\in[0,1]\); otherwise continue. At B immediately decide **Q** with probability \(s\), otherwise continue. Relative to the inherited 58th policy, the two error changes are exactly
\[
e_P-\alpha_{58}=X u+E(s-s_{58}),\qquad
e_Q-\alpha_{58}=-Y u-H(s-s_{58}),
\]
where
\[
\begin{aligned}
X&=p_A(1-c_A.e_P)=\frac{37315375}{200385994162176},&
Y&=q_Ac_A.e_Q=\frac{4521875}{35664401793024},\\
E&=p_B(1-c_B.e_P)=\frac{48828125}{46438023168},&
H&=q_Bc_B.e_Q=\frac{48828125}{52242776064}.
\end{aligned}
\]
Set
\[
s(u)=s_{58}-h_{59}u,\quad
h_{59}=\frac{X+Y}{E+H}
=\boxed{\frac{1097388201}{6963200000000}},\quad
\eta_{59}=X-Eh_{59}=-Y+Hh_{59}>0.
\]
The endpoint value \(s(1)=6488639185595039/10444800000000000\) lies between 0 and \(s_{58}\). For every real \(u\in[0,1]\),
\[
e_P=e_Q=\alpha_{58}+\eta_{59}u.
\]
The disjoint tied-state first-arrival cylinders make all four risks affine in u,s (the mixed four-corner coefficient is exactly zero). The selected decisions attain the Bellman minimum, hence
\[
t_P(u)=V_{58}-\Gamma_{59}\eta_{59}u.
\]
Exact backward and forward risk recursions yield
\[
\begin{aligned}
t_P(0)-t_Q(0)&=\frac{327588224513205281}{620845906412961792}>0,\\
t_P(1)-t_Q(1)&=\frac{328510182739260281}{620845906412961792}>0.
\end{aligned}
\]
Affineness gives \(t_P\geq t_Q\) everywhere. Hence the constructed feasible family reaches the universal lower bound for **all real** parameters on the interval, proving the theorem.

## 4. Strict right-end sharpness of this supporting line

The finite horizon randomized occupancy-measure feasible region is a compact polytope. At any parameter where this same line were attained, strict positivity of both multipliers requires \(e_P=e_Q=\alpha\) and all reached actions to attain their Bellman minima. Only A59 and B permit a choice; other action gaps are strictly positive. Even when different ordered histories of a count state are randomized differently, identical continuation suffix risks allow a mass-weighted effective pair \(u,s\in[0,1]\). Their first-arrival cylinders are disjoint. Balancing errors forces \(s=s_{58}-h_{59}u\) and therefore \(\alpha=\alpha_{58}+\eta_{59}u\leq\alpha_{59}\). A larger alpha attaining this same supporting line is impossible.

## 5. Reproduction and remaining obligations

The portable Python-stdlib exact-Fraction program checks all 680 count states, all 1240 Bellman differences, first-hit masses, suffix risks, 7 rational mixing parameters, endpoint time dominance and the next dual candidate. A **separately organized author-side** crosschecker enumerates all nominal words at A59 and a relevant later stop, independently minimizes every Bellman action, then checks backward exact risks at all four (u,s) corners and seven mixtures. Both actually executed and passed locally; they share the inherited stop sets. Therefore this is an **author-level** exact finite-model proof, not a clean independent Driver review, Lean formalization or native BRC/X6/Heartbeat correspondence theorem.

After fixing A59 to immediate Q, the **unproved** next dual crossing is
\[
\boxed{K_{60}=\frac{1259712}{139}},\qquad
\boxed{A_{60}=(11,6,5)}
\]
with continuation/Q tie. Its first-arrival, error compensation, full optimal interval and sharpness remain unproved.

The current native active-owner query returned CONTROL_QUOTA; no owner, formal CLAIM, frozen Result, external review or mathematical admission is inferred. GitHub source publication is author evidence only. P000 and the ACTIVE residual-faithful worldview remain unchanged. The theorem concerns only the declared auxiliary iid finite problem.
