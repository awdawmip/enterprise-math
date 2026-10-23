# N=14 auxiliary iid sequential test: 64th exact optimal affine interval

**2026-10-24. AUTHOR EXACT FINITE-MODEL PROOF; DRIVER UNREVIEWED; NOT A FORMAL ENTERPRISE MATH RESULT.**

## Provenance and exact model
This continues the 63rd author-level proof at `enterprise-math@05ed5dcc5c8b5ae1403e7a16a3b73468d0f475cb`, `research_notes/n14_aux_iid_affine_63_20261024/PROOF.en.md`. Account knowledge pinned at verified `GLOBAL_KNOWLEDGE_V1 main@dae2d3974fa237fbf09aea29233e8a9b21a9d42d`; EM source read at `main@21c62ae4aafd8ecde26d38a44eb60ce9b421382b`. This is an external auxiliary iid mathematical model, not a native Heartbeat/X6 experiment or physical-residual claim.

Under iid alternatives P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), an arbitrary ordered-history-dependent randomized policy stops by time N=14 and decides P or Q. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf {max(tP,tQ): eP,eQ<=alpha}.

Inherited exact anchor:
alpha63=5171859005503598567/14900301753911083008;
V63=12336363560670376789/931268859619442688;
s63=26146535894657099/41779200000000000.
Here s is the immediate-Q probability at balancing state B=(12,0,1), and the previously tied A63=(9,2,3) is now fixed to immediate Q.

Define K64=2103023591496/315065929, lambdaQ=K64,
lambdaP=72+(8/9)K64=1892039050440/315065929,
Gamma64=lambdaP+lambdaQ=3995062641936/315065929,
eta64=1575329645/103474317735493632.

**THEOREM (all real parameters).** For every real delta in [0,eta64], including irrational delta,

V14(alpha63+delta)=V63-Gamma64*delta.

The exact right endpoint and optimal value are
alpha64=5171859232351067447/14900301753911083008,
V14(alpha64)=12336183782851489669/931268859619442688.
This is the sharp right endpoint of *this support line*, not the end of the global value function.

## I. Universal lower bound
At count state (n,a,b), a and b count the first two symbols, and the prefix likelihood ratio Q(h)/P(h)=L(n,a,b)=2^(a+b)/3^a. Define the P-normalized Bellman minimum D(n,a,b) backwards as the minimum of
(1) immediate P: lambdaQ*L;
(2) immediate Q: lambdaP;
(3) continue: 1+sum_i P_i*D(child_i),
with the third option omitted at n=14.

Under iid sampling, any histories with the same (n,a,b) have identical conditional futures and likelihood ratio, so this conditional Bellman quotient applies even to the full class of randomized ordered-history-dependent policies. It does NOT permit dropping first-stop path provenance when evaluating any policy.

The complete exact-rational verification checks 680 states, 1240 nonchosen-action gaps, 1238 strictly positive and zero negative gaps. Precisely two zero gaps occur:
A64=(6,5,0): CONTINUE versus immediate P;
B=(12,0,1): CONTINUE versus immediate Q.
Minimum positive gap=734765377967/13066414207488.
The exact root is
D(0,0,0)=19047875907885376670263883141/4314868947128974955249664
          =V63+Gamma64*alpha63.

Since lambdaP and lambdaQ are strictly positive, for any alpha-feasible policy,
D(root)<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma64*alpha.
Thus V14(alpha)>=D(root)-Gamma64*alpha universally.

## II. Exact first-hit masses and attaining family
Keep all previously established deterministic stops (including fixed immediate Q at A63). The new tie state A=(6,5,0) has 6 nominal ordered histories; **all 6 survive** every earlier stopping rule. Its exact first-hit masses are
pA=5/32768 and qA=5/248832.
The balancing state B has 12 nominal and 12 surviving histories, with
pB=48828125/725594112, qB=48828125/362797056.

For continuation followed by the inherited deterministic policy, conditional risk tuples (eP,eQ,tP,tQ) are
RA=(4270381/6115295232, 213669785/214990848, 923168579/764411904, 26184445/17915904);
RB=(63/64, 1/144, 9/8, 13/12).

At A randomize between immediate P (probability u) and continuation; at B randomize between immediate Q (probability s) and continuation, 0<=u,s<=1.
Define
X=pA*eP(RA)=21351905/200385994162176;
Y=qA*(1-eQ(RA))=6605315/53496602689536;
E=pB*(1-eP(RB))=48828125/46438023168;
H=qB*eQ(RB)=48828125/52242776064.

No ordered history can visit both A and B: their first-symbol counts are aA=5 and aB=0, whereas a never decreases. Exact four-corner backward recursion additionally verifies that the mixed u*s coefficient is zero for all four risks. Therefore, relative to the inherited anchor (u,s)=(0,s63),
Delta eP=-X*u+E*(s-s63);
Delta eQ=Y*u-H*(s-s63).

Take h64=(X+Y)/(E+H)=20161471343/174080000000000 and s=s63+h64*u. Its endpoint is
s64=26151374647779419/41779200000000000,
so 0<s63<=s<=s64<1 for the whole parameter interval.
The two error coordinates are exactly equal:
eP=eQ=alpha63+eta64*u,
where eta64=Y-H*h64=E*h64-X=1575329645/103474317735493632>0.

Exact full-tree forward recurrence yields tP=V63-Gamma64*eta64*u and endpoint gaps
(tP-tQ) at u=0:
640187516716220513/1241691812825923584>0;
at u=1:
640005246393385873/1241691812825923584>0.
Because all four risks are affine functions of u (the mixed term is zero), tP>tQ for all real u in [0,1]. This attaining policy matches the global Bellman bound, proving the entire real affine interval.

Ordered first-stop evidence is necessary: at the old terminal-P state (7,6,0), all 6 previously surviving terminal histories pass through A. At terminal-P state (7,5,0), 6 of the 21 surviving terminal histories pass through A. Early stopping at A truncates these descendants; summing nominal terminal-state masses as independent contributions would double count.

## III. Sharp right endpoint
Suppose alpha>alpha64 and some alpha-feasible policy attains the same support line. A minimizer exists: N=14 yields finitely many ordered histories and a compact polytope of randomized policy probabilities. Equality in the Bellman lower bound forces use exclusively of minimizing actions at every positively reached history. The strictly positive gaps leave only A and B free to randomize. History-specific choices at the same count state can be averaged over its first-hit masses into effective u,s in [0,1], because likelihood ratio and conditional futures coincide at that state. Equality in the alpha upper bound and positivity of both multipliers force eP=eQ=alpha. The two exact affine equations then imply s=s63+h64*u and alpha=alpha63+eta64*u<=alpha64, contradiction. Hence this support line ceases to be optimal immediately to the right of alpha64.

## Reproducible exact verification, source and limits
`verify_n14_64.py` recomputes complete Fraction Bellman gaps, first-hit mass, conditional suffix risks, forward risks, endpoint margins, seven exact rational mixtures and the next-dual scan. `verify_n14_64_crosscheck.py` uses a separately organized Bellman minimization, enumerates all 3^6 length-six words for A and all 3^12 length-twelve words for B, checks old descendant terminal cuts, verifies the zero mixed term via four-corner backward recursion, and checks seven rational mixtures. Both executed locally and returned PASS; the two authorship-side checks share the inherited stop-set assumption and **are not independent Research Driver review, Lean formalization or native physical validation**.

For this auxiliary model, the provenance-preserving branch carrier is (ordered-prefix label, P-weight, Q-weight), with alternative addition and independent serial multiplication in nonnegative rationals. Conditional count compression is justified for this iid Bellman observer; first-stop masks remain required for risk and future history-dependent observations. This supplies a typed positive-mass BRC-compatible calculation, *not* execution of an actual native BRC dynamics engine nor a proven bridge to Heartbeat X6.

The next **unproved candidate** K65=832984560/130907 at A65=(9,6,1) has CONTINUE versus immediate P as competing actions. Actual first arrivals, descendant interactions, balancing h65, eta65 and sharpness are open.

At intake, native task inventory returned CONTROL_QUOTA and session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The active Owner and formal CLAIM are therefore unverified. GitHub source persistence is authorship provenance only, not a formal Task Result or a Driver disposition.
