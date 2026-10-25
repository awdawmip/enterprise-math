# Stage143 — exact N=14 full-real optimal affine segment (AUTHOR PROOF)

**Scope and strength.** This is an author computation-assisted exact proof in an external ternary iid sequential decision model, not a P000, X6, Heartbeat or native-BRC theorem; independent Research Driver review and native task admission have not occurred.

## Statement

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14. Tests may randomize based on the **entire ordered ternary history**, stop no later than N, and decide P or Q. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

The predecessor Stage142 author endpoint is
```
alpha142=12238552734313788965/35205614928358539264
V142=24070360310471940161/1955867496019918848
```

**Theorem.** For every **real** 0<=delta<=eta143,

```
eta143=45614547809953/11735204976119513088
V14(alpha142+delta)=V142-(38293991218112550/45614547809953)*delta
alpha143=1529836197244652353/4400701866044817408
V143=1503998623662640921/122241718501244928
```

The supporting line is **strict** below V14(alpha) for every alpha>alpha143 (right-end sharpness).

## Exact dual and complete Bellman gaps

At state s=(n,a,b), where a and b count outcomes 0 and 1, Q(prefix)/P(prefix)=r(s)=2^(a+b)/3^a. The exact dual costs at K=19411949464309662/45614547809953 and L=18882041753802888/45614547809953 are: decide P = K*r(s), decide Q = L, continue = 1+sum(P_i*H(child_i)) (continue not allowed at n=14). Recursing over ALL 680 count states gives

```
Hroot=42222189293875024646776690163383/138821594513174762290616991744
ties: B=(11,0,1), Q/continue; C=(3,3,0), P/continue
other strict positive action gaps: 1238; negative: 0
minimum strict gap: 1685757022745149/59116453961699088
```

By backward induction and iid suffix sufficiency for *every ordered-history policy*,
Hroot <= tP + L*eP + K*eQ <= max(tP,tQ)+(K+L)*alpha.
No restriction to count-Markov competing strategies is made.

## Branch-aware exact primal construction

Use literal ordered words with P positive integer weights (3,1,20)/24 per step and Q weights (1,1,10)/12 per step. B contains no outcome-0 observations while C contains three and has smaller depth, so their entire first-hit path cones are disjoint. However C may precede old J=(4,3,0): J is now **fixed P-stop**, not independently randomized, and its effect is included in C's continuation suffix.

Literal first-hit inventories checked by a separate forward integer-weight DFS:
```
B: 11 words; P mass 107421875/1451188224; Q mass 107421875/725594112
C:  1 word;  P mass 1/512;              Q mass 1/1728
```

Let w be B's immediate Q-stop coin and z C's immediate P-stop coin. All other states choose their strict Bellman-minimizing action. The complete four-vector M=(eP,eQ,tP,tQ) is **exactly affine**:
```
M(w,z)=M00+w*dB+z*dC
M00=(
2428600686317767769/7011906707722862592,
447752847899641/1283918464548864,
10836481648042301591/876488338465357824,
141396978702037/11888133931008)
dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128)
dC=(
-8602848506345/779100745302540288,
801193733/47552535724032,
-84381541471757/32462531054272512,
-105617097053/106993205379072)
```

The four-corner mixed interaction M(1,1)-M(1,0)-M(0,1)+M(0,0) is the zero four-vector exactly, consistent with the disjoint cones. Independent forward integer-weight DFS agrees with backward Fraction observer recursion at **all four** deterministic corners (w,z)=(0,0),(1,0),(0,1),(1,1), visiting respectively 621718, 621586, 608608, 608476 literal prefix nodes.

Solving eP=eQ yields, exactly,
```
w(z)=50180601034414837/81438720000000000
     +(17778769059123/2467840000000000)*z
w(1)=6345912551670737/10179840000000000
```
Thus 0<w(z)<1 throughout z in [0,1]. The resulting eP=eQ=alpha142+eta143*z and tP=V142-(K+L)*eta143*z. The endpoint differences tP-tQ are, respectively,
```
z=0: 82155858325532762167/158425267177613426688 >0
z=1: 80069565131574865/154712174978138112 >0
```
so tP=max(tP,tQ) for **every real** z. The exact endpoint identities tP+L*eP+K*eQ=Hroot extend to the whole segment by affinity. Therefore the constructed policies attain the universal dual lower bound for all real alpha in the stated interval.

## Strict right sharpness

The finite-horizon randomized policy space is compact. If alpha>alpha143 attained the same support, positive K,L and equality in the dual chain force eP=eQ=alpha and every positive-probability selected action to be a Bellman minimizer. Exactly 1238 positive gaps prohibit any mixed action except at B,C. Even arbitrary history-specific coins at a tied count state induce the same four observations as one effective likelihood-weighted coin because prefix Q/P ratio is constant across that state's histories and iid suffixes coincide. Disjoint cones make those two effective coins independent. Error equality then requires the displayed w(z), hence alpha=alpha142+eta143*z<=alpha143. Contradiction: the line is sharp.

## Verification and authority boundaries

Locally **executed**: exact rational 680-state Bellman and four-observer solver, separate forward integer-weight ordered DFS at four corners, and exact dual-ray discovery of Stage144; all tests PASS. The full executed source, output logs, detailed proof and SHA256 manifest are preserved in the user-visible local research archive. The portable GitHub checker is reproducible source, not an assertion of remote execution or independent review.

Read pins: GLOBAL_KNOWLEDGE_V1 main@a7b8a07c3e007b62749724b848c8d96a681e2868; EM initial research input main@77698674b3e3d50ff916d474b309e0a4e906b622; Stage142 actual proof blob 4ba1af74b0f644a2ba38c3d06a9b6dbc4859f727. P000 projection matches original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Connected GitHub login awdawmip does **not** prove native Source ownership. Native task list failed CONTROL_QUOTA; session_start failed STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Current owner, formal CLAIM, immutable Result and independent Driver acceptance remain unverified.
