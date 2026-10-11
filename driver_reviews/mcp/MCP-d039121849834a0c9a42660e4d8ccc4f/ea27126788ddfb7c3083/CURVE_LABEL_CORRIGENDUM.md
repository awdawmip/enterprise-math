# Displayed E3(t) curve-label correction

本次更正仅针对我们的参数代入说明，不改变外部 Theorem 1、文献 receipts 或 PDF bytes。独立 review 指出此前把共轭参数曲线的 j 标作显示曲线本身；本文件记录修正和精确重算。

对于显示 E3(t): y²+xy+(t/27)y=x³，通用 Weierstrass invariants 给 b₂=1、b₄=t/27、b₆=t²/729、b₈=0。因此 c₄=1−8t/9，Δ=(t/27)³(1−t)，以及 j(t)=27(9−8t)³/[t³(1−t)]。

代入 t=(2−sqrt2)/4 得 j(t)=2417472+1707264sqrt2；取共轭 t̄=1−t=(2+sqrt2)/4 得 j(t̄)=2417472−1707264sqrt2。旧公式 27(1+8t)³/[t(1−t)³] 等于 j(t̄)，是共轭参数分支的值。它不应标作上述显示曲线的 j。

两条 j 都是 H_{−24}(X)=X²−4834944X+14670139392 的根，NormΔ=1/(2¹²3¹⁸) 保持。因此两个分支都有相同 CM 域，p>3 的 good-reduction 与 unramified 前提仍成立。p≡13,19(mod24) 均有 (−6/p)=−1、(2/p)=−1，故定理中的 supersingular sgn=−1 与后者相乘得到 +1；weighted 第一位仍 S_p≡+p(modp²)。这不是推翻 UR，也不是关闭 UR/LIFT 或证明更高位。

旧 note SHA256: fb907d57fd7c7e5ea51cefe2a3bc4f100d44c8cc6bc667fd900a3d3087b79622。

旧 matrix SHA256: 40ec7d62d76ea4b4f3f084f7c3f56077d62d57223d207b67d2f983f56f661d3a。

旧 script SHA256: 1645593f9f9afcec29b27d96bd2b4b630d0a5e2436e484b3af45bf3def161878。

旧版本与其 final pins 保存在 superseded-20261011T173045Z/，新 note、matrix、script、check output 的 UTF-8 bytes/hash 固定在 FINAL_ARTIFACT_PINS.json。本轮没有重开检索或新建 Task、Claim、native authority；Root 可发布更正版。
