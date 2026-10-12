# PREFIX-44 | Exact finite-guard criterion and unbounded-source BRC obstruction

**Status:** mathematical auxiliary-model proof and exact rational reference checks; UNREVIEWED / NOT ADMITTED; no formal CLAIM or native ControlPacket pass. Project activity: RA-44FB80BA103A99F3C2B6F9A6, locally allocated Researcher-ID EM-DIRECT-97BE84. GitHub identity does not confer a native Researcher execution session.

**Frozen reads:** GLOBAL_KNOWLEDGE_V1 main 7ed5158a117d13a0093e75588d8f26dd06ba61d3 (P000 projection verified against original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview and BRC policy); Enterprise Math main 8bcc273b2c1370217f69872b10474adeb8456457 (portable protocol, activity policy, typed positive BRC substrate, finite predictive quotient sources). Continues unreviewed PREFIX-43, without treating that draft as admitted. This work concerns an external six-position permutation *auxiliary BRC*, not native Heartbeat six-axis geometry, physical force, or a complete three-dimensional slice.

## 1. Sufficient and necessary criterion for a finite provenance guard

Let Sigma be a finite raw-source alphabet and P=(P_1,...,P_t) a finite vector of binary predicates on full ordered histories Sigma*. These decide guarded edge eligibility in a finite-base-control BRC. An updateable guard register is a finite-state map g(h) with g(hc)=u_c(g(h)) and P(h) determined by g(h). Define the future-right congruence

    h ~ k  iff  P(hw)=P(kw) for EVERY raw-source continuation w in Sigma*.

**Theorem 44.1.** Such a deterministic finite monitor exists if and only if ~ has finite index; the minimum number of reachable monitor values is the number of right-congruence classes.

Proof. If two histories reach the same finite register state, deterministic updates give equal future P outputs, hence they are ~ equivalent, implying at least index(~) register values. Conversely right-invariance permits transition [h] --c--> [hc] on the quotient Sigma*/~, with current output P(h) well-defined (w=empty). This yields a monitor of exactly index(~) states. QED.

This is a typed application of the classical Myhill–Nerode theorem, NOT a newly invented automata theorem. When its hypotheses hold, augment each *individual positive path branch* by the finite register and compose the existing PREFIX-43 finite S×G×M Laurent observer. Never average/recoalesce different hidden guard values without the separately proved future-observer quotient. Finite output alphabet alone does NOT imply finite index, nor is there a blanket algorithm for arbitrary program-defined P. Source reference: https://doi.org/10.1016/j.jlamp.2018.03.002 ; see also Vaandrager–Midya, arXiv:2007.03540 for related register-automata provenance.

## 2. Constructive exact positive-weight noncommutative counterexample

Base port U permits operations a and b, each a single positive rational branch of weight 1/2 returning to U, both emitting public source class r and internal distinct raw tags a,b. Their effects are X=(12) for a and Y=(23) for b in S_6, composing on the LEFT. X Y != Y X. The hidden source counter is Delta(h)=#a(h)-#b(h), updated +1/-1. Terminal operation z is enabled at U if and only if Delta=0; it emits two *distinct* positive branches, each weight 1/3 and identity effect, to terminal port T. Their distinct internal identities are retained; the declared projected joint histogram merges their otherwise identical public terminal atom with positive INTEGER multiplicity 2. All other forbidden operations have empty histogram, not zero-weight edges. Future outputs retain exact rational weight, full S_6 accumulated effect, public emitted sequence, optionally original target-port sequence, and integer multiplicity. Original full raw history is retained separately if demanded by that stronger observer.

**Theorem 44.2 (fixed-current-carrier obstruction).** No fixed finite updateable guard can preserve all future operation-dependent histograms in this model, EVEN WHEN it may also inspect the exact current total prefix weight, full S_6 effect, base port, public label history, and any preselected fixed-length suffix of raw tags.

Proof. Fix suffix length d and choose N>=ceil(d/2). For n=0,...,N-ceil(d/2), take

    u_n = a^(2n) b^(2(N-n)).

Every u_n has length 2N, prefix weight 2^(-2N), accumulated effect I since even powers of X,Y are I, port U, the same public source string r^(2N), and the same raw suffix b^d. But their hidden counters Delta_n=4n-2N differ. For each n, the common challenger w_n is a^(-Delta_n)z when Delta_n<0 or b^(Delta_n)z otherwise. After u_n w_n, the projected histogram has one atom of weight 2^(-2N-|Delta_n|)/3 and multiplicity 2, with ordered effect determined by w_n. After u_j w_n for ANY j!=n the histogram is EMPTY, as terminal z is forbidden. All compared histories have identical prior current q/effect/port/declared finite suffix; along each challenger the same operations are applied. Thus a fixed observable fiber contains N-ceil(d/2)+1 mutually distinct future profiles, arbitrarily large. No finite guard exists. QED.

An unbounded integer counter is sufficient but is not a finite monitor. An external system that keeps the entire raw action log has simply retained the unbounded information elsewhere; this does not establish a finite-state reduction.

## 3. Exact memory vs future-horizon law

**Theorem 44.3.** Fix H>=1 and compare the future-only exact projected positive-path BRC response of abstract counter states Delta in Z for all operation words over {a,b,z} of length at most H. Exactly 2H equivalence classes occur: 2H-1 individual values Delta=-(H-1),...,H-1, and one joint overflow class consisting of every |Delta|>=H.

Proof. A z event is reachable within H operations iff |Delta|<=H-1, by first balancing Delta with a/b moves. Each such inside Delta is uniquely separated from every other value by its own balancing word followed by z, of length |Delta|+1<=H. Outside values cannot reach z, and the outputs of all a/b-only words do not depend on Delta. Therefore all outside values form one class. QED.

For this residual-only observer the minimum profile coding budget is ceil(log2(2H)) bits, not a fixed H-independent finite register. A horizon-countdown monitor may be formed with an overflow marker and a remaining-step-dependent clip; this does not prove perpetual finite memory. This 2H count does NOT claim that the full reachable BRC has only 2H control states or that every fixed q/effect fiber realizes all Delta values.

**Theorem 44.4 (genuine finite alternative, different model).** If z instead requires Delta=0 mod k for a specified k>=1, an exact all-future guard is Delta mod k, with transitions +/-1 mod k, and the guard-only minimal index is exactly k: each residue r is singled out by the suffix b^r z. This MODIFIES the eligibility rule and cannot be used to erase the residual of the original exact equality guard. If z is entirely outside the permitted future operation scope, the counter guard is invisible for that scope only; including z restores the obstruction.

Adding raw source identity or original target address to the observer may refine future equivalence but cannot make exact equality eligibility regular. Streaming raw-source outputs differs from rebuilding an entire old raw log from a finite register.

## 4. Exact reference certificate and reuse boundaries

The portable checker runs an explicit positive BRC interpreter using Fraction weights, Counter integer multiplicity and S_6 tuples (X,Y do not commute) and an independently derived formula evaluator. Completed reference checks:

- H=1..7 exact future profile class counts: 2, 4, 6, 8, 10, 12, 14.
- 108179 exact comparisons of independently coded formula against BRC interpreter for all words of length <=H and all tested starting counter values.
- 121 fixed-fiber exact pairwise distinguishing certificates for (N,d)=(6,0),(7,4),(8,4),(11,8),(13,10).
- Modulo-k guard profile tests for k=1..8, including explicit suffixes of maximum length k.
- Genuine noncommutation; two positive z branches preserved as integer multiplicity 2.

Unbounded-future results rely on the supplied induction/right-congruence proofs; no limited run is silently promoted to an infinity-scale theorem. REUSE_APPLIED: native weighted BRC typed histogram and existing predictive partition laws; COMPOSE_APPLIED: PREFIX-43 guarded observer *only conditional on finite G*; EXTEND_EXISTING_TOOL: this source-guard regularity/bounded-horizon specialization. Native ControlPacket remains NOT_EXECUTED; no native six-axis physical bridge.

## 5. Actual authority, persistence and continuation

The configured Sites bridge reports backend not live-verified and read-only scopes. The authenticated native em_status call returned BACKEND_IDENTITY_CHECK_UNAVAILABLE and operation_sent=false. Hence active owner/CLAIM cannot be authoritatively checked and NO task takeover or native Result is asserted. The independent research activity record is bookkeeping only, not review or admission. This document is an unreviewed GitHub research draft.

**Next PREFIX-45:** characterize arithmetic source guards with an effective finite-index certificate (e.g. eventually periodic counter sets), combine competing predicates without losing per-branch correlation, and investigate deterministic-monitor minimization versus weighted-BRC trace minimization. First native ControlPacket code/schema audit remains outstanding; repeat neither the PREFIX-43 finite-state proof nor these completed fixed-fiber certificates.
