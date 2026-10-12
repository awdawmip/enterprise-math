# PREFIX-45: Exact arithmetic guard periods (UNREVIEWED)
Parent source: Enterprise Math PREFIX-44 at commit 6871c9e8a701426f4427f70c8f23b4b9d571ae7e.
Read snapshots: GLOBAL_KNOWLEDGE_V1 main 80c0cae04e82d3e6c361c93c02f5f76aaf881d3e; Enterprise Math main 3500956641ee0b1a0b7d966ad390ae29424988e4.
Scope: external positive-weight finite-permutation BRC; not native Heartbeat physics or formally admitted science.

Let d=#a-#b range over integers; both a(+1) and b(-1) are always allowed. A finite vector P(d) of binary source guards controls individually testable terminal probes z_i. A legal probe yields positive-rational branches, an illegal probe yields the empty histogram. Define d~e iff P(d+k)=P(e+k) for EVERY k in Z.

THEOREM 45.1: The set of shifts r preserving every P(d) is a subgroup of Z; hence it is either {0} or pZ. The minimum deterministic updateable source-monitor size is infinite in the former case and exactly p in the latter, implemented by d modulo p. Proof: the future a/b word realizes any shift k, and z_i distinguishes states whenever guard outputs differ; congruent residue states have identical future permissions by induction.

COUNTEREXAMPLE: The integer half-line d>=0 has constant (period-one) left and right tails, but no global nonzero period. For d<e, shift by -e before probing: from e the probe is permitted at 0; from d it is forbidden at d-e<0. Thus all integers have distinct future profiles. The set of even integers EXCEPT zero similarly has both tails period two but no global period.

THEOREM 45.2: Suppose each guard P_i has proven left and right eventual periods k_i^- and k_i^+ outside integer thresholds A_i<B_i. Put L=lcm(all k_i^-,k_i^+), A=min A_i, B=max B_i. Finite memory exists exactly when P(d)=P(d+L) for every integer d from A-L+1 through B-1. Outside this finite window the equality follows from certified tails. If any other global period q existed, shifting by multiples of q into the right tails forces L to be global as well; thus failure of this test rules out all possible positive periods. After success the smallest p is the least divisor of L satisfying P(r)=P(r+p) for r=0,...,L-1.

BRC EXAMPLE: a and b carry positive weight 1/2 and effects X=(12), Y=(23) in S6 with XY!=YX. Guard z1 allows two distinct positive 1/3-weight branches iff d is even; guard z2 allows one positive 1/5-weight branch iff 3 divides d. Exact source-monitor minimum is lcm(2,3)=6, keeping integer multiplicity and ordered effects; this is NOT a claim about an unrestricted full BRC state minimum.

LOCAL EXACT CHECK: 518 future-histogram evaluations; 1369 state-pair equivalence checks gave exactly 6 classes; 171 threshold-pair witnesses; joint mod-2/mod-3/mod-4 minimum 12; effects noncommute. Complete proof, checker and JSON certificate are in the local PREFIX45 handoff package. These finite tests do not imply the infinite theorem; the proofs above do.

STATUS: Unreviewed mathematical reference only. Native ControlPacket not run. No authority to claim an existing task; the gateway returned BACKEND_IDENTITY_CHECK_UNAVAILABLE. NEXT: vector-valued arithmetic guards on Z^r, semigroup reachability vs translation stabilizer and finite-index Smith form certificates.