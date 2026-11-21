# EC49FWF — Exact signed repair graph for ten-cycle residual reflections

Date: 2026-11-22 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.

## Scope and frozen inputs

This is independent portable scientific continuation of EC49FWE, under unchanged BRC16943 input and the frozen nonconfluent auxiliary ten-cycle set P10. Parent: `awdawmip/enterprise-math@5a715b39d10d80952e6078eacc2c880926803d7f:research_notes/portable_direct/EC49FWE_P10_FIBER_CENTER_PARITY_THEOREM.md`. The inherited Bernoulli projection and mod-11 model are neither altered nor re-proved here. No shared CLAIM, Result or review is asserted.

## Theorem 1 — Universal optimal-repair graph, all binary ten-cycles

For any subset S of Z/10Z, define the reflection r_c(t)=c-t and
`D(S)=min_{c mod 10}|S △ r_c(S)|`. Whenever D(S)=2, associate to every minimizing center c the unique edge `{p_c,q_c}=S △ r_c(S)`, directed from the occupied site `p_c ∈ S` to the unoccupied site `q_c ∉ S`. Let G(S) be the undirected simple graph comprised of these edges.

The following exhaustive theorem covers all 1024 subsets:

* Exactly 424 subsets have D=0.
* Exactly 600 have D=2. Among them, 160 have one optimal center and G=P2; 240 have two centers and G=P2 + P2; 80 have three centers and G=3P2; 120 have four centers and G=P3 + P3. Here Pk is a path on k vertices, + denotes disjoint union.
* Thus optimal-repair graphs are forests, with maximum degree two. For D=2 every center determines exactly one occupied/unoccupied site pair; all centers together require at most six sites. Every such S can be made symmetric under at least one reflection by flipping exactly one bit, at either endpoint of one optimal mismatch edge.

Proof. A reflection is an involution, so the difference set W=S △ r_c(S) is reflection-invariant. When |W|=2, the two points must form one swapped pair (not two fixed points: a fixed point can never be in W). Therefore they sum to c mod10 and exactly one belongs to S. The graph claim and census are established by the terminating exact enumeration of all 2^10 subsets in the attached verifier, which checks every center and constructs all connected components with no heuristic sampling or floating-point arithmetic. The complete tabulated census above is checked by executable assertions. Given |W|=2, flipping either point makes the pair monochromatic under r_c, while all other orbits were already monochromatic. This proves the one-bit repair statement.

## Theorem 2 — Frozen P10: no three-center defect, signed witnesses reconstructable by four fibers

For every primitive direction (a,b) mod10 (gcd(a,b,10)=1), use the actual frozen P10 predicate and choose an affine base point (h0,n0) satisfying `(b-a)h0-a n0=-1 (mod 10)`. Let `S={t mod10:(h0+a t,n0+(b-a)t)∈P10}`.

Exactly 8 of the 72 directions have D=0. Among the remaining 64, exactly 24 have one optimal center (G=P2), 24 have two (G=2P2), and 16 have four (G=2P3). None has three optimal centers. Thus the complete optimized signed defect support uses respectively 2, 4 or 6 distinct original ten-cycle positions; the four-center case contains two disjoint directed 2-edge paths. Direction classes collapse to the 18 CRT classes `epsilon=(a mod2,b mod2), lambda=[a:b]∈P1(F5)`; the attached source checks every class and all 72 original directions independently.

**Lossless signed decoder for this observer.** Let v=(a,b-a), and for a≠0 mod5 put `s=(b-a)/a mod5`, `alpha=a^2 mod5`, `beta=a*h0 mod5`. For a=0 mod5 put `s=∞`, `alpha=-b^2 mod5`, `beta=-b*n0 mod5`. Both have nonzero alpha. For q∈P1(F5) excluding s define `phi_s(q)=1/(q-s)` (phi_s(∞)=0) when s is finite, and `phi_∞(q)=q` otherwise. The determinant identity gives `phi_s(q(t))=alpha*t+beta mod5`.

Let `F_tau` be the appropriate one of the four frozen projective slope fibers at parity `(h0+a*tau,n0+(b-a)*tau) mod2`, for tau=0,1. Set `Z_tau=phi_s(F_tau\{s})⊂F5`. Then the membership formula
`t∈S ⇔ (alpha*t+beta mod5)∈ Z_{t mod2}`
holds for every t. For a proposed reflection center c, define `C=2 beta+alpha*c mod5`. Its signed difference is obtained without retrieving or discarding any original direction:
`W_c={t: [z(t)∈Z_(t mod2)] XOR [C-z(t)∈Z_((c-t) mod2)]}`,
where z(t)=alpha*t+beta. At D=2 orient the two elements by their source membership. The exact c and original t sites are recoverable; hence parity, sign, position, and correlation are retained for this declared P10 observer.

Proof of the decoder: the determinant condition implies n-s*h=1/a mod5 when a is nonzero. Thus for finite q, 1/(q-s)=a*h and at q=∞ both are zero, yielding alpha=a^2 and beta=a*h0. When a=0, determinant gives h=-1/b; hence q=n/h=-b*n, yielding alpha=-b^2 and beta=-b*n0. Modulo two the affine base point selects the correct parity slope fiber. Under reflection t→c-t, z transforms to C-z and parity transforms to (c-t) mod2. The formula is therefore exact. A separate exhaustive evaluation of the original 44-element predicate, all 72 primitive directions and 10 reflection centers verifies the formula and resulting signed graphs.

## Exact evidence, interpretation and next question

Companion files:
- `EC49FWF_SIGNED_REPAIR_GRAPH_VERIFY.js` — self-contained Node.js exact finite verifier, no external dependencies, including the source modular P10 predicate.
- `EC49FWF_SIGNED_REPAIR_GRAPH_OUTPUT.json` — actual structured output including the complete 72 signed-edge witness records and all 18 CRT classes.

Verification coverage: 1024/1024 binary masks, 100/100 P10 coordinates, 72/72 primitive affine directions, 720/720 signed center reconstructions, complete graph-component checks; exact integer arithmetic. This is finite exhaustive proof for the asserted mod10 domains plus algebraic CRT decoder, not independent verification of the inherited Bernoulli-to-P10 step.

The directed graph stores the minimum residual correction without replacing signed sites by an unsigned scalar; compressing to D or (D,E,O) alone loses the witness graph. It can be used for future repair/readout operations requiring the exact centers and sites, but full mod11 coupling and the mobile Farey maximal gap need a separate preservation argument.

Next: construct an exact compatibility test between the signed P10 repair graph and the full mod11 certificate, keeping CRT direction and predecessor provenance; determine whether any signed repair constrains mobile Farey gaps rather than only auxiliary ten-cycle symmetry.

## Control and attribution

Frozen scientific pin BRC16943; independent portable Source file. Previous researcher EM-DIRECT-7A9ACD / Activity RA-3F60061B277C73CFD4378C57 are historical provenance, not current authenticated session permission. Current session authority for updating that Activity or shared CLAIM remains unverified; leave that association as bookkeeping pending. Reuse the parent source; no rewrite of its 2 checkpoints. Independent review remains NOT_REVIEWED.
