# Riesel residual composition: exact spectrum in a fixed 43-channel fiber

Research continuation, 24 November 2026 (Asia/Hong_Kong).

Researcher-ID: `EM-DIRECT-970E1C / TASK_RESEARCH`  
Research-Activity-ID: `RA-D2EC212845B63844081F9A14`

## Results

This batch resumes the already-published [complete seven-cover classification](https://github.com/awdawmip/enterprise-math/blob/cadc7197ec1f1169aba937894a5988e05ed5ed24/research_notes/portable_direct/riesel_seven_cover_20261124/README.md) and closes its remaining cost-eight question. The old nineteen-file scientific batch was read back and matched to its actual Git objects. It is reused, not republished.

The native object remains the full typed integer register at a fixed Heartbeat X6 anchor,

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad F_n(a)=a^2 2^n-1.
\]

The deterministic positive BRC has weight and multiplicity one. All modular coordinates are observations; full integers and joint cofactor relations are retained. The square coefficients in the fixed root families are already Riesel by the old odd-index cover and the even-index factorization.

Let P be the established twenty-prime dictionary. Write delta_P(a) for the minimum number of supplementary primes in a complete proper-prime cover, and tau(a^2) for the minimum unrestricted total number. Infinity denotes absence of a finite cover.

### 1. Exact finite spectrum in the unchanged R3 fiber

The preceding source defines R2, the twelve-prime modulus T, and one residue r_T. Retain exactly R3 = {a in R2 : a = r_T modulo T}. The 31 fixed R2 observations plus these twelve give 43 fixed full residue-value trajectories.

The new [fiber theorem](fiber/proof.md) proves

\[
\boxed{\forall s\ge8\quad\exists^\infty a\in R_3:
\delta_P(a)=s,\quad\tau(a^2)=20+s.}
\]

No root in R3 has supplementary cost at most seven. Therefore its set of finite supplementary costs is exactly {8,9,10,...}. The costs at least nine are inherited from the preceding construction; the missing cost eight is proved here.

After the four-prime prefix {5,13,19,73}, write n=32+36w. The fixed channels 38737 and 246241 cover w=1 modulo 2 and w=1 modulo 3. The two uncovered classes w=0,2 modulo 6 are covered by

\[
33975937,\quad138991501037953,
\qquad
2^{72}-2^{36}+1=33975937\cdot138991501037953.
\]

Both primes have exact base-two order 216. CRT preserves every fixed observation. The explicit compact 162-digit root has delta_P=8 and tau<=28. The complete finite-spectrum theorem additionally constructs an infinite coprimalized progression with delta_P=8 and tau=28. The latter proof explicitly handles the fixed but unselected active observer 487824887233, rather than assuming all unselected observed primes are inactive.

The [calculator](fiber/verify_cost_eight.py) checks both prime orders, deterministic primality, all eight signed/swapped CRT progressions, a full 60,480-step scalar residue cycle, 28 private witnesses and a 478,618-bit coprimalized root. Its 378 pairwise greatest common divisors are all one. The full hexadecimal root, forcing factor and CRT modulus are retained in the [certificate](fiber/cost_eight_certificate.json).

### 2. Stronger arbitrary-observer theorem

The [permanent ternary construction](refinement/proof.md) retains both side classes w=1,2 modulo 3. At supplementary size k+7 its remaining classes are

\[
w\equiv2^{j-1}\pmod{2^j}\ (1\le j\le k),\qquad
w\equiv1,2\pmod3,\qquad w\equiv0\pmod{3\cdot2^k}.
\]

All integers w are covered, and every row has a private position. Consecutive dictionaries retire a prime of order 108*2^k and introduce primes of orders 72*2^k and 216*2^k. Common prime coordinates retain the same literal root residue. This raises the minimum changing order from the preceding 54*2^k to 72*2^k.

For any finite modulus N set

\[
B_N=\max(\{1\}\cup\{\operatorname{ord}_q2:q\mid N,\ q\text{ odd prime}\}),
\]

\[
j_N^{(1)}=\min\{j\ge0:72\cdot2^j>B_N\},\qquad
j_N^{(2)}=\min\{j\ge1:72\cdot2^j>B_N\}.
\]

For each i=1,2 there is one residue r_N^(i) such that every s>=j_N^(i)+7 occurs on infinitely many roots in Ri with that same residue modulo N, with exact delta_P=s and tau=20+s. Prime powers in N are included. These residues need not equal the historical R3 residue.

Thus

\[
\boxed{\frac9{16}2^b\le\Omega_b(R_1)\le105\,2^b\quad(b\ge7)},
\]

and the same bounds hold on R2 for b>=8. The metric is maximum base-two order among observed primes. It does not count channels, bits or running time. Complete future residue trajectories obey the same bounds. For the individual budget seven, retain the sharper classification result Omega_7(R2)=180 and hence Omega_7(R1)>=180.

The [exact checker](refinement/verify_permanent_ternary.py) and [certificate](refinement/permanent_ternary_certificate.json) verify k=0,...,12, all private cells, changed-order identities, named prime realizations, two complete 60,480-position scalar periods and three prime-power fixtures. The universal quantifiers follow from the proof.

### 3. Basic primes remain compulsory at budget eight

The [basic-pair theorem](basic_pair/proof.md) proves that every complete supplement of at most eight primes throughout R1 includes both 5 and 13. Any supplement of at most eight primes that omits either leaves full-exponent uncovered density at least 1/2520.

The all-prime capacity argument uses the exact exclusion of parity period eight and a forced intersection. A potentially complete seven-channel contribution on the missed parity has capacity sum 217/216, but its exceptional channels force overlap at least 1/36. Together with the nonexceptional cases this yields the strict bound. The [checker](basic_pair/verify_eight_basic_pair.py) and [certificate](basic_pair/eight_basic_pair_certificate.json) retain all twelve exact overlap cases. This is a necessary condition for budget eight, not its complete classification.

### 4. Actual new native execution

The [native note](native/proof.md), [script](native/verify_native_cost8.py) and [certificate](native/native_cost8_certificate.json) record the compact cost-eight root on one complete covering-predicate period of length 7,560:

| Operation | Actual count |
|---|---:|
| Native one-step BRC updates | 7,560 |
| Native composed two-step evaluations | 3,780 |
| Individual native prime cofactor/remainder readouts | 340,200 |
| Joint 45-radix native readouts and recompositions, each | 7,560 |
| Direct comparisons of the 43 fixed coordinates | 325,080 |

The selected route leaves 1296,648,234,156,78,39,26,13,0 uncovered positions at budgets zero through eight. The final full integer has 8,631 bits and is retained, as are all individual and joint cofactors. The separately calculated full residue-value period is 60,480; this native run executed 7,560 positions, while the fiber calculator executed the full scalar residue period.

## Reused seven-cover classification

The full R2 seven-cover result comprises 2 binary, 24 ternary and 120 modulo-five phase dictionaries: 146 total, with 1,160 possibly overlapping signed CRT descriptions. Its minimum root is

```text
168515727251568031139784117408423468924151126118048106286760549300706338389494633573
```

The seven-budget predicate is determined by a modulo N, or by its full future residue trajectory modulo N, exactly when T divides N, where

\[
T=\prod\{181,577,631,23311,54001,87211,246241,262657,279073,
18837001,29247661,487824887233\}.
\]

All twelve coordinates are essential. This yields Omega_7(R2)=180. Exact natural frequency within R2 is

\[
\frac{916603393453788765429110921373053984059735989421687074488}
{35095524795781473254136196580356738045833417602831290421525609131}.
\]

Collaborative checking of these saved arguments is recorded in [classification audit](reviews/classification.md), [observer audit](reviews/observer.md), and [preceding refinement audit](reviews/refinement.md). The observation count was independently recomputed within this shared research context; its [arithmetic output](reviews/observer_audit_certificate.json) is retained. This is not an independent project Review.

## Reproduction

From this directory:

```sh
python fiber/verify_cost_eight.py --coprimalized-example
python basic_pair/verify_eight_basic_pair.py
python refinement/verify_permanent_ternary.py
python native/verify_native_cost8.py --source-dir /path/to/pinned_source
```

The first three calculators use Python's standard library. The native script uses four exact modules at Enterprise Math commit b1efc6c805661ed7b476e6e730107da6043176ee; its proof lists the frozen Git blobs. No current control revision silently replaces this scientific implementation.

## Source and evidence status

Normative reads were verified at 2026-11-24T07:32:48Z (15:32:48 Asia/Hong_Kong): GK main 874e3ce7d661407b072f7d8fe04c50d54d0e1963 and EM main a88e3e001275269cae93c40d77e6984b1ef2970f. Applicable P000, Heartbeat World, joint-relation preservation, residual fidelity, mathematical evidence, code, continuation and Activity contracts were loaded or reused with source identity checks.

The seven-cover scientific publication is cadc7197ec1f1169aba937894a5988e05ed5ed24. The mathematical inputs it cites retain their own immutable versions. All current results are author proofs with collaborative checks and the explicitly reported computations; project-independent Review and formal acceptance are not claimed.

## External mathematical inputs

The arbitrary-order construction uses Bang's primitive-prime theorem: every base-two order greater than six is realized by an odd prime. A primary author-hosted statement appears as Lemma 12 in the [Filaseta–Finch–Kozek draft](https://www.whittier.edu/sites/default/files/media/academics/math/Kozek_Sierpinski_JNTdraft%282008%29.pdf); numbering varies with version.

The inherited finite-budget upper bound uses the Crittenden–Vanden Eynden interval theorem. [Balister et al., Covering intervals with arithmetic progressions](https://par.nsf.gov/servlets/purl/10165575), Theorem 1 and Corollary 2, give a short proof and the irredundant-cover modulus bound. These external inputs are credited separately from the new fiber constructions.

## Remaining scientific questions

The original fixed root a_star still has the recorded lower bound of 1,791 supplementary primes; whether it admits any finite prime dictionary remains open here. The complete eight-prime classification and the global minimum cost-eight root in R3 remain open. The uniform exponential observer constants are not optimized. These questions are distinct from the completed seven-prime classification and the now-complete finite spectrum of R3.
