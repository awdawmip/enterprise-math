# Stage271 — exact all-real Bellman face across Stage270 E–F

Date: 2026-10-29. Portable author label `EM-R2-RESEARCH2-20261029-STAGE271-LOCAL` (not an authenticated Source identity). Evidence status **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Scope: external IID sequential testing model only; there is no claimed P000 native six-axis / Heartbeat Cell dynamics theorem.

## Frozen scientific and control inputs

This proof continues the Stage270 exact source at Enterprise Math immutable commit `7d111f8a174183931b6b391b93b6692678976ac2`, PR #1571. Current scientific rule read snapshot was GLOBAL_KNOWLEDGE_V1 `main@bf2d12d1d8fbbe1efeac9ce8a37d11d6114fba36` and Enterprise Math control `main@4d641868367e435cb350b7dbaa46b02f48f976d3`, including global entry/manual, current mathematical evidence policy, P000, ACTIVE six-dimensional world constraints, source provenance preservation and portable research contract. Native gateway v0.6.11 reported `research_authority_granted=false`, quota five/five active jobs; this is a durable portable author result, not an authenticated Task CLAIM or review.

## Exact model and point theorem

The observations are IID on alphabet {0,1,2} with `P=(1/8,1/24,5/6)` and `Q=(1/12,1/12,5/6)`. A randomized policy can use every complete ordered prefix, decide P or Q, or continue before 12 observations. Set `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P[T]`, `tQ=E_Q[T]`. Define `V12(a,b)=min max(tP,tQ)` among policies `eP<=a, eQ<=b`, with infinity for infeasible caps.

At the Stage271 caps

    a271 = 133853268599/1761205026816
    b271 = 431993556815/557256278016

we prove the exact global optimum

    V12(a271,b271) = 89124381535/15479341056
                   ≈ 5.757634075802871.

The exact dual weights and Bellman root are

    lambdaP = 7566375964672/51849608449
    lambdaQ = 4026978326268/51849608449
    thetaP = 0, thetaQ = 1
    H = 1717930741512259706653/22294382577836949504.

## All-real equality-face theorem

Define four complete four-observer vectors, with coordinates `(eP,eQ,tP,tQ)`:

    E = (1133161305691/15850845241344, 146231594105/185752092672,
         27588964539587/5944066965504, 84859115435/15479341056)
    F = (1279282905691/15850845241344, 425010482315/557256278016,
         10164282046529/1981355655168, 31186005145/5159780352)
    G = (1129087690691/15850845241344, 146299619105/185752092672,
         27612319764587/5944066965504, 84999370435/15479341056)
    Hcorner = (1275209290691/15850845241344, 425214557315/557256278016,
               10172067121529/1981355655168, 93698270435/15479341056).

Each vector is realized by a deterministic full ordered-history policy. The difference `Hcorner−F = G−E` holds exactly in all four observer coordinates. Their two error coordinates form a strictly convex parallelogram

    R271 = conv(E,F,Hcorner,G)
    area(R271) = 101268766501953125/34503839932027276099584.

**For every real `(a,b) in [0,1]^2`,**

    V12(a,b) = H − lambdaP*a − lambdaQ*b
       if and only if (a,b)∈R271.

This R271 shares the complete E—F edge of Stage270's R270. Their interiors are disjoint: `orient(E,F,G)=−101268766501953125/34503839932027276099584`, while the Stage270 old C corner satisfies `orient(E,F,C)=+123370733132421875/69007679864054552199168`. These signs together with strict convexity and common endpoints establish exact adjacency.

## Exact Bellman lower bound and the entire full-history equality set

For counts `s=(i,j,k)` of an ordered prefix, put `p_s=(1/8)^i(1/24)^j(5/6)^k` and `q_s=(1/12)^(i+j)(5/6)^k`. The unnormalized backward Bellman recurrence for each individual history prefix is

    B_s = min(lambdaQ*q_s, lambdaP*p_s, q_s+Σ_{x=0}^2 B_{s+e_x})

before depth 12; there is no continuation at depth 12. The costs represent declaring P, declaring Q and continuing, respectively. Because the two IID likelihoods, all future transitions and these terminal/continuation costs depend only on counts, backward induction proves that this count quotient exactly computes the **full ordered-history** Bellman optimum for the four stated observers, despite allowing history-dependent decisions. The root is exactly H. For every randomized full-history policy,

    lambdaP*eP+lambdaQ*eQ+tQ >= H.

Both multipliers are positive and `max(tP,tQ)>=tQ`, so every feasible policy has `V12(a,b)>=H−lambdaP*a−lambdaQ*b`.

The executed exact `Fraction` checker covers all 455 count states and 1,274 legal action costs, with 817 positive gaps and the least strictly positive gap `1442084699/51366257459336331657216`. The only Bellman ties are `(0,0,5): stop P/continue` and `(1,2,3): stop Q/continue`; all other actions are strictly one-sided. Both ties are at depth 5 and have incompatible counts, so no single ordered path reaches both. Their independently reached ordered-prefix multiplicities are exactly 1 and 20, and the P/Q likelihoods and optimal suffix outcomes are identical at the 20 second-tie prefixes.

Consequently arbitrary full-history randomizations at the latter histories influence the four observers only by their arithmetic mean continuation probability `u`; the former tie has an independent probability `r`. All policies with zero Bellman slack therefore have, and only have,

    Obs(r,u) = E+r*(F−E)+u*(G−E),  0<=r,u<=1.

All four corners have strictly `tQ>tP`; hence every Bellman-minimizing mixture does. Positive multipliers force exact cap saturation `eP=a,eQ=b` whenever the affine lower bound is reached. The errors of all Bellman-equal policies are exactly R271, and the dual lower bound is attained at every R271 point. Since finitely many ordered histories induce a compact family of decision kernels and continuous four observers, any feasible minimum is attained. This excludes a limiting exterior equality point, proving the iff for all real caps.

## Matching exact primal and independent validation

For the target choose the two independent tie continuation probabilities `r=49/100, u=1/50`. The resulting exact observer tuple is

    (133853268599/1761205026816,
     431993556815/557256278016,
     3223592625343/660451885056,
     89124381535/15479341056).

The two errors saturate the caps. `tQ−tP=1737142960451/1981355655168>0`. Its maximum expected time equals `tQ=H−lambdaP*a271−lambdaQ*b271`, establishing exact global optimality.

`REPRO_STAGE271.py` is the actually executed self-contained `fractions.Fraction` verifier with its raw `REPRO_STAGE271_EXECUTED_STDOUT.txt`. Four deterministic strategies were measured in two independent ways: (i) integer multiplicity count-state positive rational P/Q source mass, and (ii) unmerged complete ordered-word DFS, propagating P/Q likelihood separately for every concrete history. Both return identical four-observer tuples; every strategy conserves exact terminal P mass one and Q mass one. The latter traversed **20,224 ordered nodes and 13,484 terminal leaves** across four corners. The actual result is `STAGE271_EXACT_ALL_REAL_FACE_PASS`. Finite arithmetic covers the declared N=12 model; universal quantification over real caps follows from the Bellman theorem, exact affine geometry and compactness, not from a finite point scan.

BRC's provenance and multiplicity principles motivate the carrier, but native typed BRC operations, signed amplitudes and native X6 Cell path geometry have not been implemented or inferred. This exact compression certificate is confined to four declared IID observers, the stopping operations and the finite horizon. A native mapping must separately specify the X6 six-axis path and three-dimensional slice/third coordinate, joint/phase residual carriers, readout and future-update preservation.

## Stage272 strict-exterior feasible frontier

Take the G-corner strategy (continue at `(1,2,3)`), modify all **35 reached ordered histories** with count `(1,2,4)` from stop Q to continue, forming G+. Mix `49/100 G + 49/100 Hcorner + 1/50 G+`. The complete ordered DFS of G+ independently verified 7,633 nodes/5,089 terminal leaves and exact mass one per P/Q source. This mix yields

    a272 = 2401128349757/31701690482688
    b272 = 288133328335/371504185344
    V12(a272,b272) <= 535594465735/92876046336.

It is strictly exterior across R271's G—Hcorner edge: `orient(G,Hcorner,(a272,b272))=−46449501199609375/552061438912436417593344`, whereas E is on its positive side. G+'s Stage271 Lagrangian slack is strictly positive, `521887904513171875/601948329601597636608`. The upper bound is a feasibility theorem, not the Stage272 optimum. Next: derive a matching exact dual or obstruction, all-real adjacent face if full-dimensional, independent ordered mass validation, and retain the current author/admission split.
