# R284FB — 跨代漏写的两边残差、精确可达集与错误代际反例

Date: 2026-11-23 (Asia/Shanghai). Research status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Mode: informed TASK_RESEARCH portable, independently saved science; no shared CLAIM, Result or independent Review.
Research lineage: R284FA_ONEWAY_OMISSION_SHARP_FOUR_CYCLE_20261123.md (commit c8245cb74d792264d05f3ec751e8dc1a0429b687), earlier R284EZ/EX/EW. Frozen R284CO Port inputs and P000/ACTIVE Heartbeat World/X6 are unchanged.
This is a discrete error-channel calculation downstream of the frozen Port model; no new native BRC numerical computation or geometric claim is made.

## Question and scoped outcome

R284FA proves the exact 5u+3q+2 label bound when each edge begins at a completely repaired, correct old tag. Here we remove **only** that reset. Each logical edge still attempts every bit whose target tag changes; at most q attempts per edge fail and retain the actual stored bit; successful attempts write the target correctly. Read noise flips at most u bits independently per read. Unchanged addresses are never written. The decoder is the exact original stateless unique radius v=u+q Hamming-ball decoder, with RETRY outside all balls.

We prove an exact two-edge memory law for this specific four-tag construction, including a reachable wrong-generation counterexample already at u=0,q=1. This **does not refute** R284FA under its reset hypothesis, nor does it determine a global optimum for reset-free protocols.

## Theorem 1 — exact physical-error recurrence

Let c_j be the intended old tag and c_{j+1} the intended new tag, D_j={i:c_j[i]≠c_{j+1}[i]}, and E_j={i:x_i≠c_j[i]} the true stable-endpoint error set. Every permitted write history has

E_{j+1}=(E_j \ D_j) ∪ M_j,
where M_j ⊆ D_j \ E_j and |M_j|≤q.

In particular, a previously erroneous bit in D_j *already equals the new target bit* because the alphabet is binary. Writing it correctly or missing the attempted write both leave it correct relative to the new tag. New errors arise only from failed attempts on coordinates previously correct, and unchanged-coordinate errors persist.

This identity is exact; it retains the carry-over residual rather than treating the current logical tag as complete physical state.

## Theorem 2 — two-edge exact stable residual for the R284FA code

For u+q≥1 the published construction has three disjoint blocks A,B,C of lengths

a=|A|=|C|=u+q+1, b=|B|=3u+q,

and tags c0=(0,0,0), c1=(0,1,1), c2=(1,0,1), c3=(1,1,0) on the block alphabet.
Edges 0→1 and 2→3 toggle B∪C; edges 1→2 and 3→0 toggle A∪B. Thus each two successive logical edges together touch all storage coordinates.

At completed generation c0, after any preceding history that includes 2→3→0, the reachable physical-error family is **exactly**

E0 = P ∪ Q,  P⊆A∪B, |P|≤q; Q⊆C, |Q|≤q.

Proof: apply Theorem 1 first to 2→3 and then to 3→0. Since the latter touches A∪B, it erases all older A/B errors, while the former touches B∪C, so no errors older than the 2→3 edge can remain. The surviving C errors come from omissions on 2→3; the new A/B errors come from omissions on 3→0. Conversely, choose only C misses in 2→3 and only the prescribed A/B misses in 3→0, with other writes successful. Their budgets are independent and each selected residual is realized. Consequently max |E0|=2q (attainable because a≥q and b≥q), whereas R284FA's repaired-endpoint model had at most q. The same cyclic statement applies at the other generations after two edges.

## Theorem 3 — sharp false stable-generation criterion for this code and decoder

Let v=u+q. At intended c0 the **minimum Hamming distances from reachable stable physical words** to the three *incorrect* labels, respectively, are

min dist(x,c1)=4u+1,
min dist(x,c2)=2u+2,
min dist(x,c3)=4u+q+1.

Proof: write P=P_A∪P_B, set p_A+p_B≤q, and |Q|=p_C≤q. Then

dist(x,c1)=a+b+p_A-p_B-p_C,
dist(x,c2)=2a-p_A+p_B-p_C,
dist(x,c3)=a+b-p_A-p_B+p_C.

Minimize these integer expressions by selecting allowed P and Q; each stated bound is attained. Read noise of weight ≤u can place a word in the radius-v ball of an incorrect label exactly when its physical distance to that label is ≤v+u=2u+q. All four R284FA codewords have pairwise distance at least 2v+1, so this is sufficient for that label to be the unique successful decoder output.

Therefore an incorrect stable-generation output is possible **if and only if**

q≥2  OR  (u=0 AND q≥1).

For u≥1,q=1 the statement certifies only the absence of false outputs at this selected *stable c0 endpoint*; it does not prove no rollback or no mid-edge error over all histories.

## Smallest explicit counterexample

Take u=0,q=1. The published construction has a=2,b=1 and

c0=00000; c1=00111; c2=11011; c3=11100.

Start at the correct c2. In 2→3, successfully update B and the final C bit but omit the first C-bit write: physical state 11110. In 3→0, successfully update both A bits but omit the B-bit write: physical state 00110. Each edge has exactly one allowed omission, and **no repair was performed**.

The true completed generation is c0=00000, but physical x=00110 has distances to (c0,c1,c2,c3) equal to (2,1,4,3). The original v=1 decoder uniquely returns c1. This is a *successful, false generation read at a stable endpoint*, not a mere RETRY. The two-error path residual was lost when the current logical generation alone was treated as the physical state.

## Recalculation and evidence

R284FB_carryover_omission_checker.py enumerates all missed-write subsets on exact edges 2→3 and 3→0, compares their entire endpoint-state sets to the closed-form P∪Q characterization, checks the attainable maximum 2q and the sharp false-label threshold. Python standard library, exact binary strings and integers only. Actual execution covers u,q∈{0,1,2}: 9 parameter configurations, including the literal five-bit witness. All assertions passed. The full JSON stdout is preserved in R284FB_carryover_omission_certificate.json. The analytic arguments above cover arbitrary nonnegative integer u,q; finite checks do not imply an independent mathematical Review.

## Scope, provenance and next scientific problem

This result describes logical four-generation tag memory, not a physical time calibration, an independently certified Port experiment or a change to P000. R284FA remains valid **with its explicit cross-edge reset**. Its 5u+3q+2 formula must not be reused unchanged as a reset-free guarantee: the published achieving code can produce false generations without repair.

The next objective is to find the minimum storage length and write schedule for reset-free, carry-over-tolerant four-generation publication, allowing exact error-cohort state (or verified scrubbing) where genuinely necessary. The two-edge recurrence is a candidate compact sufficient state for endpoint reachability, but a reset-free no-rollback proof must also cover *intermediate prefixes, read timing, and bank reuse*. Preserve the omitted-write cohort and chronology when reducing the observer state; do not infer future-operation equivalence from equal logical labels.

Provenance: direct analysis of immutable R284FA proof at enterprise-math@c8245cb74d792264d05f3ec751e8dc1a0429b687. Original contributor lineage: verified registered Researcher EM-DIRECT-138733 / RA-6ED10E3B2CC917A530F9D56A (session MCP-9558dce6e07644f0ac082f286d58240b), no current canonical CLAIM established. Publication is scientific evidence only; authenticated Activity association and owner authorization are separate.
