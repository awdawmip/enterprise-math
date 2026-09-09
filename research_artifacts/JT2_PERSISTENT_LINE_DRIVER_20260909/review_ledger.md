# JT2 source-recovery and obligation comparison

Review scope: source-exposed intake, exact text/pin recovery and comparison of declared interfaces. No mathematical computation, literature theorem verification, new formal review, or clean-independent discovery is claimed.

| Issue | Decision | Exact remaining evidence |
| --- | --- | --- |
| JT2-SOURCE-01: CM0/SIMPLE originals absent from W59A summaries | LOCATED | The full prior main return bound by RR-82F6383FB6634F72B457 contains both proofs and the polynomial definitions. Its SHA-256 is 54ab94a1899f649ae1488bececaa7c57aafbc89aef44bdd1e40cc0b45590e827. The prior source, not this table, contains the arguments. |
| JT2-SOURCE-02: original first/second digits | LOCATED_WITH_REMAINING_TAIL_DEPENDENCY | The return defines g, h, G_p=g/p, P_(2m)(T)=Q_m(T²), JT0 iff UR and JT2 iff UR+LIFT. Its reflected R_p is retained as a predecessor coordinate; no missing value was silently redefined. |
| JT2-REUSE-01: duplicate old UR work | REVIEW_BEFORE_REDISPATCH | Source-only PR1383 supplies an earlier literature-closure candidate. Readback at 9a1d0b… gives blob fdac56b533ea2b4c0be40247b008e00da828a817 and SHA-256 1f4e8207a969a5ccf151e9f60d5eece93249d655b46c78a23a8c71e77ce1e6e6. Its claimed theorem instantiation is not accepted from the GK TESTING summary or merely because a PR exists. |
| JT2-BRIDGE-01: old UR versus gen2 UR | OPEN_EXACT_TRANSPORT | Compare the different finite values at full mod-p² precision, as below. Then evaluate all six current task outputs separately; a literature proof need not provide the requested recurrence derivation. |
| JT2-BRIDGE-02: QTF3 versus old LIFT | OPEN_NORMALIZATION_AND_ADDRESS | Pin the full finite F_p/L_p definitions and the original second-digit/Clausen-tail implication. The fixed-point statement and the Frobenius-pair statement use different arguments. |
| JT2-CONTROL-01: explicitly assigned GOV versus selector-only text | REFERRED_TO_CONTROL_MAINTENANCE | Preserve the actual canonical target reduction, source-backed claim and PASS authorization. No earlier global-selector output exists or is fabricated. No other task is claimed on this rationale. |

## Interface comparison, without substituting a new theorem

The prior return uses p=6m+1 with p≡13 or 19 (mod 24), n=2m, t²=1/2, and the simple derivative. It defines

`g = sum_(k=0)^(p-1) (1/6)_k (1/3)_k / [2^k (k!)²]`.

Its UR is `(g/p)(-6 Q_m'(1/2)) = 1 (mod p)` with the divisibility of g and the derivative-unit premise supplied by the prior proof. The current W59A task instead uses `B(t)=P_(p-1)(-1/3,t)` and asks for

`3 B(t) P_n'(t) = -p t (mod p²)`.

Using only the already-declared `P_n'(t)=2t Q_m'(1/2)` interface, the old UR is written in the same slope normalization as `3 g P_n'(t)=-p t (mod p²)`. Therefore transferring that conclusion requires the exact bridge `B(t)=g (mod p²)` on the matching scope. This isolates a required interface; this intake supplies no proof of that bridge and does not assert it false. Dividing a congruence by p remains conditional on the actual divisibility certificate, and the derivative-unit premise must not be dropped.

The recorded W59A journal defines `L_p(u)=P_(p-1)(-1/3,1-2u)`. The current QTF3 hard target compares its value at u=1/2 with the other displayed truncated sum at argument 1. By contrast, B(t) is the L value at `(1-t)/2`, where `4u(1-u)=1/2`, and the old g uses the expected F-series at argument 1/2. The same quadratic-transform formula cannot be assumed at a second argument or precision merely from the stated fixed-point target. Preserve this address distinction while recovering the full F_p definition and original reduction proof.

The residue-class alignment also remains explicit: the old task fixes {13,19} mod 24; gen2 says p=3n+1, p>3 and the exchanged Frobenius ports. A reusable proof must state how these scopes match, including the coefficient algebra and both port labels, instead of silently broadening either task.

## Governance consequence

Do not issue another UR proof claim now. First review the existing source candidate and its precise applicability/bridge; retain any Sun-specific unmet obligations. Do not close QTF3, the independent audit, final JT2 integration, or the broader mother objective. No formal parent merge or task supersession is made by this comparison.
