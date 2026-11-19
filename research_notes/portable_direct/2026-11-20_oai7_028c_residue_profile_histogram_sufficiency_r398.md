# OAI7 r398 — Residue-profile histogram is sufficient shared data for coverage transfer

Date: 2026-11-20 (Asia/Shanghai). Original research context: RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19. This is a new Driver-side mathematical derivation, using the immutable source openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a (coverage-transfer.tex and schedule.tex). Original Researcher EM-EMF6D046-5A2844 and their contributions are unchanged. The present work is an author-side proof and computational check, not independent Native Result acceptance.

## Statement and proof

Let A be a finite mixing variable, Y=y(A) a point in a lattice Lambda, and nu_a a finitely supported displacement law on Lambda. Conditional on A=a, draw H=(h_1,...,h_n) iid from nu_a. Let C be the finite set of signed coordinates from the pinned coverage-transfer.tex, with homomorphisms phi_c:Lambda -> G_c. Fix the common residue-profile map

  psi(h)=(phi_c(h):c in C).

Write w_j=psi(h_j), let W=psi(union_a supp nu_a) be the finite profile alphabet of size m, and define the **shared profile histogram** B=(B_w:w in W), with B_w=#{j:w_j=w} and sum_w B_w=n. B is defined before the independently selected signed subset S.

**Theorem 1 (proof-sufficient occupancy data).** In the original one-step coverage transfer theorem, the shared-data entropy assumption may be replaced by

  H(B) <= kappa*s*Lbar,

with every other original hypothesis and the same conclusion unchanged. There is no need for an ordered physical-displacement sample to be included in the conditioning data. The same assertion holds for any deterministic finite feature psi through which every phi_c(h) factors.

**Proof.** For each deficient coordinate c and its fixed low-probability set K_c, the original candidate list has the exact representation

  L_c(B) = {x in G_c: sum_{w in W} B_w 1_{x+pr_c(w) in K_c} <= n(tau+delta)u_p/p}.

Here pr_c is the c-coordinate projection of a profile. Thus the list defined in the pinned proof from the full ordered sample H is pointwise equal to L_c(B). At the true x=phi_c(Y), the expectation of its hit count is n Pr(phi_c(Y+h_1) in K_c) <= n*tau*u_p/p. The original Markov argument applies unchanged. After fixing exact A=a, the underlying w_j remain conditionally iid; hence the same binomial Chernoff estimate and union bound apply to the **count measurable in B**. The list and its cardinality are B-measurable; the event that the true residue lies on the list is measurable in (Y,B). All later conditional entropy and deficit estimates therefore use exactly the pair (Y,B), without accessing the ordering of the auxiliary samples. Finally the original one-shared-conditioning-cost lemma applies to the pair (Y,B), replacing H(H) with H(B). The same entropy-deficit contradiction and coverage conclusion follow. QED.

The theorem is exact: no additional independence is imposed on B and Y, and no sample positions need to be resampled. The original endpoint law Z=Y+h_1 retains its original marginal; for the residue-coordinate proof, one may equivalently choose a uniform sample from the profile multiset described by B.

**Theorem 2 (finite-sample exact information and entropy).** Let q_a(w)=Pr(psi(h_1)=w|A=a), let b=(b_w) be a nonnegative integer histogram summing to n, and put

  P_a(b)=[n! / product_w b_w!] * product_w q_a(w)^{b_w},
  P(b)=sum_a P(A=a) P_a(b).

Then

  H(B)=-sum_b P(b) log P(b),
  I(A;B)=sum_a P(A=a) sum_b P_a(b) log[P_a(b)/P(b)],
  H(B) <= min{ log binom(n+m-1,m-1), n H(w_1) }.

If Wvec=(w_1,...,w_n) is the ordered profile sample, then **A is conditionally independent of Wvec given B** and, for every deterministic observable X=f(A),

  I(X;Wvec) = I(X;B).

**Proof.** The multinomial formula gives P_a(b). Conditional on A=a and B=b, every ordered word with those counts has equal probability (the product of its q_a symbols depends only on b). Consequently the conditional distribution of Wvec given B=b is uniform across its n!/(product b_w!) permutations, independent of a. This proves conditional independence and equality by chain rule. There are binom(n+m-1,m-1) histograms, so the support entropy bound follows; also H(B)<=H(Wvec)<=sum_j H(w_j)=n H(w_1). QED.

For the information-aware r396 lemma, the genuinely needed information is therefore **exactly**
  I(F_S(Y);Wvec)=I(F_S(Y);B)
for each fixed S (where S is independent). This identifies a sufficient statistic for the relevant residue information. It does NOT assert equality with I(A;H) for ordered *raw physical displacements* when psi is many-to-one.

## Exact finite sanity checks

1. Let A be equiprobable on two types, with Bernoulli profile parameters q_0(1)=1/4 and q_1(1)=3/4, and n=2. The profile histogram B is determined by the count of ones. Its unconditional law on counts 0,1,2 is (5/16, 3/8, 5/16). The ordered sample Wvec has probabilities 5/16,3/16,3/16,5/16 on (00,01,10,11). Direct summation gives

   H(B)=1.094780226007948 nats;
   H(Wvec)=1.354710418717928 nats;
   I(A;B)=I(A;Wvec)=0.230040129480311 nats.

   The entropy saving is H(Wvec)-H(B)=(3/8)log 2, while the information about A is unchanged. The rational masses establish the exact finite identity independently of floating-point rounding.

2. Reuse the distinct 128 Bernoulli laws from r397, with A=j uniform on 0,...,127, q_j(1)=1/2+(2j-127)/200000, and n=1000. Because the profile alphabet is binary, B has only 1001 possible values, compared with 2^1000 ordered words. The exact finite formula above, evaluated with stable binomial log probabilities, yields

   I(A;B) approximately 0.00027297559003 nats,
   r397 n * mean one-step KL bound approximately 0.00027305004473 nats,
   r397 n * mean chi-square bound = 0.0005461 nats.

   The value is a numerical evaluation of an explicitly finite sum, not an exact rational evaluation of the logarithms. The exact rational law probabilities and multinomial formula are the reproduction specification.

~~~python
# Standard Python 3; exact enumeration for the two-type n=2 check.
from fractions import Fraction as F
from collections import defaultdict
from math import log
laws = [F(1, 4), F(3, 4)]
joint_counts = defaultdict(F)
joint_words = defaultdict(F)
for a, p in enumerate(laws):
    for x in (0, 1):
        for y in (0, 1):
            z = (p if x else 1-p) * (p if y else 1-p) / 2
            joint_counts[(a, x+y)] += z
            joint_words[(a, x, y)] += z
pk = [sum((joint_counts[(a,k)] for a in (0,1)), F(0)) for k in range(3)]
pw = [sum((joint_words[(a,x,y)] for a in (0,1)), F(0)) for x in (0,1) for y in (0,1)]
assert pk == [F(5,16), F(3,8), F(5,16)]
assert pw == [F(5,16), F(3,16), F(3,16), F(5,16)]
H = lambda vals: -sum(float(z)*log(float(z)) for z in vals if z)
hk = H(pk); hw = H(pw)
hka = H([F(9,16), F(6,16), F(1,16)])
assert abs((hw-hk) - 3*log(2)/8) < 1e-14
print("H(B)", hk, "H(Wvec)", hw, "I(A;B)", hk-hka)
~~~

## Gaussian schedule applicability, limits, and next discriminating calculation

At one exact checkpoint A_i=a of the pinned schedule.tex, one may choose the common displacement support D_{i+1} and define W as the image of D_{i+1} in the product of all signed-prime residual groups. The same exact conditional iid continuations and all exact-start quantifiers are retained. Let m_i=|W|. A valid sufficient cost is

  kappa_i*s_i*L_* >= H(B_i)
     <= min{ log binom(n_i+m_i-1,m_i-1), n_i log m_i }.

It is a genuine strengthening of the *hypothesis* in the pinned theorem; however the schedule already proves a strong n_i log |D_{i+1}| bound, and when m_i is much larger than n_i the combinatorial correction may have little asymptotic effect. No improvement to Gaussian moat constants is asserted without computing the actual profile alphabet/effective entropy at a fixed exact-start experiment.

A more targeted calculation would evaluate (or upper-bound) H(B_i) and I(F_S(Y);B_i) for the actual conditional profile laws q_a, compare with the pinned kappa_i s_i L_* budget, and decide whether the explicit occupancy certificate is competitive with r396/r397's information certificate. The two costs should remain distinct: H(B_i) pays for the original Shannon-conditioning lemma; I(F_S(Y);B_i) pays only for what selected residues reveal.

Proof and finite check: author-side verified. Current Native Result/review/Source-Activity admission status: not changed by writing this note.
