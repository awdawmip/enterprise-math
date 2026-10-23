# Uniform eventual decline and an optimal linear observer for positive BRC occupancy

**Author-side mathematical note, 2026-10-23. UNREVIEWED / NOT ADMITTED / AUXILIARY FOUR-LABEL MODEL, NOT NATIVE X6.**

Frozen inputs: Global Knowledge main 61cfa2a580230863c0d02b5f818381adbb3cb11b; Enterprise Math main d20a2d935c4d0f05ab220148b2276f8a0e3293c7. P000 and ACTIVE worldview remain unchanged.

## Model

Let m>=3 labels, and let a nonempty set G of two-element label subsets be the exact-good-support family. A public letter a selects an independently sampled label according to probability vector q_a. For a word w of length t, let D_t be the set of labels already seen, delta_t(w)=Pr(D_t in G), delta_0=delta_1=0, Delta_t=delta_t-delta_(t-1). Let M_t=max(delta_0,...,delta_t) and R_t=sum_{j=2}^t max(Delta_j,0)-M_t, with R_0=0.

The previous full-support counterexample uses m=4, edges 01,12,13,23, word 032020, and full-support action weights (common denominator 1000):
Q0=(1,665,1,333); Q2=(333,333,1,333); Q3=(1,1,1,997).
The previously observed strict residual-growth times are 4 and 6.

## Theorem A: uniform eventual strict decrease under arbitrary public control

Assume q_{a,i}>=alpha>0 for every available action a and every label i. Let d be the number of labels incident with some good edge G. Define

beta=alpha/(1-(m-1)alpha), F_s(beta)=(1+beta)^s-1-beta^s, s>=2.

For **every public word** w of length s>=2, independently of all its action choices and the next action,

Delta_{s+1} <= [d/F_s(beta)-(m-2)alpha] delta_s.

In particular, if F_s(beta)>d/((m-2)alpha), then Delta_{s+1}<0. F_s increases to infinity; writing s_star for the first integer s>=2 meeting the inequality, **every continuation at every t>=s_star+1 strictly decreases delta and leaves R_t=R_{s_star}.** Uniform positivity does not prevent multiple earlier growth episodes, but it imposes a finite universal tail bound for all words.

**Proof.** For an s-step prefix, put A_i=prod_{u<=s}q_{a_u,i}, B_ij=prod_{u<=s}(q_{a_u,i}+q_{a_u,j}). For s>=1 the disjoint event of occupied set exactly {i,j} has probability P_ij=B_ij-A_i-A_j. For any vertex i incident with G choose one good neighbor j; r_u=q_{a_u,j}/q_{a_u,i}>=beta because q_{a_u,j}>=alpha and q_{a_u,i}<=1-(m-1)alpha. Hence for s>=2,

P_ij/A_i = prod_{u=1}^s(1+r_u)-1-prod_{u=1}^s r_u
         = sum_{nonempty proper subsets U of {1,...,s}} prod_{u in U}r_u
         >= (1+beta)^s-1-beta^s=F_s(beta).

Since delta_s>=P_ij, each incident singleton mass A_i<=delta_s/F_s. Summing over the d incident labels gives total available singleton input <=d*delta_s/F_s. The only possible input to a good exact-two occupied set at the next step comes from one-label occupied sets; its amount is at most that singleton sum. Each previous good pair loses mass if the next label lies outside the pair. There are m-2 such labels, each with probability >=alpha, so total loss is >=(m-2)alpha*delta_s. A bad pair cannot turn into a different good pair, and support with size>2 cannot shrink. Subtract inflow and outflow. delta_s>0 for s>=2 by full support and nonempty G; strict negativity follows. F_s is a positive polynomial in beta with increasing s and diverges. Negative Delta neither increases the positive-increment sum nor the running maximum, so R is frozen. QED.

**Exact specialized threshold.** For the three given four-label laws, m=d=4 and alpha=1/1000, hence beta=1/997. The strict condition is the integer inequality

998^s > 2001 * 997^s + 1.

The smallest such s is **7583**, checked by exact integer powers at s=7582 and 7583. Consequently Delta_t<0 for all t>=**7584**, for every possibly alternating control word over {0,2,3}. This is a conservative bound, not an optimized onset or a claim that 3^7583 searches were executed.

**Finite decidability.** For a finite alphabet of rational full-support laws, alpha and s_star are effectively computable with rational arithmetic. The existence of any public word with two separated strict residual-growth episodes is then decidable by exhaustively checking all words through length s_star: no later t can increase R. This is theoretical decidability, not an efficient decision algorithm.

## Theorem B: exact future-output observer and its minimal linear dimension

For the four-label G, vertex degrees are d_i=(1,3,2,2). For every NONEMPTY word,

delta(w)=sum_{ij in G} B_ij(w)-sum_i d_i A_i(w).

The empty word is exceptional because the inclusion-exclusion expression would give 4-8=-4, whereas delta(empty)=0. Set e(w)=1 if w is empty and 0 otherwise. The identity valid for **all words** is

delta(w)=sum_{ij in G} B_ij(w)-sum_i d_i A_i(w)+4e(w).

The four A_i, four B_ij and e are NINE exact coordinates. Appending action a multiplies A_i by q_{a,i}, B_ij by q_{a,i}+q_{a,j}, and e by zero. Thus this is a diagonal nine-dimensional linear realization preserving delta for every possible public continuation. To preserve residual R also retain past maximum M and positive-increment accumulator S separately; the present minimum dimension assertion concerns only LINEAR delta realization.

**Sharpness for the displayed full-support action family.** Restrict to repeated two-letter block v=02. With D=1000^2, write h_n=D^n delta(v^n). For all n>=0, adopting 0^0=1,

h_n=sum_{j=0}^8 c_j m_j^n,

m=(0,333,221445,1,110889,443556,222444,664668,111556),

c=(4,-1,-3,-2,-2,1,1,1,1).

The zero node and coefficient 4 encode the empty-prefix exception. All nine m_j are pairwise distinct and all c_j nonzero. The 9x9 Hankel matrix H_(r,s)=h_(r+s), 0<=r,s<=8, has

det(H)=(prod c_j)*prod_{i<j}(m_j-m_i)^2
      =48*prod_{i<j}(m_j-m_i)^2 !=0

by the Vandermonde factorization H=V diag(c) V^T. Independently, modulo prime 1000003, the determinant equals **139775** (verified using exact modular elimination). Scaling each h_n by D^(-n) is invertible row/column scaling and does not alter Hankel rank. Any time-homogeneous finite-dimensional linear representation of delta over alphabet {0,2,3} restricts to a linear representation of the block sequence, whose Hankel rank cannot exceed representation dimension. Therefore such a representation has dimension >=9. The nine-coordinate construction attains the bound. Eight product coordinates suffice only AFTER the first action, when e=0; they do NOT give an eight-dimensional linear realization from the empty word. No nonlinear or native-state minimality is claimed.

## Theorem C: an explicit one-action sufficient condition for zero residual

If every draw uses one fixed full-support law q and max_i q_i <= min_{ij in G}(q_i+q_j), then for t>=2

Delta_t=A_t-B_t,

A_t=sum_i d_i (1-q_i) q_i^(t-1)>0,

B_t=sum_{ij in G}(1-q_i-q_j)(q_i+q_j)^(t-1)>0.

A_(t+1)/A_t is a positive weighted average of the singleton probabilities q_i and is <=max_i q_i. B_(t+1)/B_t is a positive weighted average of the edge masses q_i+q_j and is >=min_{ij in G}(q_i+q_j). Thus A_t/B_t is nonincreasing. Delta_2=2 sum_{ij in G} q_i q_j>0; once Delta_t becomes nonpositive it never becomes positive again. Occupancy is unimodal, its sum of positive increments equals its historical maximum, and hence **R_t=0 for all t**. This is sufficient, not necessary, and it is only for repeated identical action. Example q=(3,4,4,5)/16 satisfies 5/16<7/16; rational checks for 60 rounds support the analytic result.

## Provenance correction, execution, and boundaries

The previous immutable author's EXACT_EVIDENCE.json (commit f592bd851fc5ae1ffe4f38248baca4f18f8587d9) lists sixth-round numerator 436231737917062900. Its author's proof and verifier, and the independent recomputation in this note, give **436231737917062944**. The JSON field is short by **44**. The correct Delta_6 numerator 7085532818278944 and growth rounds {4,6} remain unchanged. This note records an erratum without rewriting historical publication.

An exact-integer verifier compares independent 16-mask recurrence to the product observer for all 1+3+9+27+81+243+729=1093 words through length 6, checks witness and correction, the modular Hankel determinant, both threshold comparisons, and an independent Fraction test of the fixed-law example. Finite tests support but do not replace the analytic proof.

Current canonical research service refused a new Researcher session with STATIC_READONLY_SCOPE_DENIED and returned BACKEND_IDENTITY_CHECK_UNAVAILABLE for task listing (operation_sent=false). No live owner, formal CLAIM, native Result acceptance or independent Driver review is asserted. This note belongs only to an UNREVIEWED GitHub branch, not to P000, the official theorem ledger, or native six-dimensional Cell dynamics.

**Next question.** Improve the extremely loose full-support horizon bound using action-conditioned singleton/pair order, seek a checkable all-alternating-word one-episode condition with tractable complexity, and test what structural coordinates would be required to transfer this observer faithfully to P000 native X6. Theorem A's tail bound alone does NOT establish the desired no-reentry property: this same full-support system has early episodes at rounds 4 and 6.

Reuse resolution: REUSE_APPLIED, positive rational branch accumulation and four-good-pair inclusion-exclusion from the existing BRC observer; exact 16-mask method cross-checks the new bound. No new BRC family is proposed.
