# C306 — Supported-factorial optimal modulus for Newton-content recovery

Date: 2026-10-25. Classification: AUTHOR_EXACT / NO_CLAIM / NOT_SOURCE_ADMITTED. A universal theorem in integer-polynomial arithmetic is applied to 125 frozen C195/H168 79-positive-rational-branch **auxiliary scalar** paths, not to original signed/phase GF(2)-BRC or Heartbeat World X6 dynamics.

## Exact source and scope

GLOBAL_KNOWLEDGE_V1 main snapshot: 18f1a35ac54714743225328150aa7952a8d95899. Enterprise Math research-source main snapshot: bb10c4dbe1badc4adad436d075f2fd93f732e89c. These were fixed separately and consulted through the current global bootstrap/manual, project bootstrap, P000, ACTIVE worldview, AGENTS, X6 and joint-observer contracts, and docs/PORTABLE_RESEARCH_PROTOCOL.md. Predecessor C305: 1dc20a643c41bd3a8a0731df0abd71487b1d4898, with the C305 exact portable package and frozen C293 digest 03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89.

Current GitHub actor awdawmip has repository push permission. Native task inventory responded CONTROL_QUOTA; em_session_start(RESEARCHER) returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. The active winning task owner was **not** verified. This separate branch is an author handoff, not a CLAIM, Source Result, Driver review or canonical-main admission.

## Theorem 1 — reconstruction with a factorization-free smaller modulus

Let s>=1, d>=0, T in Z and P(t) in Z[t] of degree at most d. Let f=d! with 0!=1 and

    h=product_{p|s} p^{v_p(f)},    M=s*h.

No factorization of s is needed: start (u,h)=(f,1), repeatedly take c=gcd(u,s) and replace (u,h) by (u/c,h*c) until c=1. This h is exactly the full s-prime-supported factor of d!.

Take r_j=P(T+j) modulo M, as least nonnegative integers, j=0,...,d. Let delta_k be the k-th forward difference of the residues modulo M, k=0,...,d, and set

    a_k=gcd(k!,h),  b_k=k!/a_k.

Then gcd(b_k,s)=1; delta_k is divisible by a_k as an ordinary integer; for s>1 define

    beta_k=((delta_k/a_k)*inverse_mod(b_k,s)) mod s.

The exact identity is

    gcd(s,content(P))=gcd(s,beta_0,...,beta_d).

For s=1 the answer is 1 without modular inversion. For P=0 use content(P)=0 and gcd(s,0)=s.

**Proof.** The falling factorials e_k(t)=product_{0<=j<k}(t-T-j) are monic and hence form an integral unitriangular basis of Z[t] in degrees <=d. Write P=sum B_k e_k; the coefficient ideal, hence content, is unchanged. Newton's identity gives Delta^k P(T)=k! B_k=a_k b_k B_k. Modular differences therefore give delta_k congruent to a_k b_k B_k mod M. Since a_k divides both terms and M, delta_k/a_k is an exact integer, congruent to b_k B_k modulo M/a_k; s divides M/a_k. As b_k is a unit modulo s, beta_k is B_k modulo s. Taking gcd with s proves the identity. QED.

## Theorem 2 — least uniform modulus for these consecutive samples

Among positive integers N such that the *single uniform modulus N* on P(T),...,P(T+d) suffices to recover gcd(s,content(P)) for every integer polynomial of degree <=d, **M is the smallest**, and in fact M divides every such N.

**Proof.** Suppose p|s, a=v_p(s), w=v_p(d!), and e=v_p(N)<a+w. Set u=max(0,e-w)<a, c=(N/p^e)*p^u, P_1(t)=c*product_{j=0}^{d-1}(t-T-j) and P_0(t)=0. Both have zero values at T,...,T+d-1. At T+d the value c*d! is also divisible by N since u+w>=e. The two polynomials thus have identical samples modulo N. But the falling-factorial polynomial is monic, so content(P_1)=|c| has p-valuation u<a, while gcd(s,content(P_0))=s has p-valuation a. Their outputs differ: a contradiction. Hence v_p(N)>=v_p(s)+v_p(d!) for every p|s, equivalently M|N. Theorem 1 gives sufficiency. For s=1, M=1. QED.

**Precision of optimality claim:** only the universal, single-modulus, consecutive-integer-node information model is covered. No complexity lower bound for adaptive moduli, symbolic coefficient inspection or different sampling is claimed.

Synthetic illustrations: s=10,d=4 gives h=8 and M=80 rather than 240; k=4 uses a_4=8 and unit b_4=3 modulo 10 (inverse 7), not illegal naive division by 24. s=35,d=6 gives h=5 and M=175 rather than 25200. Direct gcd of raw integer samples is insufficient: P(t)=t(t-1) is primitive but integer-valued even.

## Author-level exact evidence, actual coverage

The factorized modular evaluator retains the original 79 terms, constructs C300's reduced numerator by the inherited exact polynomial cancellation A_shared=C*A_red and exact modular integer division by C(t), and computes only supported-factorial-modulus residues. It reconstructs B_k modulo s using Theorem 1; all 125 new gcds are individually compared to frozen C305 decimal exact gcd certificates.

| Validation item | Exact result |
| --- | ---: |
| Frozen auxiliary paths | 125/125 PASS |
| Path polynomial degrees | 124 paths: 352; 1 path: 265 |
| Modular evaluations and Newton coefficient residues | 44,038 each |
| New gcd versus frozen C305 | 125/125 PASS |
| Paths with strictly reduced uniform modulus | 125/125 |
| Original C305 modulus width | 7,233–7,897 bits |
| New C306 modulus width | 6,526–7,196 bits |
| Width saved per path | 256–743 bits; median 708 |
| Sum of per-path width differences | 88,534 bits |
| GCD-peeling loop iterations per path | 5–18 |
| Independent synthetic polynomial cases | 2,160/2,160 PASS |
| Independent sharpness witnesses N=M/p | 1,899/1,899 PASS |

The independent synthetic checker covers integer coefficients including negative values, zero polynomials, T of either sign, d=0..8 and s=1..120. Its deterministic seed is 30620261025; all decisive assertions use arbitrary-precision integer arithmetic. The 125-path evaluator, by contrast, **inherits** the C300 shared-numerator polynomial identity; C305's complete independent polynomial oracle covered only three indices (0,28,63). No new full independent check for all 125 is claimed. The sum of observed concurrent per-path durations 378.432 seconds is not a calibrated performance comparison. Width savings are modulus widths, not guaranteed runtime/RSS savings.

## Scientific interpretation and constraints

P000 fixes native Heartbeat World as a six-axis discrete X6 Cell space with separately typed time; native plane does not exist. The current 79-positive-rational-branch example is a declared auxiliary scalar model, with no native X6 embedding, preserved-sign/phase BRC operation or future-operation equivalence proof. Its source paths/79 factors remain frozen; taking a scalar content gcd neither deletes joint/composite observers nor certifies provenance, phase, branch, port or CRT-carry redundancy. No native heartbeat/BRC-Shor experiment was run. A novel arithmetic algorithm does not change P000.

## Exact reproduction and next issue

Full source, numeric audit including 125 decimal exact gcds, command logs, SHA256 manifest and frozen C305/C301 dependency inputs are in EM_C306_SUPPORT_OPTIMAL_NEWTON_125_EXACT_PORTABLE.zip. Execute the C306_SUPPORT_OPTIMAL_MODULAR_NEWTON.py reference script with the unpacked C305 inputs (parameter --indices all), plus C306_INDEPENDENT_SYNTHETIC_CHECK.py. The remote code is a research handoff; no GitHub-hosted execution is claimed.

C307: devise and prove a coefficient-index-adaptive p-adic precision schedule (or prove an obstruction) that is strictly more efficient for the actual factorized circuit; quantify exact bit operations and retain original source, phase, port and future-observer information. Separately request an independent, source-authorized review of C300-C306 without relabeling author exact checks as accepted results.
