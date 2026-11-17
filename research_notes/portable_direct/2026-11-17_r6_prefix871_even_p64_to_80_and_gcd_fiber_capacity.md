# PREFIX-871 — Exact even-source port widths 64–80 and modular-residue fiber capacity

Date: 2026-11-17. Predecessors: PREFIX-870, PREFIX-861. Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged).
Status: AUTHOR_PROVED / EXACT_BIGINT_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Scope: auxiliary named binary BRC two-port integer observer, not a native X6 Cell/Link/Port implementation.

## Model

Let \(N=2^p\). The state \(u\in\{0,\dots,N-1\}\) encodes \(p\) named binary sources. Each ordered transition is either \(v=u\) or \(v=u\mathbin{\mathrm{xor}}2^i\) for exactly one \(0\le i<p\). There are \(N(p+1)\) distinct legal ordered transitions. The two fixed odd moduli \(q_1,q_2\ge3\) give the observation \((u\bmod q_1,v\bmod q_2)\). Denote by \(B_{\mathrm{fix,odd}}(p)\) the minimum possible maximum bit length of the two moduli for injective recovery of the complete ordered transition.

## Theorem A — Residue-class capacity obstruction

Write \(g=\gcd(q_1,q_2)\). For each \(a\in\mathbb Z/g\mathbb Z\), define the number of signed named increments with that residue:
\[
n_a=\#\{(i,s):0\le i<p,\ s\in\{-1,+1\},\ s2^i\equiv a\pmod g\}.
\]
Every lossless observer satisfies, for every \(a\),
\[
\boxed{\frac{q_1q_2}{g}\ge N\left(\mathbf1_{a=0}+\frac{n_a}{2}\right).}\tag{A1}
\]

**Proof.** The output \((r_1,r_2)\) determines the increment class \(\delta=v-u\equiv r_2-r_1\pmod g\). There are exactly \(q_1q_2/g\) ordered output pairs with any specified difference class. The unchanged transition contributes \(N\) input pairs to class zero. Each signed increment \(+2^i\) or \(-2^i\) is legal at exactly \(N/2\) old states, as determined by the source bit. Thus exactly \(N(\mathbf1_{a=0}+n_a/2)\) legal transitions demand output pairs in class \(a\). Injectivity yields (A1). At \(g=1\), the no-op and all \(2p\) signed increments are in the same class, and the formula gives \(N(p+1)\), as required.

For a peak bound \(B\), set \(Q=2^B-1\). Injectivity of the unchanged transitions forces \(\operatorname{lcm}(q_1,q_2)\ge N\), hence \(g\le\lfloor Q^2/N\rfloor\). Write \(q_1=ga,q_2=gb\). Their odd cofactors \(a,b\) are coprime and, in the relevant \(N>g\) regime, distinct. If \(A_g\) is the largest odd integer not exceeding \(Q/g\), then
\[
q_1q_2\le g^2A_g(A_g-2).
\]
Consequently the following exact finite test is necessary:
\[
\boxed{g^2A_g(A_g-2)\ge
gN\max_{a\in\mathbb Z/g\mathbb Z}
\left(\mathbf1_{a=0}+\frac{n_a}{2}\right).}\tag{A2}
\]
Both sides can be evaluated using exact integer modular recurrence.

### New necessary-condition reductions for even p=32–62

At \(p=32,B=19\), \(Q=524287\) and \(g\le63\). Of the 32 odd gcd candidates, (A2) excludes precisely
\(\{17,31,33,41,43,45,51,57,63\}\), leaving precisely
\(\{1,3,5,7,9,11,13,15,19,21,23,25,27,29,35,37,39,47,49,53,55,59,61\}\).
These surviving gcd values are possible *under this necessary test*; existence of a 19-bit observer remains open.

For all even \(p\) from 32 through 62 the finite-alphabet lower-bound value is \(B=p/2+3\); the gcd cap remains 63. The numbers of gcds surviving (A2) are

\`32:23, 34:22, 36:22, 38:18, 40:18, 42:17, 44:14, 46:14, 48:13, 50:13, 52:11, 54:10, 56:4, 58:3, 60:2, 62:1\`.

**Corollary.** Any 34-bit lossless fixed odd two-port observer at \(p=62\) must use **coprime** moduli. This follows because (A2) rejects every odd \(g=3,5,\ldots,63\); \(g=1\) is the sole surviving common divisor.

## Theorem B — Nine exact global optima at even p=64–80

For each even \(p\in\{64,66,68,70,72,74,76,78,80\}\), the minimum peak bit length among **all** fixed odd two-modulus observers is exactly the value in the second column.

| p | Exact peak B | g | h(g) | q1 | q2 |
|---:|---:|---:|---:|---:|---:|
| 64 | 36 | 131 | 65 | 68719476305 | 68719476567 |
| 66 | 37 | 139 | 69 | 137438953133 | 137438953411 |
| 68 | 38 | 139 | 69 | 274877906405 | 274877906683 |
| 70 | 39 | 149 | 74 | 549755813319 | 549755813617 |
| 72 | 40 | 149 | 74 | 1099511627383 | 1099511627681 |
| 74 | 41 | 149 | 74 | 2199023255213 | 2199023255511 |
| 76 | 42 | 163 | 81 | 4398046510579 | 4398046510905 |
| 78 | 43 | 163 | 81 | 8796093021647 | 8796093021973 |
| 80 | 44 | 163 | 81 | 17592186043783 | 17592186044109 |

Here \(h(g)=\min\{d\ge1:2^d\equiv1\text{ or }-1\pmod g\}\).

**Lower bound.** Each of the \(N(p+1)\) legal ordered transitions must produce a distinct output pair. If both moduli have at most \(B\) bits, there are at most \((2^B-1)^2\) observation pairs. The BigInt checker establishes, for every listed \(p\),
\[
(2^{B-1}-1)^2<N(p+1)\le(2^B-1)^2.
\]
Therefore a \((B-1)\)-bit observer is impossible regardless of its fixed odd moduli or decoding algorithm.

**Construction and upper bound.** Let \(g\) be as in the table and \(Q=2^B-1\). Choose \(A\) to be the largest odd integer \(\le Q/g\) and let
\(q_1=g(A-2),\ q_2=gA\).
Their odd cofactors differ by 2 and are coprime. Every table row satisfies \(h(g)\ge p\). Therefore the \(2p+1\) signed increments
\(\Delta=\{0\}\cup\{\pm2^i:0\le i<p\}\)
are distinct modulo \(g\): equality between two nonzero signed powers would imply \(2^d\equiv\pm1\pmod g\) for some \(1\le d<p\), contradicting the definition of \(h(g)\). Oddness of \(g\) also rules out zero residue for a nonzero signed power.

From the observation \((r_1,r_2)\) compute \(\delta\equiv r_2-r_1\pmod g\), uniquely determining the signed update. Then solve
\[
v\equiv r_1+\delta\pmod{q_1},\qquad v\equiv r_2\pmod{q_2}.
\]
The generalized Chinese remainder theorem yields \(v\) modulo
\(L=\operatorname{lcm}(q_1,q_2)=q_1q_2/g=gA(A-2)\).
The exact checks verify \(L\ge N\), so exactly one \(v\in[0,N)\) matches. Recover \(u=v-\delta\), including the named source and direction. Every witness uses at most \(B\) bits; the lower and upper bounds coincide.

## Verification and provenance

The source files are [BigInt checker](https://github.com/awdawmip/enterprise-math/blob/c599084e31e1b2aa1c64aa09e7dd1aa3a216d142/research_notes/portable_direct/PREFIX871_R6_EVEN_WIDTH_AND_FIBER_CHECK.js) and [full result certificate](https://github.com/awdawmip/enterprise-math/blob/934202d021a3407284b516c64836a8e6ca2e8356/research_notes/portable_direct/PREFIX871_R6_EVEN_WIDTH_AND_FIBER_RESULTS.json). The checker computes all 9 exact lower bounds, direct modular distinctness of all signed increments, the CRT size conditions and the complete 16-case gcd candidate sweep, with \`ALL_EXACT_ASSERTIONS_PASSED\`. A separate Python exact-integer implementation checked all nine width constructions using minimal odd cofactors and reproduced all gcd-survivor counts; the two constructions choose different valid pairs with the same peak widths.

Theorems are exact for the auxiliary observer and inherit named-source bit semantics. They neither alter P000 nor establish a native X6 event mapping. The current shared X6 Task is not claimed by this publication.

## Research continuation

1. For \(p=32\), settle the 19- versus 20-bit question via a coupled-residue witness or an exhaustive/theoretical no-go over the 23 admissible gcd classes and their individual modulus pairs.
2. For \(p=62\), analyze the forced coprime-modulus case at \(B=34\), or construct a 34-bit observer.
3. Extend exact even-\(p\) windows above 80, ideally proving a parameter-family modulus-supply criterion that avoids single-parameter searches.
