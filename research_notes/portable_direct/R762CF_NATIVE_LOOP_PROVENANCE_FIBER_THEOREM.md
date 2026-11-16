# R762CF — X6 native-loop provenance fibres and exact finite-horizon BRC repair

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS (frozen science pin a72226e2430ffa4786321ac86e7f0c599d5f0389).
Parents: R762CA–R762CE, especially R762CE at 76028c31cfe8f2f9ed23b6af89e806e4f1c7e593.
Scope: explicit conditional typed Cell/Port/Link dynamics on P000 X6; not a selection of the still-open physical TRIADIC_CLOSURE_E licensing predicate.
Evidence: universal direct proof below and author-side exact Python enumeration q=2..16. Independent review NOT_REVIEWED.

## Statement

For **each integer q >= 2**, there exists an S6-axis-label and C3-rooted-Port covariant candidate triadic Cell/path event system satisfying P000's three-force arity, signed primitive axial steps, equal-quantum PERP_E, separate discrete time, and provenance preservation, such that one fibre of the observer

O = (final signed X6 Cell coordinate relative to a chosen anchor, three signed named Ports, cyclic Links, elapsed primitive-step time, histogram of all signed primitive-axis steps)

contains exactly q reachable states with pairwise distinguishable future event-permission languages. The minimum fixed-width full-future BRC repair information in this fibre is

R(q) = ceil(log2(q)) bits.

When the observation target is the terminal permission for a fixed legal Port replacement after **at most h future completed L-loops**, the exact number of distinguishable phase classes is

K(q,h) = min(q, h+2), h >= 0;

the corresponding minimum fixed-width repair is ceil(log2 K(q,h)) bits.

Consequently the sign-only 12-atom interface of R762CA–R762CE is insufficient to represent **all** signed-X6 Cell/path-dependent covariant event systems compatible with the stated premises. The construction provides a concrete typed enlargement rather than a determination of which native event system is physically selected.

## Precise model (all objects are typed)

Let X be an affine torsor for Z^6, with a *chosen* anchor c and native signed unit displacements ±e_i. Let a state at a completed loop boundary be (c,P,Λ,r,t,H), where:

* P = ((a_1,s_1),(a_2,s_2),(a_3,s_3)) consists of three named nonzero equal-quantum primitive forces, a_i in {1,...,6} pairwise different and s_i in {±1}. The force with Port j is incident from Cell c to c+s_j e_{a_j}.
* Λ is the directed cyclic Link ring 1→2→3→1 (pure relation metadata).
* r in Z/qZ is a path-provenance register, **not** a seventh spatial coordinate.
* t is separately typed primitive-step time; H is the ordered native step path, retained as provenance.
* The equal-quantum triple with three distinct axes is declared TRIADIC_CLOSURE_E=true in this *candidate*. No primitive stable force configuration of arity 1 or 2 is introduced.

For each j (cyclically modulo 3), write u=s_j e_{a_j} and v=s_{j+1} e_{a_{j+1}}. Define two **composite**, four-primitive-step Cell loops:

B_j=(+u,-u,+v,-v); L_j=(+u,+v,-u,-v).

Each returns to the original Cell, has length four, and contributes **identical signed-direction histograms**: one each of u,-u,v,-v. After its complete four-step path, B_j preserves r and L_j changes r to r+1 mod q. Both preserve all three attached force types and cyclic Links, translated with the moving Cell along each primitive step. Their different ordered paths remain present in H; no diagonal segment is promoted to a primitive direction.

For any axis b absent from the current triple, the event T_(j,b) replaces a_j by b (keeping the Port's sign) **iff r=0**. It leaves c, Λ and r unchanged. Such replacement is a relation/force update, not an untyped extra spatial step; the next triad still has distinct axes and equal quantum magnitude. B, L and T define a well-formed deterministic partial labelled transition system. The T-event always has some possible b because three of six axes remain unused.

S6 relabels axes, signed primitive steps and target b, fixing r; C3 cyclically relabels Ports and j, fixing r. The formulas commute with both actions. Their covariance follows directly from the absence of any preferred global axis or Port index. Thus sign-only restrictions are neither required by P000 nor forced by these symmetries.

## Exact same-observation q-fibre

Start with anchor Cell c, P=((1,+),(2,+),(3,+)), r=0 and empty H. Fix j=1. For each r=0,...,q-1 take the history

W_r = B_1^(q-r) L_1^r.

Every history has q completed loops, 4q primitive axial steps, endpoint c, unchanged signed Ports/Links and time t=4q. Its directed signed step histogram records q occurrences **each** of +e_1,-e_1,+e_2,-e_2, with zero other entries. Therefore O(W_r) is literally identical for all r. However the retained provenance register equals r mod q. All q states are reachable and distinct under future T-permission.

For r ≠ s, put k=(-r mod q), 0<=k<=q-1. The future query L_1^k followed by T_(1,4) is legal from phase r and illegal from phase s. Thus the right languages are pairwise distinct. Their minimal sufficient exact all-future quotient has q states by the direct distinguishability argument (equivalently the Myhill–Nerode right-congruence criterion). A q-valued state needs ceil(log2 q) fixed bits; storing r achieves this bound.

Importantly the common signed step histogram, full signed Cell endpoint, elapsed time and the three named signed Ports *together* do not recover r. Ordered paths or an equivalent future-sufficient residual are needed.

## Exact finite-horizon rate

Allow only the terminal Boolean questions Q_k(r) = [L_1^k T_(1,4) is legal], for 0<=k<=h, with loop counts understood modulo q. The answer vector at phase r is true at exactly those k satisfying k ≡ -r (mod q). If 0<=h<=q-2, the h+1 phases hit by k=0,...,h have different nonzero vectors, and the remaining q-h-1 phases all have the all-false vector. There are h+2 classes. If h>=q-1 every phase appears among the probes and all q phases are distinguishable. Therefore K(q,h)=min(q,h+2) for all q>=2, h>=0. Encoding the equivalence-class index achieves the lower bound ceil(log2 K(q,h)).

This is an explicit **future-scope-dependent safe quotient**: the h-truncated observer admits a smaller residual than the unlimited-future observer when h<q-2. The definition of the observer and its time horizon matters, as required by the project joint-relation and BRC contracts.

## Compatibility and exact boundary

This construction leaves the project P000 ontology unchanged: six signed X6 axes with PERP_E/120° defined natively; no native plane; three nonzero equal-quantum signed force branches at each stable event; Cell shifts only through signed single-axis primitive steps; the macroscopic four-step loops are composite paths; time and path provenance are separately typed. Cyclic Links remain named. It deliberately varies the **later event permission** based on a stored loop-order residue, while every candidate triad is closed. In particular, the result does **not** claim this event law is the actual TRIADIC_CLOSURE_E licensing selected by the project.

R762CE proves a sharp 0..6 query budget within one finite sign-only 729-law family. The present theorem identifies a concrete additional Cell/path-provenance degree of freedom that is erased by that interface. Its exact q-parameter family has an unbounded minimum full-future repair size across models, and a finite-horizon repair law within each chosen q.

## Verification and next research

Independent finite assertions check all q=2..16, the common-endpoint/time/histogram q-fibres, every pair of future distinguishing permissions, the finite-horizon formula for h<=q+3, and loop-histogram equality for 720 S6 permutations × 8 sign patterns × 3 cyclic Port pairs. These checks support the universal algebraic proof; they do not replace it.

Next: determine from the actual native Cell/Link/Port semantics which four-step path-order effects are admissible as update guards; derive the actual event-language observer quotient. Independently determine if the V17/V29/V39 signed-Port transport has a path-homomorphism preserving this loop residue or a precise obstruction. Provenance and full source remain intact pending that test.
