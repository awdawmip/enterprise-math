# Heartbeat43: local complementary formation and retained field memory

Event-ID: brc-heartbeat-local-pairing-memory-20260923-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE / SAME-AUTHOR DERIVATIONS_AND_TESTS / NOT_ADMITTED
Parent standalone: ede275dc51fc44d789322066b5921c81092f2a0f.
Global read: 6f6fa5c297564b213d19a7213c52c8629dda04d1; project control read: a5adf0446747a7f00672bf9f346bf54385f57280.

## Scope

Continue joint native Cell occupancy, complementary residual formation and same-heartbeat infinite response. Do not restore a rigid-length default or prescribed rotation. P000 and the provisional self-consistent-instant definition are unchanged. The new finite local operator and quadratic edge cost are explicit constitutive candidates, not calibrated electromagnetism or native force axioms.

## Exact field-history decomposition

Using Stage42's infinite Green interface, every square-summable admissible field satisfies j=j_*(s)+h, D h=0 and C(j)=C_*(s)+||h||^2/2. Here j_*(s)=D*G s, C_*(s)=s^T G s/2 and C(j)=||j||^2/2. A self-consistent instant need not have h=0; this divergence-free remainder carries history and a specified quadratic cost.

For a local finite-support update k, take j'=j+k and s'=s+Dk. With the orthogonal gradient projection P=D*GD, the exact update is delta j_*=Pk and delta h=(I-P)k. Away from k these two terms cancel exactly, leaving delta j=0. Thus recomputing the minimum-field component produces a noncompact response, but deleting its compensating history would implement a different, nonlocal operation. The user's global-update hypothesis remains separately testable; no universal no-signaling theorem is inferred merely from this example.

For one primitive edge increment k=q*1_e on full Z6, ||Pk||^2=q^2/6, using G00-G01=1/12. The actual local cost from zero is q^2/2, its minimum-field part q^2/12 and its retained history part5q^2/12. This follows from the infinite Fourier projection, not extrapolated finite boxes. A native four-edge square gives the independent exact example Pk=(3,-1,-1,-1)/4, h=(1,1,1,1)/4 and costs3/8,1/8. Seven finite native boxes up to64vertices/192edges were solved with exact rationals, including nonzero1e-8 updates and prior nonminimal histories.

## Conserved source sectors and imperfect large ensembles

Any closed source-conserving unitary preserves the full distribution of Q_total, not only its mean. Independent unbiased signs have P(Q_total=0)=binom(N,N/2)/2^N for evenN, not1. A local rearrangement cannot turn an all-plus/all-minus mixture into an exactly neutral paired state without retaining or exporting the excess.

Stage42's unchanged covariance interface also gives E C_*(s)=q^2*N*G00/2 for unbiased independent signs onNdistinct Cells. Therefore preformed complementary pairs are sufficient but not necessary for extensive expected minimum cost. Every realization may still have nonzero total source and an infinite tail. Zero average source is not zero expected cost.

For independent signs of meanm, E C_*(s)=(q^2*m^2/2)*sum_ij G(zi-zj)+(q^2*(1-m^2)/2)*N*G00. In a dense six-axis cube the first term is at least q^2*m^2*N^(4/3)/192. With linear energy budgetBN, a necessary condition is m^2*N^(1/3)<=192B/q^2; the associated scale varies as |m|^-6. These are conditional ensemble/cost identities, not a real material-size or binding theorem. Actual fields can carry the additional h cost.

## Executed local formation mechanism

Four consecutive native E1 Cells carry two+q and two-q material sources. All six sign configurations are initially equally likely. The three explicit chain link fields are the cumulative charges, off-chain fields are zero, and Gauss compatibility holds in every configuration. This prepared matter-field sector is not the full-Z6 minimum and is not reset to it. The initial state is full rank on the six-dimensional declared invariant sector, not on the entire infinite field Hilbert space.

Four configurations have complementary pairs at(1,2),(3,4), with field costq^2; the unpaired ++-- and --++ configurations have cost3q^2. Initial pair probability is2/3, and every one-site sign mean is zero. Add a finite two-level energy receiver with gap2q^2 and mixed initial populations(1-eta,eta). A local resonant term swaps only the middle materials, changes only the middle link from+/-2q to0, and excites the receiver; its reverse de-excites the receiver. All source constraints and the total bare energy are preserved. No rotation command, postselection, mid-process measurement or reservoir reset is used.

For couplingJ, exact dynamics gives P_pair(t)=2/3+(1-2eta)*sin^2(Jt)/3, hbar1. With eta1/4 a complete exchange gives5/6. The field cost drops5/3->4/3 while receiver energy rises1/2->5/6; total13/6 is unchanged. One-site means remain zero. A maximally mixed receivereta1/2 supplies no improvement; inverted eta reverses it. The process returns to its initial pair probability atpi/J and guarantees P_pair>=19/24 on Jt in[pi/3,2pi/3], not forever.

Full12x12 rational Pade propagation was run at times1 and4 and for detuning1/8, with separately charged continuous probability errors and110-digit full exponential references. For t4,J1/4,eta1/4 the resonant reference pair probability is0.7846789030455952 and the detuned value0.7820622137970102. A rational timing parameter tan(Jt/2)=1+1e-8 leaves an exact nonzero defect from5/6 of -13333333466666667/800000016000000160000000800000002, approximately-1.66666665e-17. This is a modeled control deviation, not a physical measurement or numerical-roundoff claim.

## Size and finite receiver memory

For Mindependent blocks with Mindependent receiverseta1/4, all-paired probability is(5/6)^M, but the probability that at least75percent of blocks are paired is the exact binomial tail with failure rate1/6. M12/60/240/960 give tolerant probabilities about0.87482190732,0.96615380063,0.99962428585,0.9999999999791169. AtM240 the all-perfect probability is only9.91975506e-20. These are exact distribution evaluations, not huge-body simulations. The local paired event is a compatibility diagnostic, not a substitute for actual macroscopic connectivity, mobility or long-time integrity.

For ONE receiver reused across blocks, eta_n=1/2+(eta_0-1/2)/3^n and the nth output's pair probability is2/3+(1-2eta_0)/3^n. With eta_0=1/4 the first two values are5/6 and13/18. Total expected improvement afterMblocks is(1-2eta_0)(1-3^-M)/2, bounded by1/4 ateta_0=1/4. The finite receiver's energy change accounts for this capacity; output histories retain correlations.

An exact two-state receiver carrier computes the paired-count distribution. The all-paired probability with reuse is2(1-eta_0)(2/3)^M+(2eta_0-1)(1/3)^M, not(5/6)^M. Full2/3/4block joint-configuration references with72/432/2592basis cases agree exactly. This quotient is restricted to the specified diagonal input and count observations; arbitrary future coherent probes require the full state.

## Verification and continuation

770main finite assertions passed, including332componentwise cancellation checks and72Cell/link compatibility checks, not770independent experiments. Four110-digit reference records, three independent full-history enumerations, and eight complete result replays passed. Eight frozen cases each have3original timing rows. The inherited Stage19 Mat/partial/pade22 and Stage42 covariance interfaces execute unchanged. All964parent-manifest files match. No original timing is overwritten. Same-author references are not independent researcher review or Lean.

Primary context actually read at official abstract scope: Yang et al.2003.08945v2; Henley0912.4531; Wundt/Jentschura1110.6210v4; Heras1103.2561. Dedicated Issue691/request04a7406c-2bc7-4654-95d9-948a30e12d07 matched comment5782942256: COMPLETED, one metadata/abstract record, oneprovider call, zerobridge-modelcalls; no dedicated full text used. Canonical cache intake pending.

Next: multi-loop local dynamics that transports h and permits mobile material clusters, then compare genuine remote records for local updates against an explicitly global minimum-reset rule with its resource assumptions. No physical instantaneous signaling, material-size calibration, N,a compiler, order extraction, Shor speedup or universal zero-temperature theorem is claimed. Project persistence, Drive delivery and activity aggregate intake remain separate.
