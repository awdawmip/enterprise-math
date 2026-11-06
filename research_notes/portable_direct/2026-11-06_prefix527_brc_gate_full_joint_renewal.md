# PREFIX-527: Complete BRC–aAc joint renewal and sharp order-11 return kernel

Date: 2026-11-06 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_SYMBOLIC_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Task line: RS-X6-NATIVE-ROTATION-DYNAMICS. Author (native Source): EM-X6-D80875; Activity: RA-C5BDC99DBFCCBF0841A7D17E.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scientific predecessors: PREFIX-518 (four-STAR candidate graph), PREFIX-522 (local aAc gate), PREFIX-524 (unweighted event distribution), PREFIX-525 (endpoint BRC and rank-one transfer), PREFIX-526 (exact rational first joint moment).
Current normative routing: global GLOBAL_KNOWLEDGE_V1 and enterprise-math/docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; P000/ACTIVE Heartbeat World, joint observer preservation, portable research protocol.

## Exact population and observer

The four fixed STAR axis sets are A={1,3,6}, B={1,4,5}, C={2,3,5}, D={2,4,6}. A phase s=(STAR, signed preceding axis, signed current axis) has three legal next phases. There are 48 phases, and each phase edge s -> v has two independently labeled signed-X6 microtraces:
INNER=(-c(s),c(v)) and OUTER=(c(v),-c(s)).
We count all 48*6^d paths of macro length d, retaining their provenance labels.

Use +L1=a, -L1=A, +/-L3=c, others filler. H(w) is the number of indexed occurrences of aAc in the *ordered* native word. The typed BRC axis-1 pair count is p1(w)=min(N1+,N1-). For each path, with unsigned axis-1 visit count K1 and phase endpoints s0,sd,
p1=(K1-|sigma1(c(sd))-sigma1(c(s0))|)/2,
where sigma1(+L1)=1,sigma1(-L1)=-1,otherwise 0 (PREFIX-525).

Define P(t,q,z)=sum_d t^d sum_w q^p1(w) z^H(w).
Let P0(t,q)=P(t,q,1) and J(t,q)=partial_z P(t,q,z)|_{z=1}.
PREFIX-526 supplies an explicit exact rational expression for J in its N,E polynomials.

## Theorem A: complete one-axis joint renewal for every event order

Let T=(A,+L1,-L3) be the phase at which an aAc hit ends precisely when the last two macro branches are INNER. Let e be its 48-component basis vector. Let W(x) be the destination-row/source-column transfer, with W(x)[v,s]=x^([|c(s)|=L1]+[|c(v)|=L1]) on an allowed phase edge, zero otherwise. Set M=I-2tW(x) and q=x^2, and define

S(t,q)=t^2 e^T W(x)^2 M^{-1}e.

Every term of S represents a return from T to T, and the endpoint-corrected BRC visit exponent is even, so S lies in Q[q][[t]]. It has only even macro-length terms.

For all coefficients in Q[q,z][[t]],

**P(t,q,z) = P0(t,q) + (z-1)J(t,q)/(1-(z-1)S(t,q)).**

Consequently, for each integer k>=1,
Fk(t,q):=sum_d t^d sum_w binom(H(w),k) q^p1(w)
**=J(t,q)*S(t,q)^(k-1)**.

Proof: PREFIX-525 proves the exact marked transfer
(I-2tW-(z-1)t^2 e e^T W^2)^(-1).
Apply formal Sherman–Morrison to M and rank-one update (z-1)t^2 e(e^T W^2):
(M-alpha e e^T W^2)^(-1)=M^-1+alpha(M^-1e)(e^TW^2M^-1)/(1-alpha e^TW^2M^-1e).
For each initial/final phase, correct its visit count by x^(-|sigma1(c(sd))-sigma1(c(s0))|) to obtain q^p1. The correction is independent of z; its first rank-one numerator is the derivative J at z=1. Between marked hits the phase returns T->T, has zero native displacement, and its BRC pairs add exactly, so the renewal denominator is scalar S. Expand in powers of z-1 and use [ (z-1)^k ] z^H=binom(H,k). All inverses exist formally because the matrices have constant term I. QED.

## Theorem B: exact 24-to-11 scalar recurrence reduction

A macro edge reverses the sign of the current direction. The two-step graph therefore acts on one parity class V of 24 phases containing T. For s,v in V let
B(q)[v,s] = sum_(s -> m -> v) q^([|c(m)|=L1]+[|c(v)|=L1]).
On a closed walk based at T this monomial records half of all axis-1 visits, exactly p1 of that return. Let b index T in V. Introduce u as a two-step formal variable. Define
C(u,q)=det(I-u B(q)), A(u,q)=det((I-u B(q)) with row and column b deleted).
Then by the exact cofactor identity,
**R(u,q)=(A/C-1)/4** and **S(t,q)=R(4t^2,q)**.
The 1/4 removes the two INNER branch decisions fixed at each inter-event return; every other microbranch has two choices.

The reduced denominator of R over Q(q)(u), normalized to constant term 1, is exactly D=D1 D2 D3, where

D1=1+2u-3qu^2,
D2=1+(4+2q)u^2-(12q+4q^2)u^3+9q^2u^4,
D3=1-u-(12+30q)u^2-(36+126q+36q^2)u^3-(324q+243q^2)u^4-729q^2u^5.

The exact cofactor numerator after cancellation is coprime with D in Q(q)[u] (the certificate computes both characteristic polynomials and a symbolic polynomial GCD=1). Since deg_u D=11, the coefficients of R have **minimal eventual constant-coefficient recurrence order 11 over Q(q)**. After the substitution u=4t^2, S has minimal eventual recurrence order 22 in t and its even-indexed subsequence has order 11. This is scalar observer compression, not an asserted minimal first-order phase automaton.

Proof: the explicit 24-state construction determines integer-polynomial B. Compute charpolys of B and its 23-by-23 principal deletion; take reciprocal polynomials to get C,A and form (A-C)/(4C). Exact polynomial division yields the displayed D, and exact Euclidean GCD with its numerator is 1. All are finite polynomial identities over Q(q), so they establish all formal coefficients, not merely a fit. The rational-series recurrence theorem and preservation of a polynomial Bézout relation under u=4t^2 establish the orders. QED.

Independently counted coefficients:
S(t,q)=20q t^4+(288q+160q^2)t^6+(7168q+11840q^2)t^8
 +(116736q+384512q^2+102912q^3)t^10+... .
At q=1, S(t,1)=[A_520(4t^2)-1]/4 exactly, recovering PREFIX-520/524.

## Theorem C: infinite exact extremal BRC–gate families

For *every integer k>=1* the shortest macro depth admitting k gates is d=4k-2. At that depth the exact number of paths with (H,p1)=(k,k) is **9*20^(k-1)**; the number with H=k and p1!=k is zero. At the next depth d=4k-1 the corresponding counts are **108*20^(k-1)** and zero, respectively. Both have H=k as the maximum possible gate number.

Proof: PREFIX-523's exact gate separation puts the first hit at macro index >=2 and all later hits >=4 macros apart. PREFIX-526 gives J(t,q)=9q t^2+108q t^3+O(t^4); the return kernel begins S(t,q)=20q t^4+O(t^6), with no t^5 coefficient by parity. Therefore [t^(4k-2)]Fk=9*20^(k-1)q^k and [t^(4k-1)]Fk=108*20^(k-1)q^k. No histories at these lengths have >k hits; hence binom(H,k) is 1 precisely for H=k. Extract powers of q to obtain the exact BRC counts. QED.
Examples: k=1: (9,108), k=2: (180,2160), k=3: (3600,43200), k=4: (72000,864000). At these shortest realizations H<=p1 is saturated.

## Executed verification and scope

A separately executed Python/SymPy integer/symbolic certificate constructs all 48 signed phases and 24 two-step phases; evaluates 24x24 and 23x23 characteristic polynomials and exact denominator/GCD; independently counts all closed T returns through macro length 14; counts every joint binomial moment of orders 1..4 by native-branch dynamic programming to macro length 15; and directly scans **74,592 original nonempty labeled primitive words** of lengths 1..4 macros for both BRC pair count and literal aAc hits. All checks return ALL_CHECKS_PASS. Code and execution JSON are stored next to this paper. Infinite theorems follow from the algebraic proof, and finite checks verify the implementation. No physical rotation-selection law is claimed.

## Next discriminating unit

Combine the explicit PREFIX-526 J, this scalar S and the baseline P0 to eliminate and factor the generic reduced denominator of the *complete* q,z-resolved P; prove its minimal eventual recurrence, and measure coefficient-generation cost against the 48-phase/96-branch transfer. For future phase continuations and intermediate Cell/source history, compare actual observer fibers before further state compression. Mother task remains arbitrary-triad C6 generators and native X6 rotation-selection dynamics.
