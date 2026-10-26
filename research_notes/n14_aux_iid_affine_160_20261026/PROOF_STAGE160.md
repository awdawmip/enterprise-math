# Stage160 — exact full-real Bellman optimum for external N=14 ternary iid model

**Status:** AUTHOR exact-rational finite-model theorem, locally checked with two author implementations, not an independently reviewed native Result. Input pins: GLOBAL_KNOWLEDGE_V1 main@dd443d4e7201a151c9d30d7eba3ba38edbff2079; EM starting main@666a969f8f6a98b2b5e3d12725e07b1b880d2e8d (Stage159). Native Task owner/CLAIM unverified; local author Researcher-ID EM-R5-Q7C2F8. P000/ACTIVE worldview are starting rules; this external model is not native P000/X6/Heartbeat.

## Theorem

The observations are ternary iid P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=14. For arbitrary randomized full-ordered-history stopping/decision policies, define eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. The verified Stage159 author endpoint is

    alpha159=381583997981821329445/1096459521159585595392
    V159=13168739674988914815857/1096459521159585595392.

Let

    K160=2521611/8218, L160=1229640/4109,
    eta160=102147171875/44615052130516992.

For every REAL 0<=delta<=eta160,

    V14(alpha159+delta)=V159-(4980891/8218)*delta.

The exact right endpoint is

    alpha160=381586508350717329445/1096459521159585595392,
    V160=13167218152253362815857/1096459521159585595392.

The same supporting line is **strictly unattainable for alpha>alpha160** (right sharpness). This does not exclude different subsequent supporting lines.

## Exact universal dual bound

For count state (n,a,b), a+b<=n<=14, ratio Q/P=2^(a+b)/3^a. Define

    H(n,a,b)=min{K160*2^(a+b)/3^a [decide P],
                  L160 [decide Q],
                  1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)
                    +(5/6)H(n+1,a,b) [continue if n<14]}.

The exact Fraction Bellman census covers 680 states and yields exactly two ties, J=(10,2,0) P/continue and S=(13,5,2) P/continue; 1238 strictly positive gaps, smallest 565771/37868544, no negative gaps. It gives

    H(root)=50182333789831153990591/225093161422134706176.

For EVERY history-dependent behavioral policy, the iid conditional law at each ordered prefix, change of measure and backward induction give

    H(root)<=tP+K160*eQ+L160*eP
           <=max(tP,tQ)+(K160+L160)*alpha,

where K160+L160=4980891/8218>0. Thus the last expression defines a global lower support for V14.

## Ordered BRC carrier and exact observer law

Retain labeled ordered prefixes with integer multiplicities, separate positive P/Q weights, stopping decision and horizon, before using the count quotient. The quotient is sufficient ONLY for the four declared observables (eP,eQ,tP,tQ) under iid suffix operations: all prefixes with equal (n,a,b) have the same likelihood ratio and conditional future law; no wider BRC/native equivalence is asserted.

The literal unmerged ordered integer-weight DFS finds at the two first hits:

    J: 45 prefixes; P mass 1953125/11943936; Q mass 1953125/26873856.
    S: 12728 prefixes; P mass 24859375/110075314176; Q mass 24859375/208971104256.

The two path cones are disjoint: going J->S takes only three observation slots (depth 10->13) but requires five increments of the (a,b) counters (2->5 and 0->2). S cannot precede J. The mixed observer vector is identically zero.

Let j=probability of deciding P at J, s=probability of deciding P at S, each in [0,1]. Exact conditional-suffix Fraction DP and a separately implemented literal ordered-prefix integer DFS agree for all four deterministic corners (j,s)=00,01,10,11, with respective visits 484744,446560,483664,445480, and P/Q terminal masses each exactly one.

For M=(eP,eQ,tP,tQ), the exact law for arbitrary real coins is M(j,s)=M00+j*dJ+s*dS, where

    M00=(610396466270800655/1752976676930715648,
         6975157942835/20061226008576,
         2640775790463380201/219122084616339456,
         154719000766399/13374150672384),
    dJ=(-3201171875/3962711310336,
        771484375/557256278016,
        -30224609375/165112971264,
        -4150390625/46438023168),
    dS=(-24859375/2641807540224,
        24859375/2507653251072,
        -24859375/110075314176,
        -24859375/208971104256).

Four-corner mixed differences all vanish; no signed-amplitude cancellation is inferred from positive masses.

## Full-real primal interval

Equalizing errors is equivalent to

    j(s)=107743801834549/461157120000000-(793909/90069750)*s.

For 0<=r<=1 put s=1-r and

    j(r)=103678987754549/461157120000000+(793909/90069750)*r.

Both coins remain legal; j stays strictly interior. Exact substitution gives eP=eQ=alpha159+eta160*r. At r=0 observations reproduce Stage159's author endpoint, and at r=1 yield alpha160,V160 above. Time dominance tP-tQ at these endpoints is respectively

    506498552912101258645/1096459521159585595392 >0,
    505710367439141258645/1096459521159585595392 >0,

hence positive on every real interpolant by affinity. Exact dual equality tP+K160*eQ+L160*eP=H(root) holds at both endpoints and by affinity everywhere. The constructed policies attain the global Bellman support for every real alpha in the stated interval.

## Strict right sharpness for arbitrary full-history policies

The horizon-14 behavioral policy space is a compact finite product of simplices with continuous observer maps, so a constrained optimum exists. Equality with THIS dual line at alpha>alpha160 requires (i) eP=eQ=alpha because K160,L160>0; (ii) tP=max(tP,tQ); and (iii) every positive-mass reached action to be a Bellman minimizer. The strict gap census leaves only J and S tie decisions. Even for prefix-dependent tie randomization, identical conditional suffix law and likelihood ratio within a count fiber allow the P-weighted average coin to represent the same four P/Q observers. The disjoint cones imply M(j,s) above. Equal errors force j=j(s), and common error is strictly decreasing in s; its maximum on the feasible coin box occurs at s=0 and is alpha160. This contradicts alpha>alpha160. Therefore the same support is strictly unattainable to the right.

## Validation, limits and next question

Locally executed PORTABLE_VERIFY_STAGE160.py and a separately written expanded verification program both passed the 680-state census, integer ordered DFS, four-corner equality, zero mixed vector, compensation, endpoint, dominance and exact dual identities. Source code and certificate are attached; this does not imply remote execution or independent Research Driver review. GitHub actor is awdawmip (push=true); native em_control_tasks returned CONTROL_QUOTA and native em_session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The author publication does not assert native CLAIM, frozen Result or Foundation status.

Stage161: Along the J-preserving ray dK=-1,dL=-25280/14751, an exact dual-only author scan finds the first positive closure at t=16778244681/4559354618, K161=168193485/554801, L161=162528200/554801, new R=(10,0,1) Q/continue tie alongside J P/continue. Stage161 primal interval remains unproved; see NEXT_TASK_PACKET_161.md.
