# High-Dimensional Prime Wall — Classical Source Map

Status: `INDEPENDENT_POST_CHECKPOINT_SOURCE_AUDIT_COMPLETE`

Researcher-ID: `EM-HDPWA-03E870`

Task-ID: `RS-HIGHDIM-PRIME-WALL-FILTER-ALGEBRA-EQUIVALENCE-AUDIT`

The pre-source proof checkpoint was frozen before any item below was opened.  This map
distinguishes original theorem sources, later proofs/expositions, authoritative data, and the
project-specific deductions made in this task.

## 1. Primary theorem sources

### P1. Jacobi — four- and eight-square theta identities

- C. G. J. Jacobi, *Fundamenta nova theoriae functionum ellipticarum* (1829), especially
  §§40–42. [Public-domain scan](https://archive.org/details/fundamentanovat00unkngoog).
- The four-square divisor formula appears in Jacobi's theta-function development; the
  eight-square identity appears there implicitly in the elliptic-function expansions.
- H-items supported: H5 and H6 after the task-specific wall-to-signed-shell reduction.

### P2. Eisenstein — explicit eight-square formula

- G. Eisenstein, “Lehrsätze,” *Journal für die reine und angewandte Mathematik* 39
  (1850), 180–182. [DOI record](https://doi.org/10.1515/crll.1850.39.180).
- Later source-critical accounts identify this as the first explicit form of
  `r_8(n)=16 sum_{d|n}(-1)^(n+d)d^3`.
- H-item supported: H6.

### P3. Glaisher — formulas through eighteen squares

- J. W. L. Glaisher, “On the Numbers of Representations of a Number as a Sum of `2r`
  Squares, Where `2r` Does not Exceed Eighteen,” *Proceedings of the London Mathematical
  Society* s2-5 (1907), 479–490.
  [DOI record](https://doi.org/10.1112/plms/s2-5.1.479).
- This is the historical source cited by the modern Sato–Tate paper for the prime
  twelve-square decomposition.
- H-item supported: H8's exact `r_12` decomposition.

### P4. Barnet-Lamb–Geraghty–Harris–Taylor — non-CM newform Sato–Tate

- T. Barnet-Lamb, D. Geraghty, M. Harris, R. Taylor, “A Family of Calabi–Yau Varieties
  and Potential Automorphy II,” *Publ. RIMS* 47 (2011), 29–98.
  [Publisher page and DOI](https://ems.press/journals/prims/articles/4468),
  [open article PDF](https://ems.press/content/serial-article-files/41128).
- Theorem B(3), pp. 31–32: for a non-CM holomorphic elliptic modular newform of weight
  `k>=2`, `a_p/(2p^((k-1)/2)zeta)` is equidistributed on `[-1,1]` with density
  `(2/pi)sqrt(1-t^2) dt` in the stated nebentypus class.
- Corollary 8.6, pp. 94–95, applies this theorem exactly to twelve squares:
  for primes `p`,
  `(N_12(p)-8(p^5+1))/(32p^(5/2))` has that distribution.  Its proof records
  `N_12(p)=8(p^5+1)+16a_p`, where `a_p` is the coefficient of the weight-6 level-4
  cuspidal newform `q product_(n>=1)(1-q^(2n))^12=eta(2z)^12`.
- H-item supported: H8 in its exact normalization.  This source directly prevents the
  twelve-square residual from being presented as a new Sato–Tate example.

### P5. Martin — multiplicative eta-quotient eigenforms

- Y. Martin, “Multiplicative eta-quotients,” *Transactions of the AMS* 348 (1996),
  4825–4856. [DOI record](https://doi.org/10.1090/S0002-9947-96-01743-6).
- The paper classifies integral-weight eta products whose forms and Fricke transforms are
  simultaneous Hecke eigenforms.  It supplies primary general infrastructure for treating
  `eta(2z)^12` as an eigenform, while P4 supplies the exact application needed here.
- H-item supported: H8 object classification.

## 2. Later proofs and authoritative expositions

### E1. Four-square triple-product proof

- M. D. Hirschhorn, “A simple proof of Jacobi's four-square theorem,” *Proceedings of
  the AMS* 101 (1987), 436–438.
  [AMS/DOI page](https://doi.org/10.1090/S0002-9939-1987-0908644-9).
- It derives Jacobi's formula directly from the triple-product identity.  This corroborates
  the independent checkpoint's shortest symbolic route for H5.

### E2. Eight-square arithmetic proof and source history

- K. S. Williams, “An arithmetic proof of Jacobi's eight squares theorem,” *Far East
  Journal of Mathematical Sciences* 3 (2001), 1001–1005.
  [Author publication index](https://people.math.carleton.ca/~williams/papers/2001papers.html).
- The introduction states the exact signed divisor-cube formula and distinguishes Jacobi's
  implicit appearance from Eisenstein's explicit statement.  It is a later proof, not the
  priority source.

### E3. Twelve-square exact formulas and historical audit

- J. G. Huard and K. S. Williams, “Sums of twelve squares,” *Acta Arithmetica* 109
  (2003), 195–204. [Open author PDF](https://people.math.carleton.ca/~williams/papers/pdf/254.pdf),
  [DOI](https://doi.org/10.4064/aa109-2-7).
- The introduction records Liouville, Petr, Humbert, Glaisher, and Ewell formulas; equations
  (1.2)–(1.5) separate even and odd cases.  It is a later proof/exposition and does not replace
  Glaisher as the historical source.

### E4. Authoritative newform data

- LMFDB newform orbit [4.6.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/4/6/a/a/).
- The database records level `4`, weight `6`, dimension `1`, trivial character, `CM=no`,
  Sato–Tate group `SU(2)`, the q-expansion beginning
  `q-12q^3+54q^5-88q^7-...`, and the eta quotient `eta(2z)^12`.
- This is authoritative computational metadata, not the primary proof of Sato–Tate; P4 is
  the theorem source.

## 3. Standard transforms, not novelty-bearing theorems

| H-item | Standard content | Audit classification |
|---|---|---|
| H1 | partition by support set plus binomial counting | elementary standard combinatorics |
| H2 | affine scaling `F-1 -> lambda(F-1)` | semigroup only before support collapse |
| H3 | Cauchy product of generating series | requires the degree-zero identity coefficient |
| H4 | indicator expectation plus coordinate exchangeability | elementary finite probability/counting |
| H7 | proportionality of two three-entry coefficient vectors | elementary polynomial algebra after the wall basis is chosen |

These rows need no priority claim.  Their useful Enterprise content is notation and the joint
support-basis presentation, not a new theorem family.

## 4. Project-specific inferences in this audit

The following statements are not imported from the classical sources; they are exact deductions
from the packet's wall coefficients and the classical formulas:

1. `Q4(n)=r_4(n)/8+delta_square(n)` for every `n>=1`.
2. `Q8(n)=r_8(n)/16+delta_square(n)` for every `n>=1`.
3. Hence, for odd `n`, `Q4=sigma_1+delta_square` and
   `Q8=sigma_3+delta_square`.
4. The H5/H6 prime biconditionals follow because a composite has an additional proper
   divisor term; they do not express a new primality-complexity result.
5. H7 is unique at `lambda=2` only when proportionality quantifies over the formal structural
   grades `{2,3,4}`.  It is false when quantified only over nonzero grades of one fixed prime.
6. For primes, subtracting the twelve-square Eisenstein term leaves exactly `a_p` of
   `eta(2z)^12`; after subtracting that already-classical newform coefficient, the project
   residual is identically zero.

## 5. Source-to-claim boundary

- P1/P2/P3 supply classical representation formulas; they do not supply the packet's wall
  coefficient combinations.
- P4 supplies both the precise twelve-square normalization and the distribution theorem; no
  source-independent novelty remains in H8.
- E1–E4 verify modern notation and metadata but do not upgrade numerical checks into proofs.
- The withheld free-research branch and its proof were not read.  Post-source reconciliation
  is reserved for the Driver and cannot alter the independent classifications above.
