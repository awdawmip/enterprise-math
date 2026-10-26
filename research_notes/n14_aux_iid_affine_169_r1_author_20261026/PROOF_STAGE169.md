# R1 — Stage169: exact interval and right-support sharpness (author computation-assisted)

## Scope, frozen sources and admission status

This theorem concerns an **external positive ternary IID sequential-testing model**, not the P000 native six-dimensional Cell system. There are at most 14 observations, and the policy may randomize, stop and decide on every full ordered history. The two data laws are
(P=(1/8,1/24,5/6)), (Q=(1/12,1/12,5/6)).
Let (e_P=P(	ext{decide }Q)), (e_Q=Q(	ext{decide }P)),
(t_P=E_P	au), (t_Q=E_Q	au), and
(V_{14}(alpha)=min_{max(e_P,e_Q)lealpha}max(t_P,t_Q)).
Finite horizon guarantees attainment. All reported exact computations use rational arithmetic.

Frozen GLOBAL_KNOWLEDGE_V1 main: 97fddf10a23d1b365a89029b1a7bdee752b84d24.
Frozen Enterprise Math main input: 02755d46a9afc42afcf841ba643d27daec5fa20b.
Predecessor: Stage168 author result at immutable commit 253334e2a08694d8a564338414b5ab73ee08f899.
The research mode is locally registered TASK_RESEARCH, with **no native session, Task CLAIM or independent Driver review**. Native control task-list returned CONTROL_QUOTA and native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. GitHub connected identity awdawmip has push permission. This proof is an author result, not a formal Source Result or Working Truth.

## Exact new theorem

Define
[
 alpha_{168}=rac{882432475025404219615}{2530093150022563528704},qquad
 V_{168}=rac{4191390146637112343957}{361441878574651932672}
]
and
[
 eta_{169}=rac{1973578354315}{3904464737689141248}.
]
For **every real** (0ledeltaleeta_{169}),
[
 oxed{V_{14}(alpha_{168}+delta)=V_{168}-
 rac{601328993941480}{1184147012589}delta.}
]
In particular,
[
 oxed{alpha_{169}=rac{882433753904177815735}{2530093150022563528704}},
 qquad
 oxed{V_{169}=rac{4191297370163761372757}{361441878574651932672}}.
]
For every (alpha>alpha_{169}), the **same affine supporting line** is strictly below (V_{14}(alpha)). This is right sharpness of the line, not an assertion that the value function terminates.

## Dual lower bound (all ordered-history policies)

For the IID count state (s=(n,a,b)), where (a) counts symbol 0 and (b) symbol 1, the common likelihood ratio is
(ell(s)=Q(h)/P(h)=2^{a+b}/3^a).
Set
[
 K=rac{100796326719840}{394715670863},qquad
 L=rac{298940013781960}{1184147012589}.
]
Backward induction over all (nle14) gives
[
 H(s)=minigl(Kell(s),L,1+sum_{i=0}^{2}P_iH(s+i)igr)
]
for (n<14), omitting the continuation at (n=14).
This produces 680 count states, 1,238 strictly positive nonminimizing action gaps, no negative gaps, with minimum
(199132488595033/18415854339784128) and
[
 H(arnothing)=
 rac{24482517961003925257583517135827}
 {129736380945356220519564705792}.
]
There are exactly two Bellman ties:
(R=(10,0,1):Q/C) and (Y=(6,4,1):P/C).
All other actions have unique minimizers.

The Bellman recursion evaluates iid conditional action costs but does **not** restrict policies to count-based histories: backward induction, at each full history with count state (s), proves
[
 H(arnothing)le t_P+Ke_Q+Le_P
 le max(t_P,t_Q)+(K+L)alpha
]
for every admissible full-history randomized policy with (e_P,e_Qlealpha).
This is the universal lower bound for the claimed value.

## Genuine ordered paths and primal witnesses

Let (rin[0,1]) be the probability of immediately deciding Q at R (otherwise continue), and (yin[0,1]) the probability of immediately deciding P at Y (otherwise continue). Use the unique Bellman minimizer elsewhere.

An unmerged integer-numerator ordered-prefix DFS (P numerators 3,1,20 divided by 24; Q numerators 1,1,10 divided by 12) gives invariant first-hit information:

| Tie | First-hit ordered histories | P mass | Q mass |
|---|---:|---:|---:|
| R=(10,0,1) | 10 | 9765625/120932352 | 9765625/60466176 |
| Y=(6,4,1) | 18 | 5/32768 | 5/82944 |

Their true ordered first-hit cones are disjoint: a history at Y has four occurrences of symbol 0, while R has zero; counts cannot decrease, so Y cannot precede R. R is already at depth 10 and cannot precede depth-6 Y. Consequently every observer vector (M=(e_P,e_Q,t_P,t_Q)) is **exactly affine**:
[
 M(r,y)=M_{00}+r,Delta_R+y,Delta_Y
]
with no (ry) term. Four independently enumerated deterministic corners from the unmerged ordered-prefix DFS agree exactly with a cached Fraction count-suffix recursion. The integer DFS explores 365077, 352333, 364837 and 352093 nodes in corners (0,0),(0,1),(1,0),(1,1), respectively. Both P- and Q-terminal mass equal exactly 1.

The exact error balance is
[
 e_P-e_Q =
 -rac{44847797844773705}{10517860061584293888}
 +rac{225517578125}{40122452017152}r
 -rac{486031965605}{146081389744226304}y.
]
Thus (e_P=e_Q) iff
[
 oxed{r(y)=rac{8969559568954741}{11823616000000000}
 +rac{874857538089}{1477952000000000}y}.
]
For every (yin[0,1]), both coins are legal, strictly inside R's boundaries, with (y) reaching 1 at the right endpoint. At (y=0), the exact observer equals the inherited Stage168 ((alpha_{168},V_{168})). At (y=1), the values equal ((alpha_{169},V_{169})), and the error increment equals (eta_{169}). The time-dominance gaps (t_P-t_Q) are, respectively,
[
 rac{939301590775510833895}{2530093150022563528704}>0,quad
 rac{939181182760914408775}{2530093150022563528704}>0.
]
At both endpoints (t_P+Ke_Q+Le_P=H(arnothing)) exactly. Affinity preserves error balance, positive time gap and dual equality at **every real** intermediate (y). Since (alpha) grows strictly linearly with (y), the exact theorem follows for the entire real interval, not finite samples.

## Right-support sharpness

The finite full-history behavioral strategy polytope has an attained optimum (equivalently use the compact finite realization-plan polytope). Suppose for (alpha>alpha_{169}) the above supporting lower bound were tight. Since (K,L>0), equality in both inequalities forces (e_P=e_Q=alpha), (t_P=max(t_P,t_Q)), and Bellman-minimizing actions at every visited positive-P history. Strict positivity of every other action gap confines effective randomization to R/Y. Within one count state, the P and Q prefix masses have constant ratio (ell(s)), and the suffix law depends only on s; hence arbitrary history-specific tied coins reduce to a P-weighted effective coin for **all four specified observers**, without assuming the policies were originally count-based. The disjoint cones give (M(r,y)). Error balance forces the displayed (r(y)); feasibility (0le yle1) bounds (alphalealpha_{169}), contradiction. Therefore the same line is strictly below (V_{14}(alpha)) for all larger (alpha).

## Reproducibility, limitations and next

Two locally executed exact programs checked the 680 Bellman states, rational gap spectrum, four corners, literal ordered paths, independent observer agreement, exact inherited endpoint, dual attainment, affine balance and sharpness prerequisites. The portable checker's exact executed source and stdout are stored alongside this proof; the longer independent author source and complete certificate are in the local evidence bundle. No independent Driver review, Lean proof, native CLAIM/Result, native six-dimensional embedding, third-slice-coordinate semantics, or physical correspondence has been established.

The new dual-only Stage170 candidate uses
(K_{170}=4773735/18929), (L_{170}=14183320/56787), with ties R=(10,0,1) Q/C and T=(12,5,2) P/C. That candidate does **not** establish a primal interval; see NEXT_TASK_PACKET_170.md.
