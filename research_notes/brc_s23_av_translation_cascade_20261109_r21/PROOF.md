# Source-labelled translated-gap cascade across a circle-cluster order exit

2026-11-09. Enterprise Math / S23 auxiliary circle AV observer. Author-side mathematical result. Independent review pending.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: r20 PR #1878, commit `8b1bd6b49dc2d5df5b84620acc3e7acb2c51e644`, plus r18/r19 circle risk definitions. These are scalar circle results, not native X6 dynamics.

## General translated-gap cascade lemma

Let 0<theta<1 be irrational; write phi_j={j theta}, P_t={phi_j:0<=j<t}. Fix historical cut count m and its clockwise arc partition. Define R(m,n-m)=1-sum_{historical arcs I} max_{subarcs J of the n-cut refinement of I}|J|, n>=m.

Fix integers t0>=m and u,v in [0,m-1] such that the clockwise historical arc I_0=(phi_u,phi_v) is an **uncut n=t0 arc**, i.e. contains no points of P_{t0} in its interior, and phi_{t0} lies strictly inside I_0. Let its two clockwise pieces have lengths a>0 and b>0, so the original length is d=a+b.

For each integer s>=0 such that (i) u+s<m and v+s<m, and (ii) the clockwise arc I_s=(phi_{u+s},phi_{v+s}) is also a historical arc, one has:

* I_s contains no point of P_{t0+s} in its interior;
* phi_{t0+s} is inside I_s and splits it into the same exact lengths a,b;
* the whole-future-block risk increment for insertion of the index t0+s is
  `R(m,t0+s+1-m)-R(m,t0+s-m)=min(a,b)`.

**Proof.** Rotation by s theta carries I_0 to I_s and carries the cut labels 0,...,t0-1 to s,...,t0+s-1. Hence no label in that latter range lies in the interior of I_s. The only remaining prior labels are 0,...,s-1; because u+s<m and v+s<m, s<m, so these labels are historical cuts and cannot lie inside the historical arc I_s. Therefore I_s is an *unrefined* historical arc just before t0+s is inserted. The new phase is the rotation of phi_{t0}, so the pieces are a,b. Its historical-arc maximum changes from a+b to max(a,b), while the other historical arcs are unchanged. Substitution into the defining risk formula yields min(a,b). QED.

### Minimum-return adjacency criterion

If d=min_{1<=j<m}||j theta||>0 and the clockwise length from phi_u to phi_v equals d, for u,v in [0,m-1], then phi_u and phi_v are consecutive historical cuts: any intermediate historical point would be within clockwise distance <d of phi_u, contradicting the minimum-return bound for its index difference of magnitude <=m-1. This criterion supplies condition (ii) for translated pairs whenever their clockwise length is d.

## Exact S23 application: 67 identical positive increments after the order exit

Use m=128 and the strict pre-certified interval

`262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24`.

Define
`d=16-61 theta`, `a=164 theta-43`, `b=59-225 theta`.
Endpoint-certified strict inequalities give `0<a<b<d` and `a+b=d`. For j=1,...,127, the unique smallest return is attained at j=61 and equals d. Among the first 225 phases, phi_61 is strictly the largest, so the old clockwise gap from phi_61 to phi_0 is uncut. The next index 225 enters that gap, splitting it into a,b.

For s=0,...,66, the translated gap endpoints `u_s=61+s` and `v_s=s` both belong to the 128 historical indices and have clockwise separation d. The minimum-return adjacency criterion applies, and the general translated-gap lemma gives, for each integer n=226,...,292,

`R(128,n-128)-R(128,n-129)=a=164 theta-43`.

In source-index form, every step inserts t=n-1=225+s into the intact historical arc from (61+s) to s, with exact subarc lengths (164 theta-43,59-225 theta). The 67 original historical arcs are distinct. Hence, from `R(128,225-128)=-2047+7808 theta`,

`R(128,n-128)=-2047+7808 theta+(n-225)(164 theta-43)` for 225<=n<=292, and
`R(128,292-128)=-4928+18796 theta`.

**Mechanism.** The original 61-cluster order stops at the 226th cut, yet a translated family of 67 intact historical gaps survives. Thus each of those 67 insertions repeats the same source-labelled local split even after the nominal cluster order has changed.

## Adjacent plateau (finite exact certificate)

For each integer n=293,...,328, the newly split subarc is of length d, but the same historical arc has **another still-unsplit subarc of length d**. Consequently its historical-arc maximum remains d and the risk increment is exactly zero. The standalone checker exhaustively reconstructs all corresponding partitions, labels, lengths and maxima using the strict rational interval. Therefore

`R(128,n-128)=-4928+18796 theta` for every integer 292<=n<=328.

At n=329 the increment is again a, giving
`R(128,329-128)=-4971+18960 theta`.

The 36-step plateau claim is a complete finite certified computation for the specified parameter interval and indices, while the translated-gap cascade is an all-theta mathematical lemma under its hypotheses.

## Certification and claim scope

`VERIFY_R21_STANDALONE.py` is a self-contained exact-Fraction verifier. It checks 0..328 phase floor stability, ordering and historical-arc max-choice stability at **both** endpoints of the inherited strict rational enclosure, uniqueness of the 61-minimum over differences 1..127, the base 225-point maximum, all 67 translated intact gaps and all 36 post-cascade plateau insertions. The risk function is independently rebuilt from full n-cut circles for n=225..329 (104 updates), retaining exact affine integer coefficients. No floating point, earlier table or external file is needed. End-point checking is sufficient here because all phase/gap/max comparisons use affine functions with fixed floors; the minimum-return distance is the minimum of two affine branches and its difference from d is concave, so a nonnegative lower bound at both endpoints holds throughout the interval.

This result advances a source-provenance-preserving gap carrier for the declared scalar Bayes observer. Formal shared CLAIM and independent mathematical admission remain unresolved. It neither changes the task's frozen scientific pin nor promotes a native-X6 bridge.
