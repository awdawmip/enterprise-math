# R762EP — q=9 terminal BRC content and an 18-step three-adic shadow (finite exact certificate)

**Date:** 2026-11-18. **Project task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS. **Scientific model:** frozen positive six-named-branch terminal observer. **Status:** AUTHOR_EXACT_FINITE_VERIFIED / GENERAL_ODD_Q_PARITY_PROVED / NOT_REVIEWED.

## Fixed object and observer

Work in the commutative group ring (R_q=\mathbb Z[(\mathbb Z/q\mathbb Z)^3]) with its *named* six-branch update
[
P=1+X+Z+XY+YZ+XYZ.
]
Each word is counted with full positive multiplicity; all branch identities, names, and full three-coordinate terminal coefficients are retained throughout calculation. Let (C_q(n;u,v,w)=[X^uY^vZ^w]P^n), (0\le u,v,w<q), and
[
c_q(n)=\gcd_{u,v,w} C_q(n;u,v,w)>0.
]
This is the positive terminal-coefficient observer embedded as a restricted representation in the native signed X6/Heartbeat-World project. It is **not** a claimed native signed Cell/Link/Port event language or a replacement for `TRIADIC_CLOSURE_E`.

The scientific input retains the original P000 and Task pin from enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 and taskbook@e3f42efac29a2da2d95be391f3231a664e2fade0. Earlier author results R762DZ, R762EK–EL, R762EM, R762EN–EO are acknowledged as separately stored, `NOT_REVIEWED` scientific context. No dependent mathematical assertion is being promoted to native X6 physical truth.

## Theorem A (all odd moduli: full content is a three-power)

For every odd (q>1) and every (n\ge0),
[
\boxed{c_q(n)=3^{v_3(c_q(n))}.}
]

**Proof.** Augmentation (X=Y=Z=1) gives (\sum C_q(n;u,v,w)=6^n), so the positive integer (c_q(n)) divides (6^n). Its only possible prime divisors are 2 and 3. To exclude 2, work in the algebraic closure of (\mathbb F_2). Since (q>1) is odd, choose a nontrivial (q)th root (z) (the order can be exactly (q)). The valid group-ring character with (X=Y=1,,Z=z) evaluates
[
P(1,1,z)=3+3z=1+z\ne0\quad\text{in characteristic two}.
]
Hence (P(1,1,z)^n\ne0), including (n=0). If all coefficients of (P^n) were even, evaluation would instead be zero. Thus (2\nmid c_q(n)), completing the proof. This proof concerns the exact declared terminal group ring for odd (q), independently of spectral factorization.

## Theorem B (all 1,008 horizons through n=1007)

For (q=9), and **each integer** (0\le n\le1007), the exact integer gcd is
[
\boxed{c_9(n)=3^{\max(0,\lfloor n/3\rfloor-2)}.}
]

This is a *finite exhaustive theorem* established by a deterministic modular-integer certificate, not an extrapolation to every (n\ge0). For (n=1007), its precise exponent is (333).

**Proof/certificate.** Define (k(n)=\max(0,\lfloor n/3\rfloor-2)). The companion executable `R762EP_Q9_FINITE_CONTENT_SHADOW_VERIFY.py` uses the original six **named coordinate shifts**, starting from coefficient 1 at ((0,0,0)), to calculate all 729 residues of (P^n\bmod 3^{340}), sequentially for all 1,008 times. It verifies for every (n):

1. Every one of the 729 residues is divisible by (3^{k(n)}).
2. At least one normalized coefficient ((C_9(n;u,v,w)/3^{k(n)})\bmod3) is nonzero.
3. The total coefficient mass equals (6^n\bmod3^{340}).
4. Aggregating the 729 coefficients through the natural (q=9\to q=3) reduction agrees *coordinate by coordinate* with a separately propagated 27-position six-branch recurrence.

The recurrence is exactly (C_{n+1}(g)=\sum_{b\in B}C_n(g-b)), with (B) the six displayed triples, so induction proves the stored residues are exactly the integer coefficients modulo (3^{340}). Since (k(n)\le333<340) on this finite domain, tests (1)–(2) determine the actual integer 3-adic content valuation without truncation ambiguity. Theorem A excludes the only other possible prime divisor. QED.

## Theorem C (18-step normalized shadow, bounded domain)

Write in the coefficientwise finite-field group ring
[
S_n=3^{-k(n)}P^n\pmod3\ \in\mathbb F_3[(\mathbb Z/9)^3],\qquad 9\le n\le1007.
]
This quotient is well-defined by Theorem B. The exact certificate verifies the **981 independent repeated-horizon comparisons**
[
\boxed{S_{n+18}=S_n\quad(9\le n\le989).}
]
Since (k(n+18)=k(n)+6) in this range, the equivalent coefficientwise integer congruence is
[
\boxed{P^{n+18}-3^6P^n\in3^{k(n)+7}R_9\quad(9\le n\le989).}
]
There are 18 nonzero initial shadow vectors (S_9,\ldots,S_{26}); their 729-coordinate vectors have **rank 17 over** (\mathbb F_3), and the script computes the explicit relation
[
\boxed{2S_{11}+S_{14}+S_{20}+S_{26}=0.}
]
The dependence is an exact finite-field relation among these declared terminal-observer vectors. It does not discard a native joint-relation direction. Deterministic modular Gaussian elimination checks the rank, and the per-class SHA-256 hashes, supports and first nonzero terminal witnesses are recorded in `R762EP_Q9_FINITE_CONTENT_SHADOW_EVIDENCE.json`.

A compact support profile for the eighteen residues (n=9,...,26) is
[
(27,162,486,717,108,324,525,522,468,18,108,324,519,360,468,237,450,324).
]
SHA-256 of the concatenation of those 18 length-729 byte arrays is:
`fb37bdb7463e493b32dbd5d43157621dfaab2b8f92381a062c25da7b9f4798a4`.
This represents the exact ordinary integer sequence of 0/1/2 residues, sorted by (u,v,w) lexicographically, not an algebraic or platform authorization signature.

## Verification scope and independent obligations

- **Algorithm:** six explicit named BRC branch shifts in cyclic (q=9) group ring; coefficient arithmetic modulo (3^{340}); group-ring reduction consistency with (q=3); all integer operations. No π, trigonometry, floating point, Taylor expansion, or physical residual attribution.
- **Exhaustive domain:** (n=0,...,1007), 729 coefficient cells at every horizon; exact finite-field shadow comparisons (n=9,...,989).
- **Proof status:** Theorem A is a symbolic all-odd-(q) proof; Theorems B–C are exact *finite computational* theorems with executable, fully specified exhaustive loops and machine-checkable residue hashes. Mathematical independent reviewer: `NOT_REVIEWED`; Lean/formal checker: `NOT_PERFORMED`.
- **Actor/authority:** a project-portable GitHub research artifact; previous Researcher ID `EM-X6-3050F6` is historical task provenance. This file grants no new session, CLAIM, Source PROGRESS, Result or Review. The active native owner remains determined only by authenticated current control.
- **Provenance preservation:** all 6 branch words are retained as separate shifts. The 729 positions are terminal-count readouts, not Cell identity or a future-operation safe native quotient. The q=3 aggregation is an additional checked observer, never substituted for the q=9 computation.

## New precise next problem

Prove, or locate the first exact counterexample to,
[
v_3(c_9(n))=\max(0,\lfloor n/3\rfloor-2)\quad\text{for every }n\ge0.
]
A useful sharper proposed route is to establish a stable (\mathbb Z_3)-lattice on which the renormalized 18-step multiplication by (P^{18}/3^6) is integral and acts as identity on the relevant mod-3 residual orbit. The 981 verified comparisons supply discriminating targets, *not* that lattice theorem. For a disproof of global 18-periodicity, only (n\ge990) needs to be tested after the present finite interval.

Separately resolve the actual source-licensed signed `TRIADIC_CLOSURE_E` Cell/Link/Port updates and V17/V29/V39 transport before interpreting any terminal spectral relation as a native future-permission statement.

**Archive links:** predecessor R762EN–EO GitHub Draft PR #2727@39563fc6fff07e8483a8e4bab9bed8cdf2837d82; source scientific task record `RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142`.
