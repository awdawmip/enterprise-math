# Recovered LINE-TRANSPORT-14: line invariants and the joint carried-quantity/path interface

Event: `NS-NATIVE-LINE-TRANSPORT-20260909-D5C00D-14`  
Recovery date: `2026-09-10`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **RECOVERED_PRIOR_EXECUTED_RESULT; summary representation, not an independent re-execution or physical admission.**

This recovers the supplied prior research package, distinct from CAUSAL-RETURN-14. Source-time snapshot was `d40aa672623d6fc82af4cbb60964e6a628267e62`. Its original complete derivation SHA256 is `71d4cef331517c8bdec2b1c9df6947ebfa71c5ce680f18a7b590ebcc72b74cb2`; checker SHA256 `bbba23a20933935f7a42dd219b20f8ff66d7cd563315cd63c105ab67765b55fc`; output SHA256 `f0131bddc075643f1e687c7e98c409a390e5fcce739cd4c11bb7153ffbf90445`. The supplied ZIP retains those full files. This recovery does not claim its checker was rerun in this turn.

## Exact scope and proofs retained

Let a collision output m from integer signed-channel populations n and preserve p_i(z)=n_{i,+}(z)-n_{i,-}(z) at each Cell. Let subsequent streaming be n'_{i,sigma}(z)=m_{i,sigma}(z-sigma e_i). For every i-coordinate line with transverse address y, finite reindexing gives

    L_i(y;n')=sum_s [m_{i,+}(y+(s-1)e_i)-m_{i,-}(y+(s+1)e_i)]
             =sum_s p_i(y+s e_i)=L_i(y;n).

The theorem applies to finite populations, finite deviations from constant backgrounds, and declared periodic boxes. It does not depend on collision arity, density scoring, or a particular incidence palette. The exact native-edge flux is J_i(z)=m_{i,+}(z)+m_{i,-}(z+e_i), giving p_i'(z)-p_i(z)=J_i(z-e_i)-J_i(z). No off-axis p_i flux occurs in this identification.

For a translation-equivariant full rule, an initial full state invariant along e_i remains so, and its entire transverse p_i profile is frozen. The prior actively colliding side-four periodic example kept p_1(z)=(-1)^{z_2} unchanged while executing 2,048 first-step collisions. It differs by L1=4,096 from the explicitly declared transverse-averaging benchmark that annihilates this profile. This rejects that exact readout-preserving diffusion bridge, not all hydrodynamic limits.

For the full local neutral-pair-switch palette plus axial streaming on a d-dimensional periodic box (d>=3), every common time-independent rational linear invariant has coefficients a_{i,sigma}(z)=c+sigma beta_i(z_without_i). The dimension is 1+sum_i product_{j!=i} L_j; for six side-two periods it is193. The prior exact constraint matrix had768 variables and rank575. A more restricted nonlinear rule can have additional invariants.

The original growing perturbation had D_t=2,34,322,1794,7458 through four ticks but zero relative L_i on every line. Growth is real within that invariant sector, not evidence of transverse net-momentum transfer.

## Positive carried-quantity/path interface

For a labelled token alpha retain a carried integer vector q_alpha separately from its actual primitive movement direction. Using the published native two-tick three-token route, a token carrying e1 can move e1 -> e1+e3 -> e3. Define J^sigma_{a;j}(z) by summing the carried a-components on exactly the tokens moving z -> z+sigma e_j. The exact local identity is

    Q'_a(z)-Q_a(z)=sum_{j,sigma}[J^sigma_{a;j}(z-sigma e_j)-J^sigma_{a;j}(z)].

Global carried totals are conserved while line totals need not be. Distinct label/path matchings with equal marginals can give different next fields, so the joint matching must be retained. This is a transport interface, not a proof that q is physical momentum, a force, or a kinetic velocity.

Prior reported checks:354,402 local identities;17,280 router boundary states;103,680 moved native edges;720 transported-coordinate comparisons; clean-directory matching output. These are recovered source results rather than new execution claims. New INTEGER-EXCHANGE-15 extends this interface with a separately declared local load-exchange rule and its own fresh executable evidence. Neither event proves native force admissibility, viscosity, physical f=0, or classical NS, and neither has independent review or a Lean build.
