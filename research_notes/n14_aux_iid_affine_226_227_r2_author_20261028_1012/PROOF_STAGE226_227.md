# Stage226–227: exact all-real N=14 IID minimax intervals (author evidence)

Status: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Scope is the external IID auxiliary model, not P000 or a native X6 dynamics theorem.

## Exact model, universal dual bound
P=(3,1,20)/24, Q=(2,2,20)/24; an arbitrary randomized policy uses the complete ordered sequence of up to N=14 observations, stopping to decide P or Q. Define eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP,tQ=the two expected lengths and V14(alpha)=inf_(eP,eQ<=alpha) max(tP,tQ).

At count-state s=(n,a,b), likelihood ratio dP/dQ=(3/2)^a(1/2)^b. For any K>0 the P-weighted Bellman recursion is
B_K(s)=min{K*2^(a+b)/3^a [decide P], K [decide Q], 1+sum_j P_j B_K(next(s,j)) [continue]}; the last action is omitted at n=14. Its root H_K yields tP+K(eP+eQ)>=H_K for *every* full-ordered-history randomized policy by conditioning on the first action and converting Q-error probabilities to P weights. Therefore V14(alpha)>=H_K-2*K*alpha. Count-state aggregation is valid only for this IID additive Bellman certificate; the exact primal verification keeps complete ordered histories unmerged.

## Stage226
Previous endpoint alpha225=312728966121555653/876488338465357824; V225=511537461689062799/54780521154084864.
K226=22581264879576/259377559703; H226=7932877273030669030641345071/111006546064102353706942464.
For EVERY REAL 0<=delta<=6484438992575/2629465015396073472:
V14(alpha225+delta)=V225-(45162529759152/259377559703)*delta.
New alpha226=469096691401829767/1314732507698036736; V226=255756969769073287/27390260577042432.

Exactly two ties in the complete 680-state Bellman enumeration: T=(5,3,1) P/continue, and Z=(14,0,0) P/Q. The other 1238 action gaps are strictly positive, minimum 3959345399/259377559703. At T choose P with probability u (otherwise continue); at Z choose P with probability z (otherwise Q). T has positive symbol-0 and symbol-1 counts whereas Z has neither, so T cannot be an ancestor of Z; Z is terminal. Thus the mixed u*z coefficient of O=(eP,eQ,tP,tQ) is zero. The certificate contains the exact four corner vectors independently computed by Fraction suffix DP and unmerged positive-integer-mass ordered DFS. Equal errors uniquely require
z226(u)=82313414737998927/204800000000000000 - (999830906729/8192000000000000)*u.
Both endpoint coin values lie strictly in (0,1), the common error increases affinely from alpha225 to alpha226, and tP-tQ at the endpoints is respectively 50214638814080399/54780521154084864 and 25103722217534087/27390260577042432, both positive. Every action achieves a Bellman minimum, so tP=H226-2*K226*alpha, matching the universal lower bound for the entire real interval including irrational mixing parameters.

## Stage227
K227=45953726534712/538227241171; H227=493933159371125439911699/7029621308010268532736.
For EVERY REAL 0<=delta<=538227241171/876488338465357824:
V14(alpha226+delta)=V226-(91907453069424/538227241171)*delta.
New alpha227=938194997485383047/2629465015396073472; V227=511508195322329735/54780521154084864.

The 680-state Bellman scan has exactly two ties: T=(4,3,1) P/continue, and Z=(14,0,0) P/Q; all other 1238 action gaps positive (minimum 12710812557/538227241171). The same path-ancestry argument implies zero mixed u*z term. Equal errors uniquely require
z227(u)=41144209482665351/102400000000000000 - (5895669828999/204800000000000000)*u.
Both endpoint coin values are strictly between zero and one; common error is increasing affine; tP-tQ endpoint margins are 25103722217534087/27390260577042432 and 16735238759687725/18260173718028288, both positive. The witness attains the universal Bellman lower bound on the entire real interval. Exact junction:
H227=H226+2*alpha226*(K227-K226).

## Verification semantics
Actual local execution of two full exact Fraction-Bellman and unmerged integer-mass ordered DFS programs produced STAGE226_EXACT_PASS 22636 and STAGE227_EXACT_PASS 20128. A further independently coded compact standalone reference also passed the eight corners and all interval identities, with 22,636 + 20,128 = 42,764 ordered DFS visits. Each stage has 680 states and 1238 strict action gaps. Integer branch weights for both P and Q preserve paths and positive rational BRC-compatible provenance until division by 24^14. The universal real claim is justified by affine identities and exact endpoint inequalities, not by sampling irrational inputs. Two algorithmic implementations are not independent researcher review or Lean verification.

## Stage228 next scientific frontier, dual only
K228=22177458672696/263038955731; H228=238775201049969851829137/3435471315090760605696. Exact 680-state Bellman scan ties: (4,2,2) Q/continue and Z=(14,0,0) P/Q. Exact contact H228=H227+2*alpha227*(K228-K227), with K228<K227, shows strict-right separation of Stage227's FIXED support; no claim of a new primal optimum interval.

## Source/authority limits
This turn fixed GLOBAL_KNOWLEDGE_V1 main@2bccd0522d7ed724311b3ed1c85842b95cdeba8d and Enterprise Math main@65a18bbfac5e5f304f12ca62f4c5529f29a1675f. Project P000 V5 native source Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; global original P000 V4 source blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Predecessor author commit 8f1abc7c883fd7d908d99a2ca66729454ac75abb. The IID finite model is an explicitly external observer, no X6 embedding, native 3D slice or future-operation joint-relation law is established. P000 and ACTIVE worldview unchanged.

Native em_status and Sites confirm research_authority_granted=false (static read-only); em_control_tasks failed with CONTROL_QUOTA. Owner unconfirmed. No native session, CLAIM, Source Result, independent Driver review, mathematical admission, or registered native activity is claimed. Scientific file is portable author evidence, activity REGISTER_PENDING / SYNC_DEBT.