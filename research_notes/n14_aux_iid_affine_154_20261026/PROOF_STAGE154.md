# Stage154 — second exact full-real interval (external N14 ternary IID auxiliary)

Date 2026-10-26. Status: AUTHOR_EXACT, SOURCE_ONLY, NOT_ADMITTED. Frozen knowledge GLOBAL_KNOWLEDGE_V1 main@c7df6a7f96975759dc1b960a3e0c19134208dbcb; Enterprise Math main@5c8d97aa71aefa1fca7cb10db926634e5dc27aa9. Predecessor Stage153 source-only author proof commit 66111b54accb3d7800d3c32f536f0c5b653ac9a2.

## Theorem
For IID observations P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon 14, and arbitrary randomized COMPLETE ORDERED-HISTORY sequential tests, put eP=P(decide Q), eQ=Q(decide P), tP,tQ the expected stopping times. V14(alpha) minimizes max(tP,tQ) subject to eP,eQ<=alpha.

Stage153 right endpoint:
alpha153 = 18373341781933759925/52808422392537808896,
V153 = 318626572163909741813/26404211196268904448.

For EVERY REAL 0<=delta<=24903625/2200350933022408704:
V14(alpha153+delta)=V153-(136694960/199229)*delta.

New endpoint:
alpha154 = 18373341782531446925/52808422392537808896,
V154 = 318626571958867301813/26404211196268904448.

For alpha>alpha154, the fixed Stage154 dual supporting line is strictly below the true value V14(alpha).

## Dual transition and exhaustive rational Bellman bound
Count state s=(n,a,b) has Q/P likelihood ratio (2/3)^a 2^b. At Stage153 the dual was K153=5994/17, L153=5960/17, and B=(11,0,1) was Q/C tied. Preserve the equality at B along the exact ray dK=-1, dL=-112/129. The old saturated Z=(12,2,2) Q-stop remains locally strict on this side: its continuation-minus-Q gap has derivative +17/13932. Scan every nonchosen action at ALL 680 count states. The first strictly positive gap closes at t=30922074/3386893, for U=(10,5,4) and competing continuation C versus baseline Q-stop. Its old gap is 4439/528768, derivative -199229/216670464.

This yields K154=68426856/199229 and L154=68268104/199229; K154+L154=136694960/199229. A new complete exact Bellman calculation finds H(root)=1824690544010408840595299/7275912299338115579904, exactly two Q/C ties B=(11,0,1), U=(10,5,4), 1238 strictly positive other action gaps (minimum 4439/398458), zero negative gaps. The Bellman bound for every policy is H(root)<=tP+K154 eQ+L154 eP<=max(tP,tQ)+(K154+L154)alpha. Hence V14(alpha)>=H(root)-(K154+L154)alpha. Source-only exact algorithm and dual evidence: SCAN_STAGE154.py and dual154.json.

## Full ordered-history realization and both observers
B and U are incomparable: U has depth10 and a=5, while B has depth11 and a=0; counts never decrease and B is deeper. Thus no ordered path passes both ties. Literal ordered first-hit DFS enumerates B: 11 prefixes with P mass 107421875/1451188224 and Q mass 107421875/725594112; U: 300 prefixes with P mass 125/5435817984 and Q mass 125/2579890176.

All ordered first-hit prefixes sharing a count state have identical likelihood ratio and conditional continuation law. Once first-hit disjointness is proved, every admissible complete-history Bellman-optimal policy has the same four observable coordinates (eP,eQ,tP,tQ) as effective stop-Q coins b,u in [0,1], with exact affine form M00+b dB+u dU. Two structurally different methods (Fraction backward count recurrence and literal ordered-prefix INTEGER DFS with P=(3,1,20)/24, Q=(1,1,10)/12) agree on all 4 deterministic coin corner vectors, 16 rational coordinates total, and zero mixed cross term. The literal DFS visits 473212,466012,473080,465880 ordered prefixes in the respective four corners; all source vectors and logs are in the accompanying reproducible evidence.

Exact eP=eQ balance gives:
b(u)=7483738461750611/8143872000000000
     -(1149859/2714624000000)*u, 0<=u<=1.
This b(u) stays strictly inside (0,1). At u=1 its value 7483735012173611/8143872000000000 matches the already verified Stage153 endpoint (alpha153,V153). At u=0 the resulting policy has (alpha154,V154). Along the whole real u interval alpha(u) decreases strictly and affinely, with alpha(0)-alpha(1)=24903625/2200350933022408704>0. The exact time dominance margins at u=1 and u=0 are respectively
36937438597383360865/79212633588806713344 and
36937439023305630865/79212633588806713344,
both positive. Because the full four-observer path is affine, tP>tQ on EVERY REAL u in [0,1]. In addition tP+K154 eQ+L154 eP=H(root) exactly at both endpoints and hence throughout. The primal feasible family attains the universal dual lower bound for every alpha in the real interval, proving the theorem.

## Strict right sharpness
There are finitely many ordered histories and therefore a compact randomized policy space with attained feasible minima. Equality of V14(alpha) with the Stage154 support line would force (since K,L>0) both errors eP=eQ=alpha, max(tP,tQ)=tP and Bellman minimization at every reached positive-probability history. All other actions have strict gaps, so only the B/U Q/C coin choices remain. The proved disjoint first-hit aggregation gives some b,u in [0,1], and equality of errors forces b=b(u). The maximal balanced alpha in this Bellman-optimal family is alpha154 (at u=0). Thus for every alpha>alpha154 equality is impossible; the support line lies strictly below V14(alpha).

This is an external finite N14 model and does NOT establish a native P000 six-axis discrete Cell or heartbeat theorem. Preserve positive BRC-style branch weights and complete ordered histories; no native CLAIM, Source Result, Driver review or Foundation acceptance exists for this author result. Stage155: hold B Q/C equality while U continuation is saturated at u=0, scan the next exact Bellman gap, and test for mixed first-hit interactions before quotienting ordered history.
