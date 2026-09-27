# Exact native checks and symbolic review

Activity RA-CAAAC604CB513AEA8BBC1DFC. Shared-context author work, not an
independent admission. All preceding published dependencies were retained.

`check_observer_contracts.py` executed successfully on N=21, a=2, t=4,
both the exact D=6 carrier codec and all D=61 native coordinates. Each
dimension checked all 15 positive parent prefixes. The checker enumerates
the exact native state for validation only; it is not a proposed efficient
online certificate oracle. This four-round fixture is not the default
ten-round factoring instance for N=21.

The 120 projective trials cover common scaling by 8, predetermined sign
changes by work label, keeping even labels, and an all-zero approximation
with fair fallback. They verify the exact rational inequality
`M * local_TV^2 <= Eproj`, including `u=8v`: raw error `49M`, projective
error zero and identical local sampler. The two dimensions have identical
reported numerical observations.

The 86 support-leakage checks enumerate eligible subsets only in this
small validation fixture. They verify `fair_TV^2 <= epsilon(1-epsilon)`.
The exact fair joint error equals `L/(2M)` and its single-bit marginal
error equals `|G|/(2M)`. No strict signed-cancellation example occurred in
this reachable fixture; the stronger distinction is proved symbolically.

A simple local-kernel example illustrating that distinction is a four-cycle
permutation, T=I, and scalar rows `(1,1,-1,-1)/2` in cyclic order. Then
M=1, G=0, L=1: the marginal bit is already fair while the joint
bit/label fair-replacement error is 1/2. This is an algebraic kernel
example, not an executed or asserted reachable standard Shor prefix.

The successful checker used 2052 actual BRC core calls. Complete observer,
typed modular, bank and source bindings are in `OBSERVER_CONTRACT_RESULTS.json.gz`.
Payload SHA256: `44f1d9127ede455447540c226f30e0ab076e7e39354edae618a59663f6cd5504`.
Gzip SHA256: `fa8ec8ccf703ef34a55b8b822534143fe4595b12fdb7fc2f480c5b14753fdf31`.
The first attempt completed assertions but failed while serializing an
already serialized byte string. The final source corrected that packaging
call and was rerun successfully; no result from the failed packaging
attempt is presented as a durable execution artifact.

A second shared-context author independently checked the derivations in
`PROJECTIVE_AND_COHERENCE_BOUNDS.md`: the zero optimal-scalar limit, joint
versus marginal coherence, support-set fidelity bound, and the a=1
counterexample to treating raw Monte Carlo variance as a TV lower bound.
This was symbolic peer checking, not independent formal admission.

These checks establish finite native correctness of the displayed
inequalities. They supply neither a generic cheaply computable coherence
certificate nor a polynomial-time approximate row oracle. Errors relative
to this native instrument and errors from its bank relative to ideal QFT
remain separate budgets.
