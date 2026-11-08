# PREFIX-604-R6 — Full seven-axis BRC rewards do not repair singular phase information loss

Date: 2026-11-08 Asia/Shanghai.
Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Source: original native PREFIX565 BRC edge and successors, source blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
Dependent verified mathematics: PREFIX600/601/602/603, original all-1 section retained.
Status: AUTHOR_PROVED / EXACT_NATIVE_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Question and precise model

PREFIX-601 established that the declared 12-incidence weighted extension of the original native 48-phase transition loses exactly 2k source-phase directions when k reciprocal incidence pairs satisfy 4t_e t_f=1. PREFIX-603 showed that adding one bit indicating the original internal slot=0, JOINTLY with next phase, recovers all source-phase information. Can a more accessible observable—the original six BRC axis rewards, gate marker and exact next original 96-port—replace that internal branch-origin tag?

All nine original reward roots, all 48 native signed phases and original six action labels (slot,newbit) are retained; cross-star slot weights are reweighted with t_e>=0 as declared by PREFIX-601, applied equally to both newbit choices. We study one-step seven-reward O7 without revealing the original action slot. The initial 96-port law can be arbitrary. A *subfamily* used for an exact lower bound consists of strictly positive phase distributions pi and an independent initial branch bit B~Bernoulli(beta), with 0<beta<1.

## Lemma 1 — every six-axis reward is determined by the terminal phase

The native successor construction has the exact identity

    PHASES[next_phase][1] = PHASES[source_phase][2]

for all 48 phases and all 3 slots. The original BRC edge function defines each axis reward using only the signed source c, signed target c and the fixed root r. Therefore for every root r and destination q, the original six-reward vector is a deterministic function w_r(q), independent of which predecessor p or action slot led to q. Explicitly, if PHASES[q]=(a,p',c'), define

    left_k  = sign(p') if abs(p')=k else 0,
    right_k = sign(c') if abs(c')=k else 0,
    w_r(q)_k = (abs(left_k)+abs(right_k)-abs(right_k-r_k)+abs(left_k-r_k))/2

for k=1,...,6. The original typed BRC rewards are integers in {0,1}. This formula is exactly the pinned source's edge definition, not a replacement scientific arithmetic model. QED.

## Theorem 1 — factorization of complete O7 through the lossy phase observer

Let z(q)=sum_p pi(p)P(t)[p,q] be the next phase law and suppose initial B is independent of the initial phase with Pr(B=1)=beta. In the original native action model, the newbit is uniform independently of source phase, source bit, slot and endpoint. The gate is

    G = 1{B=1, newbit=1, next_phase=TARGET}.

Together with Lemma 1, the complete joint law of

    O7 = (six original BRC axis rewards, gate, exact next original port)

is determined entirely by z(q), beta and root r. More precisely: for every q and newbit=0, the atom at (2q,w_r(q),gate=0) has mass z(q)/2. For newbit=1 and q!=TARGET, the analogous atom has mass z(q)/2. For q=TARGET,newbit=1, the gate-1 atom has mass beta*z(q)/2 and the gate-0 atom has mass (1-beta)*z(q)/2.

Thus, at fixed beta and root, this complete seven-reward/next-port observer has EXACTLY the same initial phase rank as the untagged terminal phase map: 48-2k. Gate and reward labels do not recover its lost phase directions. This holds for all finite nonnegative real weights t, across all nine frozen allowed roots. QED.

## Theorem 2 — sharp worst-case 2k extra scalar readings even after observing O7

For ANY initial law over the original 96 ports, O7 visibly determines its next-phase marginal z=pi_phase P(t). The 2k scalar initial phase statistics r_ell from PREFIX-602 therefore suffice to reconstruct the source phase marginal pi_phase, and by PREFIX-603 each may be extracted from a FOUR-SUPPORTED signed projection of the separately retained internal-slot-tagged endpoint histogram.

They are necessary in the class of extra real LINEAR scalar measurements, even after O7 is available. Restrict initial laws to the valid product subfamily pi_phase ⊗ Bernoulli(beta) with fixed beta in (0,1); Theorem 1 makes O7 depend only on pi_phase P(t), whose nullspace has dimension 2k. Any fewer than 2k extra linear scalar functionals leaves a nonzero common null direction. Such a direction has zero total mass because P(t) is stochastic; sufficiently small opposite perturbations about strictly positive phase/bit laws give different strictly positive initial 96-port laws with identical O7 and all extra measurements.

Therefore the exact minimum number of extra linear scalar readings needed to reconstruct the ORIGINAL 48-PHASE MARGINAL from O7 uniformly over all initial 96-port distributions is 2k. This does not claim reconstruction of the full initial 96-port bit distribution, nor rank equality for arbitrary correlated-bit O7 maps (the rank statement in Theorem 1 is on fixed independent-bit subfamilies).

## Exact executed native validation

Executed Python standard-library Fraction certificate with the exact original PREFIX565 BRC edge implementation, the original twelve-incidence weighted deformation and PREFIX603's native left-null basis.

- Exhaustively checked 48 source phases x 3 slots x 9 roots x 4 oldbit/newbit choices = 5184 exact typed BRC reward and gate identities.
- Checked all nine roots on the exact 96-port O7 distributions, including target original port and gate.
- For t=1, and for k=1,2,6 singular-pair deformations, reconstructed output via the explicit factorization and directly enumerated all 96*6 labeled native actions with proper weights.
- At k=1,2,6, constructed TWO DISTINCT STRICTLY POSITIVE 96-port probability laws from the original left nullspace. Their complete O7 output laws were IDENTICAL at each of nine roots; initial phase laws were not identical.
- Result: ALL_CHECKS_PASS. Finite tests support the constructive algebraic proof; they are not the justification for the universal real-weight quantifier.

## Research significance, scope and next step

This establishes a sharp separation between BRC reward information and action-source provenance in the declared one-step weighted native phase observer. The complete seven-reward and endpoint readout can fail to distinguish exact phase histories even though a single original native action-origin bit, retained JOINTLY with endpoint, restores them. The original all-1 frozen law has k=0, so this is a model-family singular-stratum result and does not imply an information defect in the original frozen one-step phase matrix.

Next: examine restricted observer alphabets that retain only a subset of native slot labels; classify sufficient Boolean partitions of three slots; determine robust sample/error bounds of sparse tagged measurements near the critical reciprocal surfaces. Source Result/Review, independent review, physical transfer and broader-than-one-step claims remain open.
