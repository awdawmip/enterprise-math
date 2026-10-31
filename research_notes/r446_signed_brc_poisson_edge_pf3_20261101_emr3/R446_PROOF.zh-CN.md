# R446｜signed BRC Poisson 边缘极限与无限参数 PF₃ 局部证书

2026-11-01。作者侧：UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。对象为 signed BRC **辅助标量** Toeplitz 矩阵；绝非原生 X6 动力学的保真证明。P000 与 ACTIVE 世界观未改变。

## 精确定理

沿用 R445：H(r,s)=binom(r+s,2s)[t^r](1-t)(1+t)^(2s)(1+t²)^(r-s)；对奇数 r≥9，b_h=H(r,r-h) (0≤h≤r−2)，超出支撑为0，a_h=b_h/gcd(b)，T_ij=a_(j−i)。令 C_r=binom(2r,r)/(r+1)>0。

**R446-A（解析）**：对任意固定 h≥0，rho_h(r)=H(r,r-h)/C_r=r^h/h!(1+O_h(1/r))（r→∞，奇数）。因此对任意固定 m 和严格递增的 J=(j1,...,jm)，归一化的连续行子式极限为

det[H(r,r−(j_v−i))] / (C_r^m r^(sum J−m(m−1)/2)) → product_(v<w)(j_w−j_v)/product_v(j_v!) > 0。

这只保证每个**固定窗口**最终为正，绝不推导对随 r 增长的窗口的统一 PF₃。

**R446-B（精确符号计算证书）**：全部奇数 r≥9 的一至三阶连续行、列 J⊂{0,...,6} 的 63 个参数化子式均严格为正；对全部奇数 r≥99，列范围扩大至 {0,...,8} 的 129 个参数化子式，也均严格为正。复用 R441 斜 Schur–Littlewood–Richardson 非负展开，推得相应左上 7×7、9×9 Toeplitz 块全部 ≤3 阶子式非负；进而任意平移位置满足 j_max−i_min≤6（第二域≤8）的 Toeplitz ≤3 阶子式非负。不能由此推出**整个**矩阵 PF₃。

## R446-A 的完整证明

记下降阶乘 (x)_{n}=x(x−1)...(x−n+1)。对任意固定 h、整数 r≥2h+2，原始 signed 卷积与二项系数相邻差恒等式给出准确有理函数

rho_h(r) =
 [(r+1)(2r−h)_{h}/(h! (2r)_{2h})]
 × sum_(q=0..h) binom(h,q)
 [(r)_{2q} (r)_{2h−2q} (4q−2h+1)/(r−2h+2q+1)]。

其中 binom(2r−2h,r−2q)−binom(2r−2h,r−2q−1)
=binom(2r−2h,r−2q)(4q−2h+1)/(r−2h+2q+1)。
除以 Catalan C_r 的步骤精确，仅用整数、阶乘和有理运算，未把 signed 抵消改为正质量。

当 r→∞，(2r−h)_{h}∼(2r)^h、(r)_{2q}(r)_{2h−2q}/(2r)_{2h}→4^(−h)、(r+1)/(r−2h+2q+1)→1；并且 sum_q binom(h,q)(4q−2h+1)=2^h。于是 rho_h(r)/r^h→2^h 4^(−h) 2^h/h!=1/h!。有理函数结构保证 O_h(1/r) 余项。

将固定 J 的行列式每列提取 r^(j_v)、每行提取 r^(−i)、每行提取 C_r，则极限矩阵为 [1/(j_v−i)!]，负阶乘为0。由于 1/(j−i)!=(j)_{i}/j!，该行列式等于严格正的 Vandermonde / product j!。证毕。

## R446-B 的可复算有限证书

按上述有理恒等式精确构造 rho_0,...,rho_8。前四项是：
rho_0=1；rho_1=r−2；
rho_2=(r−1)(r²−5r+9)/(2r−1)；
rho_3=(r−4)(r−2)(r²−5r+15)/(3(2r−1))。

对每个 m≤3、J⊂{0,...,L}，定义 D_(m,J)(r)=det[rho_(j−i)(r)] (0≤i<m,j∈J)，负指标为0。写为有理多项式 N(r)/Q(r) 并代换 r=R+u；必要时对 N,Q 同时取负。代码完全以 SymPy 精确整数/有理式重算每个 D，验证**全部 192 组**中 N(R+u)、Q(R+u) 的每个整数系数都严格为正，故 u≥0 时 D>0。两组 (L,R) 分别是 (6,9)：7+21+35=63 组，与 (8,99)：9+36+84=129 组。

示例：D_(3,(1,2,3))(r)=(r−2)(r+2)(r²−2r−9)/(3(2r−1))，对 r≥9 正。

从连续行到有限方块及平移窗口的推论复用 R441-A：任意行列子式是斜 Schur 特化，Littlewood–Richardson 展开为普通 Schur 子式的非负整数线性组合，后者的最大列号不超过原最大列号。对平移宽度≤L：最小行移到0，负列对应整列零、超过 L 的行对应整行零，其余落在左上 (L+1)² 块。结构零仍存在，因此一般子式只能断言非负。

## 实际验证、复现、边界与下一单元

运行命令：python R446_VERIFY.py（需 SymPy）。程序重新构造 192 个符号行列式及平移的分子/分母正整数系数，生成全部系数证书 R446_CERTIFICATES.json；独立从原始 signed 卷积计算 r=9、99、343 的 26 个标量并与有理函数精确核对，同时核查 h≤8 的渐近最高项。实际执行返回 R446_PASS；证书 JSON 72,772 字节，SHA256 4fb62ae4d2bf6b6945fda0d61d9619bb2c4a58604b811887830e6cd20e994550。原始运行日志见 R446_RUN_OUTPUT.txt。全部判号为整数系数，没有浮点容差。程序可直接再生 JSON，无需用户手工拼合输入。

本轮真正的新科学增量是**无限参数的有限列窗正性**与固定边缘解析极限，不再延长有限 r 的逐行穷尽。下一问题：给出 j/r∈[0,α] 的一致 Schur 子式正性下界，或寻找不能通过固定窗口极限覆盖的三阶负例；扩展窗口≤9,10 是可证伪的辅助方向，但不替代完整 PF₃ 定理。

BRC 复用：REUSE_APPLIED，保持 signed cancellation / positive-weighted BRC 的类型区别；只用原始卷积、Catalan 正归一化和 R441 Schur–LR 工具。无 X6 原生转移。沿用 R445 源提交 d5519896d2b7f65f0dbe83dc1bea80265e8421b3、R441 证明 8fba98f1654ef4050ccc562be1ec197c01f31a47；经典依据 van Leeuwen, Schur Functions and Alternating Sums (2006), DOI 10.37236/1897。

固定来源 GLOBAL_KNOWLEDGE_V1 main@e1e9409728a16a133670c599579b488a6aa5796f，Enterprise Math main@1fde72896593e8b10c9abb356983a265d2a4600f。原生 research authority=false，活跃 owner 查询 CONTROL_QUOTA；没有合法 CLAIM、Result 或 Driver 接纳。本文件只作作者侧可移植研究。
