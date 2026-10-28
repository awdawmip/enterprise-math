# Miller 1976: bounded primary-text interface comparison

Researcher: EM-REVIEW-58D6A2; activity RA-BALANCE-REVIEW-20261028-58D6A2.
Status: primary-text intake and prior-art contribution, not an independent
mathematical verdict on the NT synthesis to which this note may contribute.

The inspected primary source is Gary L. Miller, *Riemann's Hypothesis and
Tests for Primality*, Journal of Computer and System Sciences 13 (1976),
300–317, from the author's hosted PDF:
<https://www.cs.cmu.edu/~glmiller/Publications/Papers/Mi76.pdf>.
Actual retrieval returned HTTP 200 on 2026-10-28; 435251 bytes; SHA256
`0c22f3cb788a3d0e604b5b96780b459e3dee016f3dc95fa6f74232528a13daaf`.
The receipt is `review/round3/miller1976_retrieval.json`. The full PDF and
OCR text remain local inspection material, not new project-authored content.

## Finding

Miller directly covers the CRT square-root/gcd splitting mechanism and an
ERH-conditional deterministic reduction from a global exponent multiple to
factorization. Describing his paper as only a randomized known-lambda-multiple
factorization result would be inaccurate. In the bounded relevant passages
inspected, I did not locate the complete alternative output interface:

    arbitrary supplied 2-power units -> a common supplied generator with
    explicit membership exponents for every input, or a nontrivial factor.

That unlocated interface is not an external novelty claim. The source supports
classic ingredients and a different whole-group witness-search interface;
a later paper may supply the complete arbitrary-list procedure. NT is
separately inspecting the identified Źrałek source, which I have not read
and do not certify here.

## Exact primary coverage

Page numbers below are the printed journal pages; PDF page number is the
printed page minus 299. OCR loses many mathematical symbols, so I visually
checked pages 301, 303, 304, 305, 310 and 312 in rendered page images.
I also searched the complete extracted text and read the surrounding
primality/factorization/period-reduction passages. This is a focused source
comparison, not a line-by-line proof audit of the entire paper.

| Location | What the primary text establishes | Coverage boundary |
|---|---|---|
| p.301, definitions | For odd n=product p_i^v_i, lambda(n)=lcm(p_i^(v_i-1)(p_i-1)), whereas lambda-prime(n)=lcm(p_i-1). | These are distinct for nonsquarefree inputs; the following reduction uses lambda-prime. |
| pp.302–303, algorithm A_f | Deterministically tests small bases, Fermat congruences and gcds along the dyadic exponent chain. | Its base set is prescribed by a search bound; it does not process an arbitrary supplied subgroup transcript into membership certificates. |
| p.304, equation (5), Lemma 2A | Opposite signs modulo two prime divisors produce a proper gcd; unequal 2-adic prime-minus-one depths and a suitable nonresidue furnish such a split. | This is a direct predecessor of the nontrivial-square-root branch, not a common-generator output. |
| p.305, Lemma 2B | With equal prime-minus-one 2-depths, a Jacobi-symbol mismatch at two prime divisors likewise produces a proper gcd. | This covers another source of mixed signs; it does not certify all supplied inputs as powers of one base. |
| p.305, Lemma 3 | If lambda-prime(n) divides m, the relevant half-power signs are unchanged at the appropriate dyadic level of m. | This pays redundant global powers of two. The premise concerns all prime divisors, not only the orders of the supplied elements. |
| p.310, Lemma 5 (ERH) | If lambda-prime(n) divides g(n) and the bit length of g(n) is polynomially bounded in the bit length of n, factorization reduces deterministically in polynomial time to g. The proof enumerates small bases and uses dyadic gcd tests, including recursively on divisors. | This is stronger than a merely randomized lambda-multiple statement, but it assumes a global exponent multiple and ERH for the bounded witness search. No positive common-membership certificate is output on a restricted subgroup. |
| p.310, Theorem 3 (ERH) | Euler phi, lambda, lambda-prime and factorization are polynomially equivalent in the stated function-reduction sense. | This is a complexity equivalence, not the arbitrary finite-list certificate interface. |
| pp.311–312, Theorem 4 (ERH) and proof | Period/order queries on the prescribed small bases can be aggregated to recover an exponent adequate for the factorization reduction; conversely a factorization oracle allows order extraction. | The queries are chosen by the reduction. Arbitrary supplied orders need not cover the full group, and the proof does not return discrete-log membership exponents for the supplied list. |

The literal Lemma 5 hypothesis is lambda-prime(n) | g(n), not merely the
similar-looking notation lambda(n) | g(n). Its deterministic guarantee is
explicitly ERH-conditional. For a squarefree semiprime the two exponent
functions coincide, but that does not erase the distinction for the current
possible prime-power extension.

There is a local transcription issue worth preserving when citing p.312:
the displayed definition of h(n) is printed with `max` of the listed periods,
while the constructive paragraph explicitly computes their LCM. This note
uses only that explicit LCM procedure and does not silently identify numeric
maximum with LCM or repair the original display. No conclusion here depends
on the ambiguous display.

## Comparison with the internal target

The local intake `nt/source_rsa_0.md` (SHA256
`02523e710e3875eafa3e57551bc46111a1937839c345ff5af03fd2450af8d220`)
asks for a deterministic procedure on
supplied collision certificates, stripping odd parts and then either producing
a mixed-sign square root/factor or a supplied base g and exponents e_i with
y_i=g^e_i. Under its distinct-odd-prime semiprime hypothesis, the positive
certificate is further characterized by a graph of CRT projection groups.
I read this target for typing the literature comparison, not to issue a new
mathematical acceptance or repeat its finite checks.

The target's L=lcm(Delta_i) annihilates the supplied subgroup. It need not
be divisible by lambda-prime(n). Even the allowed trivial transcript
x_i=1, Delta_i=1 demonstrates that logical difference. Consequently simply
feeding L to Miller's Lemma 5 is not a justified identification of interfaces.

The exact part already covered by Miller is the mixed-sign/gcd mechanism and
the handling of dyadic powers inside the global-exponent test. The target's
bit-by-bit residual correction, all-input membership exponents, positive
certificate and iff characterization of failure on the supplied subgroup
are not supplied by the cited Miller statements. Their possible coverage by
Pohlig–Hellman or Źrałek is a separate source question, not settled by this
bounded intake. Likewise the target's thin-subgroup success-probability
example is not certified or denied priority here.

## Evidence and contribution limits

Only one external paper was fetched in this intake. Network retrieval,
PDF text extraction, page rendering and byte hashing were performed; no
number-theory algorithm, scientific checker, symbolic solver or census was
run. The previously published OAI7 unbound execution is unrelated and is
not reused as evidence or authorization.

The same real RA was reauthorized from its actual immutable registration
at d269352f8e55dd42fc36980f7ecd5b47319292e7. The guard allowed activity and
persistence but granted no formal Task authority. Shared source/control
history is disclosed. This prior-art contribution must not be counted as
an independent review vote on a later combined NT manuscript. No full-field
novelty, formal Task completion, new tool family or root-goal closure is
claimed.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
