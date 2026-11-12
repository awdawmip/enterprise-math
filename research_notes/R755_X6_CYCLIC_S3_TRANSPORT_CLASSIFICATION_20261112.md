# R755 — Exact cyclic S3 frame quotient for the three-support BRC scheduler
Status: AUTHOR-PROVED EXACT FINITE THEOREM; independent Driver and native event admission pending.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R754 PR #2184. P000 and ACTIVE worldview unchanged.

## Precise question

R754 constructed an S6-equivariant positive BRC kernel on an unmarked oriented signed-port triad x=[p,q,r], uniform on exactly the three *forward cyclic* serializations of its PASS edges, and proved that independence of the final S3 frame from all SIX serial orders holds iff the three fixed S3 frame increments commute pairwise. What is the correct, potentially weaker, information-loss criterion for the actual three-support kernel?

**Conditional bridge hypothesis H:** these three occurrences may be represented by three admitted, composable V39 based-loop packets at a compatible base, with fixed, order-independent frame increments a,b,c in S3. Products for the forward cyclic orders are abc, bca, cab. This is an algebraic candidate interface. H is NOT supplied by a V29 count grammar, nor does it assert a native TRIADIC_CLOSURE_E event. Final-frame observation is distinguished from intermediate-time PASS observations.

## Theorem 1 (arbitrary group: exact cyclic quotient certificate)

Let a,b,c lie in any group G and let z=abc. The following are equivalent:

1. abc=bca=cab.
2. z commutes with a and b.
3. a,b,c all belong to the centralizer C_G(z).

Proof. bca=a^{-1}za and cab=(ab)^{-1}z(ab), so the first condition is equivalent to z commuting with a and ab, hence with a and b. Since c=(ab)^{-1}z, it also commutes with c. Conversely these centralizer relations make both cyclic conjugations invariant. □

Consequently scheduler cyclic-rotation provenance can be omitted from the *final S3 frame* exactly on this condition, as long as H holds. The same quotient need not preserve any prefix readout.

## Theorem 2 (complete S3 classification)

For all 6^3=216 ordered triples (a,b,c) in S3:

| Frame observer | Triple count |
|---|---:|
| Equal on three forward cyclic orders | 66 |
| Equal on all six orders (pairwise commuting) | 48 |
| Equal on forward three, unequal on all six | 18 |

More sharply, in S3:

    abc=bca=cab
      iff
    (a,b,c pairwise commute) OR (abc=identity).

Proof. In S3, centralizers of identity, transpositions and 3-cycles have sizes 6, 2 and 3; the two nonidentity types have abelian centralizers. For z=identity, choose a,b freely (36), and c=(ab)^-1. The number of commuting ordered pairs is sum_g |C(g)| = 6+3*2+2*3=18. The remaining 18 identity-product triples are noncommuting. For any transposition z, the centralizer gives 2^2=4 triples per z, or 12 in total; for any 3-cycle z, 3^2=9 per z, or 18 in total. Since these centralizers are abelian, every nonidentity-product cyclic-invariant triple is pairwise commuting. Hence 36+12+18=66, versus 18+12+18=48 fully invariant. Full six-order invariance iff pairwise commutativity follows by comparing adjacent swaps and cancelling the third factor. □

## Theorem 3 (orientation residual is strictly needed)

In every one of the 18 exceptional noncommuting triples with abc=identity, the three forward cyclic products all equal identity, whereas the reverse products (acb,cba,bac) are nonidentity 3-cycles. Their exact multiplicities are (1,2) over the two 3-cycles.

Proof. If one reverse product were identity, combining with abc=identity yields two commuting factors and then all three commute, contradiction. These exceptional triples necessarily have two transpositions and one 3-cycle (an identity factor or two 3-cycles would make the factors commuting). Thus every reversed product is even; being nonidentity, it is a 3-cycle. If all three reverse products coincided, Theorem 1 for the reversed triple would make all factors commute with one nonidentity 3-cycle, hence with each other because its centralizer is abelian; contradiction. There are exactly two 3-cycles, so their nonconstant multiplicities must be 1 and 2. □

Witness (one-line permutations, composition x∘y): a=(0,2,1), b=(1,0,2), c=(1,2,0). Forward abc,bca,cab all equal (0,1,2); reverse acb,cba,bac equal (1,2,0),(2,0,1),(2,0,1).

## X6 BRC consequence and counts

R754's signed X6 C1 candidate has 20 axis triples * 8 sign patterns * 2 oriented cycles = 320 triad classes. For each triad, assign a fixed ordered triple of S3 packet labels. This yields 320*216=69,120 candidate assignments, of which:
- 320*66=21,120 preserve the final frame across the forward three-support kernel;
- 320*48=15,360 preserve the final frame across all six orders;
- 320*18=5,760 provide new **noncommuting but forward-scheduler-invisible** cases.

These are exact algebraic model counts, not claims of 69,120 admitted physical V39 events. A forward/reverse branch flag distinguishes the two scheduler *families*, but can be insufficient to recover the exact reverse frame value because its three cyclic starting positions yield a 1:2 split. Retain full ordered provenance for that future language. In the same model, R754's V29 prefix imbalance remains nonzero for the first two serial PASS steps, so time-prefix observation still distinguishes schedules even when the final frame quotient is safe.

## Evidence and next native test

The associated standard-library Python script enumerates all 216 S3 label triples using integer permutations, checks the group-theoretic equivalences and counts, and verifies every exceptional reverse product and one-line witness. Its JSON result contains exactly 66/48/18 and the 320-fold candidate count. The combinatorial proof establishes completeness independently.

Next: identify an actually admitted V39 based-loop packet and Cell/Link/Port incidence under the task's frozen science, test compatibility of three packet occurrences and whether the frame increments depend on serial order; apply the proven cyclic criterion only after H is verified. If label dependence is found, retain it as a new source-order residual and compute the three actual products. Native Source CLAIM/Result and independent Driver review retain their own current authority requirements.
