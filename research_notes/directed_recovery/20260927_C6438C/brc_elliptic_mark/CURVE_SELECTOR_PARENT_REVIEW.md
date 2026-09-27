# Parent review of the curve/exponent selector analysis

Status: FULL_TEXT_SYMBOLIC_PASS / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

The coordinator read the complete CURVE_EXPONENT_SELECTOR_ANALYSIS.md at SHA-256 e8b2fbaba788c51e379c05f1050cadfecf671a10f3129d52715608381b34aad0 and checked its algebra against the frozen Jacobian doubling formula. This is symbolic substitution and a probability calculation for an explicitly specified distribution, with no scientific module or new numerical experiment.

The parameter change B=10+4A gives 16(A^2-4)=(B-2)(B-18). In the first doubling, M=(B+3)B^2, S=8B^5 and Z2=2B^2. The X bracket reduces to 9 using 4A=B-10, while the Y bracket reduces to 15B-27=3L. Thus (X2,Y2,Z2)=(9B^4,3LB^6,2B^2) and Z4=12LB^8. Removing only the already admitted unit factors proves g4=gcd(N,3L), including partial prime powers.

In the second doubling, the terms in M2 give 243+72AB+16B^2=34B^2-180B+243=H. The 2S2 and a2*Z4^2 terms combine to 36(B^2-10B+18)L^2; omission of the a2 term would invalidate this calculation, but it is retained. The resulting X4,Y4,Z4 are B^16*K,B^24*J,12LB^8. Consequently Z8=24B^32*L*J and g8=gcd(N,3LJ). The degree of J is at most six. Its constant term check reduces symbolically to 3^14-8*3^12=3^12, so J is a nonzero polynomial modulo every prime above three.

For p>5, the three excluded L values -9,1,81 are distinct, since their differences have only 2,3,5 as prime factors. Zero is admitted. The stated one-root E4 probability 1/(p-3) and the CRT formula for a conditional uniform admissible draw are therefore correct. They are not the law of an uncharged sampler; the note explicitly keeps setup and rejection costs separate. Globally imposing L=0 synchronizes the return and saturates rather than separating components. The local p=3 and p=5 qualifications are also necessary and correctly stated.

The doubling-layer result follows from primitivity: a residue prime dividing Y and Z would also divide X by the curve equation. Hence the gcds of Y and Z have disjoint prime support. Since 2 is a unit, the divisor of the next Z is exactly their integer product, with no prime-power truncation conflict. Once a component is in Z, its Y remains a unit and further doubling preserves the capped depth. In particular the g4 and J divisors are coprime. The pure power-of-two schedule cannot remove an odd factor of the point order. Retaining first-hit layers may prevent saturation from erasing separation, but provides no uniform favorable local order distribution.

No substantive defect was found in the declared scope. The analysis is a useful reduction of this curve family to exact parameter conditions, not a lower bound for all geometry or a new general factoring algorithm. An intended shorter native observer must still have its own frozen program, actual arithmetic receipts and equal-output cost comparison; the saved elliptic ladder cost is unchanged.

The full-text review also consumed TWO_CLOCK_TRANSLATED_SECTION.md and both source-bound symbolic reviews. The product identities there concern E and E+2; the selector analysis concerns E and 2E. Their hypotheses and remaining cost obligations are kept distinct.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
