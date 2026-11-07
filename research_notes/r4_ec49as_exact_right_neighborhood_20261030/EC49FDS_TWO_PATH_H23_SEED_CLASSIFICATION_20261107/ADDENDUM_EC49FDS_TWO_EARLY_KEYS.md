# EC49FDS addendum — Complete 8-case two-BRC-key H2(3)/H3(2) seed census

Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Date: 2026-11-07.

The EC49FDS two-word/two-word theorem established four viable three-key early seeds. This addendum separately exhausts an alternate, potentially more useful seed class: exactly **three distinct selected H2 words**, exactly **two distinct selected H3 words**, exact rational observation rank nine at both horizons, and **exactly two distinct complete positive BRC keys** over both horizons. Keep all signed native X6 primitive path order and count the primitive-prefix union exactly.

There are 6 valid H2 individual words, 38 valid H3 individual words. Of the C(6,3)=20 H2 triple subsets, **6** have rank nine; of the C(38,2)=703 H3 pair subsets, **16** have rank nine. Thus exactly **96** rank-feasible joint triple/pair candidates occur before the full-key-budget filter. Requiring *exactly two* full early keys leaves **8 seeds**: **four have 31 primitive-prefix edges**, and **four have 35**. Each of the eight is explicitly listed in EC49FDS_two_key_three_H2_report.json and reconstructed by EC49FDS_two_key_three_H2.py.

The eight seeds have one of two H2 triples:
- H2={ce,ed,ge}, H3 in {feg,fge} × {gef,gfe}, early keys (2,1,1),(3,1,1), costs 31,35,31,35 in that H3 order.
- H2={de,ec,fe}, same H3 alternatives, early keys (3,0,1),(3,1,1), costs 31,31,35,35.

Each rank condition was checked by the existing literal signed primitive-step Fraction row-elimination implementation, independently of the signature-clause sieve. The complete key is counted from positive signed primitive axis steps. Exactly two new keys must be introduced to reach H4 and H9 (H4 feasibility implies x+y<=8, H9 implies x+y>=10; the initial keys expire by H3); consequently these seeds reserve **up to three key slots** under the five-key mother budget, providing a distinct search branch from the four viable three-key 2+2 seeds.

Reproduce by running, in the sibling EC49FDS directory:

    python EC49FDS_two_key_three_H2.py > EC49FDS_two_key_three_H2_report.json

This is an exact classification of an early-window subfamily, not a full H2–H9 93-edge witness. The eight seeds are concrete inputs for a joint H4–H9 five-key, primitive-prefix optimization. Preserve the 94-edge legal upper bound and all previously frozen science; Source-native CLAIM/independent Driver review remain open.
