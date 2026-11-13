# R43 — Certified rolling last-source vectors

Date 2026-11-10. Scientific freeze: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor: R42 PR #1983 @ `2f32697f0313d8cde7d21c15b0374c208b270c14`. Status: author proof and exact regression, independent review pending. Auxiliary irrational-circle observer, with historical labels and exact arithmetic; not native X6 dynamics or a change to P000.

## Definitions

Fix irrational `0<theta<1`, labelled cyclic half-open historical arcs `I_0,...,I_(m-1)` from phases `{z*theta}`, `z=0,...,m-1`, `m>=2`. For integer `J` and `N>=1`, let `W_J=[J-N,J) intersect Z`. Let `owner(t)=k` when `{t*theta}` lies in `I_k`. Define `tau_k(J)=max {t in W_J:owner(t)=k}`, or `None` if no source. Preserve original source indices and historical arc labels, not merely sorted counts.

## Theorem R43.1: one entering source, at most one expiry repair

Given exact `tau(J)` and a certified owner `k=owner(J)`, set `tau_k=J` and leave every other component unchanged. Move to `J+1`. If some stored value is less than `J+1-N`, replace this **one** expired component by exact single-label last-source selection over `[J+1-N,J+1)` (possibly None). The resulting vector equals `tau(J+1)` for all J and N.

**Proof.** The source set changes by removing exactly `J-N` and appending `J`. If a label receives `J`, its maximum becomes `J`. For all other labels, the previous maximum remains a member and remains maximal unless it was `J-N` itself. This departing source has precisely one original owner, so at most one label can lose its maximum. Exact single-label selection repairs that label, including the empty case. Induction proves arbitrary consecutive windows, including negative J. QED.

## Corollary R43.2: a verified zero-repair horizon

Suppose all m owners are covered at the initial J. Put `H0=max_k(J-tau_k(J))`. For every integer `K>=0` with `H0+K<=N`, each initial last source remains in all windows from J through J+K because `tau_k(J)>=J-H0>=J+K-N`. Since adding newer sources cannot reduce a maximum, **all K window updates require no expiry repair**. This gives a finite exact batch certificate, not an asymptotic assumption.

## R43.3 Integer owner certificate

Reuse the exact R42 rational enclosure `theta in [A/D,B/D]`, `Q=2D`, `U=A+B`, `delta=B-A`, and `r_t=tU mod Q`. Preserve original labels when sorting historical residues. For each cyclic historical adjacent pair (a,b), require `min(g,Q-g)>delta*abs(b-a)`, where `g=(r_b-r_a) mod Q`. The midpoint owner for a new t is the arc (a,b) with `d_left=(r_t-r_a) mod Q` and `d_right=(r_b-r_t) mod Q`. Check `d_left+d_right=g`, `d_left>delta*abs(t-a)` (or `t=a` and `d_left=0`) and `d_right>delta*abs(t-b)`. R42's strict cyclic-boundary proof certifies this owner for every irrational parameter in the stated enclosure. Initialize `r_J` with one product; update by `r_(t+1)=(r_t+U) mod Q`, at most one subtraction of Q per step. If a certificate fails, refine the enclosure or use a separately validated exact owner oracle.

## Cost scope

Let `b=ceil(log2(Q+1))`, `j=ceil(log2(max(2,abs(J)+N+K)))`; let M(s) bound s-bit multiplication. Once R42 initialized the m owners and historical residues, K steps need K new owner labels with O(K*(M(b+j)+b*log(m))) bit-cost, plus at most K exact *single-label* repair selections. In the zero-repair horizon there are none. Incremental event output requires O(K*(log(m)+j)) bits plus O(m*j) bits for the initial vector; full serialization of every vector costs Omega(K*m*j). Include input rational enclosure and its common denominator, initial R42 selection, optional repair costs and all output conversions when comparing algorithms.

## Executed evidence and next problem

`VERIFY_R43.py` checked 491 vectors comprising 17,447 exact labelled entries in 11 cases, with independent Euclidean Floor Sum / R42 reference and brute-force oracles for short windows. S23/AV `m=128,J=10^12+128,N=10^9,K=32,H0=164`: 32 certified new sources, 31 modular additions, zero repair, all 33 full vectors agree with independent Floor Sum. For `m=16,N=5,K=80`, 78 selective repair operations also agree. See EVIDENCE.md. Next: precision-adaptive interval refinement and full bit-cost of consecutive risk readouts. Formal Owner/CLAIM and independent theorem review remain separate.
