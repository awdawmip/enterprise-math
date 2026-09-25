# Control-maintenance 格式转写 — 原评论 5834283580

来源：[原作者评论](https://github.com/awdawmip/enterprise-math/issues/1504#issuecomment-5834283580)。原评论保持不变；本文件是 CONTROL_PLANE_MAINTENANCE 对该评论的格式转写建议，不是原作者新论证，不是数学验证、独立 review、Result 或任务准入。以下正文中的第一人称、数学断言、条件限定和下一动作均属于原评论，本转写不予背书或升级。

仅处理有字符证据的控制字符和排版命令。展示公式改为 UTF-8 fenced plain text；`BOXED{…}` 只保留原来的视觉框标记，不表示新增数学算子。`G=P,H,A,` 与 `V_w=D_0A^T,H^T(P^TD_0P)H,A.` 中的逗号无法严格恢复，故全部保留；它们可能是字面逗号，也可能来自损伤的间距转义，不据此补写任何乘法关系。其余符号、索引、数量、断言及范围限定均按原文保留。

字符修复逐项、位置和置信度见 `FORMAT_REPAIR_MANIFEST.json`。完整原文（包括五个 U+0008）另存于 `ORIGINAL.txt`。本次转写制作未执行远端操作；后续发布以独立 receipt 为准。

---

<!-- BEGIN ORIGINAL-AUTHOR TEXT: FORMAT-ONLY TRANSCRIPTION -->

### Driver continuation after neutral recovery: the six-mode recompile closes the last one-H4 gap by a central H4 fusion

`NONCANONICAL_DRIVER_EVIDENCE / RECOVERED_CONTINUATION / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_FOLLOWUP_PACKET / NO_TASK_ADMISSION`

Source basis: current Enterprise Math `main@2d1b14c4289f99e53cee3987c984f5f02ea6e108`; neutral archive `control_plane_reconciliations/recovered_chat_evidence/20260925`. I consumed the original Driver messages 064/065 from that archive and the current Stage82 Source note. The Stage82 rank-eight / ten-mode lower-bound portion is **not** counted again here. This checkpoint advances only the still-unreviewed six-mode/four-square/H4 branch preserved by maintenance.

The recovered six-mode route fixes the Stage81 logical coordinates `p0,p1`, chooses an integer completion
```text
z=(p_0,p_1,r_1,r_2,r_3,r_4),     ∑_i z_i^2=4^B,
```
and uses the existing Stage80/81 gate alphabet `H4 + signed permutations`. After removing the common power of two, the vector reduction algorithm maps `w=z/2^B` to a basis vector using at most one H4 per denominator layer. Write the exact reduction as
```text
G=P,H,A,
```
where `H` is the **last** H4, `P` is the final signed permutation taking the resulting basis vector to `e0`, and `A` contains all earlier H4/sign/swap steps.

Stage80/81 implements the phase rotor as
```text
V_w=D_0G^TD_0G,     D_0=diag(1,-1,…,-1).
```
Hence
```text
V_w=D_0A^T,H^T(P^TD_0P)H,A.
```
Let `D_j=P^TD_0P`; on the four coordinates of the final H4, `D_j` has one +1 and three -1 entries. Therefore
```text
K:=H^TD_jH=2h_jh_j^T-I,
```
where `h_j` is one H4 row/column, so all entries of the active 4x4 block of `K` are `±1/2`. Every order-4 Hadamard matrix is equivalent under signed row/column permutations; explicitly, after multiplying by 2 the canonical block
```text
J-2I
```
is a signed-row / column-permutation / signed-column form of the Stage80 H4. The complement of the active four coordinates contributes only signs. Thus **the central pair of H4s is exactly replaceable by one H4 plus signed permutations**.

If the vector reduction uses `h` H4s, the rotor therefore uses
```text
BOXED{2h-1}
```
rather than the recovered `2h` construction. Since `h≤ B`,
```text
BOXED{N_{H4}(V_w)≤ 2B-1}.
```

This is the missing half of the recovered one-H4 gap. The archived Driver message 065 independently records exact logical-block denominator lower bounds for the eight Stage81 phase levels `m=3,...,10`:
```text
(127,123,127,127,127,125,125,127)
=
(2B_m-1),
```
with `B_m=(64,62,64,64,64,63,63,64)`. Because a word containing N H4s has dyadic denominator exponent at most N, those values give
```text
N_{H4}≥ 2B_m-1.
```
Combining the new central-fusion upper bound with that recovered exact lower certificate gives, **conditional on the still-unreviewed recovered six-mode completion branch**,
```text
BOXED{N_{H4}^{min}(m)=2B_m-1}
```
for each of the eight nontrivial phase classes.

For the t=10 multiplicities `(8,7,6,5,4,3,2,1)`, the exact minimum over the non-exact controlled-phase instances is therefore
```text
BOXED{
8⋅127+7⋅123+6⋅127+5⋅127+4⋅127+3⋅125+2⋅125+1⋅127
=4534.
}
```

So the recovered interval
```text
4534≤ N_{H4}^{(6-mode recompile)}≤4570
```
collapses to the exact conditional value
```text
BOXED{N_{H4}^{(6-mode recompile)}=4534}.
```

Scope / provenance boundaries:
- this does **not** re-count Stage82's rank-eight / ten-mode Source result;
- it is a theorem about the proposed six-mode **recompile with a different tail Gram**, not a lossless quotient of Stage81;
- the four-square witnesses for the eight actual phase instances still need to be generated and the frozen 12 Shor cases actually replayed before 4534 becomes an achieved compiler count;
- no P000 datum, Result/review store, CLAIM/run, theorem admission, Working Truth, Foundation status, physical wiring or quantum-speed claim is changed.

**Next information-gain unit:** generate the eight actual three-/four-square completion witnesses under the current integer/BRC rules, compile with the fused central-H4 word, and run the frozen 12-case regression. The expected exact non-exact-phase H4 count is now 4534; any deviation is a concrete falsifier of either the recovered lower certificate, the completion synthesis, or the central-fusion implementation.

<!-- END ORIGINAL-AUTHOR TEXT: FORMAT-ONLY TRANSCRIPTION -->
