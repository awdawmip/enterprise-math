# The exact small-cost gap and the sharp four-channel residual density

Status: author derivation and exact arithmetic certificate, in the existing direct research activity. Researcher `EM-DIRECT-970E1C`; Activity `RA-D2EC212845B63844081F9A14`. This is not an independent project Review.

## 1. Setting and results

Keep the typed integer register

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

with its native positive singleton BRC update \(x\mapsto2x+1\), weight and multiplicity both 1, at the unchanged X6 anchor. Arithmetic indices and prime observer channels retain their earlier types; the channels are not new spatial axes or native branches.

Use the fixed old root and prime dictionary from the earlier source:

\[
a_*=690786768637635218740714348513373826260012289,
\]

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
1321,14449,29191,65537,6700417\},
\]

\[
M=\prod_{p\in P}p
=1397394912916194098609132326092145093313722687204526281.
\]

Throughout, \(a>0\) and \(a\equiv a_*\pmod{2M}\). These roots have exactly the same full old P residue trajectory. The old primes cover all odd indices, while the old holes at even indices \(n=2u\) are exactly

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}
\subset\mathbb Z/105\mathbb Z.
\end{split}
\]

There are 36 such residues. Thus the density of old holes among all exponent indices is \(36/210=6/35\). Every sequence term is composite: the old dictionary covers odd indices, and the even terms factor as \((a2^u-1)(a2^u+1)\). The smallest positive root in this congruence class is already much larger than 1.

Write \(\delta_P(a)=\min_C|C\setminus P|\), where C ranges over finite proper prime covers, with infinity if there is none.

**Theorem A — sharp four-channel obstruction.** Let Q be any set of at most four odd primes outside \(P\cup\{3\}\). For every root a in this old class, the positive exponent indices having no divisor in \(P\cup Q\) have natural density at least

\[
\boxed{\frac1{140}.}
\]

The density exists because each finite prime dictionary defines a periodic divisibility predicate. The bound is attained by an explicitly realizable root and the four channels in Section 6. In particular, the assertion is uniform in prime sizes, orders, phases and the chosen root; there is no prime cutoff.

When \(3\mid a\), prime 3 is inactive, so the same bound applies to **every** set of at most four new prime channels, including one that redundantly lists 3.

**Corollary B — complete classification below 5.**

\[
\boxed{\delta_P(a)=1\iff 3\nmid a.}
\]

For \(3\mid a\), either \(\delta_P(a)\ge5\) is finite or \(\delta_P(a)=\infty\). Additional costs 0, 2, 3 and 4 never occur in this old residue class. Section 6 supplies a 61-digit root with exact additional cost 5. Combining this obstruction with the companion construction attaining every integer at least 5 gives the complete **finite** additional-cost spectrum

\[
\{1\}\cup\{5,6,7,\ldots\}.
\]

The last displayed spectrum uses that companion construction; the proof below independently establishes all its exclusions and the two explicit costs 1 and 5. Whether infinity occurs at a root in this class is a separate open question in this research.

## 2. Exact density of a congruence class inside a periodic set

Let \(A\subseteq\mathbb Z/L\mathbb Z\), with \(|A|=K>0\), and put
\(A^*=\{u:u\bmod L\in A\}\). For a congruence class \(c\pmod d\), let

\[
g=\gcd(d,L),\quad e=d/g,\quad
K_g(c)=|\{h\in A:h\equiv c\pmod g\}|.
\]

Its relative density in \(A^*\) is exactly

\[
\rho_A(c,d)=\frac{K_g(c)}{Ke}.
\tag{1}
\]

Indeed, in one period \(\operatorname{lcm}(L,d)=Le\), the set A has Ke positions. Each compatible residue h supplies exactly one intersection by the elementary CRT, so the intersection has \(K_g(c)\) positions. This is a finite count, and immediately proves the density statement. For a union of channels, the sum of their relative densities is an upper bound; no independence assumption is made.

For H, the exact incidence table is:

| \(g\mid105\) | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\max_c K_g(c)\) | 36 | 23 | 11 | 7 | 6 | 4 | 2 | 1 |

The only nonempty residues modulo 3 are 0 and 1. More precisely:

| Subset \(H_r=\{h\in H:h\equiv r\pmod3\}\) | Size | Maximum in one mod-5 class | Maximum in one mod-7 class |
|---|---:|---:|---:|
| \(r=0\) | 23 | 6 | 4 |
| \(r=1\) | 13 | 5 | 3 |

The certificate recomputes these tables directly from the given H.

## 3. Three uniform channel bounds

An active odd prime q has one zero class \(u\equiv c\pmod{d_q}\) in the even subsequence, where

\[
d_q=\operatorname{ord}_q(4).
\]

An inactive prime contributes density zero. All upper bounds below allow every phase, so root compatibility cannot weaken them.

### 3.1. All old holes, with 5 and 13 absent

For \(q\notin P\cup\{3,5,11,13\}\), we have \(d_q\ge7\). The complete factorizations of \(4^j-1\), for \(1\le j\le6\), only involve primes

\[
\{3,5,7,11,13,17,31\}\subseteq P\cup\{3,5,11,13\}.
\]

Applying (1) for every possible \(g=\gcd(d_q,105)\) gives the following upper bounds when \(d_q\ge7\):

| g | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Relative density bound | \(1/8\) | \(23/108\) | \(11/72\) | \(7/36\) | \(1/6\) | \(1/9\) | \(1/18\) | \(1/36\) |

Each entry uses the smallest possible d for that gcd; all larger d reduce its value. The maximum is \(23/108\). Prime 11 has \(d_{11}=5\) and density at most \(11/36\). Consequently any at most four channels avoiding 3, 5 and 13 cover at most

\[
\frac{11}{36}+3\frac{23}{108}=\frac{17}{18}
\tag{2}
\]

of H. If 11 is absent the upper bound is smaller; adding its upper bound is harmless.

### 3.2. One fixed parity of the old holes

Fix \(\varepsilon\in\{0,1\}\) and write \(u=\varepsilon+2v\). Because 2 is a unit modulo 105, the old-hole residues in v form an affine permutation of H. Their incidence maxima are therefore exactly the same table. The effective period of a prime channel in v is

\[
e_q=\operatorname{ord}_q(16)=d_q/\gcd(d_q,2).
\]

Suppose \(q\notin P\cup\{3,5,13\}\). Then \(e_q\notin\{1,2,3,6\}\). If it were in that set, it would divide 6 and q would divide

\[
16^6-1=2^{24}-1=3^2\cdot5\cdot7\cdot13\cdot17\cdot241,
\]

whose primes all belong to the excluded set.

For the eight possible gcds \(g=\gcd(e_q,105)\), formula (1) now gives:

| g | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Relative density bound | \(1/4\) | \(23/108\) | \(11/36\) | \(7/36\) | \(1/6\) | \(1/9\) | \(1/18\) | \(1/36\) |

In the g=3 column, e=3 and e=6 are excluded, so e is at least 9. Thus every remaining prime covers at most

\[
\boxed{11/36}
\tag{3}
\]

of the old holes in either fixed parity. This also covers primes with very large orders.

### 3.3. One fixed parity and one fixed mod-3 residue

Now restrict to \(u\equiv\varepsilon\pmod2\) and \(u\equiv r\pmod3\), with \(r=0\) or 1. Parameterize this progression by \(u=u_0+6v\). Its hole residues form an affine permutation modulo 35 of \(H_r\), after removing the fixed mod-3 coordinate. There are 23 or 13 residues respectively, with the mod-5 and mod-7 maxima in Section 2.

The effective prime-channel period is

\[
f_q=\operatorname{ord}_q(4^6).
\]

For the same remaining primes \(q\notin P\cup\{3,5,13\}\), we have \(f_q\ge3\): periods 1 and 2 would again make q divide \(4^{12}-1=2^{24}-1\).

There are only four possible gcds with 35. Formula (1) yields:

| Subset | gcd 1 | gcd 5 | gcd 7 | gcd 35 | Maximum |
|---|---:|---:|---:|---:|---:|
| \(r=0\), size 23 | \(1/3\) | \(6/23\) | \(4/23\) | \(1/23\) | \(1/3\) |
| \(r=1\), size 13 | \(1/3\) | \(5/13\) | \(3/13\) | \(1/13\) | \(5/13\) |

Both maxima are strictly smaller than one half.

## 4. The complete four-channel argument

Measure all following gaps **relative to the entire old-hole set**. The two parities each contain exactly one half of it because 105 is odd. A fixed parity and residue r modulo 3 contain \(|H_r|/72\) of it.

Discard inactive channels. If a listed 5 or 13 is inactive, it falls in the corresponding absent-channel case. For an active 5 its zero class has one fixed parity; for an active 13 its zero class modulo 6 has one fixed parity and one residue modulo 3.

1. **Neither 5 nor 13 is active.** Equation (2) leaves a gap of at least \(1/18\), which is larger than \(1/24\).

2. **Exactly one of 5 and 13 is active.** In the parity missed by that channel, the other at most three channels have individual density at most \(11/36\) by (3). The missed fraction of the full old-hole set is at least
   \[
   \frac12\left(1-3\frac{11}{36}\right)=\frac1{24}.
   \]

3. **Both are active, with the same zero parity.** In the opposite parity only at most two other channels can hit. The gap is at least
   \[
   \frac12\left(1-2\frac{11}{36}\right)=\frac7{36}>\frac1{24}.
   \]

4. **Both are active, with different zero parities.** Work in the parity hit by 13 and missed by 5. If 13's residue modulo 3 is 2, it hits no old holes there, and the preceding two-channel bound applies. If its residue is 0, restrict to the remaining r=1 holes. The two other channels cover at most \(10/13\) of that subset, leaving at least
   \[
   \frac{13}{72}\left(1-\frac{10}{13}\right)=\frac1{24}
   \]
   of all old holes. If its residue is 1, restrict instead to r=0 and obtain the larger gap
   \[
   \frac{23}{72}\left(1-\frac23\right)=\frac{23}{216}>\frac1{24}.
   \]

These cases exhaust every set of at most four channels. The uncovered fraction of old holes is always at least 1/24. Multiplying by their full exponent-index density gives

\[
\frac6{35}\cdot\frac1{24}=\frac1{140},
\]

which proves Theorem A.

The proof uses one complete list of gcds with 105 or 35 and a few exact small factorizations. It never assumes that the added primes, their orders or a finite search range bound the whole problem.

## 5. The small-cost classification and the density of its easiest branch

If \(3\nmid a\), then \(a^2\equiv1\pmod3\). For every even n,

\[
a^22^n-1\equiv0\pmod3.
\]

Thus \(P\cup\{3\}\) is a proper cover. Old holes exist, so no cover using only P is possible and \(\delta_P(a)=1\).

If \(3\mid a\), prime 3 divides no term. Theorem A excludes every supplement of size at most four. It follows that additional costs 2, 3 and 4 cannot occur, and cost 1 occurs exactly in the stated branch. Cost 0 is excluded by the nonempty periodic hole set.

Prime 2 is inactive because every \(F_n(a)\) is odd, so allowing it in an arbitrary prime cover does not change any of these minima.

Since \(\gcd(2M,3)=1\), the positive roots in \(a_*+2M\mathbb Z\) visit the three classes modulo 3 equally. Therefore the roots with \(\delta_P(a)=1\) have exact relative density 2/3 within this arithmetic progression. The other third is the branch in which every four-channel supplement retains the sharp positive residual density of Theorem A.

## 6. Sharpness and a small exact-cost-five root

The following four channels realize equality:

| q | \(\operatorname{ord}_q2\) | \(\operatorname{ord}_q4\) | Even zero class | Root congruence |
|---:|---:|---:|---|---|
| 5 | 4 | 2 | \(u\equiv1\pmod2\) | \(a\equiv3\pmod5\) |
| 13 | 12 | 6 | \(u\equiv0\pmod6\) | \(a\equiv1\pmod{13}\) |
| 11 | 10 | 5 | \(u\equiv0\pmod5\) | \(a\equiv1\pmod{11}\) |
| 61 | 60 | 30 | \(u\equiv16\pmod{30}\) | \(a\equiv25\pmod{61}\) |

They leave exactly

\[
u\equiv64,154,184\pmod{210},
\]

or equivalently

\[
\boxed{n\equiv128,308,368\pmod{420}.}
\]

No old prime hits these indices. All other indices are covered by \(P\cup Q_4\), so the uncovered density is exactly \(3/420=1/140\).

One additional channel completes this dictionary:

\[
q=331,\quad\operatorname{ord}_{331}(2)=30,\quad
u\equiv4\pmod{15},\quad a\equiv269\pmod{331}.
\]

Impose all five displayed root congruences, \(a\equiv0\pmod3\), and the old class. Their moduli are pairwise coprime apart from the already consolidated old modulus, so CRT gives the progression

\[
\boxed{
a=8681796600341899699165924755002845830837950628236344137765453
+121041494945903853943122890515382691774327737794816871699188590\,t,
\quad t\ge0.
}
\]

Every root in this progression has \(3\mid a\), the four-channel sharp residual pattern, and a five-channel completion. Theorem A supplies the lower bound, hence

\[
\boxed{\delta_P(a)=5}
\]

throughout the progression. The displayed first root has 61 decimal digits. Its square, all root residues, orders and periodic coverage checks are included in the certificate.

All five new channels have even zero phase modulo an even base-2 order. They therefore preserve every old private odd witness. The explicit five-channel private even coordinates can be chosen as

\[
u_5=1,\quad u_{13}=6,\quad u_{11}=10,\quad u_{61}=16,\quad u_{331}=64.
\]

This compact numerical root has exact additional cost 5 and total cost at most 25. No exact total-cost assertion is attached to it without the separate coprimalization construction. Also, primes 11 and 331 have base-2 orders dividing 210, so this alternative seed does not preserve the earlier condition \(T_{3,1}\mid a\); the companion refinement construction retains that stronger condition.

## 7. Reproducible evidence and dependencies

Run `python verify_small_gap.py` beside this file. The program writes `small_gap_certificate.json` and checks:

- every entry of the incidence and density tables with rational arithmetic;
- the complete small factorizations supporting the all-order exclusions;
- all case bounds and their universal minimum 1/24 of old holes;
- exact orders, primality and CRT compatibility of the sharp dictionary;
- the three missing index classes across the full old period 6720;
- a complete proper cover of that period after adding 331;
- the 61-digit root, its progression and all five private even witnesses.

The same run imports the four native BRC modules pinned at source commit `b1efc6c805661ed7b476e6e730107da6043176ee`, after matching their existing Git blob identities. It generates all 6720 successive integer states using the actual positive packet, verifies the exact formula for every state, and performs 168000 actual `euclidean_digits` readouts across the 25 old and new channels. Each native readout agrees with an independent modular calculation. It also verifies the composed even packet \(x\mapsto4x+3\), all five new private witnesses, and an odd private witness for each old channel. These source identities and actual counts are recorded in `native_verification` in the certificate.

The verifier locates the pinned modules under an ancestor's `src` or `vendor_src`, or accepts `--source-dir` pointing to their containing directory. The four exact module pins are inherited from the earlier scientific source; no canonical foundation or implementation is changed.

The universal conclusion is the argument in Sections 2–4, not an extrapolation from the finite periodic example. The exact H predicate and the old odd cover are inherited from the published source `research_notes/portable_direct/riesel_mixed_20261119/certificate.json` at commit `e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe`, as restated and checked in the sixth continuation's `cost/proof.md` at commit `2feef401388e6e81a35dd8b0e66383f43561ad12`.
