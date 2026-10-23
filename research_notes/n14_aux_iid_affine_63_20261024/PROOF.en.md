# N=14 auxiliary iid sequential test: 63rd exact optimal affine interval

**2026-10-24 — AUTHOR EXACT FINITE-MODEL PROOF; DRIVER UNREVIEWED; NOT A FORMAL ENTERPRISE MATH RESULT**

Source: inherited 62nd exact author proof at enterprise-math@ee3f360b93c18bb4d4681de656dc0428290d8876, path research_notes/n14_aux_iid_affine_62_20261024/PROOF.en.md. The 62nd verifier Git blob bbf102f8459fd5e69ea86aa668b60e2205146910 was checked against the locally inherited research package. Account knowledge snapshot GLOBAL_KNOWLEDGE_V1 main@c7595dc39a2a68074c2c732a0a8b5c16d3a4e60a, Enterprise Math read main@49b2545cb2cdcde3b7ac32d7821c57fdb6f2f412. The P000 projection's original blob pointer 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches the original file. The iid decision problem is an **auxiliary external mathematical model**. No native BRC/X6/Heartbeat faithful map, independent Driver acceptance, or frozen Result is asserted.

## Exact problem and theorem

Under two iid laws on symbols 0,1,2,
P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14.
All randomized ordered-history-dependent stop and P/Q-decision policies are permitted. Set eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf{max(tP,tQ): eP,eQ <= alpha}.

The inherited exact frontier is:
alpha62=5171858457511598567/14900301753911083008;
V62=12336844228881016789/931268859619442688;
s62=26159228380097099/41779200000000000, where s is the immediate-Q probability at B=(12,0,1).

Put
K63=10902924/1475,
lambdaQ=K63,
lambdaP=72+(8/9)K63=9797688/1475,
Gamma63=lambdaP+lambdaQ=20700612/1475,
eta63=39640625/1077857476411392.

**Theorem.** For every real delta in [0,eta63], including irrational delta,

V14(alpha62+delta)=V62-Gamma63*delta.

The exact sharp right endpoint of *this supporting line* is

alpha63=5171859005503598567/14900301753911083008,
V14(alpha63)=12336363560670376789/931268859619442688.

This does not assert the full value function ends at alpha63.

## I. Universal Bellman lower bound

State (n,a,b) counts symbols 0 and 1 in the first n observations. At every ordered history with those counts the likelihood ratio Q(h)/P(h)=L(n,a,b)=2^(a+b)/3^a. Using the P-normalized Lagrangian tP+lambdaP*eP+lambdaQ*eQ, define

D(n,a,b)=min{lambdaQ*L(n,a,b), lambdaP, 1+sum_i P_i D(child_i(n,a,b))},

where continuation is omitted at n=14. The alternatives are immediate P, immediate Q, continue. After a given history the conditional future iid distribution and relative P/Q prefix weight depend only on (n,a,b). Therefore this count-indexed backward minimization is valid for **every** history-dependent random stopping/decision policy, including histories with distinct origins. First-stop survival is nevertheless retained when constructing an attaining strategy.

The complete exact-rational backward computation covers 680 states and 1,240 nonchosen-action comparisons. Exactly 1,238 gaps are positive (minimum strictly positive gap 239707/2548800), none negative, and exactly two zero gaps:
A63=(9,2,3), CONTINUE versus immediate Q;
B=(12,0,1), CONTINUE versus immediate Q.

The exact root is
D(0,0,0)=1578702717230407050462403/323205074809100697600 = V62+Gamma63*alpha62.

Since lambdaP,lambdaQ>0, for any admissible strategy D(root)<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma63*alpha. Consequently V14(alpha)>=D(root)-Gamma63*alpha globally.

## II. Exact first arrivals and attaining policies

The inherited deterministic 62nd tree is fully reproduced by two explicit terminal stop sets SP/SQ plus integer terminal inequalities in verify_n14_63.py, with old tie A62=(10,4,0) fixed to immediate P.

Of 3^9=19683 ordered words of length 9, 1260 nominally attain A63=(9,2,3). Exactly **774** survive earlier stops; **486** are truncated. Their first-hit P,Q masses are

pA=26875/63700992, qA=26875/17915904.

At B=(12,0,1), all 12 nominal ordered prefixes survive; pB=48828125/725594112, qB=48828125/362797056.

The conditional risks (eP,eQ,tP,tQ) of **continuing** at the two tie states, then following the inherited deterministic policy, are

RA=(98221/98304, 41/248832, 15703/12288, 24331/20736);
RB=(63/64, 1/144, 9/8, 13/12).

Let u in [0,1] be the probability of *immediate Q* at A instead of continuing. Let s be the corresponding immediate-Q probability at B. Define

X=pA*(1-eP(RA))=2230625/6262062317568,
Y=qA*eQ(RA)=1101875/4458050224128,
E=pB*(1-eP(RB))=48828125/46438023168,
H=qB*eQ(RB)=48828125/52242776064.

The two error changes relative to (u,s)=(0,s62) are exactly
Delta eP = X*u + E*(s-s62),
Delta eQ = -Y*u - H*(s-s62).

There is no product u*s: A already has two symbol-0 occurrences, whereas B has none, so A cannot precede B; n_B>n_A, so B cannot precede A. Independent four-corner backward risk recursion also establishes zero mixed difference for *all four* risks.

Choose h63=(X+Y)/(E+H)=13221339/43520000000 and s=s62-h63*u. Then the whole parameter path obeys 0<s63<=s<=s62<1, where
s63=26146535894657099/41779200000000000.

Both error rates bind:
eP=eQ=alpha62+eta63*u,
eta63=X-E*h63=H*h63-Y=39640625/1077857476411392 > 0.

Exact forward recurrence yields tP=V62-Gamma63*eta63*u. The endpoint margins are

(tP-tQ)|u=0 = 638697869546300513/1241691812825923584 > 0;
(tP-tQ)|u=1 = 640187516716220513/1241691812825923584 > 0.

The four-corner result means all four risks depend affinely on u. Therefore tP>tQ throughout the *whole real interval*, not only the seven checked rational test points, and the global lower bound is attained. Taking delta=eta63*u proves the theorem.

**First-stop provenance:** The inherited immediate-Q successor (10,2,3) has 1530 actually surviving terminal histories, of which 774 pass through A63. If A63 is randomized to stop, those descendant paths must be cut; summing nominal stopping masses would double count. Both checkers preserve earlier stopping order.

## III. Sharpness of this line

Any strategy achieving equality in the Bellman lower bound must use Bellman-minimizing actions at all positively reachable histories. All non-tie alternatives have strict positive slack, so only A and B may randomize. All surviving histories with the same count-state have equal likelihood ratio and conditional future laws, allowing their history-specific mixing probabilities to be aggregated to effective u,s in [0,1]. Positivity of lambdaP,lambdaQ forces *both* constrained error rates to equal alpha if equality is attained. Their two affine equations then force s=s62-h63*u and alpha=alpha62+eta63*u <= alpha63. Thus no alpha>alpha63 can attain this same supporting line.

## Reproducible scope, scientific provenance, and successor

The first exact Python verifier applies Fraction DP, complete state action comparison, weighted first-hit recursion, all four risk coordinates, endpoint margins and the next-dual scan. A separately organized author cross-check explicitly enumerates 3^9 ordered words at A and 3^12 at B, recomputes Bellman minima, calculates backward risks, verifies four-corner zero interaction and seven exact randomization points. Both were executed locally on these inputs and returned PASS. They share the inherited stopping-set premise: this is **author-level exact verification**, not blind external review, Lean formalization, or native Heartbeat/BRC physics.

The first unproved next exact Bellman crossing is K64=2103023591496/315065929, at A64=(6,5,0), CONTINUE versus immediate P. Its new reachable-history mass, successor interactions, compensation equation, exact affine interval and sharpness remain open.

Control-plane query returned CONTROL_QUOTA. Native new-session registration returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Hence current active owner and formal CLAIM were not verified. This author note is not a frozen Task Result, nor does connected GitHub write capability substitute for native execution authorization. No Drive route is used to bypass the native denial.
