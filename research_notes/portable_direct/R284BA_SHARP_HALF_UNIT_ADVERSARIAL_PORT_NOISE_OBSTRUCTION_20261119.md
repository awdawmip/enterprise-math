# R284BA — Sharp half-unit adversarial-noise boundary for two named Ports

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AX → R284AY → R284AZ. Frozen inherited observer scope: strictly positive integer matrices C in {1,...,H}^{n×n}, programmable diagonal and simultaneous row-zero star edits, scalar determinant outputs. This is an auxiliary named-Port observation, not a native X6 dynamic.

## Theorem BA1 (a sharp, all-read impossibility at n=2)

For n=2 and any H≥2, consider any deterministic adaptive protocol of any finite number q of queries, with each query choosing arbitrary real diagonal controls d_0,d_1 and an arbitrary real star strength z at E_{01}, then observing

    y_C(d_0,d_1,z)=det(diag(d_0,d_1)−C−z E_{01})+epsilon,
    |epsilon|≤delta.

When delta≥1/2, there are two distinct strictly positive integer matrices in the allowed alphabet which **no such protocol can distinguish with certainty**, regardless of adaptive choices, magnitude of the controls, number of scalar observations or computation time.

Proof: take

    C0 = [[1,1],[1,1]],  C1 = [[1,2],[1,1]].

For every real d_0,d_1,z,

    det(diag(d)−C0−z E_{01})
       = (d_0−1)(d_1−1)−(1+z),
    det(diag(d)−C1−z E_{01})
       = (d_0−1)(d_1−1)−(2+z).

Their exact responses differ by exactly 1 for *all* settings. Under delta≥1/2 an adversary may report the midpoint of the two exact responses after every query. Both matrices are consistent with the same reported history. By induction, an adaptive protocol seeing this history chooses the same next settings in both possible worlds. Its final guess cannot be guaranteed correct for both matrices. This also excludes zero-error randomized identification under worst-case admissible noise: fix any random seed and use the same midpoint transcript. QED.

## The sharp boundary when delta<1/2

R284AZ proves the existence of a fixed integer single-read instrument whose exact outputs are pairwise distinct across the entire finite alphabet {1,...,H}^{2×2}. Since all such outputs are integers, every possible observation perturbed by |epsilon|<1/2 rounds uniquely to its exact integer. Consequently, for n=2 and any H≥2, a finite worst-case-noise-correcting instrument exists precisely when delta<1/2. At delta=1/2 (closed noise balls) the two explicit worlds above are indistinguishable, even under unlimited query repetitions.

The boundary applies to *this named two-Port star-only determinant interface*. A different permitted edit location, additional independent sensors, stochastic rather than adversarial noise or a changed observation operator defines a different question. In particular, this theorem does not assert the same impossibility at all n≥3.

## Exact finite verification

The general obstruction is the symbolic two-by-two determinant identity. An independent complete integer-grid check evaluated all 9³=729 triples (d_0,d_1,z) with each coordinate in {−4,...,4}; every triple satisfied y_C0−y_C1=1 exactly.

Reproduction using Python 3 standard library:

\`\`\`python
from itertools import product
C0=(1,1,1,1)
C1=(1,2,1,1)
count=0
for d0,d1,z in product(range(-4,5),repeat=3):
    def y(C):
        return (d0-C[0])*(d1-C[3])-(C[1]+z)*C[2]
    assert y(C0)-y(C1)==1
    count+=1
assert count==729
print("PASS",count)
\`\`\`

Finite grid checking is a reproducibility check; the impossibility over all real settings and adaptive finite sequences is justified by the preceding identity and midpoint-adversary proof. Independent review: NOT_REVIEWED.

## Residual interpretation and next direction

A change in one directed coupling can remain a constant, one-quantum readout residual under all star controls while remaining algebraically identifiable with exact integer readout. Measurement precision thus matters separately from formal observer injectivity and actuator range. Named directionality and signed residuals are preserved; no global BRC quotient or P000 modification follows.

Next: investigate the n≥3 minimax adversarial-noise threshold under finite star queries, and examine whether additional observation operators can eliminate the n=2 constant-gap obstruction without increasing the number of independent Port controls.
