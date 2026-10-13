# Explicit period-table cost: auxiliary mathematical review

Status: PASS under the stated additive cost model.
Auxiliary native identity: UNKNOWN / directed nonblind. No SID or RA created.
This is a local mathematical check of Root's new review lemma, not a formal native review.

Let T be the true nonnegative integer Fermat offset and let M=M(N) be any positive integer. On the same instance assume:

1. F_N(t+M)=F_N(t) for every integer t>=0, and F_N(T)=1.
2. Before the search, all M cells of an explicit period table are computed, each with cost at least lambda>0.
3. Every retained candidate in the full prefix 0,...,T incurs cost at least mu>0.
4. These are distinct, additive charges to total work W; a shared operation is not charged twice.

The retained positions T-jM for j=0,...,floor(T/M) are distinct and nonnegative. For integer T,M, write T=aM+r with 0<=r<M. Then floor(T/M)+1=a+1=ceil((T+1)/M). Thus the stronger endpoint bound is

    W >= lambda M + mu ceil((T+1)/M)
      >= lambda M + mu (T+1)/M
      >= 2 sqrt(lambda mu (T+1)).

The last inequality follows from (sqrt(lambda M)-sqrt(mu (T+1)/M))^2>=0. The strengthened chain is non-strict: its endpoint equalities can occur under additional divisibility and cost conditions. The original strict comparison floor(T/M)+1>T/M also remains correct, but gives the weaker T-based bound. No fixed-period-across-instances assumption is needed. The statement holds for every per-instance choice M(N) satisfying the explicit-table assumptions. Uniform fixed lambda,mu imply an Omega(sqrt(T+1)) work bound within this model.

For T=0, the direct bound is W>=lambda M+mu>=lambda+mu>=2 sqrt(lambda mu), consistent with the new bound. M*=sqrt(mu (T+1)/lambda) minimizes only the relaxed function lambda M+mu (T+1)/M over positive real M. With M>=1, the constrained relaxed minimizer is M=1 when mu (T+1)<=lambda. The integer ceiling objective and actual survivor count require separate treatment: rounding M* is not established as the integer optimum. This does not construct an algorithm, establish attainability, or show that a factor-blind rule can choose a one-survivor period containing the true T.

Scope is limited to full per-instance explicit-table preprocessing plus charged full-prefix candidate examination. Implicit or CRT-compressed representations, vectorized cells with nonuniform per-cell charging, free or cross-instance amortized tables, and methods avoiding this prefix model are not covered without a new accounting proof. In particular, this is not a general factorization lower bound and does not rule out square-root-scale gains relative to linear scanning.

The lemma is mathematically acceptable as a separately disclosed new Root review derivation. It neither upgrades the frozen 600-case empirical failure to a universal theorem nor changes the original RR verdict or target. Acceptance of the whole Task still requires Root's actual bounded scope judgment.

Underlying frozen evidence:

- RR-C5769D6B237D02BFF025 SHA256: 1149fb488e66bdff40cd52b79b1566400c4691b8254ec884aa113a4a4d7c934f.
- Scientific return SHA256: 27359fab6b2faeeb7cd1528d1473e37e67f359bfdd601f31a693521984a41eff.
- Taskbook SHA256: 50934aad4f07e43f52ff6970387392fb9d91d58cda2d98b6015fdd8a30222779.

No experiments, checker execution, Source/native mutation, original RR edits, or formal review creation occurred. Mathematical parent remains OPEN.
