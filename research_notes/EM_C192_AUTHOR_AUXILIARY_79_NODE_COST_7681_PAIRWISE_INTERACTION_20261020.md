# C192 auxiliary 79-node rational interpolation — author research draft

Status: AUTHOR_CONDITIONAL_EXACT / NO_FORMAL_CLAIM / NOT_DRIVER_REVIEWED / NOT_ADMITTED.

Frozen read authority: GLOBAL_KNOWLEDGE_V1 main@361de014f64b10384acaccca0d3773362e951d43, Enterprise Math main@7a3e6ac9517ec758653b681efa557ee9099abfaa; P000 remains ACTIVE_LOCKED.

Parent: C191 author-proven local package. Model: u_j in [0,1] 79 reduced rational nodes, t(u)=1-(u²-2)(u²-3)/12, eta(u)=(17/50000)t(u). Cost is the sum of numerator/denominator bit_length over (u,t,eta). The new five replacements by zero-based index are 4: 1/153 ->1/136 (+4 saved bits); 10: 1/25 ->1/26 (0); 37: 5/11 ->4/9 (+9); 42: 6/11 ->5/9 (-6); 52:14/19 ->17/23 (-5). Recomputed exactly, coordinate cost C191=7683 -> C192=7681.

With the declared C168/H168 auxiliary interpolation kernel (not native C102 GF(2)-BRC), let M(u)=(u²-2)(u²-3), L_j(z)=prod_{k != j}(z-u_k)/(u_j-u_k), K(z)=6912/(17/50000)^2 sum_j |L_j(z)|/M(u_j)^3. Both an integer square-root bracket checker (T=10^25) and a direct Fraction checker (T=10^14) confirm 2^165<K(sqrt2)<2^166, 2^203<K(sqrt3)<2^204, 2^185<10^6 K(sqrt2)<2^186, 2^223<10^6 K(sqrt3)<2^224. Hence sufficient joint measurement precisions remain 204/224 bits.

New unconditional algebra theorem: For arbitrary legal simultaneous replacements I of distinct nodes and z>1, define W_k(S,z)=|L_k^S(z)|/M(u_k)^3 and chi_ij=|v_i-u_j||v_j-u_i|/(|v_i-v_j||u_i-u_j|). Then

W_k(S^I,z)/W_k(S,z) = [prod_{i in I} W_k(S^{i},z)/W_k(S,z)] [prod_{i<j, {i,j} subset I, k in {i,j}} chi_ij].

Proof: log W_k(S,z)=-3 log M(u_k) + sum_{l != k}[log(z-u_l)-log|u_k-u_l|]; each summand involves at most two Boolean replacement switches, so all order>=3 mixed differences of log W_k vanish. C191 pairwise cross-ratio gives the only nonzero mixed terms. This concerns individual log W_k, NOT log(sum W_k), which can have higher interactions. An exact five-node Fraction example checks all 20 pair/triple mask-weight identities.

Global optimality, native correspondence, live owner/CLAIM, independent Driver review, and Source mathematical admission remain unestablished. The complete full proof, 79-node JSON, two proof scripts and replay evidence are in the current conversation attachment; these are not represented by this compact source draft alone.