# PREFIX-459 — Universal signed-native X6 boundary-kernel family and exact ranks through degree ten

Date 2026-11-03. Status: AUTHOR_PROVED (all-degree constructive inequality); AUTHOR_EXACT_COMPUTER_ASSISTED_PROOF (degrees 8,9,10); UNREVIEWED / NOT_ADMITTED.
Predecessor: PREFIX-458, commit b846c32e5c4f0a4c291883ff21eb2d7749957c29.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Current norms read independently from global-knowledge canonical main and Enterprise Math main. This is an author-side, non-CLAIM research contribution.

## Exact question and model
At degree d, determine the rational rank of endpoint monomial observations of degree at most d on all N-step signed-native X6 ordered paths, separately for each history residue (number of -e1 steps modulo q). The native primitive set has twelve signed axis directions in SIX spatial axes. Give arbitrary finite positive-rational path weights; history-conditioned endpoint moments are linear in those weights. Standard coordinates per residue: B_d=binom(d+6,6). The X6 displacement origin is chart-relative. This is a snapshot-rank/observer theorem; provenance and other typed observations remain separate.

Fix d>=3, m=d-1, q>=d and N=q+d-2=q+m-1. Let D={+e1,+e2,-e2,...,+e6,-e6}, and W_m be the distinct sums of exactly m members of D.

## Theorem A — new all-degree constructive lower bound on deficiency
For every integer d>=3, q>=d, the total sector-separated rational moment rank satisfies:

R_d(q) <= q*binom(d+6,6)-16(d-1).

Precisely, the first q-1 history sectors each have full rank B_d, while the last sector has at least 16(d-1) independent rational vanishing moment relations. This assertion holds for ALL such d,q, without numerical extrapolation.

**Proof of sector reduction.** In sector r=q-1 at N=q+m-1, there are exactly q-1 steps -e1: the next congruent count 2q-1 is larger than N because q>=m+1. The remaining m steps come from D. Translation by -(q-1)e1 preserves ranks. For each r<=q-2, paths containing r copies -e1, q-r-2 copies +e1 and d free D steps are legal and remain in sector r. Seven affinely independent D vertices are (-e2,+e2,+e1,+e3,+e4,+e5,+e6), whose 6x6 difference determinant has absolute value 2. Their d-step sums form an affine image of {a in Z_+^6: sum a<=d}; multivariate Newton interpolation is nonsingular for all B_d degree-<=d monomials. Thus each earlier sector has full rank.

**Explicit all-degree kernel.** Write any x in W_m as x=(s,y1,...,y5) where s is its nonnegative number of +e1 steps. For epsilon in {+1,-1}^5 put L_epsilon=sum_i epsilon_i*y_i. Each of the m allowed D steps contributes +1 or -1 to s+L_epsilon, so s+L_epsilon=m-2j with 0<=j<=m-s. For every integer 0<=k<=m define the degree-m+1 integer polynomial

G_(k,epsilon)(s,y) = [product_(h=0,...,m-k-1)(s-h)] * [product_(j=0,...,k)(s+L_epsilon-(m-2j))].

Empty products are 1. At a point x in W_m, either s<m-k, annihilating the first factor, or 0<=j<=m-s<=k, annihilating one factor of the second. Thus every G vanishes on W_m.

For T subset {1,...,5}, with sign character chi_T(epsilon)=product_(i in T)epsilon_i, form the character projection G_(k,T)=2^-5 sum_epsilon chi_T(epsilon) G_(k,epsilon). Every such polynomial also vanishes. Its top homogeneous component is s^(m-k)*2^-5 sum_epsilon chi_T(epsilon) (s+L_epsilon)^(k+1).

Let t=|T| and delta_(m,t)=max(0,floor((m-t+3)/2)). For l=0,...,delta_(m,t)-1 choose k=t+2l-1, except k=0 when t=l=0. Within the T-character, the leading homogeneous polynomials for these choices have strictly increasing maximal total y-degrees t+2l, with nonzero top coefficient; they are linearly independent. Different T have disjoint y-exponent parity types and therefore give independent polynomials. Their exact number is sum_(t=0,...,5)binom(5,t)delta_(m,t)=16m for m>=2: grouping by total y-degree a gives counts 1,5,11,15 for a=0,1,2,3 and 16 for each a>=4 up to m+1. The seven-vertex simplex argument also shows there is no vanishing polynomial of degree <=m, so these are genuinely new degree-m+1 relations. QED.

## Theorem B — three new exact high-degree ranks
For every integer q in each stated range and N=q+d-2:

- d=8, q>=8: R_8(q)=3003q-112; last-sector rank 2891; |W_7|=9108.
- d=9, q>=9: R_9(q)=5005q-128; last-sector rank 4877; |W_8|=17469.
- d=10, q>=10: R_10(q)=8008q-144; last-sector rank 7864; |W_9|=31471.

**Complete finite-lemma proof.** W_m equals the points (s,y) with integral s>=0, s+sum|y_i|<=m, and m-s-sum|y_i| even. Sufficiency follows by adding opposite ±e2 pairs. Its support-size generating function is (1+z)^4/(1-z)^7.

Under the five independent sign flips y_i -> ±y_i, polynomial functions split into 32 characters (over Q and any odd prime field). The T-character polynomial basis is y_T*s^b*product_i(y_i^2)^c_i with b+2sum(c_i)+t<=m+1, t=|T|. For each t=0,...,5 take representative T={1,...,t}; the signed evaluation matrix has the same rank as the integer matrix with rows indexed by all (s,a_1,...,a_5) satisfying a_i>=0, s+sum a_i<=m, m-s-sum a_i even, a_i>0 for i<=t, and columns (b,c) as just defined, with entries s^b*product_i(a_i^2)^c_i. This drops the nonzero row multiplier product_(i in T)a_i, which is invertible over Q and modulo either prime below (all a_i<=m<32003). Every sign orbit and every monomial character is represented; character multiplicity is binom(5,t).

The companion actually executed Python/NumPy certificate completely enumerates these finite integer matrices and computes ranks via modular Gaussian elimination using the independently trial-divided primes p=32003, 32009. Since a nonzero minor modulo p is a nonzero integer minor, each modular rank gives a characteristic-zero lower bound. For m=7,8,9, every character block has exact modular rank equal to its column count minus delta_(m,t). Theorem A supplies 16m independent rational kernel polynomials, giving the matching rational-rank upper bound. Thus these two bounds agree EXACTLY, proving Theorem B over Q.

Character block summary as tuples (t, row count, column count, rank, deficiency):
m=7: (0,1106,294,289,5); (1,610,168,164,4); (2,314,112,108,4); (3,148,56,53,3); (4,62,35,32,3); (5,22,14,12,2).
m=8: (0,1897,420,415,5); (1,1106,294,289,5); (2,610,168,164,4); (3,314,112,108,4); (4,148,56,53,3); (5,62,35,32,3).
m=9: (0,3108,672,666,6); (1,1897,420,415,5); (2,1106,294,289,5); (3,610,168,164,4); (4,314,112,108,4); (5,148,56,53,3).
All 36 modular evaluations PASS. Array arithmetic uses exact residues with each multiplication <32009^2<2^63; no floats in the mathematical matrix calculations.

## BRC reuse, scope, and next question
BRC resolution: REUSE_APPLIED. Population is positive-rational weighted native ordered paths; identity includes their history port. The named observer is the sector-separated degree-<=d X6 endpoint moment; the allowed exact snapshot operations include parallel positive-rational source addition and history-conditioned positive-rational branching. A rational pivot basis exists for each exactly ranked sector, and standard moments can be recovered by linear algebra before rational-affine polynomial pullbacks. No high-degree typed native-class import or explicit decoder benchmark was executed here. Endpoint-moment redundancy is certified only for this observer and known fixed support: path order, signed/phase effects, and other future ports have separately typed meaning.

Next PREFIX-460 mathematical unit: prove or refute the all-degree matching character-block nullity formula dim ker_(m,t)=max(0,floor((m-t+3)/2)) for every m>=2, t=0,...,5, ideally by an explicit Newton basis for the parity-restricted simplex. Complementary engineering: construct exact rational pivot decoders at d=8,9,10 and benchmark bit growth, serialization and native BRC integration.

Evidence: prefix459_compact_certificate.py and PREFIX459_COMPACT_EXECUTION.log. Verified frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d; predecessor PREFIX-458. Verified GitHub collaborator role admin for awdawmip. Current native service status 2026-11-03: research_authority_granted=false; task list read returned CONTROL_QUOTA; active Owner and native Researcher-ID unconfirmed. This report is an author-side result, not a formally CLAIMed, independently reviewed or admitted theorem.
