# Exact 55th affine interval of the N=14 auxiliary iid sequential test

**Date:** 2026-10-23. **Status:** AUTHOR-LEVEL exact finite-model proof, two author-side checks; **NOT** independent Research Driver review, native CLAIM/Result freeze, Lean formalization, or a theorem about native BRC/X6/Heartbeat. P000 and ACTIVE worldview remain unchanged.

## Model, provenance and theorem

Let (P=(1/8,1/24,5/6)), (Q=(1/12,1/12,5/6)) be iid three-symbol laws. A randomized stopping and terminal-decision strategy can depend on the entire ordered history, with horizon (N=14). Write (e_P=P(mathrm{decide Q})), (e_Q=Q(mathrm{decide P})); let (t_P,t_Q) be expected sample counts, and
[
V_{14}(alpha)=inf_{e_P,e_Qleqalpha}max(t_P,t_Q).
]
At the inherited 54th right endpoint (see source note and checker at `main@1da5fc197dab4e64dc27c97f298cb347475b2e6f`):
[
alpha_{54}=rac{1292956446620724215}{3725075438477770752},quad
V_{54}=rac{24752812246356430757}{1862537719238885376},quad
s_{54}=rac{6623086977728539}{10444800000000000}.
]
Here (s) is the probability of immediate Q at (B=(12,0,1)). Earlier deterministic stopping actions, including immediate Q at (A_{54}=(7,3,4)), are explicitly inherited in the attached portable checker.

**Theorem:** Put (K_{55}=183708/13), (Gamma_{55}=347940/13), (eta_{55}=89375/718571650940928). For **all real**
[
0leqdeltaleqeta_{55},qquad
oxed{V_{14}(alpha_{54}+delta)=V_{54}-Gamma_{55}delta.}
]
The sharp right breakpoint and value are
[
oxed{alpha_{55}=rac{1292956447084044215}{3725075438477770752}},qquad
oxed{V_{55}=rac{24752806046065630757}{1862537719238885376}}.
]

## Full global dual certificate

Write the count state (x=(n,a,b)), where (a,b) count symbols 0 and 1; the history likelihood ratio is (r(x)=Q(h)/P(h)=2^{a+b}/3^a).
Set (lambda_Q=K_{55}=183708/13), (lambda_P=72+(8/9)K_{55}=164232/13). Define the exact rational Bellman value
[
D(x)=min{lambda_Qr(x) [P], lambda_P [Q],1+sum_iP_iD(x+i) [C]},
]
with continuation omitted at (n=14). Exhaustively check all 680 count states and 1240 alternative-action comparisons: exactly 1238 are strictly positive, none negative; the only equalities are (C=P) at (A_{55}=(12,7,2)) and (C=Q) at (B=(12,0,1)). The root is
[
D(0,0,0)=rac{13250436445753530899023}{1424293550006206464}
=V_{54}+Gamma_{55}alpha_{54}.
]
Backward induction at each *ordered* history justifies this as a bound even for history-adaptive randomized policies; hence
(D(0,0,0)le t_P+lambda_Pe_P+lambda_Qe_Qlemax(t_P,t_Q)+Gamma_{55}alpha).

## Exact first stops, compensation and primal attainment

There are (12!/(7!2!3!)=7920) nominal ordered histories ending at (A_{55}). Applying the complete inherited first-stop tree eliminates 1980; **5940 are first hits**, with masses
[
p_A=rac{6875}{2415919104},qquad
q_A=rac{6875}{10319560704}.
]
All 12 histories leading to (B) are first hits, with masses (p_B=48828125/725594112), (q_B=48828125/362797056). Conditional on *continuation*, the quadruples ((e_P,e_Q,t_P,t_Q)) are
[
c_A=(1/576, 143/144, 25/24, 13/12),quad
c_B=(63/64, 1/144, 9/8, 13/12).
]
The two states are at the same time depth (n=12) and have disjoint ordered-history cylinders; neither randomization coin changes the other's first-arrival mass. Put
[
X=p_Ac_A.e_P=rac{6875}{1391569403904},quad
Y=q_A(1-c_A.e_Q)=rac{6875}{1486016741376},
]
[
E=p_B(1-c_B.e_P)=rac{48828125}{46438023168},quad
H=q_Bc_B.e_Q=rac{48828125}{52242776064}.
]
Randomly decide P at (A_{55}) with probability (uin[0,1]), and decide Q at (B) with probability (s). Relative to ((u,s)=(0,s_{54})):
[
e_P-alpha_{54}=-Xu+E(s-s_{54}),quad
e_Q-alpha_{54}=Yu-H(s-s_{54}).
]
Taking
[
s=s_{54}+h_{55}u,quad
h_{55}=rac{X+Y}{E+H}=rac{83853}{17408000000}
]
makes the errors equal:
[
e_P=e_Q=alpha_{54}+eta_{55}u,quad
eta_{55}=Eh_{55}-X=Y-Hh_{55}=rac{89375}{718571650940928}>0.
]
All coins are valid, with (0<s_{54}le sle s_{55}<1) and (s_{55}=6623137289528539/10444800000000000). Exact expectations satisfy
[
t_P(u)=V_{54}-Gamma_{55}eta_{55}u.
]
The affine difference (t_P-t_Q) is positive at both endpoints: respectively
(875360315426015843/1862537719238885376) and (875356767487775843/1862537719238885376). It is therefore positive for all (u). This construction attains the global dual bound on the **entire real interval**, not just tested sample parameters.

## Sharpness for all history-dependent randomized strategies

Assume the same support line were optimal for some (alpha>alpha_{55}). A finite-horizon policy has a compact occupation-measure polytope, hence a minimizer exists. Equality in the dual inequalities, with both multipliers strictly positive, forces (e_P=e_Q=alpha). The complete Bellman slack certificate forces only minimizers at all positive-mass histories: apart from fixed actions, the sole randomization sites are (A_{55}) and (B). Histories with identical count state have identical continuation likelihood and cost, so their choices can be weighted-averaged to effective (u,sin[0,1]) without changing either error or expected sample count. Solving the exact two error equalities forces (s=s_{54}+h_{55}u) and (alpha=alpha_{54}+eta_{55}ulealpha_{55}), contradiction. Thus **this specific dual line** is sharp at (alpha_{55}), not the entire value function.

## Reproduction, status and next scientific question

The portable Fraction checker enumerates 680 states, 1240 comparisons, the exact inherited first-stop tree, the conditional suffixes, five rational mixtures, and the next crossing. A separate author-side checker enumerates all (3^{12}=531441) ordered strings for each target, independently minimizes the Bellman recursion and verifies four absorbing-DP corners plus affine interpolation. The implementations share authored first-stop rules, so **neither constitutes an independent Research Driver review**. Evidence is scoped solely to the auxiliary finite model; no native BRC arithmetic, Lean proof, or physical bridge has been established.

**Next dual candidate only:** (K_{56}=1211436/91), (A_{56}=(9,0,2)), with continuation/immediate-Q tie after fixing (A_{55}) to immediate P. The 56th first-hit mass, descendant impacts, balancing and full optimal interval remain open.

Fixed provenance: global `GLOBAL_KNOWLEDGE_V1 main@14984f59f1539e8fe47c5d3aee52cdefd798ec0a`; Enterprise Math source prepublication `main@1da5fc197dab4e64dc27c97f298cb347475b2e6f`; existing Research5 author activity `RA-R5N14-20261023-RESEARCH5-T11`. The native tasks query currently returned `CONTROL_QUOTA`; no active owner or native CLAIM was verified. This is an **author research note**, not a formal frozen Result.
