# PREFIX-971 — Complete seven-gap named XOR reconstruction by parity-lifted congruences

Date: 2026-11-21 (Asia/Shanghai). Independent auxiliary integer observer, continuing PREFIX-970. Scientific input remains frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: **AUTHOR_PROOF / INDEPENDENT_FULL_Q19_XOR_VERIFIED / NOT_REVIEWED**. This note is not native X6/triadic dynamics and does not acquire a shared Task CLAIM.

## Model

For integer \(p\ge4\), \(H=2^{p-1}\), \(Q_p=\{H+1,H+3,\ldots,2H-1\}\), odd \(k>0\) satisfying \(k+2<H\), and gap \(m\in\{0,\ldots,6\}\), determine all *named* non-diagonal solutions with \(a,b\in Q_p\), \(a\ne b\), \(1\le t\le2k\), and \(i,j,I,J\in\{0,\ldots,p-1\}\):
\[
 (ka\mathbin{\mathrm{xor}}2^j)-2^i=tb,\qquad
 ((k+2)a\mathbin{\mathrm{xor}}2^J)-2^I=(t+m)b.
\]
The output is the sorted list of complete tuples \((a,b,t,t+m,i,j,I,J)\), not only distinct modulus pairs. Let the signed source-fiber residuals be \(c=2^i-s2^j\), \(C=2^I-S2^J\), with signs verified from the original XOR source bits (equivalently the relevant target-end bits). Every possible signed slot \((i,j,s)\) or \((I,J,S)\) remains attached to its numeric residual.

## Theorem 971.1 — Unified odd-modulus parity lift

Set \(d=2t-km\), \(N=kC-(k+2)c\). For every nonresonant branch \(d\ne0\), put \(g=\gcd(k,t)=\gcd(k,d)\) and \(q=|d|/g\). A residual pair can yield legitimate odd \(a,b\) **only if**
\[
 c\equiv 1-t\pmod2,\qquad C\equiv1-t-m\pmod2,\qquad g\mid c
\]
and the single reduced congruence
\[
\boxed{C\equiv \left((k+2)c/g+d/g\right)(k/g)^{-1}\pmod{2q}.}
\]
Conversely, these congruences, together with
\[
 b=\frac{kC-(k+2)c}{d},\qquad
 a=\frac{mb+C-c}{2},\qquad a,b\in[H+1,2H-1],\quad a\ne b,
\]
make both \(a,b\) **odd integers** satisfying the two *linearized* collision equations. Expanding all signed source slots and applying the **actual original XOR bit checks** is therefore necessary and sufficient for named XOR solutions.

**Proof.** Subtract the two linearized equations to get \(2a=mb+C-c\); eliminate \(a\) to obtain \(db=N\). Since \(b\) is an odd integer, \(N\equiv d\pmod{2|d|}\), and the converse also holds. Now \(kC\equiv(k+2)c+d\pmod{2|d|}\). Because \(k\) is odd, \(g=\gcd(k,2|d|)\); and \(\gcd(g,k+2)=1\), so \(g\mid c\). Divide by \(g\), invert the coprime odd integer \(k/g\) modulo \(2|d|/g=2q\), obtaining the displayed congruence. Conversely it makes \(b=N/d\) odd and integral. The two residual parity conditions make \(mb+C-c\) even, hence \(a\) integral. The algebraic identity \(k(mb+C-c)=2tb+2c\) gives \(ka=tb+c\); modulo 2, \(ka\equiv t+c\equiv1\), so \(a\) is odd. The second equation follows by subtraction. The strict modulus interval and the actual XOR source signs complete sufficiency. QED.

The parity-lift modulo \(2q\) is applicable to **even as well as odd** \(m\). It is an exact congruence filter for odd second moduli, not an approximation. For fixed \((2q,\operatorname{parity}(C))\), sorted buckets may be reused; intersecting the two determinant-derived modulus intervals makes the search exact without a full pair scan.

## Theorem 971.2 — Complete resonant branch

Within \(m\in\{0,\ldots,6\}\) and \(1\le t\le 2k\), \(d=0\) is possible precisely for \(m=2,t=k\) and \(m=4,t=2k\). In that case the linearized equations are equivalent to
\[
 c=kr,\quad C=(k+2)r,\quad a=(m/2)b+r\qquad (r\in\mathbb Z).
\]
These equations, modulus range, non-diagonality and the original XOR bit checks enumerate all resonant named witnesses. Enumerate each integer \(r\) for which \(kr\) and \((k+2)r\) occur in the signed source-residual dictionary, then the odd \(b\) for which \(a=(m/2)b+r\) is an odd modulus in \(Q_p\), excluding \(a=b\). In the exactly checked \(p=19,k=21\) instance the residual dictionary permits only \(r=0\). This makes \(m=2\) diagonal, while \(m=4\) yields \(a=2b\notin Q_p\), so both resonant branches contribute zero non-diagonal named witnesses in that instance. No universal empty-resonance assertion for other parameters is needed.

## Complete Q19, k=21, k+2=23 exact enumeration

| m | Distinct ordered non-diagonal pairs | Complete named witnesses | SHA256 of sorted tuple CSV |
|---:|---:|---:|---|
| 0 | 6 | 6 | `2e726efbb2d3232c1c7b441af19f038c40148dc8a24b356ccdc4f9f9aeba8605` |
| 1 | 442 | 614 | `ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71` |
| 2 | 4,724 | 6,509 | `6ceb12fffda02b91e8acd19726fefa4e75dba39f45122c3f87d9ff35aef7395e` |
| 3 | 839 | 1,286 | `1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3` |
| 4 | 190 | 231 | `42eaf49ffebb55ddcc8be1294c665dd2e32a627b842fda74bf705504d77dcfce` |
| 5 | 3 | 3 | `c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b` |
| 6 | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| **All gaps** | **6,203 unique pairs** | **8,649 named witnesses** | The seven per-gap digests are the exact certificate |

The sum of the per-gap distinct-pair counts is 6,204, with exactly one cross-gap repetition: \((a,b)=(278529,290817)\) occurs in both \(m=1\) and \(m=2\). Hence the union contains **6,203** pairs. The \(m=1,3,5\) hashes reproduce PREFIX-966–970, and \(m=0\) reproduces PREFIX-965. A zero \(m=6\) count is **specific to this Q19/k21 instance**; other widths/cores can realize \(m=6\).

## Reproducibility and independent verification

- `PREFIX971_R6_ALL_GAP_PARITY_LIFTED.py --check --benchmark --output ...` implements the generic integer join, source-slot expansion, direct small-domain raw-XOR reference and Q19 certificate. Exhaustive independent raw-XOR comparisons were completed for every eligible odd core at \(p=4,5,6,7\): **56 core configurations × 7 gaps = 392 cases**. All full named tuples agree as multisets.
- `PREFIX971_R6_RAW_XOR_INDEPENDENT.cpp` is a structurally distinct direct source-first enumerator: for each of all **131,072** Q19 odd \(a\), it builds the original right-XOR target dictionary, enumerates all original left-XOR source slots and legal \(t,b\), then directly matches each of seven target gaps. It does **not** use the determinant, residual dictionary, gcd, or congruence buckets. Running the executable with `19 21` produced all seven full CSV files whose SHA-256 digests match the table **byte for byte**; one measured local invocation took about 5.55 seconds. This timing is environment-specific and is not compared as a same-language benchmark.
- The Python run recorded 392 small cases, the seven Q19 counts/hashes above, a shared numerical-index population of 129 buckets / 31,989 entries, a median of ~0.097 seconds across six complete Q19 Python runs, and the sole cross-gap pair. These are implementation observations, not asymptotic theorems.

All arithmetic is integral; no floating approximation is used to establish any witness. The independent raw enumerator was compiled locally with `g++ -O3 -std=c++17`. Reference code is standard-library Python and standard-library C++. Raw source slots and all original XOR equations are validated at output.

## Provenance, limits and next research question

Predecessor: `awdawmip/enterprise-math@e5f13deb671a9bb7050b9044b07e812595117110:research_notes/portable_direct/2026-11-21_r6_prefix970_gcd_reduced_cross_gap_index.md`. Scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` remains unchanged. The auxiliary two-core observer has not been identified with native BRC dynamics or a complete native X6 three-dimensional slice. No task owner, formal Result/Review, P000 or working-truth status is changed.

Next: derive a joint-fiber observer interface preserving the named XOR source slots under a specified BRC composition or future operation. Explore a memory-efficient cache for all seven gaps and parameterized core families. The mother target \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\) remains unresolved.