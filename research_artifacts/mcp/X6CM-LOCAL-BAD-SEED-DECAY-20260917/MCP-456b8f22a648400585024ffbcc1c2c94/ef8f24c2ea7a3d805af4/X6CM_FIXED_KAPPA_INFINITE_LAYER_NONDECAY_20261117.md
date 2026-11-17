# X6CM fixed-geometry bad-seed fraction: an infinite level-family obstruction

Date: 2026-11-17. Task: X6CM-LOCAL-BAD-SEED-DECAY-20260917; publication TP2-EDB5E5D91A3A79938443.
Researcher: EM-X6CM-EDBD55. Status: original scoped proof plus exact finite author tests; NOT independent review, NOT global gamma/alpha closure.

## Frozen mathematical interface

Use the cyclotomic degree-six ideal block from research_notes/x6_tunable_geometry_and_second_moment_barrier_20260911.md and its proven local T4: at the penultimate s=f-1=5 layer, distinct projective Krylov witness classes correspond bijectively to individual dual-seed atoms. Keep signed integer witnesses and prime/provenance labels until applying this observer-scoped Boolean seed-event quotient. For inert p congruent to 3 or 5 mod 7, set kappa=1/sqrt(42), I_0=Z^6. The strict cutoff is ||z|| < kappa p^(5/6), or exactly 42^3*(sum z_i^2)^3 < p^5. The exact finite bad fraction is
b_p= #{[z mod p] : z in Z^6, z != 0, 42^3*(sum z_i^2)^3 < p^5} / (1+p+p^2+p^3+p^4+p^5),
excluding zero residues.

## Infinite nondecay theorem along prime-power level

Fix inert p and ANY fixed positive kappa, and let I_r=P^r for r>=0. Because P=p O_K for an inert prime, I_r=p^r Z^6, D_r=det(I_r)=p^(6r), and the threshold R_{r,5}=kappa(D_r p^5)^(1/6)=p^r kappa p^(5/6). Writing every z in I_r uniquely as z=p^r w, the witness inequality and the finite-field reduction after dividing by p^r become exactly the base-level condition in w. The cyclic Krylov and dual seed lines are unchanged. By the frozen T4 bijection, b_{p,r,5}(kappa)=b_{p,0,5}(kappa) for ALL r>=0.

Whenever kappa p^(5/6)>1, e_1 is a short nonzero witness and b_{p,r,5}(kappa)>=1/(1+p+...+p^5)>0 for all r. For p=17,kappa=1/sqrt(42), exact enumeration gives b=36/1508598 independent of r (42^3<17^5). For every kappa>0, there exists some arbitrarily large inert prime p≡3 mod7 (Dirichlet theorem) with kappa p^(5/6)>1. Fix this p and let r grow: an infinite family has a nonzero fixed bad-seed fraction. This is a rigorous nondecay obstruction to pure *layer-based* decay for ANY fixed positive geometry constant in the declared model.

Global implication is SCOPED. A fixed p contributes conditioning factor (1-b_p)^(-1), independent of r. At p=17,kappa=1/sqrt(42), this factor is 1508598/1508562. A finite collection of such primes may only alter the multiplicative constant in an arithmetic mean. Neither the critical gamma/alpha equality nor an obstruction to decay over *distinct growing primes* follows from this fixed-p layer theorem. The open global question is whether the distribution b_p over distinct primes yields zero mean-log conditioning exponent while preserving all four frozen seed locks and mixed-composite provenance.

## Verified exact finite census at the same fixed positive kappa

Inert p | max squared length Q | signed short integer vectors | projective bad atoms | total dual seed atoms
17 | 2 | 72 | 36 | 1508598
31 | 7 | 2300 | 1144 | 29583456
59 | 21 | 50012 | 24572 | 727250580
73 | 30 | 144816 | 71136 | 2101864254
101 | 52 | 750872 | 368864 | 10615201506

All counts are exact integers. Earlier p=17 and 31 counts reproduce frozen parent T4; new p=59,73,101 are additional integer enumerations. The attached Python checker computes the q cutoff, enumerates all 6-coordinate lattice points, normalizes each nonzero residue by its first nonzero coordinate, verifies primality/inert residue and both old counts. It uses only Python standard library and exact arithmetic; finite counts do not prove a distinct-prime asymptotic.

Next scientifically discriminating step: derive an analytic bound for collisions/second moment of primitive short integer lifts on random projective residue lines for growing inert p, at one fixed kappa, and propagate the exact b_p series to the gamma/alpha conditioning frontier. Keep projective event equivalence separate from native direction/port provenance, and independent Driver assessment separate from this author's proof.

Source pins: taskbook research_tasks/X6CM_LOCAL_BAD_SEED_DECAY_GEN2_20260917.md blob 913e3fccfadfa307ab7a3eace420a5ba9ba01568; parent research_notes/x6_tunable_geometry_and_second_moment_barrier_20260911.md blob aa6005f0e53d9d9d86331adcec64f783ae646259.
