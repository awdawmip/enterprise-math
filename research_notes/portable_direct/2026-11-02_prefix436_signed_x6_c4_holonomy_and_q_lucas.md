# PREFIX-436 — Signed-X6 phase-path BRC, exact holonomy, and all-scale cancellation

2026-11-02. Author-side exact algebraic result; finite exact checks; portable direct; **UNREVIEWED / NOT_ADMITTED / NATIVE_CLAIM_ABSENT**.

## Scope and pinned inputs

Continues PREFIX-435 (Git commit d8a16a34b6188eff944d521ab622a303c43d75ee). Task scientific input remains frozen at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Current P000 is the six-axis signed Cell torsor with ordered native primitive steps and a separately typed time. The calculations here use the **full X6 step alphabet**. The displayed two-component restrictions are partial formulas, not a separate two-dimensional native plane or a complete three-dimensional research slice. The auxiliary phase tag is not a seventh spatial coordinate or physical heartbeat time.

Typed BRC sources read: experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py, Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176; src/enterprise_math/brc_transport.py; src/enterprise_math/brc_control_port.py; definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md. The first provides exact positive signed-X6 shortest path counts/weights; the others retain different typed effect/provenance capabilities. PREFIX-435 supplied a finite C4 path semiring but **not** a positional X6 phase-update law.

## Theorem A: explicit signed edge-update and nontrivial central extension

Choose a chart relative to a Cell, x=(x1,...,x6) in Z^6. Introduce an **auxiliary candidate** tag group C4=Z/4Z. For an edge beginning at x, let theta(x,+e2)=x1 mod 4 and theta(x,-e2)=-x1 mod 4; let theta(x,±ej)=0 for j!=2. Every edge is one legal signed native X6 primitive step, but the newly attached tag is an added model rule, not a measured or previously released native law.

For an ordered path w, sum the edge tags using the actual intermediate Cells to obtain tau_x(w) in C4. Then tau_x(pq)=tau_x(p)+tau_(x+d(p))(q), and any edge immediately followed by its inverse contributes zero. Fix a normal word T_d for each displacement d in Z^6 that moves along e2 before e1 and uses any fixed ordering for the other axes. Its phase is tau_x(T_d)=x1*d2 (mod 4), also for signed d. Define nu(w)=tau_x(w)-x1*d2. It is independent of the starting x1, since changing x1 by c shifts the total tag by c times the signed net count d2.

For concatenable p of displacement d and q of displacement e,

  nu(pq)=nu(p)+nu(q)+d1*e2 (mod 4).

Hence the multiplication (d,t)*(e,s)=(d+e,t+s+d1*e2 mod 4) defines an associative central extension Z^6 x_c C4. Associativity follows because d1*e2+(d1+e1)*f2=e1*f2+d1*(e2+f2); the inverse of (d,t) is (-d,-t+d1*d2). The group commutator tag is d1*e2-e1*d2. In particular c(e1,e2)=1 and c(e2,e1)=0, so the extension is noncommutative; it cannot be reduced to a displacement-only scalar character by a gauge potential, because a coboundary on the abelian Z^6 translation group is symmetric.

The oriented native-step plaquette (+e1,+e2,-e1,-e2) returns to its Cell with **auxiliary** tag 1, i.e. i, and the reverse plaquette has tag 3, i.e. -i. Endpoint equality does not imply phase-state equality for this proposed extension. This is a mathematical connection/holonomy construction, not an established P000 physical phase.

**Chart lemma.** Under a chart translation by c, the old e2 phase becomes x1'+c1 while the new rule is x1'. Their difference is the edge derivative of phi(x')=c1*x2'. Therefore paths with the same start/end acquire the same endpoint factor i^(phi(end)-phi(start)), and their *coherent intensity* is chart-independent. The raw tag itself is chart/gauge dependent.

## Theorem B: closed exact coherent sum over every positive shortest-path shuffle

Fix a,b>=0 and consider the signed-X6 native shortest-path family of a positive e1 steps and b positive e2 steps, keeping the other X6 components unchanged. The existing signed BRC counts B(a,b)=binom(a+b,a) ordered witnesses.

For an ordered shuffle w let N(w) count pairs of an e1 step preceding an e2 step. The proposed tag sum is b*x1+N(w) modulo 4. Thus E_x(a,b)=i^(b*x1)*F(a,b), with F(a,b)=sum_w i^N(w) and candidate intensity I(a,b)=|F(a,b)|^2. No floating-point phase approximation appears.

**Exact all-scale formula.** Write n=a+b=4N+r and a=4K+s with 0<=r,s<4. Then F=0 when s>r. Otherwise F=binom(N,K)*g(r,s), where g(2,1)=1+i; g(3,1)=g(3,2)=i; all other entries with 0<=s<=r<=3 equal 1. Therefore I=0 when s>r; I=2*binom(N,K)^2 for (r,s)=(2,1); I=binom(N,K)^2 in the remaining nonzero cases.

**Complete proof.** For an indeterminate q form P_n(t)=product_(j=0)^(n-1)(1+q^j*t). Choosing the a positions of the e1 steps gives

  [t^a]P_n=q^(a*(a-1)/2) * sum_w q^N(w).

Indeed subtracting a*(a-1)/2 from the sum of chosen position indices counts e2 steps before e1 steps, and reversing words bijects this statistic with N(w). This is a polynomial identity over Z[q,t], so no division at roots of unity is needed. At q=i, each four-factor block is (1+t)(1+i*t)(1-t)(1-i*t)=1-t^4. Therefore P_(4N+r)=(1-t^4)^N P_r. For a=4K+s, the target coefficient is zero when s>r, or (-1)^K*binom(N,K)*[t^s]P_r otherwise. Since

  i^((a*(a-1)-s*(s-1))/2)=i^(8K^2+4Ks-2K)=(-1)^K,

division by the prefactor exactly cancels the block sign. Expansion of P_0,...,P_3 yields the displayed g table. QED for **all** a,b>=0.

This proves an infinite, exact *auxiliary-model* cancellation family: whenever a+b is divisible by 4 but a is not, I(a,b)=0 while positive native B(a,b)>0.

At x1=0: (a,b)=(1,1) has B=2, histogram (1,1,0,0), E=1+i, I=2; (1,3) has B=4, histogram (1,1,1,1), E=0, I=0; (2,2) has B=6, histogram (2,1,2,1), E=0, I=0; (4,4) has B=70, histogram (20,16,18,16), E=2, I=4; (5,7) has B=792, histogram (198,198,198,198), E=0, I=0.

## Theorem C: two precisely scoped obstructions

**Flat-step scalar obstruction.** If each primitive displacement is assigned a position-independent, commuting unit phase, every shuffle with fixed endpoints has the same phase. Hence its intensity is B(a,b)^2. For (1,3) this equals 16, whereas the position-dependent candidate above gives zero. This rules out the **flat scalar translation-character class** as an implementation of this particular nonflat coherent observer. It does not rule out native phase state, ordered-path memory or a noncommuting native operator.

**Strict rotation-symmetry obstruction.** Let an S6 axis-permutation action preserve the C4 center *pointwise* on a candidate central extension. Its commutator B(ei,ej) must be invariant under swapping axes i,j. Antisymmetry also gives B(ej,ei)=-B(ei,ej). Thus 2B(ei,ej)=0 mod 4: odd quarter-turn flux 1 or 3 is incompatible with this **extra strict equivariance** hypothesis. P000's permutation skeleton does not by itself impose an action on a new phase carrier. Nontrivial center action, orientation data and symmetry breaking remain live alternatives.

## Exact BRC observer and evidence scope

For each same-endpoint family store (Cell x, histogram h0..h3 in N^4). Alternatives add histograms. Appending a legal signed primitive edge shifts tag bins by theta(x,edge) and updates the native Cell. The declared coherent readout is E=(h0-h2)+i(h1-h3), I=|E|^2. This is an exact typed **candidate C4 BRC sidecar**, not an implementation already in the released BRC control port. It preserves counts and phase under any finite sequence of these specified edge updates and alternative merges. The quotient is not safe for future observers asking for original path-order provenance, nonlocal history, or arbitrary complex Port couplings; PATH_FORMAL_BRC must then be retained.

The checked executable prefix436_remote_reproducer.py calls the **actual current signed_brc.py** through a byte-identical source copy, verifies the original Git blob, and computes the separate auxiliary C4 DP by integer histogram shifts. Executed output in PREFIX436_REMOTE_EXECUTION.log: 961 exact input pairs (0<=a,b<=30) matched signed BRC count and the root-of-unity formula; 198 exhaustive finite word enumerations (a+b<=10, three starts); positive weight cross-checks; and 15,625 signed cocycle associativity triples; PASS. A longer local author checker also checked primitive inverses, plaquette orientations and gauge changes. These finite checks supplement, **not substitute for**, the algebraic proofs. No pi/trigonometry/ordinary propagator or physical heartbeat was executed.

**Typed reuse:** REUSE_EXECUTED (source-verified signed-X6 BRC count and unit-weight positive mass); COMPOSE_APPLIED (PATH_FORMAL_BRC / N_BRC plus candidate endpoint-indexed C4 tag histogram). **No native physical phase law, no actual Port-probe actuator, no source-side deployment, no independent review, and no formal Claim/Result/Admission.** In particular the four complex tomography probes of PREFIX-435 have not been shown to descend to permitted native X6 operations.

## Smallest next open question: PREFIX-437

Determine whether existing source-versioned X6 field, rotation or typed BRC control-port interfaces can carry an oriented/gauge phase action, and supply an actual update intertwiner and exact Port readout. First decide whether the required S6 action fixes the phase center or may invert/rotate it; test the explicit odd plaquette witness above. Only then attempt to realize PREFIX-435's four auxiliary tomography probes. If the transfer fails for a particular interface, retain the exact scoped falsifier without promoting it into a negation of P000 or general discrete models.

Source control and authority: GLOBAL_KNOWLEDGE_V1 active main read, current EM P000, ACTIVE worldview, joint-observer contract, Portable Research Protocol and research_method consulted. GitHub account awdawmip has admin/push; native owner query returned CONTROL_QUOTA and Sites reported research_authority_granted=false. This is author-side portable research; the frozen scientific pin and formal owner remain unchanged.
