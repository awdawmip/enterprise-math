# Riesel residual composition: all seven-prime covers and exact observer thresholds

Researcher: `EM-DIRECT-970E1C` / `TASK_RESEARCH`  
Activity: `RA-D2EC212845B63844081F9A14`  
Continuation date: 2026-11-24 (Asia/Hong_Kong)

Status: author mathematical proofs, shared-context mathematical cross-checks, exact arithmetic certificates and separately recorded native execution. These are not independent project Review, formal proof-checker acceptance or Foundation promotion. Scientific derivation, execution, remote publication and Activity association have separate evidence.

## 1. Results

The seven-prime supplementary covers on the established fixed fiber R2 are now completely classified over all primes and orders. Every one contains 5,13,19,73. Its three remaining primes belong to exactly one of three structural families: binary, ternary or modulo five. There are 146 phase dictionaries and 1,160 sign-specific CRT progression descriptions. These progressions can overlap, so their number is not a count of disjoint root classes.

The complete classification upgrades the previously scoped 84-digit minimum to the minimum of **all roots in R2 with supplementary cost seven**. It also gives the exact finite observation needed to decide that predicate: the product T of twelve specified additional primes divides every sufficient root modulus N, and this divisibility is sufficient. The same characterization holds for observation of the complete future residue trajectory modulo N. Thus twelve additional distinct prime or prime-power channels are necessary and sufficient; the corresponding minimum maximum base-two prime order is exactly 180.

The newly identified ternary family also yields a consecutive irredundant covering construction. It strengthens the arbitrary-finite-observer theorem and improves the constant in the exponential order lower bound by a factor of eight:

\[
\frac{27}{64}\,2^b\le\Omega_b(R_1)\le105\,2^b
\qquad(b\ge7).
\]

The same bounds hold on R2 for b at least eight, while the seven-budget value there is exactly 180. These quantities measure the maximum base-two order of the observed odd primes. They are not the number of channels, modulus bit length, or computation time.

## 2. Native object and established square-Riesel family

Retain the fixed X6 anchor, typed integer register, positive singleton BRC weight and multiplicity one. The initial integer and its update are

\[
x_0=a^2-1,\qquad T(x)=2x+1,\qquad
T^n(x_0)=F_n(a)=a^2 2^n-1.
\]

The native two-step composition is 4x+3. The exponent n is an arithmetic update count. Prime and prime-power channels observe this integer state; they are not additional axes. The full integer state and joint cofactor relations remain available.

The inherited original root and old twenty-prime dictionary are

\[
a_*=690786768637635218740714348513373826260012289,
\]

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\},
\]

\[
M=\prod_{p\in P}p
=1397394912916194098609132326092145093313722687204526281.
\]

Every positive root a congruent to a* modulo 2M shares the complete P-residue trajectories. P covers every odd exponent; the holes of P have full-exponent density 6/35 and all lie at even exponents. Every even term is nevertheless composite by the exact joint factorization

\[
F_{2u}(a)=(a2^u-1)(a2^u+1).
\]

Thus all these roots already give Riesel coefficients k=a². A hole in one finite dictionary is not a prime term. This batch studies finite prime-cover structure and the information needed to decide its cost, without reclassifying membership in this established Riesel family.

Let \(\delta_P(a)\) be the minimum number of primes outside P needed to supplement P into a proper-prime cover of every positive-index term. Let \(\tau(a^2)\) be the minimum total number of covering primes, with no requirement to retain P. Use infinity when the corresponding finite cover does not exist. These are different minima: \(\delta_P(a)=7\) implies \(\tau(a^2)\le27\), but does not alone prove equality.

## 3. Fixed fibers and inherited lower bound

Put L=80754838636615 and

\[
R_1=\{a>0:a\equiv a_*\pmod{6M},\quad
a\equiv12926327728523\pmod L\}.
\]

The additional root residues are:

| Prime | 5 | 13 | 11 | 61 | 331 | 19 | 37 | 73 | 109 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| a modulo prime | 3 | 1 | 0 | 0 | 0 | 6 | 0 | 37 | 0 |

This is the fixed 29-channel fiber, counting P and these nine primes. Define the fixed 31-channel fiber

\[
R_2=\{a\in R_1:a\equiv0\pmod{433},\quad
a\equiv38733\pmod{38737}\}.
\]

Its positive progression has start and step

\[
\begin{aligned}
A_2&=9807947978443488306255509703402695727949968778703073231931137913705883712843,\\
S_2&=11356718000553566643685496313583434507970452519839503606327232707476034989690.
\end{aligned}
\]

The previous all-prime six-budget theorem proves that every supplement of at most six primes on R2 leaves uncovered exponent density at least 1/420. Hence every complete seven-prime supplement has exact supplementary cost seven. That theorem is reused at its published scope; its calculation is not relabelled as a new run.

## 4. Complete seven-prime classification

The proof is split into three complementary parts:

| Source | All-prime conclusion | Main obstruction |
|---|---|---|
| [Forced basic pair](basics/proof.md) | Every complete supplement of at most seven primes throughout R1 contains 5 and 13 | Omitting both covers at most 95/108 of the old holes; keeping exactly one covers at most 11/12 on its missed parity |
| [Forced W prefix](prefix/proof.md) | On R2, a seven-prime supplement containing 5,13 also contains 19,73 | Exact incidence capacities, the complete inventories of effective periods 6,7,10, and lifts of residual classes |
| [Complete tail classification](tail/proof.md) | After that forced prefix, the only three-prime tails are the three families below | An all-prime period reduction, followed by complete small-order factorization |

These implications do not assume that the optimal dictionaries at successive budgets are nested. The previously found binary and modulo-five routes were therefore inputs to the question, not an assumed exhaustive list.

Write n=2u. The forced prefix phases are

\[
(q,d,c)=(5,2,1),(13,6,0),(19,9,4),(73,9,1),
\qquad u\equiv c\pmod d.
\]

After them, the exact remaining positions are

\[
u=16+18w,\qquad n=32+36w,
\]

\[
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\]

Set

\[
E=\{577,487824887233\},\qquad
D=\{87211,246241,262657,279073\},
\]

\[
C=\{181,631,23311,54001,18837001,29247661\}.
\]

| Family | Three tail primes | Required w phases | Phase dictionaries | Sign-specific CRT descriptions |
|---|---|---|---:|---:|
| Binary | 38737 and both primes in E | 38737 takes odd w; the E primes take 0 and 2 modulo 4 | 2 | 8 |
| Ternary | Any three distinct primes in D | All three classes 0,1,2 modulo 3 | 24 | 192 |
| Modulo five | Any three distinct primes in C | The occupied classes 0,1,3 modulo 5 | 120 | 960 |
| Total | | | 146 | 1,160 |

For a prime assigned phase b, the root constraint is

\[
a\equiv\pm2^{-(16+18b)}\pmod q.
\]

The new ternary primes have exact base-two orders 54,108,27,108. Their effective order on w is three. The modulo-five orders are 180,45,45,180,90,180; the two E orders are both 144.

For completeness, the all-prime tail reduction uses the exact relative contribution

\[
\frac{K_g(c)}{13(h/g)},\qquad
h=\operatorname{ord}_q(2^{36}),\quad g=\gcd(h,35),
\]

whose maximum incidence values are 13,5,3,1 for g=1,5,7,35. If 38737 is omitted, each of three channels must contribute at least 3/13; this forces h into {3,4,5,7}. The classes of period four, period seven and mixed periods three/five cannot finish the residual lifts. The remaining pure period-three and pure period-five covers give D and C. If 38737 is included, the two remaining channels must each cover exactly half of the even-w remainder; this forces effective order two on z=w/2 and yields exactly E. The complete products of 2^108−1, 2^144−1 and 2^180−1 identify the eligible primes. No prime-size cutoff is used.

## 5. Global minimum within R2 and exact frequency

The minima of the 1,160 CRT progression descriptions are compared exactly in the tail certificate:

| Family | Digits of the minimum | Minimum root |
|---|---:|---|
| Binary | 90 | 142182133093029631521252488222753720130073171510309885943518183289197140261893115365205303 |
| Ternary | 91 | 1046533155647696956851681902279650889819246480725727047415947079817885251912744029965820233 |
| Modulo five | 84 | 168515727251568031139784117408423468924151126118048106286760549300706338389494633573 |

Therefore

\[
\min\{a\in R_2:\delta_P(a)=7\}
=168515727251568031139784117408423468924151126118048106286760549300706338389494633573.
\]

At this root the modulo-five phase assignment is 631 at w=0, 181 at w=1, and 23311 at w=3. The root residues are respectively 337,178,22892. The corresponding Riesel coefficient is its square. This is not a minimum over every Riesel number or over every root in R1.

To count roots rather than overlapping dictionary descriptions, let T_E, T_D, T_C be the products of the primes in the three disjoint sets E,D,C. Their event counts are

\[
\begin{aligned}
N_E&=8,\\
N_D&=T_D-3\prod_{q\in D}(q-2)+3\prod_{q\in D}(q-4)-\prod_{q\in D}(q-6),\\
N_C&=T_C-3\prod_{q\in C}(q-2)+3\prod_{q\in C}(q-4)-\prod_{q\in C}(q-6).
\end{aligned}
\]

The three events use disjoint prime coordinates, so CRT gives

\[
T=T_ET_DT_C,
\qquad N_7=T-(T_E-N_E)(T_D-N_D)(T_C-N_C).
\]

The exact values are

\[
\begin{aligned}
T&=35095524795781473254136196580356738045833417602831290421525609131,\\
N_7&=916603393453788765429110921373053984059735989421687074488.
\end{aligned}
\]

The frequency of exact supplementary cost seven **among the roots of R2** is N7/T, approximately 2.6117386726297526683×10^−8. Since gcd(S2,T)=1, this is the exact natural frequency along the R2 progression. It is neither a density among all integers nor a probability that a general integer is Riesel. The [observer proof](observer/proof.md) supplies the weighted category counts and disjoint overlap accounting.

## 6. Necessary and sufficient observation

For every positive integer N, the following are equivalent on the entire fixed root family R2:

1. a modulo N determines whether \(\delta_P(a)\le7\).
2. The complete future sequence of residues \([F_n(a)]_N\), for n at least one, determines that predicate.
3. \(T\mid N\).

Sufficiency follows from the full classification and its root-square phase tests. For the trajectory observation, F1 modulo the odd integer T recovers a² modulo T. For necessity, every one of the twelve prime coordinates is essential: put the other two families in their false states, supply all but one required phase in the chosen family, and change the remaining coordinate between its missing phase and an inactive residue. If q is missing from N, CRT realizes both outcomes while preserving a modulo N and every fixed R2 coordinate. Increasing finite powers of the other observed primes cannot distinguish these two roots.

Thus T is the least positive sufficient root modulus and the least additive period of the cost-seven predicate along the progression parameter. In the explicit counting model of distinct prime or prime-power readout channels, twelve additional channels are necessary and sufficient, or 43 when the 31 fixed coordinates are counted. This is not a universal lower bound for arbitrary information encodings.

Define

\[
B(N)=\max(\{1\}\cup\{\operatorname{ord}_q2:q\mid N,\ q\text{ odd prime}\}).
\]

If \(\Omega_b(R)\) minimizes B(N) over moduli sufficient for \(\delta_P\le b\) on R, then

\[
\boxed{\Omega_7(R_2)=180.}
\]

The same value holds for full residue-trajectory observations. Its scope is R2; it is not an asserted value of \(\Omega_7(R_1)\).

## 7. Consecutive covers and arbitrary finite observations

For every positive integer N define B(N) as in Section 6 and

\[
j_N=\min\{j\ge0:54\cdot2^j>B(N)\}.
\]

The [consecutive-cover theorem](finite/proof.md) constructs one residue rN modulo N such that

\[
\forall s\ge j_N+7\quad\exists^\infty a\in R_1:
\quad a\equiv r_N\pmod N,
\quad\delta_P(a)=s,\quad\tau(a^2)=20+s.
\]

For R2 the identical statement holds with the lower restriction j at least one in the definition of jN. The residue is chosen once before s varies. Each cost is attained on an arithmetic progression after deletion of finitely many small terms. These sufficient thresholds are not asserted optimal.

The construction starts with a cost-seven ternary dictionary using 87211,246241,279073 after the permanent four-prime prefix. For k at least one, use k dyadic rows in w of moduli 2^j and phases 2^(j−1), a permanent row w=1 modulo 3, and two final rows with moduli Hk=3·2^(k−1), Gk=3·2^k. Their respective phases are (0,2^(k+1)) for even k and (2^k,0) for odd k. The dyadic complement is w=2^k t; the last three rows cover its three t-classes modulo three exactly once. Explicit private cells establish irredundancy of all k+3 tail rows.

These covers have consecutive supplementary sizes k+7. Adjacent covers are not a chain of subsets or a refinement restricted to the retired row. They retain the same literal phase and chosen root residue at every common prime; the orders of the retired and two introduced primes are exactly

\[
54\cdot2^k,\qquad72\cdot2^k,\qquad216\cdot2^k.
\]

Once the smallest changing order exceeds B(N), no observed prime ever changes again. The same root lifts modulo every prime power in N can therefore be fixed for all later costs. The inherited coprimalization factor, with all dictionary prime powers removed, is compatible with those lifts. It makes the 20+s private terms pairwise coprime and proves both minima exactly. The special k=0 member lies in R1 but not R2; every k at least one retains 38737 at the prescribed root residue and forces 433 inactive, so lies in R2.

If a modulus could decide budget b while B(N)<54·2^(b−7), the theorem would put exact costs b and b+1 in one observed root residue. This gives

\[
\frac{27}{64}2^b\le\Omega_b(R_1)\le105\,2^b\quad(b\ge7),
\qquad
\frac{27}{64}2^b\le\Omega_b(R_2)\le105\,2^b\quad(b\ge8).
\]

The upper bound is the previously proved finite-budget observer: every inclusion-minimal supplement of at most b primes uses only primes with ord_q(2^210) at most 2^(b−1), hence ord_q(2) at most 105·2^b. The same exponential bounds hold for complete residual-trajectory observations. The construction still uses the credited primitive-prime existence theorem for base-two orders greater than six; the two needed distinct order-108 primes are explicit.

There is a particularly concrete consequence for the twelve-prime modulus T of the complete seven-budget observer. Its B(T) is 180, so jT=2. Fix

\[
a\equiv182629\pmod{246241},\qquad
a\equiv487823838657\pmod{487824887233},
\]

and root residue zero at each of the other ten primes in T. Their combined root residue is

\[
r_T=21450781839625171583347380029424471704699683386785900439176732195
\pmod T.
\]

Within R2 and this one fixed residue modulo T, every exact supplementary cost s at least nine occurs on infinitely many roots, with exact total cost 20+s. Thus one and the same **43 complete prime-residue trajectories** support all those finite costs. All three seven-budget family predicates are false at this observation. No claim is made about the possible occurrence of cost eight in that particular fiber. A minimal observer for one fixed budget need not determine all higher costs.

## 8. Exact evidence and reproduction

The [native execution note](native/proof.md) records two newly executed roots: the 84-digit complete-classification minimum and the 91-digit ternary minimum. Their full residue-value periods are 20,160 and 60,480; each contains sixteen complete coverage periods, of lengths 1,260 and 3,780 respectively. Every residue-value period was actually executed with the frozen native source.

The run made 80,640 one-step BRC updates, 40,320 native composed two-step evaluations, 2,741,760 individual prime quotient/remainder readouts, 80,640 native joint 34-radix readouts and 80,640 native joint recompositions. Every integer update was compared with an independently advanced scalar integer and the exact formula. All singleton weights and multiplicities stayed positive and equal to one.

The joint readout retains its cofactor and mixed-radix digits; these are distinguished from the independent prime residues. Native recomposition recovers the full integer at every step. The complete final integers, every final individual-prime cofactor, joint cofactors and digits, private witnesses and stream digests are retained in the native certificate. The two final integers have 20,713 and 61,079 bits. The actual two-root comparison covered 624,960 fixed-coordinate equalities; the all-future equality of the 31 fixed observations follows separately from their root congruence.

The finite calculators check complete factorizations and exact orders, all reduced tail patterns and 1,160 CRT starts, weighted observation counts, twelve explicit essential-coordinate witnesses, complete consecutive-cover patterns for k=0 through 8, the concrete seed covers and prime-power compatibility fixtures. Universal claims remain the scope of their proofs, rather than an extrapolation from these checks.

From this directory, with the earlier dependency paths retained in the repository layout, the calculators are:

```sh
python basics/verify_basics.py
python prefix/verify_prefix.py
python tail/verify_tail.py
python observer/verify_observer.py
python finite/verify_refinement.py
python native/verify_native.py --source-dir /path/to/pinned_source
```

The native source directory contains the pinned enterprise_math package. The isolated nineteen-file research directory is not a replacement for those explicitly named historical inputs and frozen source modules.

The standard-library calculators and their certificates are linked with their proofs:

| Component | Calculator | Certificate |
|---|---|---|
| Forced basic pair | [verify_basics.py](basics/verify_basics.py) | [basics_certificate.json](basics/basics_certificate.json) |
| Forced W prefix | [verify_prefix.py](prefix/verify_prefix.py) | [prefix_certificate.json](prefix/prefix_certificate.json) |
| Complete three-prime tails | [verify_tail.py](tail/verify_tail.py) | [tail_certificate.json](tail/tail_certificate.json) |
| Complete cost-seven observer | [verify_observer.py](observer/verify_observer.py) | [observer_certificate.json](observer/observer_certificate.json) |
| Consecutive cover construction | [verify_refinement.py](finite/verify_refinement.py) | [refinement_certificate.json](finite/refinement_certificate.json) |
| Native execution | [verify_native.py](native/verify_native.py) | [native_certificate.json](native/native_certificate.json) |

Universal all-prime completeness and all-cost claims follow from the written proofs. The exact calculations check their explicit factorization, order, incidence, covering, CRT and native-execution inputs. A finite sample of roots or costs is not promoted to a universal theorem.

## 9. Immutable dependencies and entrance state

| Commit | Reused source | Scope |
|---|---|---|
| `e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe` | `research_notes/portable_direct/riesel_mixed_20261119/certificate.json` | Old root, old dictionary and frozen native pins |
| `2feef401388e6e81a35dd8b0e66383f43561ad12` | `research_notes/portable_direct/riesel_budget_20261120/budget/proof.md` | Finite-interval covering theorem and finite sufficient budget observers |
| `af9e1a5e49386a28283781876e10742a71991036` | `research_notes/portable_direct/riesel_spectrum_20261121/spectrum/proof.md` | Primitive-prime existence input, private witnesses and coprimalization |
| `b1de1acbdc97b5e51d486127abd1fadd24babd99` | `research_notes/portable_direct/riesel_five_cover_20261123/` | Fixed R1, inherited incidence bounds and observer framework |
| `f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5` | `research_notes/portable_direct/riesel_finite_observers_20261124/` | Complete six-prime theorem, R2 six-budget gap, scoped modulo-five minimum and arbitrary-N construction |
| `b1efc6c805661ed7b476e6e730107da6043176ee` | `src/enterprise_math/` | Frozen native integer BRC implementation |

Current normative reads began at 2026-11-24T04:49:14Z (12:49:14 Asia/Hong_Kong), with canonical GK main `b7f1066501848d4f1abee3949119115ce98928f5` and EM main `213c3ec64486ac904789902cd4c13481b881fffd`. The global bootstrap/manual, project router and AGENTS entry were followed. Applicable mathematical, code, output, continuation, Activity and journal rules were read or reused under verified unchanged source identities within the active lease. The updated foundation router was checked for relevance; unrelated work was not imported. These current rule snapshots are distinct from frozen scientific dependencies.

## 10. Interpretation and remaining boundaries

For this question, residual composition is made concrete by compatible zero phases covering every remaining integer index, and by joint cofactor identities retained in the native state. The new classification shows that several distinct joint structures can solve the same seven-channel task; reducing them to the single scalar count seven loses their geometry. Their full observer is now both sufficient and provably necessary within R2.

Across unbounded budgets, every prescribed finite congruence observation still identifies roots of arbitrarily different exact finite covering costs. A finite observation may commute perfectly with the update without carrying every global covering property. The consecutive construction quantifies how the observation order must grow when the budget changes. None of this discards the original integer or its joint relations.

These results establish sufficient Riesel construction mechanisms and precise covering/observation theorems for the stated square family. They do not assert that every Riesel number has this form or that a finite prime covering system is necessary for every Riesel number. For the original unchanged root a*, the earlier lower bound of 1,791 supplementary primes remains, and existence of a finite covering dictionary at that root remains unresolved in this research record. The figure 1,811 requires retaining all twenty old primes; it is not an unconditional lower bound for the unrestricted total minimum.

The compact cost-seven examples have exact supplementary cost seven and total cost at most 27. Exact total minima 20+s belong to the separate coprimalized constructions. Unbounded finite costs across different ordinary roots do not prove an infinite cost at a single ordinary root. No literature-wide novelty, independent acceptance or formal shared-task closure is inferred from this coherent research batch.
