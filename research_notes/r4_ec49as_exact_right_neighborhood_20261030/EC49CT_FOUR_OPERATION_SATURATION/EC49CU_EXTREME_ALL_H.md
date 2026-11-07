# EC49CU — Universal extreme-fiber saturation lower bound for expanded signed-X6 BRC

Date 2026-11-01 Asia/Shanghai. Status: AUTHOR_ANALYTIC_PROOF / VERIFIED_LITERAL_BRC_TRANSFER / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. This is one completed subunit of EC49CU; full h=5 all-fiber rank determination remains open.

## Source and unchanged model

Reuses the same canonical GLOBAL_KNOWLEDGE_V1 main a1eb5340e1c814b20999bbcb07a6781aca621257, Enterprise Math main 993a408982a302265cb3c31f93e69e4751299500, P000/ACTIVE worldview, native signed six-axis positive BRC and 9-state ordered A/B DFA. The exact EC49CT genuine length-14 and length-16 extreme-target path certificates are preserved in PR #1730 within sibling EC49CT_FOUR_OPERATION_SATURATION. Its BRC channel weights are w0=(2,3,3,2,1,1), w1=(3,2,3,2,1,1), negative weights 1, plus exact path count. Operation e=(+E3,+E1,+E1,-E3) has signed displacement +2E1 and native weight factors (12,27,1). All other operations a,b,c,d contribute at most zero E1 displacement. Final joint tag3 means both adjacent ordered patterns A=(+E1,+E2) and B=(+E2,+E1) occurred.

## Theorem for every integer h>=4

For either exactly h complete operations S'^h or cumulative one-through-h operations S'^{1..h}, consider the **extreme displacement fiber** of genuine native prefixes with endpoint D_h=(-2h,0,0,0,0,0). In the formal additive rational-linear observer this fiber is 12-dimensional, indexed by four joint tags and three BRC/count channels. Its unique cancellation suffix among words of length at most h is e repeated h times.

**At genuine prefix length n=2h+6**, the extreme fiber has exact Q-rank **11 of 12**. **At n=2h+8**, the extreme fiber has exact Q-rank **12 of 12**. Both conclusions hold for every integer h>=4, not merely for tested h. In particular, the earliest *global* genuine-prefix saturation of the full observation language, if attained, obeys the unconditional lower bound

    n_sat(h) >= 2h+8 ,  h>=4.

This theorem does not assert that all the other fibers are saturated at n=2h+8; that is a separate EC49CU/continuation obligation.

### Analytic upper bound at n=2h+6

For any genuine n-step signed X6 path at endpoint D_h, let p1 and p2 be the numbers of +E1 and +E2. Signed displacement implies n>=2h+2(p1+p2); for n=2h+6, p1+p2<=3. Future suffix e^h contains no +E2 and begins +E3, so neither A nor B can be formed within it or across the prefix-suffix join. Any final joint tag3 requires both A and B already within the prefix, which entails at least three positive letters in one of the two orders (+E1,+E2,+E1) or (+E2,+E1,+E2). Thus p1+p2>=3; equality holds and consumes the entire length budget. Consequently the two possible positive multiplicities (p1,p2) are (2,1) or (1,2); all other primitive-axis steps are absent. The correlated native prefix BRC channel weights are exactly (12,18) or (18,12).

The suffix e^h multiplies channel weights by (12^h,27^h,1). Therefore every genuine path in this fiber contributing to the final joint tag3 satisfies the exact pathwise readout relation

    R(e^h,3,count) =
         R(e^h,3,w0) / (30*12^h) + R(e^h,3,w1) / (30*27^h).

It is a nonzero rational dependence among 12 formal readout rows, so actual fiber rank <=11 for all h>=4. For h=5 these denominators are respectively **7464960** and **430467210**.

### Uniform literal-path lower witnesses

EC49CT provided authentic signed-X6 path witnesses at h=4, extreme D4=-8E1. At prefix n=14, eleven genuine paths have an 11x11 nonzero minor 920330 mod 1000003. At n=16, twelve genuine paths have a 12x12 nonzero minor 548822 mod 1000003. For any h>=4, transform each such path p into

    p_h = p concatenated with (-E1,-E1) repeated (h-4) times.

The resulting prefix has endpoint -2h E1, length respectively 2h+6 or 2h+8. The negative appended letters neither introduce A/B positive pairs nor alter either positive BRC product, and the e^h suffix adds exactly h-4 extra e operations relative to e^4. Thus for each tag the readout matrix differs from the original at h=4 only by an invertible diagonal row multiplication: w0 rows by 12^(h-4), w1 rows by 27^(h-4), count rows by 1. In characteristic zero, the two nonzero minors stay nonzero for every integer h>=4; indeed the modular witnesses remain nonzero modulo p=1000003 since p divides neither 12 nor 27. This establishes the rank >=11 and rank >=12 matching the respective upper bounds.

At lower even prefix lengths, prepending neutral (+E3,-E3) pairs embeds readouts into length 2h+6 without changing tag or endpoint, so they cannot saturate this deficient fiber earlier. At odd prefix lengths the parity of signed six-axis displacement precludes the even target D_h. Therefore the **global saturation lower bound** follows.

## Actually executed witness-transfer check

The stdlib-only source EC49CU_EXTREME_RECHECK.py reads the two original EC49CT JSON witness blocks, appends the exact negative native steps and re-evaluates literal paths/positive native BRC products/adjacent-pair tags/modular minors, plus the analytic tag3 identity. Original certified seed minors and transferred minors were checked at h=4,5,6,7,10,20. The n=2h+6 rank11 and n=2h+8 rank12 nonzero residues were:

- h4: 920330 / 548822
- h5: **407 / 305495**
- h6: 499102 / 566852
- h7: 199163 / 422896
- h10: 935040 / 361642
- h20: 142516 / 540038

Finite checks corroborate the explicit all-h proof; they do not themselves prove it. The proof requires no new physical dynamics or unverified BRC numeric approximation. The scripts reapply the original typed positive BRC kernel semantics, not Euclidean/trigonometric or phase cancellation.

## What remains

At h5 the formal full observer dimensions remain exact 537 and cumulative 582. The extreme D5=-10E1 rank is now proved 11/12 at n16 and 12/12 at n18; the other 35 displacement fibers still need exact-Q upper ranks and genuine-path lower minors to determine whether n_sat(5)=18. No general full-saturation formula has been proved. Native status at the run was authority_granted=false and current owner query CONTROL_QUOTA; no formal CLAIM/Result/independent Driver review is established.