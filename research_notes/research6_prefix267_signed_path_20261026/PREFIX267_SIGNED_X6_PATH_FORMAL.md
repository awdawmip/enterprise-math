# PREFIX-267 | Signed-X6 Path-Formal BRC: future-safe quotient, exact fibers and residual bound

Status: AUTHOR_SIDE_EXACT_PROOF / FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
This is an independent formal path study, NOT a native Task CLAIM, Result, Driver review, approved BRC heartbeat operation, or physical-law assertion.

## Frozen provenance
Global knowledge main: `1f73bff7ce37e663922e3c8dd29411441b0e37a7`; Enterprise Math input main: `538e56949b4ca9d23b492995728cbb4bb3377b1e`. Read the global bootstrap/manual, current task router, P000_STARTUP (original P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`), ACTIVE worldview, current EM AGENTS, portable protocol, BRC-only arithmetic, X6-time, X6 Cell torsor and joint-observer rules. P000 six spatial axes + one separate time remain fixed; ±E_i are 12 signed *directions*, NOT twelve dimensions. Coordinates here are raw relative Z^6 charts, not final registered Cell addresses.

GitHub authenticated login: `awdawmip`; GitHub repository permission: admin. Native `em_control_tasks` -> `CONTROL_QUOTA`; native `em_session_start` -> `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Active canonical Task Owner/CLAIM unavailable. Nothing here is a formal Task publication or unauthorized native action. Portable author-side proof only.

## Typed object and theorem
Fix 1<=m<=6, alphabet A_m={+1,-1,...,+m,-m}, with d(±i)=±e_i in the native six-axis chart. The formal BRC path-word set is X_{m,n}=A_m^n, retaining every ordered source label; no signed/complex phase cancellation is inferred. Endpoint observation q(w)=sum d(a). Define formal last-step deletion D(w), NOT physical heartbeat reversal, and h-step future observation O_h=(q(w),q(Dw),...,q(D^h w)) for 0<=h<=n.

**Minimal quotient.** For any u,v in X_{m,n}, O_h(u)=O_h(v) iff q(u)=q(v) and their last h signed labels agree in order. Indeed q(D^{j-1}w)-q(D^jw)=d(a_{n-j+1}); all ±e_i are different and hence every deleted label, including its sign, is recovered uniquely. Conversely equal endpoints plus equal suffixes reconstruct O_h. Therefore (endpoint, ordered last-h signed suffix) is the coarsest observer-fiber partition retaining all declared future endpoint observations.

**Reachable prefix endpoints.** A displacement z is reachable by k signed steps iff norm1(z)<=k and k-norm1(z) is a nonnegative even integer. Necessity follows by expressing net positive/negative step counts, and sufficiency by making norm1(z) net steps and inserting inverse-step pairs. Let N_m(0)=1 and N_m(r)=sum_{j=1}^{min(m,r)}2^j*C(m,j)*C(r-1,j-1) for r>=1; this chooses j nonzero coordinates, signs and positive component magnitudes. Write S_m(k)=sum_{0<=r<=k, r≡k mod2} N_m(r). A quotient class is uniquely (prefix displacement z reachable in k=n-h steps, arbitrary ordered length-h signed suffix s), so

`Q_m^±(n,h)=(2m)^h * S_m(n-h)`.                                    (267.1)

**Exact source multiplicity.** For prefix length k and reachable z, set z_i^+=max(z_i,0), z_i^-=max(-z_i,0), b=(k-norm1(z))/2. The number of ordered source words at z, hence the mass of any class (z,s), is

`M_{m,k}(z)=k! * sum_{c_i>=0, sum_i c_i=b} product_i 1/[(z_i^++c_i)! (z_i^-+c_i)!]`.    (267.2)

The proof enumerates signed step counts a_i=z_i^++c_i, b_i=z_i^-+c_i, with the multinomial factor k!/product(a_i!b_i!). It retains ordered BRC source multiplicity and branch provenance; a positive path count is NOT a signed physical amplitude. Summing all prefix fibers gives (2m)^k, and all quotient classes give (2m)^n.

**Sharp residual bound at a fixed endpoint.** If n is even and n>=2h, every signed suffix of length h is compatible with the SAME total endpoint zero. For suffix displacement δ, norm1(δ)<=h and norm1(δ)≡h mod2, so -δ is reachable in k=n-h steps. Thus the zero-endpoint fiber contains (2m)^h distinct future-signature classes. Any extra fixed-size residual label added to current endpoint needs at least (2m)^h values, or exactly `ceil(h log2(2m))` fixed binary bits; storing the signed suffix attains the bound. This does not claim any optimal physical storage/energy cost.

For m=6,n=12,h=2: all source words =12^12=8,916,100,448,256; endpoint-only classes S_6(12)=227,305; future-safe classes 12^2*S_6(10)=144*85,305=12,283,920; at zero endpoint all 144 signed two-step suffixes occur, requiring at least 8 additional fixed bits. M_{6,10}(0)=96,807,312.

## Exact computation and verification scope
Python script `verify_prefix267.py` in the matching local reproducibility archive exhaustively enumerated (m,n)=(1,7),(2,7),(3,6),(6,4): 83,904 total words, every h=0..n. For each word it independently formed all deletion endpoints; the observed fiber map and predicted (prefix endpoint, suffix) map agreed bijectively. Every class's cardinality matched (267.2) and total class count matched (267.1). A second independently implemented C++17 signed-walk dynamic program checked m=1..6, k=0..10. At m=6,k=10 it returned 85,305 endpoint states, 96,807,312 length-ten paths at zero and total mass 61,917,364,224; PASS. The 12^12-word case was NOT enumerated: its numbers follow from the exact proved formulas. No trigonometry, pi, ordinary matrix exponential, phase or physical heartbeat operation was executed.

There is no native Cell/Port/phase/time evolution in this formal deletion model. The pure signed-coordinate adjacency is source-backed, but the deletion operator was introduced only as an explicit observer-information test; it must NOT be silently substituted for a native BRC evolution Phi. Full signed, phase, multiplicity, ordered source and joint relation information remains preserved in the underlying carrier. PREFIX-266 (previous author-side positive-only path model) is a weaker, different-alphabet predecessor, not proof of this full signed theorem.

## Next precise problem: PREFIX-268
Obtain a genuinely Source-backed, authorized native typed state x=(Cell,Port,sign,phase,t,provenance) and update Phi, with its exact allowed future operation scope. Test q(x)=q(y) => q(Phi(x))=q(Phi(y)). Either give a typed descent proof or a minimal pair of fully-typed same-q states with distinct observed successors. Test whether last-h signed labels suffice for that exact Phi and retain any omitted Cell/Port/phase relation until certified. Native Owner/CLAIM and legitimate Source publication must first be established; no formal task/Driver admission is inferred from this note.

Archive-level local full paper, Chinese derivation, validators, raw results and next task were produced together in `em_research6_prefix267_20261026_local_handoff.zip`, SHA-256 `efaefc890f0ab09719c7a2ee8c1ab3325b51c2e7f0ff53854519ec18a404d537`; the local archive is conversation-scoped until uploaded to an allowed durable destination. This Source note is self-contained for all load-bearing math and finite evidence claims.
