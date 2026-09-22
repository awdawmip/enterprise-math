# Heartbeat43B: local loop dynamics, mobile cohesion and conditional readout

Event-ID: heartbeat-formation-readout-20260923-CEA756CC
Research-Activity-ID: RA-CEA756CC3E2849788E9DA07D
Status: RESEARCH_CANDIDATE / SAME_AUTHOR_PROOFS_AND_CHECKS / NOT_ADMITTED.
Global read: 6f6fa5c297564b213d19a7213c52c8629dda04d1.
User task: continue joint Cell occupancy, finite-scale integrity and irreducible residual/global-field research; no primitive fixed length or rigidity.

## Recovery and attribution

Stage42 PROOF.md was read from Library file_000000009818820bbee5747c044c3310/version1. Before publication, original activity's newer Stage43 was read at enterprise-math@f55bd8d2cc53f9c9531da30c5ecc1a9a0aba80bc:research_notes/BRC_HEARTBEAT_LOCAL_PAIRING_MEMORY_20260923_6EF011.md. This is a separate continuation activity, not replacement of that source. The other activity's770checks were not rerun or counted here.

Inherited exact interface: on full native Z6, D is edge divergence, L=DD*, G=L^-1 on finite sources with decaying boundary, P=D*GD. E(j)=||j||^2/2, j=j_*(s)+h, j_*=D*Gs, Dh=0, E=E_*(s)+||h||^2/2. A local edge increment k gives delta j_*=Pk and delta h=(I-P)k; the remote components cancel. This is inherited, not a new theorem claim. Source values q are hypothetical compatibility contributions, not probabilities or calibrated physical charges; all source/material identities and quantum phases remain typed. No P000/worldview change or primitive two-force balance claim.

## New: local dissipative update with the same static endpoint

Let C send each elementary native i/j plaquette to its four oriented edges. DC=0. M=CC* satisfies M+D*D=L_edge, where L_edge applies six-axis L componentwise. Its Fourier symbol has eigenvalues0 and ell(k)=12-2sum_i cos(k_i), so0<=M<=24I.

Choose alpha=1/24 and j_(n+1)=(I-alpha M)j_n. This reads only neighboring plaquette edges, preserves Dj=s and obeys
E(j_(n+1))-E(j_n)=-alpha<j_n,Mj_n>+alpha^2||Mj_n||^2/2 <=-alpha<j_n,Mj_n>/2<=0.
Lost field cost must be booked to a stated receiver/bath. For a single plaquette column c, ||c||^2=4, j'=j-c(c*j)/4 releases exactly(c*j)^2/8 locally. A material move can first add finite k and source Dk, charging work<j,k>+||k||^2/2, before loop relaxation.

With the same past and one local input k, delta j_n=(I-M/24)^n k. If edge-coupling graph distance from support(k) exceeds n, delta j_n is EXACTLY ZERO, hence equal local total-field readouts outside this cone. The noncompact optimum component Pk is still canceled by history there. On infinite Z6 in ell2, Fourier spectral convergence gives(I-M/24)^n j0 -> Pj0=j_*(Dj0), not in a uniform finite number of beats. On a finite torus, harmonic circulation remains: it must NOT be silently deleted. Thus the same Gauss/cost problem admits both global-minimum reset and local finite-support dynamics, with different propagation.

curl_verify.py executed19exact integer checks on a3^6torus:729Cells,4374edges,10935plaquettes; DC=0, Hodge identity, divergence,0..4beat support and decreasing rational energies, plus retained harmonic circulation. The torus checks do not prove the infinite theorem or approximate infinite Green values.

## New: infinite-lattice internal binding threshold

Two distinguishable mobile materials +q,-q, co-occupancy allowed. Candidate eliminated-field potential V(r)=q^2[G0-G(r)], hopping J_A L_x+J_B L_y. At total quasimomentum K=0, subtract the dissociation continuum threshold, let t=J_A+J_B and lambda=q^2/t: h=t(L-lambda M_G).

C2=sum G(x)^2 is finite in six dimensions. Weighted Schur applied to sqrt(G)(L+eps)^-1sqrt(G), weight sqrt(G), has row bound(G*G)(x)<=C2. Therefore <psi,M_G psi><=C2<psi,Lpsi>, ruling out negative binding for lambda C2<=1. Trial psi=G in ell2 gives <G,LG>=G0 and sum G^3>=G0^3, so lambda>1/G0^2 ensures a negative eigenvalue. Since G decays, M_G is compact and the negative state lies below the essential continuum. Hence1/C2<=lambda_c<=1/G0^2; threshold equality and possible embedded states are not classified.

An interval calculation of G0=int p(u)du and C2=int u p(u)du, p=[exp(-2u)I0(2u)]^6, kept all infinite tails. I0 positive series with geometric remainder; monotone Riemann intervals; p(u)<=pi^3/(4096u^3). At T=128, G tail<=pi^3/(8192T^2), C2tail<=pi^3/(4096T).4865dyadic cells,40-digit interval arithmetic yielded outward bounds G0 in(0.09294889825914530,0.09321212064956651), C2 in(0.01048141948988700,0.01059978184423082). Direct margins1-94C2>0.0036205 and116G0^2-1>0.0021817 prove94<lambda_c<116. Not a finite-box fit or exact critical constant.

General K has relative hopping a_i(K)=|J_A+J_B exp(iK_i)|. For equal J and K=(kappa,...), a_i=2J|cos(kappa/2)|. Thus the threshold is K0-specific; do not erase total-motion provenance or claim a universal material threshold. Fixed-K center plane waves are not normalized whole objects; wavepackets must be assembled over a bound-band neighborhood.

## New: from disconnected occupancy to sustained connection

Explicit three-cell trap0,e1,2e1, reflecting boundary, two labeled+q,-q materials. Initial(0,2) is disconnected under d<=1. Energies E0=0,E1=q^2/12,E2=q^2[G0-G(2e1)]>E1. Only one material makes one native step; bath rates w(Y<-X)=kappa min(1,exp[-beta(EY-EX)]). These are explicit effective-model assumptions, not a derived full matter-field quantum dynamics.

Set a=exp(-beta E1),b=exp[-beta(E2-E1)]. Group states E={00,22},M={11},A={01,10,12,21},D={02,20}. Exact lumpability C Q9=Q4 C was checked. Column generator Q4/kappa has rows[-2a,0,1,0];[0,-4a,1,0];[2a,4a,-2-b,2];[0,0,b,-2]. Stationary weights(2,1,4a,2ab)/Z,Z=3+4a+2ab retain multiplicities.

P_connected=(3+4a)/Z; at a=1/99,0<b<1, P_connected>301/303. For the entire stationary window[0,T], failure implies initially D or an A->D entry. Expected entries=4kappa abT/Z, so P(no disconnection)>=max(0,1-2ab(1+2kappa T)/Z)>=max(0,1-(2+4kappa T)/303). At kappa T=1 this is>=99/101. This is a path event, not just sampled-time marginals.

q=kappa=1,beta=12ln99 floating example: P_connected(t4)=0.9895050692204664; P(connected throughout[4,5])=0.9800474998833623; stationary P_connected=0.9958616578875302. Decimals are diagnostics, not certified physical quantities. Infinite-volume finite-beta single-pair Gibbs normalization fails because V approaches a finite constant; finite-trap results do not prove arbitrary-N or infinite-time integrity. A fixed closed Hamiltonian also preserves its bound spectral weight, so bound-state existence is not spontaneous capture.

## New: explicit conservative remote readout, conditional on global elimination

Two neutral devices: s_A(u)=u q_A(delta_e1-delta0), s_B(v)=v q_B(delta_(r e2+e1)-delta_(r e2)). All alternatives preserve total source and distant boundary/preparation. The mixed energy difference is
K_r=q_Aq_B[2G(r e2)-G(r e2-e1)-G(r e2+e1)]
=2q_Aq_B int_0^infty exp(-12u) I_r(2u) I0(2u)^4[I0(2u)-I1(2u)]du>0
for every finite r>=1 and q_Aq_B>0. Integral u is NOT time. A neutral source move also admits a compact one-edge flow: its optimal noncompact response is not a monopole ineliminability proof.

Explicitly choose H_eff=E_A n_A+E_B n_B+K_r n_A n_B with E_A=q_A^2/12,E_B=q_B^2/12. Common past A0,B|+>; local material bit control sets A to u; same evolution exp(-i tau H_eff/hbar); receiver uses a fixed self-energy phase calibration and measures(I-Y)/2. Then p(1|0)=1/2,p(1|1)=[1+sin(K_r tau/hbar)]/2. For q_Aq_B=tau=hbar=1,0<K_r<0.187 so the difference is nonzero at every finite r.

This is an explicitly NONLOCAL effective update, not a proof a local operation in the full matter-field space realizes global dressing. At tau=0 both probabilities are1/2. By contrast the local loop update above retains the cancellation outside its finite beat cone. Physical instantaneous signaling, unique dynamics and real detector calibration remain unproved. The two models are deliberately different candidates, not one silently inconsistent combined model.

K_r->0. For this specific independent Bernoulli readout repeated M times, KL<=4M delta^2, Pinsker and error<=1/3 require M>=1/(18delta^2). Nonzero tails do not imply distance-uniform finite measurement resources. No universal optimal-quantum-metrology bound or fitted asymptotic exponent is claimed.

## Checks, sources and unfinished unit

verify.py57checks plus curl_verify.py19checks =76same-author checks. Infinite results rely on written proofs; interval thresholds and floating diagnostics are separated. The first symbolic stationarity test required algebraic simplification, not changed dynamics. No independent reviewer, Lean, real material data, new Shor or zero-temperature conclusion.

Official external background actually consulted: NIST DLMF10.37(Bessel monotonicity); Dowker arXiv1207.2096(discrete heat kernel abstract); Bravyi/Hastings/Verstraete quant-ph0603121(local propagation abstract); Verstraete/Wolf/Cirac Nature Physics DOI10.1038/nphys1342(dissipative preparation abstract); PRE66,016130/PMID12241449(momentum-dependent lattice binding abstract). These are antecedents/frameworks, not proof of the new physical hypothesis.

Next smallest unit: couple the already-constructed local loop field update to mobile quantum material and an explicit finite receiver, retain full rho and energy/memory, derive rather than assume any effective K_r interaction, and test a growing unconfined cluster's finite-time integrity. Do not redo Stage42 Green/covariance/capacity, inherited43history cancellation, or43Bthreshold/local-loop/three-cell certificates. Local code and the full Chinese derivation are delivered in this conversation's standalone43Bbundle; this note is the minimal faithful EM research checkpoint, not a replacement of the other activity's bundle.
