# NEXT_TASK — exact unrestricted stochastic four-code rate-distortion

The five-code unrestricted problem has now been closed: R5(all S23;epsilon)=R5(all S2;epsilon)=1/40 for every real epsilon in [0,1/2]. This is proved in PROOF.md, with precise test coverage in VERIFY.js/RUN_EVIDENCE.txt. Do not redo the previous 2/143 sandwich as still open.

**New primary question:** Determine R4 for a fixed common stochastic four-code encoder, arbitrary cross-S code sharing and policy-aware stochastic decoders, scored by the same complete public record O=(T,Decision,Z_BU), first for all S23, then all S2. The deterministic/source-homogeneous value is 1/5; the unrestricted randomized value requires proof.

**First minimal unit:** For the six-class M in PROOF.md, every stochastic 6x4 encoder E has a zero-sum left nullspace of dimension >=2. Obtain an exact rational 2D subspace lower-bound certificate using all 64 Boolean LR stop observers; incorporate E>=0, E1=1 and full-output decoder constraints. Either prove R4>=1/5 or exhibit one exact rational four-code E and all required policy-specific decoders proving a strict improvement; do not elevate a restriction to all S23/S2 unless it supports their entire stochastic/adaptive language. Report proof and program evidence separately.

**Separate native-model task:** Specify physically grounded source-preparation state, transition kernel, independent time and observation interface from P000 native X6 to this external finite BRC experiment before making dynamical or empirical interpretations.

Independent mathematical review and current native Owner/CLAIM remain distinct role-authority requirements. This file is an author-side handoff, not native task publication.
