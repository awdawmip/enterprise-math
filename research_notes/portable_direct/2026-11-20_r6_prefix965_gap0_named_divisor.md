# PREFIX-965 — Exact named XOR gap-zero reconstruction by source slots and divisor fibers

Date: 2026-11-20. Status: AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED.
Researcher attribution: portable R6 continuation after PREFIX-964E; historical provenance EM-DIRECT-58C410 retained but not asserted to authenticate the present session.
Scientific input freeze: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Scope: auxiliary named-XOR integer observer, **not** native P000 X6, BRC event admission, formal CLAIM, Result or independent Review.

## Question and definitions

For p>=4, H=2^(p-1), Q_p={H+1,H+3,...,2H-1}; fix an odd core k>=1 with k+2<H. Consider the actual named equations

    ((k*a) XOR 2^j) - 2^i = t*b
    (((k+2)*a) XOR 2^J) - 2^I = T*b

with a,b in Q_p, i,j,I,J in [0,p-1] and positive integer quotients t,T. Put m=T-t. The source signs are fixed by the actual bits, not chosen independently. Their numerical residuals are

    c = 2^i - s*2^j,  s=1-2*bit_j(k*a),
    C = 2^I - S*2^J,  S=1-2*bit_J((k+2)*a).

The exact identity C-c=2a-mb follows by subtraction. The previous PREFIX-964E established that m=0 implies a=H+2^r-1, 1<=r<=p-2. Here we fully classify source slots and reconstruct actual named witnesses for m=0.

## Theorem 965.1 — Exact source-slot classification at gap zero

Every actual gap-zero named joint witness has a=H+2^r-1, 1<=r<=p-2, and exactly one of the following source-slot patterns. Conversely, each listed pattern yields a genuine named witness for each b in Q_p satisfying the listed bit predicates and b | (k*a-c), with t=(k*a-c)/b>=1.

**Type B (all 1<=r<=p-2):**

    c=2-2^(r+1), C=2H;
    (i,j,I,J)=(1,r+1,p-1,p-1);
    bit_(r+1)(k*a)=0, bit_(p-1)((k+2)*a)=1.

**Type A1 (1<=r<=p-3):**

    c=2-H, C=H+2^(r+1);
    (i,j,I,J)=(1,p-1,p-1,r+1);
    bit_(p-1)(k*a)=0, bit_(r+1)((k+2)*a)=1.

**Type A2 (1<=r<=p-3):**

    c=2-H, C=H+2^(r+1);
    (i,j,I,J)=(1,p-1,r+1,p-1);
    bit_(p-1)(k*a)=0, bit_(p-1)((k+2)*a)=1.

For the entire gap-zero necessary-support family, there are precisely **2p-5 distinct ordered numerical residual pairs (c,C)**, and exactly **3p-8 source-slot patterns (a,i,j,I,J)** before checking the true source bits and integer divisors. The counts are across all candidate a, not a claim of the same number of actual witnesses.

### Proof

Any actual m=0 witness satisfies C-c=2a>2H. The positive residual C is at most 2H, and c must be negative. The residual dictionary D_p={2^u +/- 2^v: 0<=u,v<p} has positive values above H only of the form C=H+2^e for 0<=e<=p-2, or C=2H. A negative dictionary value is c=2^u-2^v with u<v.

PREFIX-964E gives a=H+2^r-1, so 2a=2H+2^(r+1)-2.

If C=2H then c=2-2^(r+1). Since 1<=r<=p-2, its only difference-of-two-powers representation is (u,v)=(1,r+1), because the 2-adic valuation of 2^(r+1)-2 is 1. The only representation of C=2H as a sum of two allowed powers is 2^(p-1)+2^(p-1). The actual XOR signs force the Type B source bits.

If C=H+2^e then c=-H+2^e-2^(r+1)+2. Since c>=1-H, e>=r+1. If e=r+1, c=2-H, whose unique negative-powers representation is 2^1-2^(p-1); C has exactly two slot orders, yielding A1 and A2. If e>=r+2, the integer X=2^e-2^(r+1)+2 satisfies 2<X<H/2 and v_2(X)=1. The negative residual c=-H+X has magnitude >H/2, so its negative-power representation would have largest exponent p-1 and X=2^u. But X>2 and v_2(X)=1, a contradiction. Thus no additional cases exist.

Conversely, each pattern has C-c=2a. Its stated bit predicates turn the signed numerical residuals into the actual XOR residuals. For every b|k*a-c in Q_p with t>0, the first source equation holds. The second follows from (k+2)*a-C=k*a-c=t*b; the actual bit predicate supplies the second XOR equality. Therefore the list is both necessary and sufficient.

There are p-2 Type B patterns and 2(p-3) Type A patterns: (p-2)+2(p-3)=3p-8. There are p-2 distinct Type B numeric residual pairs and p-3 distinct Type A numeric pairs: 2p-5 total. QED.

## Q19 core 21/23: complete exact original XOR results

p=19, H=262144, k=21. There are 17 possible first moduli a, 33 numerical residual pairs and 49 named source-slot patterns. Exactly 12 of those 49 patterns pass both real XOR-bit predicates; their Q19 odd-divisor fibers yield **six named joint witnesses at m=0 and six different ordered modulus pairs**:

| a | b | t=T | i | j | I | J |
|---:|---:|---:|---:|---:|---:|---:|
| 262207 | 262213 | 21 | 1 | 7 | 18 | 18 |
| 263167 | 325209 | 17 | 1 | 11 | 18 | 18 |
| 264191 | 427085 | 13 | 1 | 12 | 18 | 18 |
| 266239 | 266629 | 21 | 1 | 13 | 18 | 18 |
| 266239 | 509019 | 11 | 1 | 13 | 18 | 18 |
| 278527 | 470093 | 13 | 1 | 18 | 18 | 15 |

These six coincide in count with the PREFIX-955/PREFIX-957B previously recorded m=0 column. The present program generates them without loading any previous pair certificate.

## Verification and reproducibility

The accompanying Python 3 program PREFIX965_R6_GAP0_NAMED_DIVISOR.py performs the theorem's slot/divisor reconstruction and compares against an **independent direct original XOR evaluator**. For p=4..7 it exhausts every permitted odd core k and every first modulus a in Q_p, all original i,j,I,J positions and quotient/divisor matches: **56 complete core-domain tests**. For p=8,9 it checks five chosen cores at each width using every source slot over the previously proved full gap-zero necessary first-modulus family: **10 additional controls**. At p=19,k=21 it again uses all original source positions over the 17 proved necessary first moduli and independently reproduces precisely the six witnesses above. These verification modes are recorded separately; the p19 reference is not a Q19^2 brute-force loop and it relies only on the already proved necessary a-support lemma.

Run from a writable directory:

    python3 PREFIX965_R6_GAP0_NAMED_DIVISOR.py

It writes PREFIX965_R6_EXACT_RESULTS.json with the actual witness tuples, 66 smaller-core checks and provenance. The local source SHA256 at validation was 6a1c13479ac68fd8d839aa559c4c78aed087f4921f6ce28e17d45a53995cafdc; the local JSON SHA256 was 105c675c3ec8045121c925a1e6ed3dfbeaee4c2313143d70b6fd659f8e206b6c. These hashes refer to the locally executed attached program/result before remote publication.

The algorithm reduces a gap-zero named-witness search to at most 3p-8 bit-predicate checks and divisor extraction for the surviving slot patterns. Factoring/divisor extraction is an explicit arithmetic cost and is **not** claimed polynomial in input bit length. Preprocessing and output reconstruction remain included in any future performance comparison.

## Relation to Enterprise Math and next question

This result strengthens PREFIX-964E's m=0 necessary value support to an **exact, source-sign-consistent and multiplicity-preserving reconstruction algorithm**. Distinct ordered witnesses (a,b,t,i,j,I,J) remain separate. The value-only projection is a rejection filter; its safe use for BRC path composition would require a typed map preserving downstream branch/source observers, which this auxiliary arithmetic theorem does not assert.

Next: derive similarly source-faithful classifications for m=1 and m=6 where feasible; combine slot-pattern classification with PREFIX-959B odd-divisor fibers and compare end-to-end runtime including divisor extraction and source recovery. Do not repeat the already proved m=0 family. The overarching B_fix,odd(32) in {19,20} remains open. The work is an author proof and reproducible computation, not an independent mathematical admission.
