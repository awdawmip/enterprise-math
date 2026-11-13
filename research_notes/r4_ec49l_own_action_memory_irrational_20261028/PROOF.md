# EC49L — Own-action recall does not guarantee rational behavioral realizability

STATUS: AUTHOR_PROVED / EXACT_FRACTION_AND_SYMBOLIC_CHECK_PASS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Author: R4-EC49L-20261028-2126-LOCAL (locally declared TASK_RESEARCH author; no native session/CLAIM).
Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@2799b8b74f23b071340d43d53fd7cc18038d189b; enterprise-math main@7f23e5cb67cd455564317004e377feba60ace1bb. Previous EC49K: PR #1644, commit 192e82d610eab777248ffa134bafe46847e29b53. P000 / ACTIVE unchanged.

## Question and model

For a finite two-source, strictly positive rational auxiliary BRC probability model, may a rational four-vector O=(P(accept),Q(accept),E_PT,E_QT) be achievable by real behavioral probabilities but by no rational behavioral policy, **even though the observer remembers every own action**? YES, within the fully specified information/terminal protocol below. No claim about general perfect recall or native signed BRC/X6 is made.

At the initial decision an external W in {U,V,C0,C1} is observed. P(W)=(3/8,3/8,1/8,1/8) and Q(W)=(1/8,1/8,3/8,3/8), ordered U,V,C0,C1. In U the observer can STOP (reject, T=0) or take first action A=1, taking A=1 with probability p0. In V it can STOP or take A=0, taking A=0 with probability p1. C0 and C1 force the first actions A=0 and A=1, respectively. Any taken first A action costs one observation-count unit. At the second decision the observer retains its **entire own action sequence A** but loses external W, its earlier menu, and information about forcedness. It may buy Y with probability q0 following A=0 or q1 following A=1; purchase adds one T unit, no purchase rejects. Fresh, independent behavioral randomization is used at each observable information set, and no ex ante persistent private seed exists. These are the only legal decisions. After a purchase the terminal rule is FIXED: accept iff Y=1 (no discretionary terminal acceptance).

The second-stage information classes are exactly I0={(V,A0),(C0,A0)} and I1={(U,A1),(C1,A1)}. Thus own-action history is **not** forgotten, while the external W context is forgotten. Conditional sensor success P(Y=1|W)=(1/4,3/4,1/2,1/2) and Q(Y=1|W)=(3/4,1/4,1/2,1/2). Every one of the 8 latent W×Y atoms under EACH source has strictly positive rational probability; the first-stage randomization changes accessible histories but not that latent source table.

## Theorem: rational O with no all-rational behavioral realization

Define u=p0+p1, v=q0+q1, w0=p0*q1, w1=p1*q0, X=u+w0+w1. Exact common-source branch summation gives

    alpha  = (3/32)w0 + (9/32)w1 + (1/16)v
    beta   = (3/32)w0 + (1/32)w1 + (3/16)v
    E_PT   = 1/4 + (3/8)X + (1/8)v
    E_QT   = 3/4 + (1/8)X + (3/8)v.

The constants 1/4 and 3/4 are the expected mandatory first actions in C0/C1, respectively. All action probabilities are common to P and Q; no source-specific controller is smuggled in.

These equations have a rational inverse from O to (u,v,w0,w1): set SP=8(E_PT-1/4), SQ=8(E_QT-3/4), X=(3SP-SQ)/8, v=(3SQ-SP)/8, a'=alpha-v/16, b'=beta-3v/16, w1=4(a'-b'), w0=(32b'-w1)/3, and u=X-w0-w1.

For the rational target

    O*=(7/64, 13/64, 27/32, 41/32),

this inverse returns u=v=1 and w0=w1=1/8. Thus every allowed behavioral implementation satisfies

    p0+p1=1, q0+q1=1, p0*q1=1/8, p1*q0=1/8.

Let x=p0 and y=q1. Then xy=(1-x)(1-y)=1/8, so x+y=1 and x(1-x)=1/8. Hence x obeys x²-x+1/8=0, whose roots are (2±sqrt(2))/4, both strictly between zero and one. For either root, p0=x, p1=1-x, q1=1-x, q0=x implements O*. No root is rational, because 1/2 is not a rational square. Therefore all real behavioral implementations require irrational probabilities: a complete elimination proof, not inference from a finite search.

## Two exact scope-separating constructions

1. Additional external memory: remember just one more bit D=TEST (U/V) vs CALIBRATION (C0/C1) at the second stage. Use p0=p1=1/2; take q=1/4 for either TEST continuation and q=1/2 for either CALIBRATION continuation. All probabilities are rational and direct branch sums reproduce O*. This proves a genuinely external-history-dependent causal obstruction under the specified interface; remembering own action A alone does not repair it. It does NOT establish that this bit preserves the entire observation region.

2. Persistent ex ante random seed: mix the deterministic policy tables (p0,p1,q0,q1)=(0,0,0,0), (0,1,0,1), (1,1,1,1) with rational mixing weights 1/8, 3/4, 1/8. Their O values are (0,0,1/4,3/4), (1/16,3/16,3/4,5/4), (1/2,1/2,2,2); their mixture equals O*. Such a retained random seed correlates decisions across information sets and is NOT the fresh behavioral policy class. For any finite rational model, the convex hull of rational pure-policy O vectors is a rational polytope, so any rational point inside it has rational ex ante mixture weights (basic feasible solution of a rational system). Do not confuse this fact with rational behavioral implementation.

## Exact validation and interpretation

The accompanying VERIFY.py was actually executed locally with Python Fraction plus SymPy; it verifies 16 deterministic behavioral policies, 1296 specified rational grid policies, all 8 positive latent atoms per source, the inverse map, both exact sqrt(2) solutions, the rational external-memory repair, and rational shared-seed mixture. EXACT_REPORT.json contains that program's output. The universal real-policy assertion follows from the displayed algebra, not grid exhaustion. This is a two-step positive branch-mass auxiliary BRC calculation; neither T nor the extra information bit is a native heartbeat time or X6 spatial coordinate. Signed-BRC/X6 correspondence needs independent typed proof.

External background: Ryan A. Anderson & Guido Montúfar, ICML 2026, PMLR 306, pp. 2677–2715, https://proceedings.mlr.press/v306/anderson26a.html , studies infinite-horizon memoryless POMDP semialgebraic value sets. The model and theorem here are finite-horizon with retained own actions; general semialgebraic or rational-polytope insights are not claimed original, and no comprehensive novelty audit is asserted.

Unresolved: remove mandatory calibration branches, permit unrestricted terminal acceptance, classify minimal exact causal lift for entire four-vector region, and test typed signed-BRC/X6 bridge. The present proof is deliberately scoped to a fixed acceptance protocol, fresh behavioral randomization and the specified information partition.
