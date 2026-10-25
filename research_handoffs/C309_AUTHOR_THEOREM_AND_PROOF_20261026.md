# C309 — Primitive-cancellation content bounds and a sharp Newton-prefix certificate
Date: 2026-10-26. Status: AUTHOR_HAND_PROOF / EXACT_AUTHOR_CHECKS / NOT_SOURCE_ADMITTED.

## Source and ontology
Account rules were read at immutable GLOBAL_KNOWLEDGE_V1 main@c6d252e7e402c453dd0eb291d80b0a8a7e8f6821, including both entry files, P000 startup and ACTIVE worldview. Enterprise Math current main@cda832ba5e9f3c0856c26a607dbe3c9989c042b7 supplied P000 V5, native X6/world and joint-observer constraints, and portable research and ordinary-chat control protocols. Prior author frontier C308 is b87b93cfa78d36029bae3c9d30a4e6f325a577e5. Frozen C293 input SHA256 03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89.

## Theorem 1 — Content survives primitive cancellation
For integer polynomials C,P,J_1,...,J_m, C nonzero primitive, CP=ΣJ_a, and s≥1, define content(0)=0 and
    L=gcd(s,content(J_1),...,content(J_m)).
Then **L | gcd(s,content(P))**.

Proof: L divides every coefficient of ΣJ_a=CP. Gauss's lemma gives content(CP)=content(C)content(P)=content(P), so L divides both s and content(P). A factorized term J_a=c_a Πn_{a,l} Πq^{e_{a,q}} has content |c_a|Πcontent(n_{a,l})Πcontent(q)^{e_{a,q}}, again by Gauss's lemma. Hence this lower bound is computed without expanding a high-degree polynomial or factoring s. QED.

Application to C195/H168: Under the **author-level C300/C305 cancellation identity**, A_shared=(q_1 q_2)A_red, where the q_i are primitive integer linear polynomials. The 79 prepared terms are integer polynomial products, and their exact content gcd gives L_i dividing the scalar observer G_i=gcd(s_i,content(A_red,i)). This implication depends on the upstream identity; it is not a native BRC/X6 quotient or independent proof of that identity.

## Theorem 2 — Certified prefix stopping and its sharpness
Let P∈Z[t] have deg≤d, T∈Z, and write in the monic integral falling-factorial basis
    P=Σ_{k=0}^d B_k e_k,   e_k(t)=Π_{i=0}^{k-1}(t-T-i).
The basis transition is integral unitriangular, so content(P)=gcd(B_0,...,B_d). Assume an exact proven lower divisor L | gcd(s,content(P)). Put g_K=gcd(s,B_0,...,B_K). Then L|g_K, the sequence is decreasing under divisibility, and
    **g_K=L  ⇒  gcd(s,content(P))=L.**

The first K+1 consecutive integer samples suffice to compute g_K with the individually minimal C307 modulus
    N_{K,j}=s H_s(j!) H_s((K-j)!),  0≤j≤K,
where H_s(n) is the part of n supported on primes dividing s. The kth Newton coefficient obeys k!B_k=Σ_{j=0}^k(-1)^{k-j}binom(k,j)P(T+j). For p|s, v_p(binomial(k,j)N_{K,j})≥v_p(s)+v_p(k!), hence using sample residues leaves the kth difference unchanged modulo s H_s(k!). Dividing by H_s(k!) and multiplying by the inverse of k!/H_s(k!) mod s recovers B_k mod s. The formula is valid for K<deg(P) because these lower differences do not use later samples.

Sharpness of the stopping condition in the **prefix-only information model**: if K<d and g_K>L, let
    Q_0=Σ_{k=0}^K B_k e_k,   Q_1=Q_0+L e_{K+1}.
Both have coefficients divisible by L, and agree at all observed nodes T,...,T+K because e_{K+1} vanishes there. Yet G(Q_0)=g_K while G(Q_1)=L. Thus g_K>L cannot fix G under only those assumptions, even if prefix sample values are supplied exactly. This is no lower bound for other structural observations. QED.

## One-point fixed-divisor obstruction
P(t)=t(t−1)+2 has content 1 but is even at every integer input. For s=2, every single observation gcd(2,P(t))=2 fails to equal G=1, while the second Newton coefficient B_2=1 resolves the obstruction. More generally gcd_{n∈Z}P(n)=gcd_{k=0}^d k!B_k; this may strictly exceed coefficient content gcd_k B_k.

## Exact author evidence and boundaries
C309 factorized circuit checked 125 frozen paths, with exact divisibility L_i|G_i|gcd(s_i,A_red,i(T_i)) on all 125, using the earlier C306 exact author G_i as comparison (not as a new independent computation). L_i matched those author G_i in **106/125** paths. Exceptions: 3,6,7,8,11,12,17,26,27,29,30,33,34,38,56,75,76,97,108. None of 125 selected first values or highest-degree coefficient upper bounds equaled its structural L_i. Degrees: 124 paths 352, one path 265. Direct prefix evaluation at minimal stage-specific moduli was executed on **only** paths 0,1,2: exact g_256=L_i=G_i for each. Geometric horizons consumed 521 residue calls per path, more than 353 full-degree single-pass calls, so no speedup is claimed. Independent synthetic exact arithmetic: 2,200 polynomial cases, 14,284 prefix checks and 2,016 constructive indistinguishability witnesses, all PASS. The full author audit/data and executors are in C309 portable research package; the JSON stored alongside this paper is its scope-limited remote summary.

## BRC and control
Here the declared observer is only scalar gcd(s,content(P)). The 79 native-aspiring branch identities, port/provenance, phase/sign and future allowed operations are not erased. No native Heartbeat X6, BRC-Shor or time evolution was computed; P000 remains unchanged. GitHub actor awdawmip has repository push permission. Native gateway v0.6.11 status was readable, but em_control_tasks returned CONTROL_QUOTA and em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Current active Owner, native CLAIM, Result and independent Driver admission were not established. This file is an author branch research handoff, not main-canonical math truth.

## Next discriminating unit
C310: tighten the structural lower bound for the 19 exceptions (coefficient-module syzygies or selected subresultant certificates), validate the upstream C300 cancellation identity independently, and seek actual small-prefix certificates rather than assuming a geometric-horizon runtime win.
