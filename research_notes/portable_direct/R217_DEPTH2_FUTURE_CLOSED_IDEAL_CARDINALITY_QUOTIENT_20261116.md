# R217 — Exact future-composition-closed quotient for principal ideal cardinalities at tail depth two

Date: 2026-11-16 (Asia/Shanghai)
Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**
Native physical BRC integration: **NOT_EXECUTED**

## Source, definitions and preservation

Frozen scientific basis: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Reuse R209 (Stirling fibres), R213 (exact Green ideal membership), R214 (Green-J ideal-*membership* quotient) and R215 (exact original-J principal-ideal cardinalities, committed at \`71e9d86c4fea71a0ff1b2da66fe2b5656998a68b\`). R216 at \`ccb21b502916b65317620b82a6e84048795748cf\` motivates distinguishing present scalar information from future-closed information.

Fix \`m>=1\` directions and \`k>=0\` selected provenance tags. Let \`A=[m] × ({0}∪[k])\` with neutral tag 0; \`a=m(k+1)\`. In the chronological finite observer monoid \`J=J_{m,k,2}\`, a state is the last-appearance order of selected source tags together with the last \`min(2,|w|)\` paired letters. It is obtained as \`F(w)\` under chronological concatenation of event words. Let \`f(x)=|JxJ|\` be the cardinality (an integer) of the principal two-sided ideal of state \`x\` in the **original** monoid.

The semantics concern only this exact finite observer and the indicated ideal-size readout, not the complete BRC effect, physical propagation or source-sensitive tail output. P000's six native axes, the twelve signed directions and separate time, and the ACTIVE residual-fidelity rule remain unchanged.

## Main theorem — the minimal future-closed ideal-cardinality observer

Define a marked finite set

\[
Q_{\mathrm{card}}=\{\mathbf 1\}\ \sqcup\ \{S_t:0\le t\le k\}\ \sqcup\ \{F_U:U\subseteq[k]\}.
\]

Its cardinality is

\[
\boxed{|Q_{\mathrm{card}}|=k+2+2^k.}\tag{1}
\]

The map \`q:J→Q_card\` is:

* The empty short word maps to \`1\`.
* Each one-letter short history \`(direction,t)\` maps to \`S_t\`, **discarding only its direction in this scalar-observer quotient**.
* Every full-tail state (length at least 2) maps to \`F_U\`, where \`U\` is its complete selected-provenance support set.

For a tag \`t\` write \`s(t)={t}\` if \`t≠0\`, and \`s(0)=∅\`. Multiplication on \`Q_card\` is determined by \`1\` being the identity and

\[
S_tS_v=F_{s(t)\cup s(v)},\quad
S_tF_U=F_{s(t)\cup U}=F_US_t,\quad
F_UF_V=F_{U\cup V}.\tag{2}
\]

**Claim A.** The map \`q\` is a surjective monoid homomorphism. In particular its kernel is stable under every future left and right observer composition.

**Proof.** A chronological product of two literal short words is short precisely when their combined length is less than 2. Once a full tail has been reached, no later concatenation can make it short. Complete provenance support is the set union under concatenation. These cases give precisely (2), independently of discarded one-letter directions. Every \`S_t\` occurs as a one-letter history; every \`F_U\` is realized by emitting each tag in \`U\` at least once and then two neutral events. The identity is realized by the empty history. Thus \`q\` is onto and multiplicative. ∎

Let \`W_j=j!m^2 \sum_{i=0}^{\min(j,2)} {3\brace i+1}\` be the number of full-tail states with each prescribed provenance support of size \`j\`, and define

\[
T_r=\sum_{j=r}^{k}\binom{k-r}{j-r}W_j.
\]

**Claim B.** The principal ideal-cardinality readout factors exactly through \`q\`:

\[
\boxed{\begin{aligned}
 f(\mathbf 1)&=|J|=1+a+T_0,\\
 f(S_t)&=T_{|s(t)|}+1,\\
 f(F_U)&=T_{|U|}.
\end{aligned}}\tag{3}
\]

**Proof.** R215's exact original-monoid ideal-size formula gives the full state term \`T_r\`. A one-letter word has precisely one short literal word containing it at cutoff 2, so its two-sided principal ideal has size \`T_r+1\`. The empty word generates all \`J\`, which decomposes into one empty, \`a\` one-letter, and \`T_0\` full states. All terms depend only on the indicated \`q\` state. ∎

**Claim C (minimality).** For any two distinct \`q\` states there exists a finite right continuation \`z∈J\` such that \`f(xz)≠f(yz)\`, for any representatives \`x,y\` of these two states. Therefore two original states have the same \`f\` value after **all** right continuations if and only if their \`q\` states agree. In particular \`q\` is the **coarsest deterministic two-sided compositional quotient that exactly preserves the scalar readout** \`f\`.

**Proof.** The full sector \`F_U\` has a principal ideal consisting of all full states whose selected source support contains \`U\`. If \`U⊊V\`, this ideal strictly includes the one for \`V\`: a reachable full state with support exactly \`U\` is a witness. Consequently \`T_0>T_1>\cdots>T_k\` whenever those indices exist.

Now compare distinct proposed quotient states.

1. \`1\` differs already without any continuation: \`f(1)=|J|\`, while every nonempty state generates a strict proper two-sided ideal, since concatenating never produces an empty observer word.
2. For \`F_U,F_V\`, if their support cardinalities differ, their \`T\` values differ. If their cardinalities are equal but \`U≠V\`, append an arbitrary full context whose provenance support is \`U\`. The products become \`F_U\` and \`F_{V∪U}\`. The latter has strictly greater support cardinality, hence strictly smaller \`T\`.
3. For \`S_t,S_v\`, a neutral/nonneutral pair differs already because \`T_0>T_1\`. If \`t,v\` are distinct nonneutral tags, append one single event carrying tag \`t\`. The resulting full states have supports \`{t}\` and \`{t,v}\`, respectively, and therefore unequal \`T\` values.
4. For \`S_t,F_U\`, if \`f(S_t)≠f(F_U)\` no continuation is needed. Otherwise equality \`T_{|s(t)|}+1=T_{|U|}\` forces \`|s(t)|≠|U|\`. Append a neutral one-event history. Both products are full, of respective supports \`s(t)\` and \`U\`, with different sizes and hence different \`T\` values.

This exhausts all pairs, including \`k=0\` (where the unavailable selected-tag comparisons are vacuous). As Claim A already supplies a two-sided congruence preserving \`f\`, and Claim C distinguishes every pair of its classes by a right context, no further classes can be merged by any correct future-composition-closed deterministic scalar observer. ∎

## Exact X6 case and comparison of typed query languages

For \`m=12\`, \`k=6\`, \`L=2\`, \`a=84\`:

| Observer / query language | Number of states | Minimum fixed bits |
|---|---:|---:|
| Complete paired-tail / source action (R210) | 1,407,685 | 21 |
| Exact individual right/two-sided *ideal membership* (R214) | 149 | 8 |
| Exact scalar \`x ↦ |JxJ|\` after **all** future left/right compositions (R217) | **72** | **7** |

These are different, precisely declared observation languages. The 7-bit state \`q(x)\` does not replace the source-preserving complete BRC carrier for richer readouts. Unlike the present border-count invariant of R216, it is a genuine future-composition-closed quotient under the whole monoid.

The quotient product is a tagged union/set-bitmask operation; it can be composed directly without decoding complete direction/source tail histories. A 7-bit fixed-width representation reaches the information-theoretic minimum since \`2^6<72≤2^7\`. No end-to-end native performance improvement has been measured.

## Exact independent finite verification

The Python 3 standard-library companion \`R217_DEPTH2_CARDINALITY_QUOTIENT_VERIFY.py\` builds each complete original observer monoid by generator BFS, retains representative words, explicitly constructs the multiplication table, computes **each original principal two-sided ideal as a set** \`{p*x*q:p,q∈J}\`, computes all right-context scalar signatures \`(f(xz):z∈J)\`, and checks that equal signatures coincide **exactly** with proposed \`Q_card\` classes. It also verifies left/right generator congruence for each represented state. This is a second finite computational route independent from the use of R215's Stirling cardinality formulas inside the theorem.

Seven complete models were checked: \`(m,k)=(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,1)\`; respectively original state counts \`3,8,23,7,25,83,52\`, total **201**; quotient class counts \`3,5,8,3,5,8,5\`, total **37**. There were **2,024** exact left/right generator congruence assertions and **92** distinct-class context-signature comparisons. All checks returned **PASS**. The \`m=12,k=6\` count is a direct formula specialization, not exhaustive physical computation.

General-parameter exactness rests on Claims A–C; finite computations corroborate specific instances. Review: \`NOT_REVIEWED\`; native \`EffectHistogram\` integration: \`NOT_EXECUTED\`.

## Continuation

1. Build an actual native \`EffectHistogram\` ideal-cardinality readout that maintains the original 21-bit paired-tail/provenance action and all typed physical effects, and separately indexes the 7-bit cardinality quotient. Benchmark mapping and product cost, bit complexity, serialization and output recovery.
2. For tail depths \`L≥3\`, identify the coarsest future-composition-closed principal ideal-cardinality quotient; R216 already shows present border statistics are not enough under future composition.
3. For the minimal 7-bit quotient, analyze its possible efficient packed multiplication representation and source-support extraction with no full-tail decoding.

No new formal Task CLAIM, independent Review or Foundation promotion is asserted by this portable research publication.
