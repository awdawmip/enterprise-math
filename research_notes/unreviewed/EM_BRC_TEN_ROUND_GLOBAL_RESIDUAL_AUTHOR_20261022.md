# Enterprise Math — Ten-round auxiliary BRC exact residual (author-side, UNREVIEWED)

Date: 2026-10-22. Type: four-label auxiliary positive-branch BRC result, not native X6 dynamics, not accepted Foundation/Result. Source pins: GLOBAL_KNOWLEDGE_V1 56b7790f4d3081c4311acc7a24118cc55176ed2a; Enterprise Math dd31d08d4aeed7c69db45fad7438dcc55a311318. No native CLAIM acquired (control query CONTROL_QUOTA; session-start STATIC_READONLY_SCOPE_DENIED). Original full 13-kB Chinese paper, exact grouped certificates, code and independent raw-history evidence are kept as separate local conversation artifacts until authorized transport.

## Model and observer
U={0,1,2,3}; fixed public protection word p. Protecting 0 gives hidden draws 1,2,3 probabilities (1+z)/3,(1-z)/3,1/3; protecting any other label draws uniformly over the other three, 0<=z<1. The two worlds have first-occurrence weights (10,10,10,10) and (9,1,2,8), failing when the total first exceeds 10. Let G={{0,1},{1,2},{1,3},{2,3}} and delta_t=Pr(occupied hidden labels after t steps lie in G). Then Delta_t=delta_t-delta_(t-1), TV_L=sum_{t=2}^L max(0,Delta_t), R_L=TV_L-max_{0<=t<=L}delta_t. This is time-observer information residual, not a physical residual.

## Exact theorem
Define
Q=2z^4+4z^3+21z^2+z-26;
P=19z^4+18z^3+32z^2-9z-58;
S=2z^6+6z^5+90z^4+50z^3+15z^2-39z-122;
U=29z^6+45z^5+310z^4+105z^3-120z^2-117z-250;
W=2z^8+8z^7+203z^6+203z^5+875z^4+161z^3-637z^2-307z-506;
V=39z^8+84z^7+1008z^6+714z^5+2100z^4+84z^3-2256z^2-753z-1018.

For all real 0<=z<1,
max_{p in U^10} R10(p;z) =
[Q]+/3^5 + [P]+/3^6 + [S]+/3^7 + [U]+/3^8 + [W]+/3^9 + [V]+/3^10,
where [x]+=max(0,x). More precisely,
R10(p;z)=R9(prefix9;z)+1_{p in H10}[V(z)]+/3^10
where H10={0002000000,0000200000,0000020000,0000002000,0000000200,0000000020}.
V has exactly one root nu in (0,1), nu=0.9998561136833222593766415...; epsilon10=nu/3=0.3332853712277740864588805... . For nu<z<1 unique maximizing protection word is 0002000000. The finite-ten-horizon limit as z approaches 1 from below is 728/59049. A fixed ten-word strategy has at most one strict negative-to-positive rebound of Delta_t; thus a second rebound (if it ever exists) requires at least eleven rounds.

## Proof certificate / complete finite coverage
For each occupied subset S of U, put A_t(S;z)=3^t Pr(occupied=S). Start A_0(empty)=1, other entries zero; for each legal next label v != public protection p_t update A_t(S union {v}) += A_(t-1)(S)*c(p_t,v,z), with c=1+z,1-z,1 for protection0 and v=1,2,3, respectively, and c=1 for nonzero protection. N_t=sum_{S in G} A_t(S); B_t=N_t-3N_(t-1)=3^t Delta_t. This is an exact polynomial 16-mask BRC positive-branch pushforward.

Equal complete 16-mask polynomial states at the same t have equal future response under every fixed suffix. Group states with their exact word multiplicities; after nine steps 220 distinct states represent all 262144 prefixes. Appending four possible protected symbols yields exactly 1048576 ten-letter words but only 628 distinct B10 polynomials. For 626 polynomial groups, all degree-10 Bernstein coefficients of -B10 on [0,1] are strictly positive (smallest margin 58). These groups cover 1048566 words, which therefore have strictly negative Delta10 everywhere. The remaining ten words have B10=E10 for all-zero p and B10=V for the nine words containing a unique 2 in positions 1..9 and zero elsewhere, where E10=-1524-4356z^2+3360z^4+2856z^6+180z^8-2z^10.

Exact rational Bernstein certificates give E10<0 on [0,97/100] and Delta2,...,Delta9>0 on [97/100,1] for all-zero p, so it adds no residual; V<0 on [0,4999/5000]. For each single-2 exceptional word, on [4999/5000,1] Delta2,...,Delta9 are positive except (when 2 is at position k>=4) Delta_k is strictly negative. For k=4,...,9 the earlier peak satisfies 3^10(delta_(k-1)-delta_10)>0 on that entire interval by exact Bernstein positivity. Hence if V>0 its entire positive tenth increment adds information residual for exactly those six positions. Using the prior nine-round exact per-word formula yields the displayed ten-round per-word and global results.

V(0)<0,V(1)=2>0 and the descending coefficient signs of V change once, so Descartes + IVT establish its unique positive root. Exact rational bisection bounds this root; W(4999/5000)>0 puts its phase later than the ninth phase. The word 0002000000 realizes previous R9 maximum plus the full new term, proving sharpness. The old nine-round no-second-rebound result plus exceptional signs above excludes a second rebound through ten steps.

## Evidence and limits
The local full evidence consists of certify_ten_grouped.py, ten_grouped_certificate.json, prove_ten_phase.py, ten_phase_certificate.json, independent_ten_raw.py and its outputs, logs and full parent nine-round dependency. 96 exact rational formula checks passed. A separately implemented original-hidden-history first-failure histogram check passed for 9 cases, 358390 nonzero-weight histories. Such cross-check is author-side, not independent Research Driver review. All signs above were decided by exact rational arithmetic, not floating point samples. Mathematical admission, native-X6 correspondence, signed/complex-phase claims, and physical causation remain unproved.

Next: classify the eleventh increment and test whether a second strict negative-to-positive rebound first appears, retaining complete branch-time observation.