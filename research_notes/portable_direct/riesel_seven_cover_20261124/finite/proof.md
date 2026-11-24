# A consecutive irredundant-cover chain and an eightfold stronger observer-order bound

**Status.** Author mathematical derivation with exact supporting arithmetic, within Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. The sub-agent's mathematical check is shared-context research assistance; it is not an independent project Review, formal acceptance, or Foundation promotion. No remote mutation or new native execution is claimed here.

The canonical entry pins supplied for this round are GK `b7f1066501848d4f1abee3949119115ce98928f5` and EM `213c3ec64486ac904789902cd4c13481b881fffd`. We reuse the [v10 finite-observer theorem](https://github.com/awdawmip/enterprise-math/blob/f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5/research_notes/portable_direct/riesel_finite_observers_20261124/finite/proof.md), the spectrum/coprimalization source at `af9e1a5e49386a28283781876e10742a71991036`, and the fixed R1 fiber source at `b1de1acbdc97b5e51d486127abd1fadd24babd99`. The small ternary primes and their exact orders are also checked in the [companion tail classification](../tail/proof.md) and independently in the accompanying calculator.

## 1. Precise strengthened statements

Retain

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

the old twenty-prime dictionary

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
1321,14449,29191,65537,6700417\},
\]

and

\[
\begin{aligned}
a_*&=690786768637635218740714348513373826260012289,\\
M&=1397394912916194098609132326092145093313722687204526281,\\
L&=80754838636615,\\
R_1&=\{a>0:a\equiv a_*\pmod{6M},\quad
a\equiv12926327728523\pmod L\},\\
R_2&=\{a\in R_1:a\equiv0\pmod{433},\quad
a\equiv38733\pmod{38737}\}.
\end{aligned}
\]

Here \(\delta_P(a)\) is the minimum number of supplementary primes outside P in a complete proper-prime cover, and \(\tau(a^2)\) is the minimum total number of primes in such a cover. An absent finite cover gives value infinity.

For an arbitrary positive integer N define

\[
B_N=\max\bigl(\{1\}\cup
\{\operatorname{ord}_q2:q\text{ an odd prime divisor of }N\}\bigr).
\tag{1}
\]

N represents additional observations; the fixed coordinates defining R1 or R2 are not automatically inserted into (1). They will already be identical for all roots in the respective construction.

**Theorem A, in R1.** Put

\[
j_N=\min\{j\ge0:54\cdot2^j>B_N\},\qquad s_N=j_N+7.
\tag{2}
\]

There exists one residue \(r_N\pmod N\) such that, for every integer \(s\ge s_N\), infinitely many positive ordinary integer roots satisfy

\[
\boxed{
a\in R_1,\quad a\equiv r_N\pmod N,\quad
\delta_P(a)=s,\quad \tau(a^2)=20+s.
}
\tag{3}
\]

For each s these roots contain a full arithmetic progression after deleting finitely many initial terms. The same \(r_N\) works for every s in the stated range.

**Theorem B, in R2.** The same conclusion holds with R2 in place of R1 and with

\[
j_N^{(2)}=\min\{j\ge1:54\cdot2^j>B_N\},\qquad
s_N^{(2)}=j_N^{(2)}+7.
\tag{4}
\]

The residues chosen for Theorems A and B need not be equal. Each is fixed before s varies in its own theorem. Neither threshold is asserted optimal.

The common root residue supplies the same complete trajectory

\[
F_n(a)\equiv r_N^2 2^n-1\pmod N\qquad(n\ge0).
\tag{5}
\]

Taking an lcm handles any prescribed finite collection of moduli, including arbitrary finite prime powers. These theorems concern one observation supporting many different roots and costs; they do not assert that one root has several exact costs or has infinite cost.

## 2. A cover of each consecutive size

### 2.1 The fixed four-channel prefix

Write n=2u. The permanent prefix is

\[
(q,d,c)=(5,2,1),(13,6,0),(19,9,4),(73,9,1),
\tag{6}
\]

where a row means \(u\equiv c\pmod d\). Its root residues, using \(a\equiv2^{-c}\pmod q\), are respectively 3,1,6,37, exactly as required in R1.

After P and (6), the remaining indices are

\[
u=16+18w,\qquad
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{7}
\]

The old dictionary covers all odd n. The old even holes form the inherited 36-element set H modulo 105, checked by the calculator. In particular \(16\in H\) and \(0\in B\).

### 2.2 The shifted dyadic-ternary covers

For k at least one, put

\[
H_k=3\cdot2^{k-1},\qquad G_k=3\cdot2^k.
\]

Define \(\mathcal C_k\) to have the following k+3 rows in w:

\[
w\equiv2^{j-1}\pmod{2^j},\quad 1\le j\le k,
\qquad w\equiv1\pmod3,
\tag{8}
\]

and the two rows in the table:

| Parity of k | Phase modulo \(H_k\) | Phase modulo \(G_k\) |
|---|---:|---:|
| even | 0 | \(2^{k+1}\) |
| odd | \(2^k\) | 0 |

Phases are interpreted modulo the indicated modulus. These are exactly the v10 dyadic-ternary phases shifted by one. The extension to k=1 is intentional: at k=1 the two modulus-three rows have different phases 1 and 2 and will use different primes.

The dyadic rows cover the integers of two-adic valuation 0 through k-1. Their complement is

\[
w=2^k t.
\tag{9}
\]

On this complement, the rows of moduli \(3,H_k,G_k\), in that order, have t-phases

\[
(1,0,2)\quad(k\text{ even}),\qquad
(2,1,0)\quad(k\text{ odd})
\pmod3.
\tag{10}
\]

Thus they cover all of (9), and \(\mathcal C_k\) covers every integer w.

It is irredundant. Explicit private residues in one period \(0\le w<G_k\) are

\[
w_j=\begin{cases}
2^{j-1},&j\text{ even},\\
3\cdot2^{j-1},&j\text{ odd},
\end{cases}
\qquad(1\le j\le k)
\tag{11}
\]

for the dyadic rows, and, for the last three rows in order,

\[
\begin{cases}
(2^k,0,2^{k+1}),&k\text{ even},\\
(2^{k+1},2^k,0),&k\text{ odd}.
\end{cases}
\tag{12}
\]

For (11), the two-adic valuation selects just the intended dyadic row, and its residue modulo three is 2 when j is even and 0 when j is odd. It therefore avoids the modulus-three row. The last two rows lie in a multiple of \(2^{k-1}\), so they miss all earlier dyadic rows; for j=k direct substitution into their phases excludes both. Formula (12) selects the three different complementary t-classes in (10). These checks also apply at k=1, whose rows are

\[
(m,b)=(2,1),(3,1),(3,2),(6,0)
\tag{13}
\]

with private residues \((3,4,2,0)\) modulo six.

### 2.3 One globally consistent choice of primes

Choose primes once, for the entire chain, as follows:

- \(D_j\) has exact base-two order \(36\cdot2^j\), for j at least one; fix \(D_1=38737\) and \(D_2=487824887233\).
- Fix \(R=246241\) and \(T_0=279073\), two different primes of exact order 108.
- For j at least one, choose \(T_j\) of exact order \(108\cdot2^j\); one may fix \(T_1=33975937\), of exact order 216.
- Fix \(Z=87211\), of exact order 54.

Every unspecified order exceeds six. The same primitive-prime theorem used in the inherited v7 and v10 constructions supplies a prime of each such exact base-two order. This uses only one prime per order; the sole duplicated order 108 is handled by the two explicit primes R and T0. The numerical primes listed here are checked by deterministic trial primality and exact order tests in the calculator.

Realize the j-th dyadic row of \(\mathcal C_k\) by \(D_j\), its permanent modulus-three row by R, its \(H_k\) row by \(T_{k-1}\), and its \(G_k\) row by \(T_k\). For a row (m,b), impose

\[
a\equiv2^{-c}\pmod q,\qquad c=16+18b,
\qquad\operatorname{ord}_q2=36m.
\tag{14}
\]

Its even-index zeros are exactly

\[
u\equiv c\pmod{18m}.
\]

In particular they are confined to the progression \(u\equiv16\pmod{18}\), and within that progression they give exactly \(w\equiv b\pmod m\).

The order families for the D and T primes are disjoint (their exact three-adic valuations are two and three). Distinct orders force distinct primes. R differs from T0 by construction. The maximum old-prime order is 105, which is verified in the old dictionary and in the calculator. The only new smaller orders requiring explicit freshness checks are 54 and 72; Z and D1 are visibly outside P. All larger new orders exceed 105. None of the new primes is a prefix prime or one of the fixed inactive R1 primes.

Let \(S_k\) be P together with the four prefix primes and these k+3 tail primes. It contains

\[
|S_k|=27+k\qquad(k\ge1).
\tag{15}
\]

### 2.4 The special initial member with seven supplementary primes

Define \(S_0\) using the same prefix and the three tail rows

\[
\begin{array}{c|c|c|c}
q&\operatorname{ord}_q2&u\text{-class}&w\text{-class on (7)}\\\hline
Z=87211&54&u\equiv16\pmod{27}&w\equiv0\pmod3\\
R=246241&108&u\equiv34\pmod{54}&w\equiv1\pmod3\\
T_0=279073&108&u\equiv52\pmod{54}&w\equiv2\pmod3.
\end{array}
\tag{16}
\]

These cover (7), so S0 is a complete cover with seven supplementary primes. The Z row also hits some odd u outside (7), but every such index is already covered by prime 5. This extra overlap does not destroy irredundancy, as the explicit witnesses below show. Z still has even base-two order and even exponent phase, so it never hits an odd n.

## 3. Privacy of all 27+k channels

### 3.1 The twenty unchanged old witnesses

In the displayed order of P, retain the old private positive exponent indices

\[
37,3,89,5,293,117,413,113,41,33,87,233,773,207,237,257,53,593,63,111.
\tag{17}
\]

They are all odd. Every new tail prime has even base-two order and even zero phase, so misses them. Prefix primes 5,13,19 likewise miss every odd n. Prime 73 is the only new channel whose base-two order is odd; its zero phase is \(n\equiv2\pmod9\), and none of (17) has that residue. Thus every old witness remains private in every S_k. The calculator also verifies their old-prime privacy directly at the old root residues.

### 3.2 Fixed private witnesses for the prefix

The following old-hole witnesses work for every k, including zero:

| Prefix prime | Private u | Private exponent n |
|---:|---:|---:|
| 5 | 3 | 6 |
| 13 | 6 | 12 |
| 19 | 76 | 152 |
| 73 | 10 | 20 |

Their u values lie in H and are in just the assigned prefix class. For k at least one, none is \(16\pmod{18}\), so all tail rows miss them. For k=0, none is \(16\pmod{27}\), so Z misses them as well; R and T0 still lie inside \(16\pmod{18}\). In particular, the possible extra odd-u hits of Z do not affect the 5-witness u=3.

### 3.3 Private witnesses for every tail

For k at least one, take a private residue from (11) or (12), and lift it simultaneously to

\[
w\equiv w_i\pmod{G_k},\qquad w\equiv0\pmod{35}.
\tag{18}
\]

This is possible because \(\gcd(G_k,35)=1\). Its index \(n=32+36w\) lies in an old hole and avoids all four prefix channels by (7). It belongs to exactly the assigned tail row. Choosing the nonnegative representative in (18) gives a positive exponent even when w=0.

For k=0, the private tail w-phases 0,1,2 modulo three lift in exactly the same way. Convenient lifts are 0,70,35, giving the private exponent indices

\[
Z:32,\qquad R:2552,\qquad T_0:1292.
\tag{19}
\]

For k=1, convenient lifts for \((D_1,R,T_0,T_1)\) are \((105,70,140,0)\), giving

\[
D_1:3812,\quad R:2552,\quad T_0:5072,\quad T_1:32.
\tag{20}
\]

Together with (17) and the four prefix witnesses, this proves irredundancy of all 27+k channels in S_k. At this stage irredundancy proves that this dictionary has no dispensable channel; exact minimum cost among all dictionaries will follow from coprimalization in Section 6.

## 4. Consecutive transitions preserve every sufficiently low-order observation

For k at least one, the dyadic rows already present and the permanent R row have unchanged phases in \(\mathcal C_{k+1}\). In addition,

\[
G_k=H_{k+1},
\]

and their two prescribed phases agree. If k is even, both are \(2^{k+1}\); if k is odd, both are zero. The same prime T_k is therefore retained with exactly the same u phase and root residue.

Here the two b values are identical integers, not merely congruent phase classes. Every specified \(c=16+18b\) lies in the corresponding interval \(0\le c<\operatorname{ord}_q4\) (also c=16 for Z). Thus the retained root residues are the same actual \(2^{-c}\), with no hidden sign change from replacing c by another representative.

The transition from S_k to S_{k+1} removes T_{k-1}, adds D_{k+1} and T_{k+1}, and retains every other prime. The initial transition removes Z, adds D1 and T1, and retains R and T0 with their phases from (16). Thus for every k at least zero the exact orders of the changing primes are

\[
\boxed{
\begin{array}{c|c}
\text{retired prime}&54\cdot2^k\\
\text{new dyadic prime}&72\cdot2^k\\
\text{new last prime}&216\cdot2^k.
\end{array}}
\tag{21}
\]

The minimum changing order is therefore \(54\cdot2^k\). Every step increases the supplementary dictionary size by exactly one.

This is a chain of complete irredundant covers of consecutive sizes. It is not an inclusion chain of prime sets or a refinement confined to the retired row: a newly introduced dyadic row can overlap a retained row, and a retained row may need a different private witness. Sections 2 and 3 prove each cover and its privacy directly. Only the unchanged prime phases, not unchanged tail private witnesses, are needed for the observer argument.

Fix N and take j from (2), or from (4) for R2. For every transition starting at k at least j, all three changing orders in (21) exceed B_N. No changing odd prime can therefore divide N. It follows that

\[
S_k\cap\{q:q\text{ an odd prime divisor of }N\}
\]

is the same set for every k at least j, and every prime in that intersection has the same phase. This single stabilization applies simultaneously to all costs \(s=k+7\ge j+7\).

## 5. One compatible root residue at every finite prime-power precision

Choose j as in the preceding section, and define a residue at each prime power \(q^e\Vert N\):

| Observed prime power | Fixed root residue modulo \(q^e\) |
|---|---|
| q=2 | \(a_*\bmod2^e\) |
| q in P | \(a_*\bmod q^e\) |
| odd q in \(S_j\setminus P\), with fixed u phase c | \(2^{-c}\bmod q^e\) |
| odd q outside \(S_j\) | 0 |

All powers of two give an odd residue. The other three rows are mutually exclusive, and the inverses in the third row exist. CRT gives one residue \(r_N\pmod N\).

For every k at least j, stabilization ensures that an observed prime in S_k belongs to the same row of this table and has the same prescribed phase. An observed odd prime outside S_k is outside S_j and has residue zero. The choice is therefore independent of k and of the final cost.

The table does not infer a prime-power phase from a phase modulo q. It chooses a particular compatible lift of the root residue. Only its reduction modulo q is needed to establish the channel; the complete trajectory modulo \(q^e\) follows from fixing the root itself modulo that power.

## 6. Coprimalization, exact minima and the two fixed fibers

Fix a final k at least j. Let S=S_k, and use the 27+k positive private exponent indices constructed in Section 3. They are distinct, because an index private to one channel cannot be private to another. Define

\[
D=\operatorname{lcm}_{q\ne q'\in S}\bigl(2^{|n_q-n_{q'}|}-1\bigr),
\qquad
E=D\Big/\prod_{p\in S}p^{v_p(D)}.
\tag{22}
\]

Retain the inherited old forcing factor

\[
T_{3,1}=\frac{2^{210}-1}
{\prod_{p\in P}p^{v_p(2^{210}-1)}}.
\tag{23}
\]

Impose simultaneously

\[
\begin{aligned}
a&\equiv a_*\pmod{2M},\\
a&\equiv2^{-c_q}\pmod q\quad(q\in S\setminus P),\\
\operatorname{lcm}(E,T_{3,1})&\mid a,\\
a&\equiv r_N\pmod N.
\end{aligned}
\tag{24}
\]

### 6.1 Prime-by-prime compatibility, including arbitrary observed powers

All powers of every dictionary prime have been removed from E. A dictionary prime also dividing N belongs to the stabilized observed subset, so its fixed prime-power lift agrees with its unchanged root residue. The old-prime lifts agree with the old congruence in the same way.

Every observed odd prime outside S has residue zero modulo its observed power, which is compatible with any power of that prime in E. E is odd, so it does not constrain the prescribed odd lift at powers of two.

The old primes have been removed from T3,1. No supplementary dictionary prime divides T3,1: their exact orders are 4,12,18,9 for the prefix, 54 for Z when present, 108 for R and T0 when present, and the numbers \(36\cdot2^j\), \(108\cdot2^j\) in the remaining families. None divides 210. For an odd prime, divisibility of \(2^{210}-1\) would require its exact base-two order to divide 210. Thus T3,1 is coprime to S; its intersections with N are all observed nondictionary primes, assigned residue zero.

General CRT proves that (24) has a nonempty arithmetic progression of roots. This addresses E at all of its prime powers, additional observed primes that are absent from the dictionary, and arbitrary finite powers in N. It does not merely check compatibility modulo the squarefree part of N.

### 6.2 Exact supplementary and total costs

Suppose a prime \(\ell\) divides two different private terms. Since it divides neither a nor 2, cancellation of the two congruences gives

\[
\ell\mid2^{|n_q-n_{q'}|}-1,
\]

so \(\ell\mid D\). If \(\ell\in S\), privacy excludes its occurrence in two private terms. If \(\ell\notin S\), it divides E and hence a, contradicting \(F_n(a)\equiv-1\pmod\ell\). Therefore all 27+k private terms are pairwise coprime.

Any complete prime cover needs at least one different prime for each of these terms. S supplies exactly 27+k covering primes, while the 7+k new private terms avoid P. For all sufficiently large positive roots in the progression (24), \(2a^2-1>\max S\), so every assigned divisor is proper. Consequently

\[
\boxed{\delta_P(a)=7+k,\qquad\tau(a^2)=27+k.}
\tag{25}
\]

### 6.3 R1 is preserved for every k, including zero

The four permanent prefix residues are exactly those prescribed by R1. None of the five inactive R1 primes 11,61,331,37,109 occurs in S: their base-two orders are 10,60,30,36,36, respectively, unlike every supplementary order above, and they are outside P.

The unchanged old private indices include 3 and 63, and also 5 and 41. Hence

\[
2^{60}-1\mid D,\qquad2^{36}-1\mid D.
\]

The five absent primes divide E and therefore a. Also \(3\mid T_{3,1}\), and \(3\mid a_*\), so the old congruence becomes the required congruence modulo 6M. These are exactly the R1 root restrictions. Adding N has not changed them. Together with (25), this proves Theorem A.

### 6.4 R2 is preserved for every k at least one

The old private indices 113 and 41 differ by 72, so

\[
2^{72}-1\mid D.
\]

Prime 433 has exact order 72 and is absent from every S_k; D1 was chosen to be 38737 instead. Thus \(433\mid E\) and \(a\equiv0\pmod{433}\).

For every k at least one, D1 is retained with u phase 34. Since \(\operatorname{ord}_{38737}2=72\),

\[
2^{-34}\equiv-4\equiv38733\pmod{38737}.
\]

These are the additional constraints defining R2. Therefore every coprimalized member with k at least one lies in R2, proving Theorem B when j is chosen from (4).

For k=0, 38737 is absent, so the same difference of old witnesses instead forces \(38737\mid E\) and \(a\equiv0\pmod{38737}\). The special cost-seven member therefore belongs to R1 and not to R2. This is why the lower index in (4) is one, even when B_N is small.

## 7. Necessary exponential order growth for exact budget decisions

Suppose a residue observation modulo N decides the Boolean predicate \(\delta_P(a)\le b\) on every root in R1. For each integer b at least seven, Theorem A implies

\[
\boxed{B_N\ge54\cdot2^{b-7}=\frac{27}{64}\,2^b.}
\tag{26}
\]

Indeed, if B_N were smaller than the displayed bound, then \(j_N\le b-7\). One residue class from (3) would contain roots of exact costs b and b+1, giving opposite answers to the budget predicate.

The identical argument using Theorem B proves (26) for a modulus deciding the predicate on all of R2 whenever b is at least eight. If \(\Omega_b(R)\) denotes the infimum of B_N over moduli sufficient for the stated budget predicate on R (and infinity if there are none), then

\[
\boxed{
\Omega_b(R_1)\ge\frac{27}{64}2^b\quad(b\ge7),\qquad
\Omega_b(R_2)\ge\frac{27}{64}2^b\quad(b\ge8).
}
\tag{27}
\]

The coefficient is eight times the preceding v10 coefficient \(27/512\), and the sufficient ranges start earlier. These are necessary bounds, not claims of sharpness. They concern arbitrary additional finite integer moduli; repeated finite powers of the same observed primes do not increase B_N. A complete residue trajectory is a function of the root residue, so failure of this stronger root-residue observation to decide the predicate also excludes sufficiency of the associated trajectory alone.

The fixed R1 or R2 coordinates are already held identical in these counterexamples. Their orders need not be added to B_N to obtain (26). The result does not rule out adaptive procedures with unbounded access to the underlying integer state.

## 8. Application to the complete seven-budget observer on R2

Let

\[
\mathcal T=\{181,577,631,23311,54001,87211,246241,262657,279073,
18837001,29247661,487824887233\},\qquad T=\prod_{q\in\mathcal T}q.
\tag{28}
\]

These are the twelve additional prime coordinates in the complete seven-budget classification, with maximum base-two order \(B_T=180\). Since

\[
54\cdot2^1=108\le180<216=54\cdot2^2,
\]

Theorem B starts at j=2 and cost nine. The selected C2 dictionary meets this twelve-prime set in exactly R=246241 and D2=487824887233, whose phases are u=34 and u=52. In the observer construction, choose

\[
a\equiv182629\pmod{246241},\qquad
a\equiv487823838657\pmod{487824887233},
\tag{29}
\]

the respective values of \(2^{-34}\) and \(2^{-52}\), and choose residue zero at each of the other ten primes in \(\mathcal T\). CRT gives

\[
\begin{aligned}
T&=35095524795781473254136196580356738045833417602831290421525609131,\\
r_T&=21450781839625171583347380029424471704699683386785900439176732195,
\end{aligned}
\]

with \(0\le r_T<T\). The calculator checks each of its twelve root residues.

All subsequent C_k retain R and D2 with the same phases. Therefore this one twelve-coordinate observation, together with the 31 fixed R2 coordinates, supports

\[
\boxed{\text{every exact supplementary cost }s\ge9,
\quad\text{with exact total cost }20+s,}
\tag{30}
\]

each on infinitely many ordinary roots with the same **43 complete prime-residue trajectories**. The same statement also holds for the entire trajectory modulo T.

In the seven-budget classification, all three completion-family predicates are false at this observation: the binary family lacks 577, the ternary family has only one active member of its four-prime set, and all six modulo-five primes are inactive. This agrees with (30). The result shows directly that even the observer sufficient for the entire seven-budget question does not determine all higher exact costs. No claim is made here about which costs below nine occur in this particular observation fiber.

## 9. Verification and native scope

Run `python verify_refinement.py` from this component directory. The calculator checks the complete \(\mathcal C_k\) periods for k=1 through 8 and the special k=0 member, the displayed private residues and their old-hole lifts, all fixed prefix and old private witnesses, every adjacent retained phase and changed order in that range, the numerical seed primes by deterministic primality and exact orders, and concrete complete n-periods for S0 and S1. It also checks representative strict threshold boundaries and prime-power observer lifts. Universal assertions follow from Sections 2–7, not from extrapolation of these finite checks.

The external existence dependency is unchanged: the base-two primitive-prime theorem used by the pinned v7/v10 sources supplies one prime of each requested order greater than six. No new theorem about multiplicities of primitive prime factors is assumed. The two required order-108 primes are explicit and verified.

The native fixed-X6 typed integer register, positive singleton weight and multiplicity one remain unchanged. The updates are \(x\mapsto2x+1\), or \(x\mapsto4x+3\) on even indices. Congruence trajectories are observations of that state, not substitute axes. The coprimalization step explicitly uses joint integer and cofactor relations. The result identifies a limitation of every prescribed finite congruence observation for the stated exact-cost question, while retaining the complete integer state.
