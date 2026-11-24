# The complete cost-seven observer on R2: exact frequency, sufficient moduli and minimum order

**Status.** Author mathematical derivation and exact arithmetic in Research Activity `RA-D2EC212845B63844081F9A14`, Researcher `EM-DIRECT-970E1C`. This work is not an independent project Review, formal acceptance, a new native execution or Foundation promotion.

## 1. Fixed objects and theorem dependencies

Retain the sequence

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

the old twenty-prime dictionary P, and the fixed 31-channel fiber R2 of the [v10 R2 proof](https://github.com/awdawmip/enterprise-math/blob/f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5/research_notes/portable_direct/riesel_finite_observers_20261124/six/r2_proof.md). Write \(\delta_P(a)\) for the minimum number of primes outside P in a proper-prime cover, allowing infinity if no finite cover exists. The exact positive progression is

\[
R_2=\{A_2+S_2j:j\ge0\},
\]

where

\[
\begin{aligned}
A_2&=9807947978443488306255509703402695727949968778703073231931137913705883712843,\\
S_2&=11356718000553566643685496313583434507970452519839503606327232707476034989690.
\end{aligned}
\tag{1}
\]

The [forced-basic-pair proof](../basics/proof.md) and [forced-W-pair proof](../prefix/proof.md) together establish that every complete supplement of at most seven primes in R2 contains

\[
\{5,13,19,73\}.
\tag{2}
\]

The v10 six-budget gap is positive, so \(\delta_P(a)\ge7\) throughout R2. After (2), all remaining holes have

\[
n=32+36w,\qquad
w\in\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{3}
\]

Prime 433 is inactive, and 38737 has fixed phase w=1 modulo 2. The [exhaustive three-prime-tail proof](../tail/proof.md) classifies every completion of (3), over all primes and with no empirical prime cutoff. There are exactly three families:

| Family | Free prime coordinates | Required phases of w | Phase dictionaries | Sign-specific CRT progression descriptions |
|---|---|---|---:|---:|
| B, binary | \(\mathcal B=\{577,487824887233\}\) | 0 and 2 modulo 4, assigned in either order; 38737 supplies the fixed third tail prime | 2 | 8 |
| C, modulo five | \(\mathcal C=\{181,631,23311,54001,18837001,29247661\}\) | Three distinct coordinates supply 0,1,3 modulo 5 | 120 | 960 |
| D, ternary | \(\mathcal D=\{87211,246241,262657,279073\}\) | Three distinct coordinates supply 0,1,2 modulo 3 | 24 | 192 |

The totals are 146 phase dictionaries and 1,160 progression descriptions. The descriptions need not be disjoint root sets and do not have one common progression modulus. They therefore cannot be added as root densities.

## 2. The exact Boolean predicate

For each indicated prime q and required phase b, define the two-element root category

\[
R_{q,b}=\left\{2^{-(16+18b)},-2^{-(16+18b)}\right\}\pmod q.
\tag{4}
\]

This formula comes directly from

\[
q\mid F_{32+36b}(a)
\iff (a2^{16+18b})^2\equiv1\pmod q.
\]

For a given q the required categories are disjoint. Its exact effective order on w is four, five or three in the respective family. Hence each category determines exactly the displayed w-phase, rather than merely one sample hit. The verifier reconstructs every pair in (4) and compares it with the tail certificate.

Let \(E_B(a)\) mean that the two B coordinates occupy the opposite required categories 0 and 2. Let

\[
\begin{aligned}
E_C(a)&=\bigwedge_{b\in\{0,1,3\}}\ \bigvee_{q\in\mathcal C}
\bigl([a]_q\in R_{q,b}\bigr),\\
E_D(a)&=\bigwedge_{b\in\{0,1,2\}}\ \bigvee_{q\in\mathcal D}
\bigl([a]_q\in R_{q,b}\bigr).
\end{aligned}
\tag{5}
\]

Disjoint categories ensure that the three required phases in either line must be supplied by distinct primes. More than three eligible coordinates are allowed; the predicate asks whether at least one suitable triple exists.

Combining the forced prefix, exhaustive tail classification and six-budget obstruction gives the complete equivalence

\[
\boxed{
\delta_P(a)\le7
\iff\delta_P(a)=7
\iff E_B(a)\lor E_C(a)\lor E_D(a),
\qquad a\in R_2.
}
\tag{6}
\]

Every root in R2 is at least the large positive A2 in (1), so all primes in these three compact covers are proper divisors whenever they divide a term. If the predicate is false, the conclusion is \(\delta_P(a)>7\), allowing infinity. The predicate does not decide whether a finite cover of a larger size exists.

## 3. Exact family counts and the cost-seven frequency in R2

Put

\[
T_B=\prod_{q\in\mathcal B}q,
\quad T_C=\prod_{q\in\mathcal C}q,
\quad T_D=\prod_{q\in\mathcal D}q,
\quad T=T_BT_CT_D.
\tag{7}
\]

Each required category at a prime has two residues. Binary success has two phase assignments, each with four independent signs, so \(N_B=8\). For C and D, apply inclusion-exclusion to the three missing-phase events. If j required colors are forbidden, there are \(q-2j\) choices at each prime. Thus

\[
N_X=\sum_{j=0}^3(-1)^j\binom3j\prod_{q\in\mathcal X}(q-2j),
\qquad X\in\{C,D\}.
\tag{8}
\]

For D one may also count three or four active coordinates directly, obtaining

\[
N_D=48\sum_{q\in\mathcal D}(q-6)+576
=48\left(\sum_{q\in\mathcal D}q-12\right)=42008160.
\]

The exact values and approximate frequencies are:

| Family | Product modulus \(T_X\) | True classes \(N_X\) | Frequency inside R2, \(N_X/T_X\) |
|---|---:|---:|---:|
| B | 281474959933441 | 8 | \(2.84217111244699019\times10^{-14}\) |
| C | 79208819702303143625098260481 | 2068723011224822069760 | \(2.61173316178661617\times10^{-8}\) |
| D | 1574122160979454896811 | 42008160 | \(2.66867216797593141\times10^{-14}\) |

The three prime sets are disjoint and their product is coprime to S2. CRT therefore gives exact independence for uniform residue counting within R2. This is an arithmetic product decomposition, not a statistical assumption. Consequently

\[
\boxed{
N=T-(T_B-8)(T_C-N_C)(T_D-N_D).
}
\tag{9}
\]

In full integers,

\[
\begin{aligned}
T={}&35095524795781473254136196580356738045833417602831290421525609131,\\
N={}&916603393453788765429110921373053984059735989421687074488.
\end{aligned}
\tag{10}
\]

The exact relative natural density of \(\delta_P=7\) roots **inside R2** is

\[
\boxed{
\lim_{X\to\infty}
\frac{|\{a\le X:a\in R_2,\ \delta_P(a)=7\}|}
{|\{a\le X:a\in R_2\}|}
=\frac NT
\approx2.61173867262975266825491471344819448\times10^{-8}.
}
\tag{11}
\]

Equivalently, its reciprocal is approximately 38,288,669.93775846 R2 roots per successful root. This is a periodic frequency, not a claim that successive successes have equal spacing, and not a frequency among all positive integers or all Riesel numbers.

### 3.1 Intersections

All counts in the following table use the common modulus T. An intersection does not restrict the unlisted family. For example \(|E_B\cap E_C|=N_BN_CT_D\). Dividing each exact count by T gives its exact relative density in R2.

| Event | Exact classes modulo T | Approximate relative density in R2 |
|---|---:|---:|
| \(E_B\cap E_C\) | 26051381895177136364448249413268929948282880 | \(7.42299254584976191\times10^{-22}\) |
| \(E_B\cap E_D\) | 26619334171724022607248861936060199680 | \(7.58482294441247405\times10^{-28}\) |
| \(E_C\cap E_D\) | 24461088038121411560664231447535518888345600 | \(6.96985959903972300\times10^{-22}\) |
| \(E_B\cap E_C\cap E_D\) | 695225978009712971824073932800 | \(1.98095336102020625\times10^{-35}\) |

### 3.2 The disjoint partition

Write a bit string in B,C,D order, with 1 meaning that family succeeds and 0 meaning it fails. For bits \(\epsilon_B,\epsilon_C,\epsilon_D\), the exact class count is

\[
\prod_{X\in\{B,C,D\}}
N_X^{\epsilon_X}(T_X-N_X)^{1-\epsilon_X}.
\tag{12}
\]

Again, the exact density of every row is its integer count divided by T. The seven nonzero bit strings partition the complete \(\delta_P=7\) class.

| BCD state | Exact classes modulo T | Approximate relative density in R2 |
|---|---:|---:|
| 000 | 35095523879178079800347431151245816672779433543095300999838534643 | \(0.999999973882613273702473317450853\) |
| 001 | 936584477968997358954948179138944799189091871574880 | \(2.66867209827725957\times10^{-14}\) |
| 010 | 916601459394418827972131877945873927246097043407367278080 | \(2.61173316178647225\times10^{-8}\) |
| 011 | 24461088038120716334686221734563694814412800 | \(6.96985959903952490\times10^{-22}\) |
| 100 | 997474841455963067457149803738800156034185699258968 | \(2.84217103821698889\times10^{-14}\) |
| 101 | 26619333476498044597535890111986266880 | \(7.58482274631713795\times10^{-28}\) |
| 110 | 26051381895176441138470239700297105874350080 | \(7.42299254584956382\times10^{-22}\) |
| 111 | 695225978009712971824073932800 | \(1.98095336102020625\times10^{-35}\) |

The calculator checks that all eight rows sum to T and that the seven successful rows sum to N. It also compares the inclusion-exclusion counts with an exact weighted color-mask calculation, which counts overlaps within a family before combining the three independent families.

## 4. Every one of the twelve free prime coordinates is essential

Fix a prime q in one of the three families. Set every coordinate belonging to the other two families to zero, making those families false.

- For q in B, put the other B coordinate in phase 0. Putting q in phase 2 makes the predicate true; putting q at residue zero makes it false.
- For q in C, put two other C coordinates in phases 0 and 1 and all remaining coordinates at zero. Putting q in phase 3 makes the predicate true; putting q at zero makes it false.
- For q in D, put two other D coordinates in phases 0 and 1 and the remaining coordinate at zero. Putting q in phase 2 makes the predicate true; putting q at zero makes it false.

All these assignments are simultaneously realizable inside R2 by CRT, since \(\gcd(S_2,T)=1\). The certificate records explicit true and false residue vectors and positive R2 representatives for each of the twelve choices of q. Thus each coordinate is essential for the **complete** predicate (6), not merely for an isolated sufficient subfamily.

## 5. Exact characterization of every sufficient root modulus

**Theorem.** For every integer m at least one,

\[
\boxed{
\text{The residue }[a]_m\text{ determines }\delta_P(a)\le7
\text{ throughout }R_2
\quad\Longleftrightarrow\quad T\mid m.
}
\tag{13}
\]

If \(T\mid m\), all twelve coordinates are known and (6) gives sufficiency.

For necessity, suppose some \(q\mid T\) does not divide m. Start with a true positive R2 root \(a_+\) from the essential-coordinate construction of Section 4. Put

\[
K=\operatorname{lcm}(S_2,m,T/q).
\]

Because q divides none of \(S_2,m,T/q\), it is coprime to K. CRT supplies a positive integer \(a_-\) with

\[
a_-\equiv a_+\pmod K,
\qquad a_-\equiv0\pmod q.
\tag{14}
\]

The two roots lie in R2, agree modulo m and at the other eleven free coordinates, and have opposite truth values in (6). Hence m is insufficient. This argument permits arbitrary powers of primes in m and arbitrary other prime factors, including 2 and primes already fixed by R2. They cannot compensate for one missing essential q.

Consequences of (13) are exact:

1. **The smallest additional sufficient root modulus is T.** Indeed every sufficient modulus is a multiple of T.
2. **The least positive additive period of the Boolean function defined by the right-hand side of (6) on all integer roots is T; the progression-parameter period is stated separately below.** This function has period T, while any other period d would make residue modulo d sufficient on R2 and hence would satisfy \(T\mid d\). A root translation required also to preserve the fixed R2 fiber must be a multiple of S2, so the least positive such translation preserving the predicate is \(S_2T\), rather than T alone.
3. **The least positive period in the R2 progression parameter j is also T.** It is a period because (1) is invertible modulo T. If d were a j-period, observing \(a\bmod S_2d\) inside R2 would determine \(j\bmod d\), so (13) would give \(T\mid S_2d\); coprimality then gives \(T\mid d\).
4. **Twelve additional distinct prime channels are necessary and sufficient** when a channel means observation modulo a power of one prime. The twelve primes in T lie outside the fixed R2 primes, every sufficient m must contain them, and their first powers suffice. With the already declared 31 fixed prime channels, this is exactly 43 under that counting convention. It is not a lower bound for arbitrary noncongruence encodings, or for the number of composite-modulus readouts, since a single readout modulo T already packages all twelve coordinates.

## 6. Full residual trajectories and the exact order threshold

An entire fixed-modulus trajectory

\[
\bigl([F_n(a)]_m\bigr)_{n\ge1}
\]

decides the same budget-seven predicate on R2 **if and only if \(T\mid m\)**. Necessity follows from (14): equal root residues modulo m give equal squares and equal residual values at every n, while their budget-seven outcomes differ.

For sufficiency, reduce the first residual value modulo the odd number T. It recovers

\[
a^2\equiv2^{-1}(F_1(a)+1)\pmod T.
\tag{15}
\]

Each root category in (4) is a sign pair, so its membership is determined exactly by \(a^2\bmod q\). Equation (15) therefore determines all categories and (6). In particular the conclusion remains valid when m is even: inversion is performed modulo its odd divisor T, not modulo m.

Using the same order convention as the [v10 finite-budget observer theorem](https://github.com/awdawmip/enterprise-math/blob/f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5/research_notes/portable_direct/riesel_finite_observers_20261124/budget/proof.md), set

\[
B(m)=\max\left(\{1\}\cup
\{\operatorname{ord}_q2:q\text{ is an odd prime dividing }m\}\right).
\]

Let \(\Omega_7(R_2)\) minimize B(m) over root-modulus observers sufficient for \(\delta_P\le7\) throughout R2, and let \(\widehat\Omega_7(R_2)\) use complete residual trajectories instead. Here R2 is given as the domain, and m measures the additional observation; m is not required to include the already fixed progression modulus S2. The exact base-two orders of the required primes are:

| Family | Prime orders in the listed prime order of Section 1 | Maximum |
|---|---|---:|
| B | 144,144 | 144 |
| C | 180,45,45,180,90,180 | 180 |
| D | 54,108,27,108 | 108 |

Every sufficient modulus contains T and therefore has B(m) at least 180. Taking m=T attains that value for both kinds of observation. Hence

\[
\boxed{\Omega_7(R_2)=\widehat\Omega_7(R_2)=180.}
\tag{16}
\]

This is an exact threshold on the fixed fiber R2. It is not a statement that \(\Omega_7(R_1)=180\), nor that 180 is a prime-channel count, a modulus bit length, the full orbit period or an execution-time cost.

## 7. The minimum now ranges over all cost-seven roots in R2

The tail certificate exhausts the 1,160 phase/sign progression descriptions and gives their family minima:

| Family | Least positive root | Decimal digits |
|---|---:|---:|
| B | 142182133093029631521252488222753720130073171510309885943518183289197140261893115365205303 | 90 |
| C | 168515727251568031139784117408423468924151126118048106286760549300706338389494633573 | 84 |
| D | 1046533155647696956851681902279650889819246480725727047415947079817885251912744029965820233 | 91 |

The four-prime prefix is now proved necessary for every seven-prime supplement. Therefore the union of these descriptions is the entire \(\delta_P=7\) class, and the least of their starts is the global minimum in that specified fiber:

\[
\boxed{
\min\{a\in R_2:\delta_P(a)=7\}
=168515727251568031139784117408423468924151126118048106286760549300706338389494633573.
}
\tag{17}
\]

The attaining C-tail uses phases \(0\mapsto631\), \(1\mapsto181\), \(3\mapsto23311\), with root residues

\[
a\equiv337\pmod{631},\qquad
a\equiv178\pmod{181},\qquad
a\equiv22892\pmod{23311}.
\]

Its supplementary dictionary is \(\{5,13,19,73,181,631,23311\}\). Thus this root has exact supplementary cost seven and a complete cover using 27 primes including P. This note does not assert that its unrestricted total minimum covering cost equals 27, or that (17) minimizes over a larger root fiber or all Riesel coefficients.

## 8. Reproduction and native interpretation

Run `python verify_observer.py`. If the companion tail certificate is stored elsewhere, pass `--tail-certificate /path/to/tail_certificate.json`. The default resolver supports both the working directories and sibling `tail/` and `observer/` artifact directories.

The program reuses the saved prime inventory instead of repeating large factorization. It checks the exact small base-two orders, reconstructs all phase/root pairs, counts each family by both inclusion-exclusion and weighted category masks, checks every common-modulus intersection and disjoint partition, reconstructs the 1,160 short CRT starts, and supplies twelve explicit essential-coordinate witnesses. It writes `observer_certificate.json`, including all exact fractions, 60-digit decimal approximations, input hash, minima and scope boundaries. The analytic arguments in Sections 4–6 supply the universal claims about arbitrary moduli; they are not inferred from a finite sweep of moduli.

The native object remains the fixed-X6 typed integer register with positive singleton BRC weight and multiplicity one, evolving by \(x\mapsto2x+1\). The exponent coordinate w and the finite prime observations do not replace that integer state or discard its joint cofactor relations. The result identifies the precise finite residue information needed for one cost predicate on one fixed root fiber. No new native execution or independent formal Review is claimed.
