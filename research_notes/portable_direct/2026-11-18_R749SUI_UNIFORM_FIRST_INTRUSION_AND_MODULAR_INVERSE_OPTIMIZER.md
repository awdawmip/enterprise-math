# R749SUI — Uniform first-intrusion bounds and exact modular-inverse optimizer for two-Port BRC feedback

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_EXACT_NOT_REVIEWED**.

**Scientific input:** frozen WBRC-T30–T32 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This directly extends R749SUH, exact file at commit 03e7f84252e49636364754a5073ced7a68dca227, and its SUE/SUF/SUG dependencies. The subject is the labeled positive-rational WBRC Port *auxiliary feedback-bin* observer. It is not an admission of native P000/X6 events. P000, six native spatial axes, the distinct time axis, triadic closure, typed resources and source provenance are retained without alteration.

## 1. Definitions

For integers M≥2, let U_M be the labeled quadruples (a,u,v,d) in {1,...,M}^4 satisfying ad-uv=1. Set tau=max(u,v)ad. The canonical adjacent-diagonal family consists of a=d and {u,v}={a-1,a+1}, with all entries in range. Other quadruples are *noncanonical*. Write T*(M) for their maximal tau. Let F_j=(M-j+1)(M-j)^2 for 1≤j≤M-2 and let J(M)=#{j:F_j>T*(M)}.

R749SUH proved the protected prefix J(M)≥j0(M), where j0(M)=max({0}∪{1≤j≤M-2:(3j-1)^2<4(M+1)}), equal to (2/3)sqrt(M)+O(1), and proved T*(M)≤(M-(2/3)sqrt(M+1))^3 for M≥6. Its sharp crossover asymptotic was previously along M=t²-1.

## 2. Theorem A — Uniform construction

For every integer M≥15, put t=floor(sqrt(M+1)), m=t²-1 and delta=M-m. Thus t≥4 and 0≤delta≤2t. The tuple

A_t=(m-t, m, t(t-2), m-t)

belongs to U_M, is noncanonical, and has

W_t=tau(A_t)=m(m-t)²=(M-delta)(M-delta-t)².

**Proof.** For t≥4 the entries are positive and at most m≤M. Direct integer expansion gives (m-t)²-m*t*(t-2)=1. Its two off-diagonal entries differ by 2t-1, greater than 2, hence it is noncanonical. The bounds on delta follow immediately from t²≤M+1<(t+1)². QED.

## 3. Theorem B — All-M square-root crossover

For **every integer M≥15**,

j0(M) ≤ J(M) ≤ 3 floor(sqrt(M+1))-1.

In particular, J(M)=Theta(sqrt M) along the full integer sequence, not merely a square-minus-one subsequence. Moreover,

M³-(M-(2/3)sqrt(M+1))³ ≤ M³-T*(M) ≤ 8M² floor(sqrt(M+1)),

so T*(M)=M³-Theta(M^(5/2)) uniformly as M→∞.

**Proof.** Use the previous R749SUH lower bound and upper envelope. For t≥4, j=3t≤M-2. Since delta≤2t, we have M-delta > M-3t+1 and M-delta-t≥M-3t>0. Thus

T*(M) ≥ W_t > (M-3t+1)(M-3t)²=F_(3t).

The F_j are strictly decreasing, giving J(M)≤3t-1. To bound the cubic deficit use 0≤x=delta/M≤1 and 0≤y=(delta+t)/M≤1. Then

M³-W_t=M³[1-(1-x)(1-y)²] ≤ M³(x+2y)
=(3delta+2t)M² ≤8tM².

Combining this bound with R749SUH's T* upper envelope proves both inequalities and the stated asymptotic orders. QED.

## 4. Theorem C — Exact modular-inverse winner algorithm

Orient each off-diagonal pair so u=max(u,v). For each a,u in [1,M] with u≥2 and gcd(a,u)=1, let

D=min(M,floor((u²+1)/a)); r in [1,u-1] satisfy ar≡1 mod u.

If D≥r, put d*=r+u floor((D-r)/u) and v*=(ad*-1)/u. Retain (a,u,v*,d*) precisely when ad*≥u+1 and it is noncanonical. For u=1 the only feasible tuples are (1,1,1,2) and (2,1,1,1). Then

T*(M) = max( {2} union {u*a*d*: retained (a,u)} ).

All labeled maximizers and their exact multiplicity are recovered: output the orientation-swapped partner (a,v*,u,d*) when u>v*, but only once when u=v*. This requires O(M² log M) arithmetic operations using exact gcd and modular inverses; output-space aside, the search is O(M²) oriented pairs.

**Proof.** From ad-uv=1 we get gcd(a,u)=1, d≡a^(-1) mod u, and v=(ad-1)/u. The bounds 1≤v≤u and 1≤d≤M are exactly ad≥u+1 and d≤D. The largest possible d in the required residue class is d*, and tau=uad strictly increases with d. If d* is canonical, d*=a<u=a+1, so its next smaller congruent d*-u is nonpositive and there is no noncanonical candidate for this pair. If u=1, ad-v=1 with v≤u=1 forces ad=2. Every labeled tuple is covered exactly once after the indicated orientation rule. QED.

## 5. Exact computational evidence

The companion dependency-free Python certificate enumerates all labeled integer matrices in a separate exhaustive loop, and independently computes the fast modular-inverse optimizer.

- PASS: exact threshold, all maximizing labeled tuples and multiplicity agree for each M=2,...,96 (95 separate full-domain cases; 360,356 valid labeled tuples summed across all cases).
- PASS: witness feasibility, F_(3t)<W_t and j0≤J≤3t-1 for every M=15,...,256 (242 cases).
- Additional exact fast-algorithm instances M=512,1024,2048. All arithmetic in the certificate is integer-exact.

| M | T*(M) | labeled multiplicity | J(M) | example winner (a,u,v,d) |
|---:|---:|---:|---:|---|
| 15 | 1815 | 2 | 3 | (11,8,15,11) |
| 20 | 4420 | 4 | 3 | (13,11,20,17) |
| 32 | 19488 | 4 | 5 | (21,19,32,29) |
| 64 | 192576 | 4 | 6 | (51,47,64,59) |
| 96 | 685995 | 4 | 8 | (83,76,95,87) |
| 512 | 122421760 | 4 | 15 | (485,467,512,493) |
| 1024 | 1005585408 | 4 | 22 | (983,959,1024,999) |
| 2048 | 8179290015 | 4 | 33 | (1983,1952,2047,2015) |

In these checked instances the winners have q=u+v-a-d in {-1,1}; this is an **open conjecture**, not a premise or conclusion of Theorems A–C.

## 6. Next research frontier

Determine whether all maximizers satisfy |u+v-a-d|=1, or construct a counterexample using the exact modular-inverse search. Sharpen the uniform bound on J(M) to a leading coefficient or liminf/limsup classification. A native P000 transfer separately requires a specific triadically closed Cell/Link/Port event, its resource/time guards, a six-coordinate embedding/readout and proof of Port-observer preservation.

Theorems A–C have explicit human-checkable arguments; the code is finite independent regression evidence. Independent review, Activity association and native-event admission are separate pending scopes. No shared TASK CLAIM, Result, Review or Foundation promotion is asserted.