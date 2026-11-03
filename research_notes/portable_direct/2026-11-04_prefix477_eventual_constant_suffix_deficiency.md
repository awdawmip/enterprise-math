# PREFIX-477 — Eventual constancy of mixed-word BRC/KMP history deficiencies

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Source pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continues PREFIX-476@41e74ef42a2bc07ff5ffd59d5cfae11395e97135. Account rules independently read at awdawmip/chatgpt-global-knowledge@9ca4f1ad00ebb3d774a8e946a92609217e672d07.

## Model and inherited theorems

Fix any nonempty ordinary gate word w of length k>=1 using the ten signed X6 directions on E2,...,E6. A special x=+E1 step may occur initially or immediately following w; ordinary steps are always legal. For a legal ordered path of length n use the positive-BRC support observer f=(s,y1,...,y5,V,W), where s=#x, yi=c_i(+)-c_i(-), p_i=min(c_i(+),c_i(-)), V=p2+2p4+p5 and W=p3+p5. This is a typed chart-relative support observation, not path identity or a final cell address. The history label q in 0,...,k is the longest suffix matching a prefix of w since the last x; x resets q=0.

Write S_nq for achievable f ending in q, S_n=union_q S_nq, B_n=|S_n| and F_n=sum_q|S_nq|, with B_m=0 for m<0. If u_j is the length-j prefix of w, the proven PREFIX-476 inclusions are T_u_j(S_(n-j,0)) subset S_nj subset T_u_j(S_(n-j)) for j<k, and S_nk=T_w(S_(n-k)) exactly; each fixed-suffix observer update T_u is injective. Consequently

F_n = sum_(j=0)^k B_(n-j) - D_w(n),
D_w(n)=sum_(j=0)^(k-1) delta_j(n),
delta_j(n)=B_(n-j)-|S_nj|.

PREFIX-476 also proved the state-0 hole bound |R_n|<=2k^9, where R_n=S_n\S_n0. Any f in R_n must have s<=1 and every ordinary signed-letter count other than that of the first symbol of w strictly less than k. It follows 0<=D_w(n)<=2k^10. PREFIX-471 provides the exact base generating function

G_k(z)=sum_n B_n z^n=(1+2z^2)(1+z)^2(1+z-z^(k+1))/((1-z)^8(1-z^(k+1))).

The open question addressed here: can the bounded defects vary indefinitely with path length?

## Lemma 1: terminal-state-preserving single-letter pumping

Let a be the first signed letter of w, e_a its Parikh unit vector. For any ordinary/special count vector c with s=#x<=1 and c_a>=2k+1, and for every terminal KMP state q,

ExistsLegalPathWithCountsAndTerminalState(c,q) iff ExistsLegalPathWithCountsAndTerminalState(c+e_a,q).  (L1)

Proof. Terminal q is determined by the last k step symbols (where a possible x resets state). If x is noninitial, protect the k ordinary symbols immediately preceding it, needed for its legality. Protect also the last k symbols of the path. These two blocks contain at most 2k copies of a. With >=2k+1 copies there is an a outside both blocks; deleting it preserves the gate immediately before x, any initial-x privilege, and the complete terminal KMP state. Conversely, when x is absent or noninitial, insert an a at the beginning; this changes neither protected block. When x is initial, insert an a just after x but before the protected last k letters, possible since at least 2k+1 a's follow that x. This again preserves legality and terminal q. All cases use at most one x. QED.

## Lemma 2: all large exceptional fibers translate by +a

Let C_n be the observations having a count representative with s<=1 and each of the other nine ordinary signed counts <k. R_n subset C_n by PREFIX-476. Orient the a-axis signed displacement as y_a=c_a-c_(-a). Any candidate representative of length n obeys

c_a >= n-1-9(k-1),    y_a >= n-1-10(k-1) = n-10k+9.  (L2)

For n>=14k we have y_a>=4k+9. Define sigma(f) to increase y_a by 1 and leave all other coordinates fixed. Since y_a>0, adding one a to a count representative increases y_a by one, leaves p_a unchanged and hence leaves V,W unchanged. Conversely, any count representative for sigma(f) has a positive a count and, after subtracting one a, is a representative of f. Thus sigma is a bijection C_n<->C_(n+1), including all complete count fibers. Every such representative has c_a>=2k+1. By L1, for every q and f in C_n,

f in S_nq iff sigma(f) in S_(n+1,q).  (L3)

Therefore sigma maps R_n bijectively to R_(n+1). This proves:

**Theorem 1.** For every w of length k>=1, the state-0 deficiency h_w(n)=|S_n\S_n0| is exactly constant for every n>=14k.

## Main theorem: all suffix corrections become constants

For 0<=j<k, define E_(n,j)={f in S_(n-j) : T_(u_j)(f) not in S_nj}. The padding inclusions imply E_(n,j) subset R_(n-j), and the injectivity of T_(u_j) gives |E_(n,j)|=delta_j(n).

Assume n-j>=14k. Then every f in E_(n,j) satisfies y_a(f)>=4k+9. The ordinary prefix u_j changes the a-oriented displacement by an integer between -j and j, so y_a(T_(u_j)(f))>=3k+9. Any count representative of this padded observation contains >=2k+1 a's. Moreover, the fixed-suffix cancellation update is determined by displacement and signed suffix counts, and with y_a greater than k its update commutes with sigma:

T_(u_j)(sigma(f)) = sigma(T_(u_j)(f)).  (L4)

Applying L1 both to the original and padded observations, L3 and L4, sigma bijects E_(n,j) with E_(n+1,j). Hence delta_j(n) is constant for all n with n-j>=14k. Since j<=k-1, the uniform sufficient cutoff n>=15k works.

**Theorem 2 (all n>=15k).** For every fixed mixed-sign, repeated, self-overlapping word w of length k, there are computable constants d_(w,j)=delta_j(15k) in [0,2k^9] and d_w=sum_(j=0)^(k-1)d_(w,j) in [0,2k^10] such that

F_n = sum_(j=0)^k B_(n-j) - d_w.  (T2)

The bound 15k is an explicit sufficient cutoff, with no minimality claim. Define d_w=D_w(15k). Then the *whole* full-history series, including boundary lengths, is the rational formal power series

F_w(z)=(1+z+...+z^k)G_k(z)
       - sum_(n=0)^(15k-1) D_w(n) z^n
       - d_w*z^(15k)/(1-z).  (GF)

Thus a finite exact calculation through n=15k determines the entire infinite full-history count sequence. This is mathematical effectiveness, not a polynomial runtime claim. It sharpens PREFIX-476's bounded correction to a provably eventually constant correction rather than merely an eventually periodic function.

## Exact finite certificate and empirical scope

The accompanying Python-stdlib script independently enumerates (Parikh count vector, KMP terminal state) with exact integer/set arithmetic, computes full signed X6 BRC observations, and checks PREFIX-471's rational base generating function by integer-binomial convolution, PREFIX-476's padding correction inequalities and exact full-match padding. The run covers n=0,...,9 for three different words: aab, ababa, aAa. It completed with ALL_EXACT_CHECKS_PASS. At n=9:

- aab: B=66042, F=121853, h=3, D=5, history sizes [66039,33293,15697,6824].
- ababa: B=65384, F=124538, h=4, D=4, history sizes [65380,33085,15643,6814,2684,932].
- aAa: B=66042, F=121855, h=3, D=3, history sizes [66039,33295,15697,6824].

Finite checks do not reach n=15k for these words. The eventual-constant statement is supported by the above analytic lemmas, and independent proof review remains to be performed.

## External context, BRC typing and next question

Parikh images of finite automata are semilinear, and BRC signed count/min observers are Presburger-definable; general Presburger counting theory provides eventually quasi-polynomial state-count functions. With bounded defects, that general route gives eventual periodicity. The model-specific protected-block argument above proves the stronger eventual constancy and explicit cutoff.

Relevant verified literature: Anthony Widjaja To (2010), Parikh Images of Regular Languages: Complexity and Applications, https://arxiv.org/abs/1002.1464 ; Kevin Woods (2015), Presburger Arithmetic, Rational Generating Functions, and Quasi-Polynomials, J. Symbolic Logic 80(2), 433–449, DOI:10.1017/jsl.2015.4.

BRC resolution: COMPOSE_APPLIED. Full six-axis signed occupancy and collision fibers are used in the proof before the declared Boolean support projection; KMP is typed order/history, not an additional spatial axis. This theorem concerns support and terminal history states. Path multiplicity, positive mass, signed amplitude, branch/source provenance and other futures remain separate observers.

Next PREFIX-478: determine the stable d_(w,j) constants and earliest stabilization threshold for aab, ababa and aAa by exact finite exception-fiber classification, without full 15k-layer dynamic programming; use the resulting finite exception dictionary to extend PREFIX-472's rank/unrank. Remain AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED pending native ownership and independent review.