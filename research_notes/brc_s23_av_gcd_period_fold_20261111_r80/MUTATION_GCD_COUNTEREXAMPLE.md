# R80-D — One insertion can invalidate an old common-period certificate

Auxiliary circular-source model, preserving R77 original directed half-open labels and original source identities. Frozen S23/AV input stays unchanged.

For any integer g≥2, take observer j=x=0, labels a=g and b=2g, and original source E0={(4g,branch=1)}. Its exact common divisor is g, so W0(theta) has period 1/g by R80-A.

Insert a later source (4g+1,branch=1), giving E1={(4g,1),(4g+1,1)}. The new gcd is gcd(g,2g,4g,4g+1)=1, so the old 1/g period cannot be assumed for the enlarged latest-source readout.

**Explicit exact counterexample.** At theta=1/(g+1), the label endpoints are A=g/(g+1), B=(g-1)/(g+1), hence the directed arc wraps and equals [A,1)∪[0,B). The new source has phase { (4g+1)/(g+1) }=1-3/(g+1), inside the arc (including g=2, where this is 0). The old source is also a member, so the winner is (4g+1,1).

At theta'=theta+1/g, both label phases and the old source phase are unchanged. The new source phase increases by 1/g modulo one. For g≥2 one has
B=1-2/(g+1) < 1-3/(g+1)+1/g < A=1-1/(g+1).
Thus the new source lies **outside** the wrapped target arc; the old source remains inside. The winner at theta' is (4g,1), not (4g+1,1). Therefore W1(theta') != W1(theta), contradicting any reuse of the old 1/g certificate for the updated source set.

In a persistent index, every immutable historical version retains its own correct g and periodic certificate. A new version must recompute or validate g after changes to the source times or observer slopes; a cache keyed only by the original label pair (a,b), or by a reused source-root object without the current observer/source slope set, is insufficient. This is an exact **version-invalidation witness**, not an objection to the R80-A theorem for its stated unchanged event set.

This addendum supplies a specific R81 regression: insert time 4g+1 into the version with only time 4g, then query the two rational parameters above and verify the changed winner; deleting the inserted source restores the previous periodic answer in the historical version.
