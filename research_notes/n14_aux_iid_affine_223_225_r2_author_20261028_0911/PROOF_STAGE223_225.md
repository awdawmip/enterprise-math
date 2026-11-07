# Stages 223–225 — full-real optimality in the external ternary IID N=14 model

Classification: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Local author provenance EM-R2-20261028-0911-C8A3. This is neither a P000 native X6 theorem nor Source CLAIM/Result or independent Driver admission.

## Problem

Letters j=0,1,2 are IID with P=(3,1,20)/24 and Q=(2,2,20)/24. A randomized decision policy can inspect every **ordered** history, stop no later than N=14, and declare P or Q. Write eP=P(declare Q), eQ=Q(declare P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ).

## Three new theorems

For every real delta (including irrational delta) in the indicated interval:

| Stage | delta range | exact global minimax identity |
| --- | --- | --- |
| 223 | 0<=delta<=655625/219122084616339456 | V14(alpha222+delta)=V222-(944784/5245)delta |
| 224 | 0<=delta<=632226875/106993205379072 | V14(alpha223+delta)=V223-(901291536/5057815)delta |
| 225 | 0<=delta<=3044585424575/2629465015396073472 | V14(alpha224+delta)=V224-(21386261897136/121783416983)delta |

The exact prior author endpoint is alpha222=234542079040923721/657366253849018368, V222=127901570763740681/13695130288521216.

| Stage | new alpha endpoint | new V endpoint |
| --- | --- | --- |
| 223 | 58635519760722649/164341563462254592 | 31975392689089889/3423782572130304 |
| 224 | 58636490861202649/164341563462254592 | 31971787522945889/3423782572130304 |
| 225 | 312728966121555653/876488338465357824 | 511537461689062799/54780521154084864 |

### Universal Bellman bound, including full ordered-history randomized policies

Let s=(n,a,b), where a,b count symbols 0 and 1. The likelihood ratio Q(h)/P(h) for any history h with this s is rho(s)=2^(a+b)/3^a. For K>0 define the finite recursion

B_K(s)=min{ K*rho(s) [declare P], K [declare Q], 1+sum_j P_j B_K(next(s,j)) [continue when n<14] }.

At each ordered history this recursion exactly minimizes the P-conditional continuation contribution to tP+K(eP+eQ). Each declare-P leaf contributes K*Q(h)/P(h); each declare-Q leaf contributes K; each continue action contributes one unit of P-time. Backward induction remains valid even when policy choices use full order, since every conditional future distribution is IID with the declared likelihood ratio. Therefore tP+K(eP+eQ)>=H_K:=B_K(0,0,0) for every randomized ordered-history policy. When both errors are <=alpha, max(tP,tQ)>=H_K-2K*alpha.

The exact Bellman table was exhaustively checked on all 680 triples 0<=a+b<=n<=14 at each of the following K. There are exactly 1238 strictly positive alternative action gaps per stage and exactly the two ties listed (the terminal tie Z=(14,0,0) always has P/Q).

| Stage | K | H_K | other tie T / first action vs continue | minimum strictly positive action gap |
| --- | --- | --- | --- | --- |
| 223 | 472392/5245 | 165229233763072546009/2244717448852930560 | (12,6,4): Q/C | 3955909/293652864 |
| 224 | 450645768/5057815 | 631359661108760304999589/8658429425029616762880 | (6,3,1): P/C | 3955909/327746412 |
| 225 | 10693130948568/121783416983 | 3752369166154801283676185135/52119992580109135830319104 | (5,2,2): Q/C | 3959345399/365350250949 |

### Constructive full-real primal equality

In each stage, choose a Bellman minimizer everywhere, except use probability u in [0,1] for the named first action at T (continue otherwise), and probability z in [0,1] for P at Z (Q otherwise). All T have b>0; Z has b=0 and is terminal. Counts cannot decrease along an ordered history, so no path can traverse both randomized states. Hence for all real u,z (not only four corners), each observer O=(eP,eQ,tP,tQ) has the identity

O(u,z) = O00 + u*(O10-O00) + z*(O01-O00);

the mixed u*z coefficient is exactly zero by path ancestry.

All four deterministic corner vectors O00,O01,O10,O11 were computed with two distinct exact implementations: a cached Fraction suffix dynamic program and an **unmerged full ordered-history integer P/Q branch-mass DFS**. They agree componentwise; the complete rational corner certificate is stored in CERTIFICATE_STAGE223_225.json and is algebraically audited by the delivered local AUDIT_STAGE223_225.py. The complete executable PORTABLE_REFERENCE_STAGE223_225.py was also actually run, not merely written.

Solving eP=eQ gives the unique affine balance laws

z223(u) = 20590441743370313/51200000000000000 + (286071/409600000000000)*u;
z224(u) = 5147610444782297/12800000000000000 - (62448123/200000000000)*u;
z225(u) = 5143613764910297/12800000000000000 + (623779977367/8192000000000000)*u.

Both endpoint values of each z law are strictly between 0 and 1, so every real u in [0,1] is legal. The common error alpha(u) is affine and strictly increasing from the stated left endpoint to the new right endpoint. Exact positive endpoint values for tP-tQ are recorded in the certificate; affinity gives tP>tQ for every intermediate real u. Thus max(tP,tQ)=tP for each witness. All chosen actions are Bellman minimizing at the fixed K, so tP+K(eP+eQ)=H_K. With equal errors alpha, this is tP=H_K-2K*alpha, exactly attaining the universal bound for every real alpha in the full interval. This proves the three minimax identities, not merely a grid of rational samples.

Author exact executions: Stage223 33,616 ordered DFS visits; Stage224 30,286; Stage225 25,996; combined 89,898 visited nodes across four corners of each stage. Independent certificate algebra cross-checks coin solutions, endpoints, path mixed terms, strict tP-tQ, all dual contact identities, and chain junctions. The independent algebra audit does not substitute for independent Driver mathematical review.

### Stage226 boundary and successor

The *dual-only* candidate is K226=22581264879576/259377559703, H226=7932877273030669030641345071/111006546064102353706942464. Its only ties are (5,3,1): P/continue and Z=(14,0,0): P/Q, with 680 states/1238 strictly positive gaps. Exact contact at alpha225 reads H226=H225+2*alpha225*(K226-K225), with K226<K225. Thus for alpha>alpha225 the Stage226 dual lower bound exceeds the **Stage225 fixed support line** by 2*(K225-K226)*(alpha-alpha225)>0. This does not establish a Stage226 primal interval or the next unrestricted breakpoint.

### Domain, provenance, and admission

Nonnegative integer branch masses prod PN_j and prod QN_j retain ordered-path multiplicities before exact normalization by 24^14. Count-state compression is observer- and IID-specific, not a general information erasure theorem. This reuses BRC-compatible exact positive branch bookkeeping, not the native HEARTBEAT_BRC_ONLY dynamical arithmetic. No X6 embedding, future-operation joint-relation preservation, native 6D spatial Cell dynamics, or separately typed native time law is inferred from this external model. P000 and the ACTIVE worldview remain fixed starting assumptions, not conclusions of the IID model.

Pinned source reads: GLOBAL_KNOWLEDGE_V1 main@3ce1b19228802465e194f999bffdfcd5bd8de0db; Enterprise Math main@f9f753b0cccfbcff5fe36f6d91030b1cb9c426a3; prior scientific branch HEAD 78ca6610ef2286750495104b6acaef67161bfc7f; native P000 Git Blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Native research authority was false and current owner lookup returned CONTROL_QUOTA; no current owner/CLAIM/Source Result or independent Driver mathematical admission was established. This is verifiable **author evidence only**.
