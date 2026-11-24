# The exact finite cost spectrum of the fixed 43-prime observation fiber

Research continuation, 2026-11-24 (Asia/Hong_Kong). This is an author derivation with shared-context mathematical assistance and exact computation. It continues Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`; it does not assert independent project Review or Foundation promotion.

## 1. Result and dependencies

Retain the native integer trajectory

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,
\qquad F_n(a)=a^2 2^n-1,\quad n\ge1.
\]

The spatial anchor is fixed in Heartbeat X6. The integer register, positive singleton BRC weight and multiplicity one, and joint divisor relations are unchanged. Exponent restrictions and prime residues are observations of this state.

Let P be the old twenty-prime dictionary, let \(\delta_P(a)\) be the smallest supplementary-prime count for a complete proper-prime cover, and let \(\tau(a^2)\) be the unrestricted total count. We use the complete seven-cover theorem and its observer from the saved [v11 source](https://github.com/awdawmip/enterprise-math/blob/a88e3e001275269cae93c40d77e6984b1ef2970f/research_notes/portable_direct/riesel_seven_cover_20261124/README.md), specifically `observer/proof.md`, `tail/proof.md`, and `finite/proof.md`.

The v11 finite-observer construction fixed a particular 43-prime observation fiber and proved that all exact supplementary costs at least nine occur in it. Its cost-eight case was left open. We prove here:

> **Theorem.** In that same fixed fiber R3, no root has supplementary cost at most seven, and for every integer \(s\ge8\) there are infinitely many positive ordinary roots with
> \[
> \delta_P(a)=s,\qquad\tau(a^2)=20+s.
> \]
> Consequently its set of finite supplementary costs is exactly \(\{8,9,10,\ldots\}\).

Only the cost-eight construction is new here. The costs at least nine are reused from the cited consecutive-cover theorem. The statement concerns finite costs across different integer roots; the status of infinite cost at an individual root is unchanged.

## 2. The fixed fiber

Use the v11 R2 progression

\[
R_2=\{A_2+S_2j:j\ge0\},
\]

\[
\begin{aligned}
A_2&=9807947978443488306255509703402695727949968778703073231931137913705883712843,\\
S_2&=11356718000553566643685496313583434507970452519839503606327232707476034989690.
\end{aligned}
\]

Let

\[
\mathcal T=\{181,577,631,23311,54001,87211,246241,262657,279073,
18837001,29247661,487824887233\},
\]

\[
\begin{aligned}
T&=\prod_{q\in\mathcal T}q
=35095524795781473254136196580356738045833417602831290421525609131,\\
r_T&=21450781839625171583347380029424471704699683386785900439176732195.
\end{aligned}
\]

Define exactly the v11 fiber

\[
R_3=\{a\in R_2:a\equiv r_T\pmod T\}.
\tag{1}
\]

It fixes \(a\equiv182629\pmod{246241}\), \(a\equiv487823838657\pmod{487824887233}\), and root residue zero at the other ten primes of \(\mathcal T\). The existing R2 condition already fixes \(a\equiv38733\pmod{38737}\) and makes 433 inactive.

The complete seven-cover predicate has three alternatives. Its binary alternative requires both 577 and 487824887233 to be active, its ternary alternative requires three active members of \(\{87211,246241,262657,279073\}\), and its modulo-five alternative requires three active members of \(\{181,631,23311,54001,18837001,29247661\}\). In (1), 577 is inactive, only one ternary member is active, and every modulo-five member is inactive. Hence

\[
\delta_P(a)\ge8\qquad(a\in R_3),
\tag{2}
\]

where infinity is allowed. This lower bound uses the proved complete classification, with no assumption that an eight-prime dictionary must contain the four-prime prefix.

The exact positive CRT progression of (1) has

\[
\begin{aligned}
A_3={}&191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163,\\
S_3={}&398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390.
\end{aligned}
\]

Thus \(R_3=\{A_3+S_3j:j\ge0\}\), with \(S_3=S_2T\). The calculator verifies all 43 fixed prime residues directly.

## 3. A four-channel tail closes the missing budget

After P and the permanent supplementary prefix \(\{5,13,19,73\}\), the remaining positions have

\[
n=32+36w,\qquad
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{3}
\]

On this progression, the two already fixed active primes 38737 and 246241 have phases

\[
38737:\ w\equiv1\pmod2,
\qquad246241:\ w\equiv1\pmod3.
\tag{4}
\]

Together they leave only \(w\equiv0,2\pmod6\). The cyclotomic value needed for these two separate channels has **two** prime factors:

\[
2^{72}-2^{36}+1
=4722366482800925736961
=33975937\cdot138991501037953.
\tag{5}
\]

Set \(q_0=33975937\), \(q_2=138991501037953\). Each is prime and has exact base-two order 216. The new calculator proves primality by deterministic trial division and checks

\[
2^{216}\equiv1,\quad2^{108}\not\equiv1,\quad2^{72}\not\equiv1\pmod{q_i}.
\]

Since the only prime divisors of 216 are 2 and 3, these are the full exact-order conditions. Thus each has effective w-order \(216/\gcd(216,36)=6\).

Impose

\[
a\equiv\pm2^{-16}\pmod{q_0},
\qquad a\equiv\pm2^{-52}\pmod{q_2}.
\tag{6}
\]

The respective zero phases are exactly w=0 and w=2 modulo six. Every w is covered by the resulting four tail rows:

| w modulo 6 | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| An assigned covering prime | q0 | 38737 or 246241 | q2 | 38737 | 246241 | 38737 |

This covers all integers w, hence every remaining position in (3).

Both new primes are coprime to \(S_3\). Therefore CRT gives an infinite progression satisfying (1) and (6). Every sufficiently large positive root has the proper-prime cover

\[
P\cup\{5,13,19,73,38737,246241,33975937,138991501037953\}.
\tag{7}
\]

Equations (2) and (7) give exact supplementary cost eight. This already settles existence without requiring a new all-eight classification.

## 4. A 162-digit explicit root

We may interchange q0 and q2 between the two required modulo-six phases and choose either square-root sign at each new prime. There are eight resulting CRT progression descriptions. Their least positive starts are compared exactly by the calculator. The minimum **within these eight descriptions** is

```text
125881617004399660936368886076947194311916726055055408371127347321463572549463017011507634869211696849333543777014426253559019210427608296334538652533279482688323
```

It takes

\[
a\equiv27805045\equiv-2^{-16}\pmod{33975937},
\]

\[
a\equiv78995000769671\equiv2^{-52}\pmod{138991501037953}.
\]

Its progression modulus is

```text
1882193506041577506720717148257793257873305552571031460405060612994787383876103680661651551386771014417604461024539384321953341935308843344834152366111751480913790
```

This compact root has \(\delta_P=8\) and \(\tau\le28\). A separate coprimalized progression below proves exact total cost 28. No claim of the minimum over all cost-eight roots in R3 is needed or made.

## 5. Exact total cost 28 while preserving all 43 observations

Irredundancy of (7) alone would not establish a minimum among all dictionaries. We supply 28 pairwise-coprime private terms after a compatible root refinement.

### 5.1 Private positions and the additional fixed active observer

Fix the phase orientation in (6), with either sign choice. Retain the following old private exponents in the displayed P order:

\[
\begin{aligned}
P={}&(7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417),\\
n_P={}&(37,3,89,5,293,117,413,113,41,33,87,233,773,207,237,257,53,593,63,111).
\end{aligned}
\]

The remaining private positions are

| Assigned prime | Private n | Corresponding w for tail rows |
|---:|---:|---:|
| 5 | 6 | — |
| 13 | 12 | — |
| 19 | 152 | — |
| 73 | 20 | — |
| 38737 | 3812 | 105 |
| 246241 | 10112 | 280 |
| q0 | 32 | 0 |
| q2 | 5072 | 140 |

The new q0 and q2 channels have even exponent phases and order 216, so they miss all twenty odd old witnesses. They miss the four prefix witnesses by direct reduction modulo 216. The tail w values all belong to B modulo 35 and occupy respectively the private modulo-six phases 3,4,0,2. This proves privacy in (7); the calculator also checks every one of the 28 by direct modular arithmetic.

Among all 43 fixed prime coordinates, the only active prime not selected in (7) is

\[
q_*=487824887233.
\]

It has fixed exponent phase \(n\equiv104\pmod{144}\), equivalently w=2 modulo four on (3). It misses all odd old witnesses and all four prefix witnesses. The four tail w values are respectively 1,0,0,0 modulo four, so it also misses all four tail witnesses. Every other unselected fixed prime has root residue zero and therefore divides no term.

This explicit check is necessary: simply forcing all non-dictionary difference factors into a would conflict with the fixed nonzero residue at q*. We retain q* as a fixed observer and avoid it at the private positions.

### 5.2 Compatible coprimalization lemma in this construction

Let \(K=S_3q_0q_2\), and let \(a\equiv c\pmod K\) be a fixed choice from (1) and (6). Let \(n_1,\ldots,n_{28}\) be the private indices just listed. Define

\[
D=\mathop{\operatorname{lcm}}_{i<j}(2^{|n_i-n_j|}-1),
\qquad
E=\frac{D}{\prod_{p\mid K}p^{v_p(D)}}.
\tag{8}
\]

Then \(\gcd(E,K)=1\). Hence the pair

\[
a\equiv c\pmod K,\qquad a\equiv0\pmod E
\tag{9}
\]

has infinitely many positive solutions, preserving every fixed observation and every dictionary phase.

Suppose a prime \(\ell\) divides two distinct private terms. The terms are odd and \(F_n(a)\equiv-1\pmod\ell\) if \(\ell\mid a\), so \(\ell\nmid2a\). Cancellation gives

\[
\ell\mid2^{|n_i-n_j|}-1,
\]

and therefore \(\ell\mid D\). If \(\ell\nmid K\), then \(\ell\mid E\mid a\), a contradiction. If \(\ell\mid K\), it is a dictionary prime, an inactive fixed prime, 2 or 3, or q*. A dictionary prime hits exactly its own private term; the inactive primes, 2 and 3 hit none; q* was explicitly shown to hit none. This also contradicts divisibility of two private terms.

Thus all 28 private terms are pairwise coprime. Any complete prime dictionary requires at least 28 distinct primes to meet them. The eight new private terms additionally avoid P, so any supplement requires at least eight primes. The dictionary (7) supplies both upper bounds. For all sufficiently large positive solutions of (9), every chosen divisor is proper, and

\[
\boxed{\delta_P(a)=8,\qquad\tau(a^2)=28.}
\tag{10}
\]

This is an infinite arithmetic progression of ordinary integers, not a formal inverse-limit root.

### 5.3 An actually evaluated exact-total example

The optional `--coprimalized-example` computation has been executed. It computes D, E and a positive CRT root in (9), forms all 28 integer private terms, and checks all \(\binom{28}{2}=378\) greatest common divisors exactly. Every gcd is one.

The bit lengths are:

| Integer | Bits |
|---|---:|
| D | 478680 |
| E | 478087 |
| Chosen root | 478618 |
| CRT progression modulus KE | 478626 |

The certificate retains the complete root, E and progression modulus as hexadecimal integers. The existence proof is Section 5.2; the evaluated example verifies its implementation on the displayed private indices.

## 6. Complete finite spectrum in R3

The v11 consecutive-cover theorem already proves, for the exact fiber (1),

\[
\forall s\ge9\quad\exists^\infty a\in R_3:
\delta_P(a)=s,\quad\tau(a^2)=20+s.
\]

Adding (10) proves the theorem in Section 1. Equation (2) excludes every smaller finite supplementary cost. All these roots have identical full future residue-value trajectories at each of the 43 fixed primes because their root residues are fixed. The new construction fills the first possible cost, rather than changing the observed trajectory.

## 7. Verification and reproducibility

Run

```sh
python verify_cost_eight.py --coprimalized-example
```

The script uses only Python's standard library. It verifies the cyclotomic product, both new primes by deterministic trial division, exact order 216, every fixed root residue, the complete modulo-six cover, all eight signed/swapped CRT progressions, the full 60480-step selected-prime residue period of the 162-digit root, all 28 private witnesses, the exceptional fixed active observer, and the exact coprimalized example. Its scalar recurrence is an arithmetic verification; a separately reported native BRC run retains its own scope.

The saved files are `verify_cost_eight.py` and `cost_eight_certificate.json`. The compact example and the coprimalized example are distinct; their total-cost statements are respectively an upper bound and an equality.
