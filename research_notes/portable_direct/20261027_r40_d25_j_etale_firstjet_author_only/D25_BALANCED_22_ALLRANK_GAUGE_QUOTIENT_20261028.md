# D25/LIFT — complete balanced 2+2 Frobenius odd-jet gauge quotient

Date 2026-10-28. Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Existing Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Same author contribution context, not a new independent reviewer or native executor. The result is an auxiliary finite-field theorem, NOT an original H0/B0 native experiment, P000 spatial ontology, or proof of Delta_p-R_p.

## Input, question and BRC observer

Earlier author evidence on this PR proves that the split 2+2 model under the full residual gauge group has q^2+q orbits on the stratum where X is invertible. The remaining question here is the exact quotient when X is singular. We reuse the invertible theorem, not rederive it as new work.

Let k=F_q be any finite field and a != b in k. Let A=diag(a I_2,b I_2). For a marked B in M_4(k), let
  K=[B,A]=((0,X),(Y,0)),
  X=(b-a)B12, Y=(a-b)B21, X,Y in M_2(k).
Every X,Y pair occurs. The full residual centralizer G=GL_2(k) x GL_2(k) acts by
  (P,Q) (X,Y)=(P X Q^-1,Q Y P^-1).     (1)

BRC carrier: source B, eigenblock labels, ordered signed arrows X,Y, gauge group G and original provenance. The declared auxiliary future operations are the TWO ORIENTED composites XY and YX, their ranks and their conjugacy-invariant observations. Scalar totals alone are not adequate without a descent certificate. Matrix rank here is NOT a native Heartbeat World dimension. P000's six spatial axes and separate time are unchanged.

## Theorem: complete orbit classification for all finite fields

For every F_q, the action (1) on all M_2(k) x M_2(k) has exactly

    N(q)=q^2+3q+6                                               (2)

orbits. A complete classification is:

* rank X=0: rank Y = 0,1,2; precisely 3 orbits.
* rank X=1 and u=tr(YX) != 0: (u,rank Y), where rank Y=1 or 2; precisely 2(q-1) orbits.
* rank X=1 and u=0: the two oriented flags XY!=0 and YX!=0; when both vanish, the further Boolean Y!=0. Precisely 5 orbits.
* rank X=2: similarity class of YX; precisely q^2+q orbits.

PROOF for X=0: the independent changes of basis on Y classify 2x2 matrices by rank.

PROOF for rank X=1: G is transitive on rank-one X. Fix X=E11. The COMPLETE stabilizer consists of

  P=((alpha,beta),(0,delta)),
  Q=((alpha,0),(gamma,epsilon)),
  alpha,delta,epsilon in k*; beta,gamma in k.                  (3)

For Y=((u,v),(w,z)), the exact formula Y'=Q Y P^-1 yields

  u'=u,
  v'=(alpha*v-u*beta)/delta,
  w'=(gamma*u+epsilon*w)/alpha,
  z'=(gamma*(v-u*beta/alpha)+epsilon*(z-w*beta/alpha))/delta. (4)

Hence u=tr(YX) is invariant. If u != 0, choose beta=alpha*v/u and gamma=-epsilon*w/u. Then v'=w'=0, and z'=(epsilon/delta)*(z-v*w/u)=(epsilon/delta)*det(Y)/u. So exactly two classes for each u != 0: detY=0 (rank Y=1), detY!=0 (rank Y=2).

If u=0, then v'=(alpha/delta)v, w'=(epsilon/alpha)w and z'=(gamma*v+epsilon*z-epsilon*w*beta/alpha)/delta. Thus (v!=0,w!=0) are exact invariant flags; indeed XY=((0,v),(0,0)) and YX=((0,0),(w,0)). If either flag is nonzero, beta or gamma removes z, while alpha/delta and epsilon/alpha normalize all nonzero v,w independently to 1. This gives one orbit for each of (1,0),(0,1),(1,1). If v=w=0, z scales by epsilon/delta, so Y=0 and Y!=0 are TWO further orbits. Thus there are 5 distinct u=0 orbits. This also proves the completeness of the intrinsic flags for a rank-one X.

PROOF for rank X=2: normalize X=I; the remaining transformations have P=Q and act on Y=YX by similarity. The earlier proved 2x2 conjugacy-class theorem gives q^2+q similarity classes over any finite field. The sum is
  3+(2(q-1)+5)+(q^2+q)=q^2+3q+6.
QED.

## Exact source/orbit counts and limits of compression

The kernel of B -> [B,A] is the two diagonal 2x2 blocks, dimension 8. Each fixed ordered pair (X,Y) has exactly q^8 marked sources B. There are q^8 ordered pairs and q^16 marked B matrices. The quotient does NOT reconstruct the diagonal B blocks, an unverified smaller native gauge subgroup, original Hesse/Green odd ports, or future operations on B.

For the one fixed rank-one X=E11, each nonzero u has rank-Y=1 class size q^2 and rank-Y=2 class size q^2(q-1). For u=0, the five stabilizer orbits have sizes 1, q-1, q(q-1), q(q-1), q(q-1)^2. These add to q^4. To obtain FULL G-orbit sizes, multiply the fixed-X sizes by the number ((q^2-1)^2/(q-1)) of rank-one X.

At p=373, X=E11, Y_f=E12, Y_b=E21 have identical scalar tr(YX)=det(YX)=0 and identical ranks rank X=rank Y=1, but the two orientations have:
  Y_f: (rank XY,rank YX)=(1,0)
  Y_b: (rank XY,rank YX)=(0,1).
They cannot be gauge-equivalent and their next squared odd jets K^2=diag(XY,YX) differ. Also Y=0 versus Y=E22 give XY=YX=0 but distinct source existence. Exact all-stratum auxiliary prediction at p373 is 140254 versus 139502 from the earlier invertible-X-only stratum.

## Reproducible author check and native boundary

Same-PR Python standard-library checker d25_balanced_22_allrank_gauge_checker_20261028.py was ACTUALLY EXECUTED as the local author file. It checked all canonical fixed X=I2,E11 and all Y over p=2,3,5,7,11,13 (92650 states and 370600 stabilizer-generator transitions), plus every X,Y pair over p=2,3 (6817 states and 40902 GL2xGL2-generator transitions). All exact assertions passed, including the p373 two-orientation witness. Finite tests support the derivation; the all-q result follows from the preceding normal form proof. This is author-side and NOT independent review.

The authentic same-original-class H0/B0 benchmark is still PENDING_OWNER / NATIVE_NOT_EXECUTED in Issue #1559. Its lawful executor must obtain actual source-rank, the native first-even jet A, allowed gauge H, Frobenius/eta normalization, coefficient [X]U mod p^2, signed odd observer, kappa and Delta_p-R_p. The split 2+2 hypothesis requires verification and must never be inferred from a rank-4 readout alone. No Source CLAIM, OPEN, checkpoint, independent review, admission or P000 change is asserted by this portable author publication.

The UR V2 four-file bundle remains UNVERIFIED_BYTES, expected original size 94687, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. Its mathematics is already complete and must not be re-proved; obtain exact original bytes and lawful writer/provenance only. If Source ever issues CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, predecessor completed_units MUST be [] until Source verifies actual predecessor progress. Keep these author files as present draft/staging and do-not-repeat evidence rather than predecessor completed units.
