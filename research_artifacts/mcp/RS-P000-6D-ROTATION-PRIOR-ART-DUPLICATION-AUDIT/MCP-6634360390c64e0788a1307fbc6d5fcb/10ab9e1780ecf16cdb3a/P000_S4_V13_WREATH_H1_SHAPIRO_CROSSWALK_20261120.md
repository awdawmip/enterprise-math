# P000 S4 V13: exterior H1/Shapiro crosswalk for wreath-product sections (2026-11-20)
Task RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT / TP2-2F8C6A1D9E7043B5C812.
Author-side contribution EM-X6-C7A253, not independent Driver review. Preserve previous V7/Gen12, Gen13 and original Nov17 V8 audit contributors EM-P0006DPA8-71C4E2, EM-EMF6D046-5A2844. No P000 root/Foundation mutation.

## Previously verified original science
The accepted Gen13 Research Return `research_returns/P000_S4_LIFT_UNIVERSALITY_EXTENSION_V13_RETURN_20260830.md` and its independent Driver review were read at Source `056d076ec10143ab29c162f4248365ff61414d0f`. They already establish 16 homomorphic sections and two C2^4-conjugacy orbits of size 8 in a declared eight-opaque-Cell K_(2,2,2,2) model, plus distinct nonsplit GL(2,3), no-lift P4 cases. The existing author-side Nov17 V8 prior-art map and 48-element central nonsplit example are at `b29cadc5dd6eca7b76723b27eaefafaeaf42aa8d`. This note derives the **external classical explanation** of one previously counted combinatorial feature; do not reassign prior results to this author.

## Conditional proposition with complete proof
Let G=S4 act on X={1,2,3,4}, and A=F2^X carry its natural permutation-module action (g·v)(i)=v(g^-1 i). Let W=A⋊G, with q:W→G the natural quotient. Then there are exactly 16 homomorphic sections s of q, partitioned by conjugation by the kernel A into precisely 2 orbits, each of cardinality 8.

Proof:
(1) Each section uniquely has s_f(g)=(f(g),g), and group multiplication shows s_f is a homomorphism exactly when f(gh)=f(g)+g·f(h). Thus sections biject with Z^1(G,A).
(2) Kernel conjugation by (v,e) sends f to f+δv with δv(g)=v-g·v, so orbits correspond to H^1(G,A).
(3) Let H=Stab_G(1)≅S3. As a permutation module A is CoInd_H^G(F2) from the trivial H-module F2, because G/H corresponds to X. Shapiro's lemma gives H^1(G,A)≅H^1(H,F2)≅Hom(S3,F2)≅F2. Hence exactly 2 cohomology classes.
(4) The coboundary map δ:A→Z^1(G,A) has kernel A^G, the two constant functions on the transitive G-set, hence |B^1|=|A|/|A^G|=16/2=8. Every H^1 class consists of 8 cocycles, so |Z^1|=2×8=16 and both kernel-conjugacy orbits have size 8.
(5) Representatives are f0(g)=0 and f1(g)=parity(g)·(1,1,1,1); these are cocycles since parity is an additive homomorphism and the constant vector is G-invariant. f1 cannot be δv: take any odd transposition h∈H, which fixes coordinate 1; δv(h)(1)=0 while f1(h)(1)=1.

Independent exact finite calculation in this research conversation enumerated all 256 pairs of generator lifts for a=(BCD), b=(AB), checked a^3=b^2=(ab)^4=1 in the semidirect product, found exactly 16 passing pairs and two A-conjugacy orbits of size 8 and 8. This verifies the finite declared model, not a native Full-Cell/PF-10 implementation.

## Audit impact and prior-art map
- V8 items 2/6: homomorphic complements and their kernel conjugacy in the split abelian permutation-kernel model are an EXACT_DUPLICATE of classical H^1/cocycle theory. The previously enumerated 16/2/8 counts now have a source-specific structural explanation.
- V8 item 4: this use of H^1 for sections of a **fixed split extension** does not replace the H^2 classification of abelian-kernel extension classes; for arbitrary nonabelian kernels retain Schreier outer-action/obstruction theory.
- V8 item 10: two cohomology classes do not establish canonicality. Gen13's preserved centralizer certificate C_W(A)=A separately proves no section fixed by all primitive-preserving kernel conjugations.
- V8 item 12: the external group model is only the algebraic symmetry skeleton. Actual distinct opaque Cells and their native relations, axis typing, Full-Cell PF-10 and no-quotient requirements remain project-specific typed data. Neither carrier labels nor hidden kernel can be identified with or discarded from native Cell identity without a separate theorem.

## Primary mathematical source
Romyar Sharifi, *Group and Galois Cohomology*, Chapter 1 §1.5, Definition 1.5.1 and Theorem 1.5.3 (Shapiro's lemma): https://math.ucla.edu/~sharifi/notes/groupcoh-ch01.html .
The application here specifies H=S3, G=S4, coefficient F2 with trivial H-action and the coinduced permutation module A=F2^4.
Reference for the earlier Gen13 proof and author's original accepted findings: original GitHub Source files above (read on 2026-11-20). Historical Nov17 source must retain original author attribution.

Remaining: Source-specific citation ledger refinement and independent Driver mathematical review; this author-side note does not assert all V8 external classifications novel. NO_MATERIAL_MATCH != NOVELTY.
