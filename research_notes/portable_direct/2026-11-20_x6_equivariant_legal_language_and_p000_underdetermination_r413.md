# X6 r413 — Equivariant continuation-language criterion and a sharp P000 transfer boundary

Date: 2026-11-20 (Asia/Shanghai).
Status: author-side mathematical theorem with an exact finite check; NOT an independent Native Review, Native Result, or a physical X6 rotation law.
Driver contributor for this new proof: EM-DVR-DEBB5E. Original X6 researchers EM-EMF6D046-5A2844, EM-X6-DFD1FD and EM-X6CM-EDBD55 retain their prior work and provenance.
Continuity: r411@5e3d07b05799754cb1b4327e97bb30aaf12f0652, r412@7d98fdd1cd942b978f62674f812da6afee321f03 and original X6 Source-published signed-word classification@9d09f6bc13b36a8d47d11b524fae4dd5254ac333.

## Theorem A: equivariant-language simplification of r412

Let a finite group H act letterwise on a finite primitive alphabet Sigma. Let E be a finite H-set with an **injective H-equivariant fixed-length** encoding c:E -> Sigma^ell, ell>=1. Let L subset E* be a **globally H-invariant** language (gL=L for every g in H); closure under a fixed reference frame, not independent per-event rotations, is required. Fix s in E* with U_s = {u: us in L} nonempty and define O_s(u)=[c(us)]_H. Put K_s={g in H: g c(s)=c(s)}, and E^{K_s}={a in E: g a=a for every g in K_s}.

Then the following are equivalent, with NO regular-language assumption:

(1) O_s is injective on U_s;
(2) every g in K_s fixes every u in U_s;
(3) U_s is contained in (E^{K_s})*.

Proof. Global H-invariance and g s=s for g in K_s imply g U_s=U_s. If u in U_s is moved by g in K_s, then v=g u is a distinct, admissible prefix and c(vs)=g c(us); therefore O_s(u)=O_s(v), contradicting (1). Conversely, if two admissible prefixes u,v give the same orbit, equal block lengths yield a single g in H with g c(us)=c(vs). Comparing the common suffix shows g in K_s. Injectivity and equivariance of c give v=g u. If every event in u is fixed by every g in K_s, v=u, proving (3)->(1). Finally a word is fixed by all K_s if and only if all its letters are fixed by all K_s, proving (2)<->(3). QED.

This is STRICTLY scoped to an H-invariant whole language. For a non-invariant legal language r412's two-track product criterion remains necessary; this result must not be applied by assuming physical event laws are H-equivariant.

### One-track exact decision and witness

If L is regular and recognized by a DFA (Q,E,delta,q0,F), compute F_s={q:delta*(q,s) in F}. Compute E^{K_s} by the actual finite group action. Search the directed graph Q x {0,1}, initial (q0,0), with transition (q,d) --a--> (delta(q,a), d OR [a not in E^{K_s}]). Accept at (q,1) with q in F_s. An accepted path is exactly a legal prefix with a non-fixed event. An accepting path yields g in K_s moving one of its events, so (u,g u) is a concrete collision; no accepted path proves injectivity. A shortest witness has at most 2|Q|-1 event blocks per prefix (shortest simple path in a graph with 2|Q| vertices). Once K_s and E^{K_s} are computed, the DFA search is O(|Q||E|+|Q||s|) time and O(|Q|) state, rather than r412's general O(|K_s||Q|^2|E|) two-track search. Group enumeration and computing fixed events are additional explicit costs, not suppressed.

## Theorem B: two H-equivariant extensions of the *same* triadic candidate input give opposite observer outcomes

Use the **candidate static** H=(C2)^6 semidirect A6 signed-axis action on Sigma={+/-e_1,...,+/-e_6}; |H|=23040. Consider the same finite candidate alphabet E=H.a of all ordered triples of signed primitive axes with three pairwise distinct unsigned indices, with c the identity three-letter representation. Take a=(e1,e2,e3), b=(e4,e2,e3), d=(-e4,e2,e3), and suffix s=a.

Exact finite facts:
- |E|=(6*5*4)*2^3=960.
- K_s pointwise fixes axes 1,2,3; its even permutations of unused axes 4,5,6 (3 choices), with independent flips of those axes (8 choices), give |K_s|=24.
- E^{K_s} contains exactly the 3!*2^3=48 signed ordered triples using axes 1,2,3.
- The sign flip of axis 4 fixes a but interchanges b and d.

Now compare TWO prefix-closed, H-invariant event-time composition laws over the exact SAME E:

* L_repeat = union over e in E of e* (once an event type is chosen, only that exact event can recur; the initial empty state is allowed). Since a is a fixed suffix, U_a=L_repeat/a=a*. All words in U_a use an event fixed by K_a. By Theorem A the observer is injective for all prefix lengths.
* L_free = E* (any event may follow any event). Now U_a=E*. The distinct one-event prefixes b and d satisfy c(ba) and c(da) in the same H-orbit under the single sign flip of axis 4 fixing a; the observer is NOT injective.

Both candidate laws are H-equivariant, prefix-closed and regular, use the same six-axis signed primitive carrier, the same nonzero three-label event alphabet, and an ordered time index. They differ only in lawful continuation. Their exact finite discrepancy therefore persists even under **global frame covariance**. The example can be interpreted as *conditional models* of a yet-unspecified triadic closure relation (equal-quantum events on three mutually Enterprise-orthogonal distinct axes, with native 120-degree PERP_E semantics). It is **not a proof** that each listed triple is legal under the actual, still-open P000 TRIADIC_CLOSURE_E incidence. In particular, a simultaneous force triple is not three sequential Cell displacements, and no physical Cell successor is deduced from c.

Consequence: P000 arity/angle, the signed-axis group, and global frame-equivariance of a candidate triadic event alphabet do NOT determine whether suffix orbit compression is safe. The real triadic incidence AND composition/time/Cell/Port/branch admissibility must be supplied. Claiming a physical X6 observer theorem from either toy law would silently add an unproved native dynamical axiom.

## Native bridge / evidence status

P000 current global-machine blob sha1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc: six-axis Cell world, triadic nonzero closure and native 120-degree perpendicular; actual triadic admissibility is open. Project spatial Cell torsor blob e266c103cae02550c8bbaa794958f3423b41d151 explicitly keeps force/channel/time/Path history separate from Cell identity and leaves triadic incidence/dynamics open. Heartbeat time machine blob 94a02d067be2b039ca4c0f7ffedb5ebde8430e08 does not freeze a heartbeat program. Joint observer preservation blob 3923890d77a02d84b772f789e6912dd14f220d14 forbids dropping composition-relevant distinctions without a typed certificate.

The theorem resolves one precise computational/compositional issue inside r412: if a future valid native event-language model is H-equivariant and finite-state, a single-track algorithm suffices. It neither proves that the actual X6 native law is finite-state nor that the static H action is a physical rotation. Source-published author-side evidence is not a formal Result, Task closure, or an independent review; do not change existing CLAIM, owner, provenance or mother-objective state.

Companion reproducible exact finite check: research_notes/portable_direct/r413_equivariant_x6_language_check.py.
