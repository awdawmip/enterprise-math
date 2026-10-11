# Sun old A14(ii) 第一位：已找到既有定理

更正版：显示曲线与共轭分支的 j 标签已修正。此 UTF-8 版本 supersedes 旧 note SHA256 fb907d57fd7c7e5ea51cefe2a3bc4f100d44c8cc6bc667fd900a3d3087b79622；旧 bytes 保存在 superseded-20261011T173045Z/。原主文献 receipts 与 PDF bytes/hash 未改。此项局部代数标签错误不影响 Theorem 1 适用、正号结论或 UR 结论；详见 CURVE_LABEL_CORRIGENDUM.md。

本次仅核查 weighted 第一位，未做全领域 novelty audit。2013 CDLNS Theorem 1 与目标的系数、权重、截断和精度完全匹配。主定理在已出版版本 p.12；Section 5 给证明，结尾明确处理 supersingular 情形。主论文 DOI 10.3390/math1010009；已出版 PDF https://d-nb.info/1163276057/34 。作者预稿可交叉核对 https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf 。

目标写作 S_p = Σ_{k=0}^{p−1}(6k+1) C(2k,k)^2 C(3k,k)/216^k。因 C(2k,k)^2 C(3k,k)=108^k (1/2)_k(1/3)_k(2/3)_k/(k!)^3，取定理参数 d=3, λ=1/2, a=6 即为同一个有限和，结论为 S_p ≡ sgn·(2/p)·p (mod p²)。

## 参数与符号核验（我们的代入推导）

定理曲线 E_3(λ) 为 y²+xy+(t/27)y=x³，其中 t=(1−sqrt(1−λ))/2=(2−sqrt2)/4。直接代数计算：
- 由显示 Weierstrass 曲线本身的 a₁=1、a₃=t/27 推出 c₄=1−8t/9、Δ=(t/27)³(1−t)，故 j(t)=27(9−8t)³/[t³(1−t)]=2417472+1707264 sqrt2；
- 共轭参数 t̄=1−t=(2+sqrt2)/4 给 j(t̄)=2417472−1707264 sqrt2；旧 note 的 27(1+8t)³/[t(1−t)³] 实为 j(1−t)，不能标作显示 E_3(t) 本身的 j；
- 两个 j 都满足 j²−4834944j+14670139392=0，即判别式 −24 的 Hilbert class polynomial；
- Δ=(t/27)³(1−t)，Norm_{Q(sqrt2)/Q}(Δ)=1/(2¹²·3¹⁸)，所以 p>3 时本模型 good reduction；
- Q(sqrt(1−λ))=Q(sqrt2) 仅在 2 ramified，a=6 与 λ=1/2 对 p>3 都是 units。

CM 特征值可用 Cohen–Guillera 表 #30 的 τ=sqrt(−6)/3 以及 Dowd 2021 Appendix A Table 3 的 j(i sqrt6)=2417472+1707264sqrt2 交叉核对；后者直接对应显示 E_3(t)，无需先取共轭。另一参数分支仍有相同 CM 域 Q(sqrt−6)。由标准 Deuring inert criterion，p≡13,19 (mod24) 有 (−6/p)=−1，曲线 supersingular，故 sgn=−1；两类都有 (2/p)=−1。因此 S_p ≡ +p (mod p²)。该推导不要求 sqrt2∈Q_p；定理明确允许 unramified quadratic extension（p.24 的局部环构造），可适用于本项目两类。

## 研究定位

Sun arXiv:0911.5665v59 的 A14(ii) 在 2011 原文是猜想：a=1 的第一位符号为 (p/3)，在本项目两类均 +1。2021 Cohen–Guillera formula #30 同一解析公式与 Section 8 的预测，不能单独作为证明。现在找到的 2013 定理负责实际第一位证明。

建议 Root 将第一位标记为“已有结果，可引用接入”，避免以新数学定理重复推进。若当前 finite certificate 是更短、完全初等、可机核的证书，它可继续，但应独立解释方法价值。这里不声称 p³ 加权和、更高 Bernoulli 项、UR 证书或 LIFT 单元已完成。没有新增 Task/Claim/Source 写入，没有更改其他研究所有权。

详见 TARGET_MATCH_MATRIX.json；PRIMARY_RECEIPTS.json 已记录下载全bytes与SHA256，其原bytes未改。parameter_check.py 从通用 Weierstrass invariants 重算 c₄、Δ、两条 j、H_{−24}、NormΔ 与两类素数的字符符号，输出见 PARAMETER_CHECK_OUTPUT.txt。FINAL_ARTIFACT_PINS.json 固定更正后 UTF-8 bytes。10 分钟有界检索起点为 2026-10-11 17:21:53 UTC；本次只修正代数标签，没有重新扩大检索。

