# R23 addendum: the 67-step F61 restart after the 389-step plateau

Frozen science: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Same open rational interval for theta and same historical m=128 as PROOF.md. All claims are for the S23/AV auxiliary irrational-circle observer, with no native-X6 transfer.

Let a=164theta-43, e=145-553theta and f=a-e=717theta-188. Exact interval arithmetic proves 0<f<e<a.

**Proposition.** For every integer 1106<=n<=1173,

R(128,n-128)=(5505-20992theta)+(n-1106)(717theta-188).

In particular, all 67 new cut counts n=1107,...,1173 have strictly positive common risk increment f, and

R(128,1045)=R(128,1173-128)=-7091+27047theta.

The next cut count n=1174 produces exactly zero increment:

R(128,1046)=-7091+27047theta.

**Proof by labelled-fibre transport.** Immediately before the t=1106 insertion, the historical clockwise adjacent arc phi_61 -> phi_0 contains the ordered source-labelled gaps

61->778:f; 778->225:e; 225->942:f; 942->389:e; 389->553:a; 553->0:e.

The unique longest gap has length a. The newly arriving cut t=1106 falls inside this unique a-gap, splitting 389->553 into two gaps f,e, whence the increment is a-max(f,e)=f. The r22/r23 minimum-return certificate proves that for every s=0,...,66 the rotated pair (61+s,s) is still a clockwise adjacent historical arc. The translated full-fibre lemma from PROOF.md maps the entire ordered labelled partition and the insertion destination for t=1106+s to that at s=0. Thus all 67 insertions have increment f. Summing gives the asserted exact affine formula.

At pre-insertion t=1173, the newly arriving cut falls in historical owner phi_25 -> phi_67. That arc has *two* distinct longest a-gaps, specifically 517->681 and 456->620; all other gaps have lengths e or f (<a). The arriving cut t=1173 splits 456->620 into f and e, leaving the independent 517->681 a-gap intact. By the tie-max rule, the largest gap of the historical arc remains a and the increment for new cut count n=1174 is precisely zero. QED.

**Independent computational scope.** VERIFY_R23_F61_EXTENSION.py expands the prior executable interval endpoint checker to all indices 0..1173, adds the 17th labelled fibre base (1106,67,61,f), checks 681 declared updates n=493..1173 and computes the n=1174 tie update via a separate full-partition endpoint comparison. It uses Python Fraction throughout. Independently, a local extended verifier generated TEMPLATES_R23_EXTENSION.json (17 source-labelled base fibres, 22065 bytes, SHA256 cca8fa9fa43cc6d7dab35879606461f29a53cd219ad51ae0b00bc8e3653fa50d) and passed all checks. The branch verifier is a concise implementation of the same finite claims; byte-for-byte identity with the extended local checker is not asserted. Independent mathematical review is still pending.

**Next discriminating question.** Using the F42 historical arc (25+s,67+s), prove the first maximal-tie epoch after n=1174 without iterating all future cuts. Test whether a single base fibre plus its 36 translations predicts the plateau's endpoint and following positive increment; retain each source label and the exact parameter-comparison interval.