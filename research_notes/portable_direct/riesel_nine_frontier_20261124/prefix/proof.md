# The basic pair remains forced at budget nine; the one-W branch is classified

Research continuation, 2026-11-24. Author derivation and exact arithmetic in Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. This is collaborative mathematical checking, not independent project Review or formal acceptance.

The native object is the full typed integer register at the fixed Heartbeat X6 anchor, with positive singleton BRC weight and multiplicity one and update

\[
T(x)=2x+1,\qquad F_n(a)=a^2 2^n-1.
\]

The exponent fibers and prime phases below are arithmetic observations of that integer. They do not replace the native state or its joint divisor relations.

## 1. Results and scope

Retain the old twenty-prime dictionary P, the fixed 29-prime root family R1, and its historical 43-prime subfamily R3. The complete budget-eight classification is used with its proved scope.

**Theorem A (the basic pair).** For every a in R1, any complete supplement of at most nine distinct primes contains both 5 and 13. A dictionary of at most nine primes omitting either basic prime leaves full-exponent uncovered density at least 1/13860. This lower bound is a sufficient obstruction and is not asserted optimal.

Write

\[
Z=\{29,43,1429,5419\},\quad
K=\{92737,649657,77158673929,40388473189,118750098349\}.
\]

**Theorem B (all irredundant one-W dictionaries).** In R3, let Q be an inclusion-minimal complete supplement with at most nine primes, and suppose it contains exactly one of W={19,73}. Then Q has exactly nine primes. In the residual coordinate

\[
n=8+12v,
\]

its phases have exactly this form:

1. Q contains 5,13 and one W prime, whose v phase is r=0 modulo 3 for 19 and r=1 modulo 3 for 73.
2. All four primes of Z occur, with four different phases from v=1,2,3,4,5 modulo 7. Write c for the omitted phase.
3. The final two primes are different members of K. They occupy the two phases modulo 21 determined by

\[
v\equiv c\pmod7,\qquad v\not\equiv r\pmod3,
\]

one prime for each of the two missing modulo-three phases.

Every dictionary so described is inclusion-minimal relative to P and is realized by infinitely many positive roots in R3. There are

\[
2\cdot5\cdot4!\cdot5\cdot4=4800
\]

phase dictionaries and 4800*2^6=307200 sign-specific CRT progression descriptions. These descriptions need not be disjoint as sets of roots.

Inclusion-minimal means no prime can be deleted from the displayed supplement while retaining coverage with P. It does not exclude another smaller dictionary for the same root. We separately construct roots with exact supplementary cost nine by making the complete budget-eight predicate false. The displayed cover alone gives tau(a^2)<=29. For the specific 160-digit root below, an additional direct certificate of 29 pairwise-coprime integer terms proves the exact equality tau(a^2)=29.

## 2. Fixed residual sets and the all-order mass formula

The old P-holes are even indices n=2u, with

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}
\pmod{105}.
\end{split}
\]

They have full-exponent density 6/35. Their incidence maxima for gcd columns 1,3,5,7,15,21,35,105 are

\[
(36,23,11,7,6,4,2,1).
\tag{1}
\]

The R1 root residues at 5,13,19,73 give respectively the fixed u phases

\[
1\pmod2,\quad0\pmod6,\quad4\pmod9,\quad1\pmod9.
\tag{2}
\]

Primes 3,11,61,331,37,109 are inactive throughout R1. The old prime phases and these assertions are inherited verified input.

Prime 2 supplies no positive-index term, since F_n(a) is odd for n>=1. It therefore cannot increase any of the density capacities used below.

For an arbitrary residual set R modulo L and a congruence channel of period d, put g=gcd(d,L). Its absolute mass, in units of one whole residue class modulo L, is

\[
\frac{K_{R,g}(b)}{d/g},\qquad
K_{R,g}(b)=|\{x\in R:x\equiv b\pmod g\}|.
\tag{3}
\]

The total residual mass is |R|. Formula (3) is exact counting over a common period. Sums of these masses are upper bounds for the union, without any independence assumption. On one fixed residual point, a compatible channel covers one lift class of period d/g.

## 3. A nine-prime dictionary cannot omit both basic primes

On the full u-coordinate the effective period is t=ord_q(4). Apart from the following exceptions, every available supplementary prime has relative H-capacity at most 1/12:

| Prime or primes | Capacity of each | Number |
|---|---:|---:|
| 43 | 7/36 | 1 |
| 19,73, with their fixed phases | 13/108 | 2 |
| 5419 | 1/9 | 1 |
| 29 | 7/72 | 1 |
| 23,89,683 | 1/11 | 3 |

Here t=7 supplies only 43 outside P; t=14 supplies only 29; t=21 supplies only 5419; and t=11 supplies exactly 23,89,683. The new small-order identities include

\[
2^{22}-1=3\cdot23\cdot89\cdot683,
\quad \Phi_{21}(2)=7\cdot337,
\quad \Phi_{42}(2)=5419.
\]

The all-order remainder bound follows directly from (1) and (3):

| g=gcd(t,105) | Remaining t lower bound | Relative capacity bound |
|---:|---:|---:|
| 1 | 13 | 1/13 |
| 3 | 24 | 23/288 |
| 5 | 20 | 11/144 |
| 7 | 28 | 7/144 |
| 15 | 30 | 1/12 |
| 21 | 42 | 1/18 |
| 35 | 35 | 1/18 |
| 105 | 105 | 1/36 |

The fixed t=9 channels were removed as exceptions, t=18 channels are inactive, and the other excluded smaller periods contain only old/basic/inactive primes. Thus the table handles every multiplicative order.

Nine channels omitting both 5 and 13 therefore have union density at most

\[
\frac7{36}+2\frac{13}{108}+\frac19+\frac7{72}
+3\frac1{11}+\frac1{12}
=\frac{2375}{2376}<1
\tag{4}
\]

inside H. Their full-exponent uncovered density is at least

\[
\frac6{35}\left(1-\frac{2375}{2376}\right)=\frac1{13860}.
\tag{5}
\]

## 4. Exactly one basic prime is also impossible at budget nine

Either basic channel in (2) misses an entire u-parity. On that parity write u=epsilon+2z. At most eight other primes must cover the corresponding affine copy of H, and their effective periods are e=ord_q(16).

The full inventories needed here are:

| e | Eligible channels outside P/basic/inactive |
|---:|---|
| 7 | 29,43 |
| 9 | fixed 19,73 |
| 10 | 61681 |
| 14 | 15790321 |
| 18 | 433,38737 |
| 21 | 1429,5419 |

No eligible channel has e in {1,2,3,4,5,6,8,12,15}. In particular Phi_56(2)=15790321, Phi_72(2)=433*38737, and Phi_84(2)=1429*14449; the latter removes old 14449. Factorizations and exact orders are checked by the accompanying inventory certificate.

Delete all covered mod-seven rows supplied by the e=7 primes. Let m be the number of their distinct nonempty rows, so 0<=m<=2, and R the remaining subset of H. Duplicate or empty e=7 rows spend a slot without contributing to R and only strengthen the estimate below.

Write c_g=max_b K_{R,g}(b), r1=|{x in R:x=1 modulo 3}|, and

\[
G(R)=\max\left\{
\frac{|R|}{11},\frac{c_3}{8},\frac{c_5}{4},\frac{c_7}{4},
\frac{c_{15}}2,\frac{c_{21}}2,c_{35},c_{105}\right\}.
\tag{6}
\]

Every remaining prime outside the displayed exceptions has absolute mass at most G(R). This is (3), by all eight gcd columns after e=7,9,10,14,18,21 are removed. The corresponding lower periods are 11,24,20,28,30,42,35,105. The two fixed W channels have mass r1/3 each. The other exceptions contribute at most

\[
c_{21},c_{21};\quad c_5/2;\quad c_7/2;\quad c_3/6,c_3/6.
\tag{7}
\]

The affine pullback from z to the original u residues preserves every maximum c_g. Both fixed W phases satisfy u=1 modulo 3, so their masses remain r1/3 on either parity fiber; this is a fixed-phase calculation, not a freely optimized W phase.

Take the largest 8-m entries of the multiset formed by (7), r1/3 twice, and eight copies of G(R). Their sum U(R) bounds every possible remaining prime union. This relaxes simultaneous phase compatibility and therefore remains a valid upper bound.

There are only six occupied H rows modulo seven, with sizes 7,7,7,5,4,6. The 1+6+15=22 choices of deleted rows are fully and exactly evaluated. The maxima are

| m | Number of residual sets | Maximum U(R)/|R| | Minimum |R|-U(R) |
|---:|---:|---:|---:|
| 0 | 1 | 25/27 | 8/3 |
| 1 | 6 | 155/174 | 19/6 |
| 2 | 15 | 10/11 | 2 |

This is finite residue geometry after an all-prime bound, not a bounded prime search. It may equivalently be verified by listing the six deleted-row cases and the fifteen deleted-row pairs. The script retains every exact row and rational sum.

Since every parity fiber has full-exponent old-hole density 3/35, a gap of at least 2 absolute mass units leaves density at least

\[
\frac3{35}\frac2{36}=\frac1{210}>0.
\tag{8}
\]

This excludes exactly one basic prime. Together with (5), it proves Theorem A throughout R1, without using any additional R3 restriction.

## 5. The one-W residual geometry and its complete small-order inventories

After P,5,13 the holes are

\[
n=8+12v,\quad v\in A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{9}
\]

Its occupied modulo-seven rows are 1,2,3,4,5, with sizes 2,3,3,3,2. Its modulo-five column sizes are (3,5,5,0,0). Every occupied row has at most one point in each column.

The W phases are v=0 modulo 3 for 19 and v=1 modulo 3 for 73. The other fixed active small-order channels all lie in v=2 modulo 3:

\[
38737:v=5\pmod6,\quad246241:v=5\pmod9,
\quad487824887233:v=8\pmod{12}.
\]

On v=0 or v=1 modulo 3, every active remaining channel has h=ord_q(2^36)>=6. The inherited complete h=1,...,5 inventories establish this, including all nine eligible h=5 primes (11,61,331 and the old six-prime modulo-five family), which are inactive in R3.

The only h=6 primes are

\[
33975937,\quad138991501037953,
\tag{10}
\]

and the only h=10 primes are

\[
61681,\quad4562284561,\quad168692292721,
\quad469775495062434961.
\tag{11}
\]

These follow from the complete factorizations of Phi_216(2) for h=6 and Phi_40(2), Phi_120(2), Phi_360(2) for h=10. The prime inventories are based on orders, not a magnitude cutoff.

## 6. A six-class lemma: at least four period-seven rows

**Lemma.** Suppose at most six congruence channels cover every lift of A or an invertible affine copy modulo 35. Assume every active period h is at least six, at most two channels have h=6, and at most four have h=10. Then at least four distinct occupied rows modulo seven are supplied by h=7 channels.

Let m be the number of distinct occupied h=7 rows. Delete those rows from A. Duplicate or empty h=7 channels give no contribution to the residual set. We show that m=0,1,2,3 cannot cover.

### 6.1 No h=7 row

Let j be the number of h=10 channels, so j<=4. An h=6 row has absolute mass 13/6. An h=10 row has mass at most 5/2. Every other non-seven row has mass at most 5/3: the gcd-one column starts at h=8, the gcd-five column starts at h=15, the gcd-seven column starts at h=14, and the gcd-35 column has mass at most one.

If j<=2, the total mass is at most

\[
2\frac52+2\frac{13}{6}+2\frac53=\frac{38}{3}<13.
\tag{12}
\]

The right side bounds all smaller j as well, since 5/2 is the largest allowed non-seven contribution.

If j=3, the total upper bound is

\[
3\frac52+2\frac{13}{6}+\frac53=\frac{27}{2}.
\]

An h=10 row on the three-point column has mass only 3/2, losing one from this bound and making the total strictly below 13. Empty columns lose more. Thus any possible cover with j=3 places all three h=10 rows in the two five-point columns.

The entire three-point column is then left for the other three channels. Restrict to that modulo-five progression. Its three points occupy three different residues modulo seven. The effective period of a remaining channel is k=h/gcd(h,5). No k=1 or k=2 is possible, because h=5 and h=10 are unavailable here. On this three-point set the largest relative contribution is 1/3. Equality is possible only for k=3 or k=7, hence h=15 or h=35 (h=3,7 are excluded).

All three remaining channels must attain equality to cover. Their phases therefore lie on that same three-point column, and each has absolute A-mass one. The total A-mass is consequently at most 3*(5/2)+3=21/2<13, a contradiction.

If j=4, the upper bound is 4*(5/2)+2*(13/6)=43/3. Two h=10 rows on the three-point column lose at least two, leaving 37/3<13. Therefore that column has at most one h=10 row. One of its two parity subprogressions is entirely missed by all four h=10 rows.

Restrict to that modulo-ten progression. Again there are three occupied residues modulo seven. Only the two remaining channels can cover them. With k=h/gcd(h,10), no k=1 is available. Every relative contribution is at most 1/2; equality requires k=2. The possible h values for k=2 are 4 and 20, and h>=6 leaves only h=20. Thus both channels must be h=20, with phases on the three-point column. Their absolute A-mass is 3/4 each. The total mass is at most 10+3/2=23/2<13. This contradiction completes m=0.

### 6.2 One, two or three h=7 rows

Use formula (3) on the remaining rows.

| m | Residual size | Remaining slots | Sufficient absolute mass bound |
|---:|---|---:|---|
| 1 | 10 or 11 | 5 | at most 4*2+11/6=59/6 < 10 |
| 2 | 7 through 9 | 4 | each at most 3/2, total at most 6 < 7 |
| 3 | 5 or 6 | 3 | each at most 3/2, total at most 9/2 < 5 |
| 3 | 4 | 3 | each at most one, total at most 3 < 4 |

For m=1, c5<=4 and c7<=3. Only h=10 can reach mass two, and there are at most four such primes. Every other non-seven channel has mass at most 11/6, from h=6; the other gcd-column bounds are smaller. For m=2, c5,c7<=3 and |R|<=9, giving max{|R|/6,c5/2,c7/2,1}<=3/2. For m=3 the same bound applies, and the four-point case consists of two rows of size two.

These strict bounds prove the lemma. The exact script checks all residual row subsets and the rational inequalities. The restrictions to the small column used in the m=0 proof are full infinite progressions; they are not truncated executions.

## 7. Cross-phase consistency classifies the one-W dictionaries

Let Q be inclusion-minimal, contain just one W prime, and have at most nine members. Theorem A forces 5,13. The complete budget-eight theorem excludes an inclusion-minimal one-W supplement of size at most eight. Thus Q has nine members and six tail primes after these three selected primes.

Restrict to the other W phase, r'=1 if the selected prime is 19 and r'=0 if it is 73. All active tail channels have h>=6 and satisfy (10)-(11). The six-class lemma applies. Let m be the number of distinct occupied h=7 rows on this phase, so m=4 or 5.

A restricted h=7 channel has original v-period f=ord_q(2^12) equal to 7 or 21. The former is compatible with every modulo-three phase; the latter is confined to one. The complete f=7 inventory is exactly Z, containing four primes.

If m=4, the remaining A row contains two or three points, and both remaining channels are required on the first restricted phase. The same full-lift argument as in the budget-eight theorem gives just two possibilities: two h=14 rows with opposite lift parities, or (only for a two-point row) two h=35 rows, one at each point.

All these final rows occupy the same omitted mod-seven class c. On the other uncovered phase v=2 modulo 3, they cannot cover a different mod-seven row. Therefore each of the four h=7 rows must be an original f=7 row, using all Z. The two h=14 rows must both have original f=14 (rather than 42), or the two h=35 rows must both have original f=35 (rather than 105); otherwise their assigned half-lift or point is wholly or partly uncovered on v=2. But two f=14 or two f=35 rows together with the four f=7 rows already cover A on every modulo-three phase. The selected W prime can then be deleted. Inclusion-minimality excludes m=4.

Suppose m=5. Choose one restricted h=7 representative on each occupied mod-seven row. At most four of these five representatives can have original f=7. Every original f=21 representative misses the v=2 phase. Only the sixth tail prime can repair those missing rows there.

One congruence channel covering every lift of two distinct occupied mod-seven rows would have to have restricted period one: within a row its at least two modulo-five values force its period to divide seven, and between two rows its period must also divide a difference not divisible by seven. There is no active restricted-period-one prime on v=2 after P,5,13. Thus only one of the five representatives can have f=21, and the other four are precisely Z with four distinct phases.

The sixth tail prime must cover all lifts of the one remaining row on v=2. Its restricted period must divide seven; period one is unavailable, and no unused f=7 prime remains. It therefore has f=21 and the v=2 phase. The first f=21 prime occupies the other uncovered W phase r'. This is exactly the structure in Theorem B.

This reasoning also covers a sixth active h=7 row duplicating a row on the first restricted phase: such a duplicate cannot repair v=2 unless it is assigned there instead. There are only five occupied rows; m counts distinct rows, not prime slots.

## 8. The f=21 inventory, sufficiency, counts and exact-cost realization

Solving d/gcd(d,12)=21 gives d in {63,126,252}. Their complete cyclotomic factorizations are

\[
\begin{aligned}
\Phi_{63}(2)&=60247241209=92737\cdot649657,\\
\Phi_{126}(2)&=77158673929,\\
\Phi_{252}(2)&=4796135163359699664961
=40388473189\cdot118750098349.
\end{aligned}
\tag{13}
\]

Primality and exact orders are verified in the arithmetic certificate. This gives exactly K. Its five primes are all free relative to the 43 fixed R3 observations and the complete budget-eight observer.

For a tail prime q with assigned v phase b, impose

\[
a\equiv\pm2^{-(4+6b)}\pmod q.
\tag{14}
\]

CRT preserves R3 and realizes all six independent signs, since the six selected tail primes are distinct and coprime to the R3 modulus. The selected W prime covers one modulo-three phase throughout A; Z covers four mod-seven rows on every phase; the two K primes cover the other two modulo-three phases of the remaining row. This proves complete coverage.

Every tail prime has a private residual position: take an uncovered-by-W phase in its assigned mod-seven row, and for the two K primes use their respective assigned modulo-three phases. The W prime has a private point in the omitted row at its own modulo-three phase.

The basic primes are also necessary in this dictionary. If either could be deleted, the resulting complete dictionary would have at most eight primes and omit a basic prime, contrary to Theorem A (or the already proved budget-eight basic-pair theorem). Thus the supplement is inclusion-minimal. The 4800 and 307200 counts follow from the independent choices listed in Section 1.

To obtain exact cost nine, set a=0 at all 27 free coordinates of the complete budget-eight observer other than Z. These consist of its twelve retained-prefix tail primes, its three f=14 primes, and its twelve f=35 primes. These coordinates are all disjoint from the fixed 43 R3 primes and from K. This makes both alternatives of the complete budget-eight predicate false, while preserving (14) and the nine-prime cover. Therefore delta_P(a)=9 for every sufficiently large positive root in each resulting CRT progression. There are infinitely many such roots for every one of the 4800 phase dictionaries.

The script also finds the following 160-digit root, by taking the least CRT start among the 64 signs for one specified phase dictionary:

```text
2770714492093438838433084226801660296418766175867271008480060095168867099351242904608463381362983433276866993594996807812925055515290327478920627884582606119453
```

Its supplementary dictionary is

\[
\{5,13,19,29,43,1429,5419,92737,649657\}.
\]

The six new root conditions are:

| q | v period | v phase | a modulo q |
|---:|---:|---:|---:|
| 29 | 7 | 2 | 7 |
| 43 | 7 | 3 | 21 |
| 1429 | 7 | 4 | 665 |
| 5419 | 7 | 5 | 256 |
| 92737 | 21 | 1 | 40663 |
| 649657 | 21 | 8 | 2048 |

Here the omitted row is c=1, the selected W prime 19 covers v=0 modulo 3, and the two final channels cover v=1 and v=2 modulo 3 within that row. All 43 historical R3 coordinates are retained. The script evaluates the full 31-coordinate budget-eight predicate on this ordinary root and obtains false. Its supplementary minimum is therefore exactly nine.

The selected 29-prime dictionary's full residue-value period is 20160. The script actually performs all 584640 scalar prime-residue updates on that period, finds no uncovered index, and records a private index for each selected prime and the final full integer (21220 bits). This scalar calculation is not a new native BRC execution. The smaller common covering-predicate period after the old-hole reduction is 1260. The minimum scope of this displayed root is only the 64 signs of the specified phase dictionary, not the entire one-W family or all R3 cost-nine roots.

A separate 364-digit root recorded in the certificate sets all 27 additional observer coordinates to zero and gives a uniform exact-cost-nine CRT progression as described above. For that separate root the total-cost conclusion remains tau(a^2)<=29. Section 9 supplies a direct additional lower bound for the 160-digit root; no total-minimum equality is inferred from dictionary irredundancy.

## 9. The same 160-digit root has exact total cost 29

The new checker `verify_compact_coprime.py` uses the already verified selected dictionary and its complete 20160-position period. It lists all 6752 private indices in that period, retaining the entire index list for every selected prime. It then selects the following 29 exponents:

| Assigned prime | Private exponent n |
|---:|---:|
| 5 | 6 |
| 7 | 28 |
| 13 | 12 |
| 17 | 3 |
| 19 | 440 |
| 29 | 32 |
| 31 | 149 |
| 41 | 5 |
| 43 | 212 |
| 71 | 1133 |
| 97 | 117 |
| 113 | 413 |
| 127 | 113 |
| 151 | 341 |
| 241 | 33 |
| 257 | 87 |
| 281 | 233 |
| 337 | 248 |
| 641 | 207 |
| 673 | 237 |
| 1321 | 257 |
| 1429 | 2912 |
| 5419 | 4352 |
| 14449 | 53 |
| 29191 | 1853 |
| 65537 | 63 |
| 92737 | 20 |
| 649657 | 4640 |
| 6700417 | 495 |

Every displayed exponent belongs to the assigned prime's private set. All lie within the original complete period; the selection does not shift an index into a later period.

A purely first-feasible greedy pass in increasing assigned-prime order stalls at 92737. Its reason is explicit: all 32 private terms assigned to 92737 are divisible by the unselected but fixed prime 73, whereas the earlier first choice for 43, at n=128, is also divisible by 73. Any pairwise-coprime selection must reserve 73 for the 92737 witness. After imposing that necessary condition and continuing the same increasing-prime greedy rule, the displayed set is obtained; in particular the 43 witness becomes n=212.

The checker constructs all 29 **full integers** F_n(a), verifies their assigned proper divisor and private status, and computes every pairwise integer gcd. The actual result is

\[
\gcd(F_{n_i}(a),F_{n_j}(a))=1\quad(i\ne j),
\qquad\binom{29}{2}=406\text{ checked pairs}.
\]

A single prime cannot divide two of these terms. Any complete covering dictionary must therefore contain at least 29 different primes, regardless of whether it keeps the selected dictionary or any old prime. The proper 29-prime cover gives the matching upper bound. Hence this same ordinary root satisfies

\[
\boxed{\delta_P(a)=9,\qquad\tau(a^2)=29.}
\]

`compact_coprime_certificate.json` retains all private-index lists, the chosen full integers in hexadecimal, their exact assigned-prime quotients, the rejected earlier candidates, and all 406 gcd results. This is direct exact integer computation. It does not rerun the 4800 phase classification or claim a new native BRC execution.

## 10. Arithmetic verification and remaining scope

`verify_nine_prefix.py` uses only the Python standard library. It verifies the complete small-order factorization and prime certificates, the exact global capacity sum, all 22 residual H geometries for Theorem A, the six-class lemma's row geometry and strict rational inequalities, every phase pattern in the classified one-W family over a complete residual period, and an ordinary CRT root with false complete-eight predicate and a proper nine-prime supplement.

The all-prime statements rest on the gcd-column inequalities and phase-consistency arguments above. Finite computations certify their explicit arithmetic and finite incidence data. They are not a finite-prime approximation to the classification.

This component does not classify all nine-prime dictionaries in the two-W or zero-W branches, does not claim a global minimum cost-nine root, and does not claim a new native BRC execution. Theorem B is a complete classification of inclusion-minimal one-W nine-prime dictionaries in R3. Its exact-cost realization is a separate CRT restriction using the full proved budget-eight observer. The displayed 160-digit root additionally has a direct unrestricted-total-minimum certificate in Section 9.

Immutable dependencies: the v11 seven-cover source supplies the fixed H geometry and basic small-order inventories; v12 supplies the R3 lower bound and fixed fiber; v13 supplies the complete budget-eight prefix/tail classification and its 31-coordinate observer. Earlier proof files and certificates are used with their original scopes.
