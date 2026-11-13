# PREFIX-601C-R2：两条正门控碰撞曲线上的26阶锐递推

日期 2026-11-08。冻结科学输入：awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d。承接本分支 PREFIX-601 双奇偶24维定理及 PR #1812 PREFIX-600 的正门控谱碰撞曲线。保留96原生端口、576带标签动作和三个门控来源；P000不变。Researcher-ID EM-DIRECT-4A37D4，Activity RA-420E5CA18B6618002BCE5A9F；AUTHOR_SIDE_EXACT / UNREVIEWED。

## 定理：两个精确正有理碰撞点

六轴权重固定 (1,1,1,1,2,2)，即 w=2。选择

* A 点：z=109/17；原生谱碰撞因子 u-8。
* B 点：z=153/13；原生谱碰撞因子 u+24。

将原生48维正尾态 Q 排成 [[0,B],[C,0]]，M=BC。令

```text
F15(u)=(u-4)(u-8)^6(u+24)^2(u^2+12u-96)^3;
H5(u)=(u-4)(u-8)(u+24)(u^2+12u-96);
R9(u)=charpoly(M,u)/F15(u).
gcd(H5,R9_A)=u-8;   gcd(H5,R9_B)=u+24.
nu_A=H5*R9_A/(u-8);  nu_B=H5*R9_B/(u+24).
```

**精确结论：**

```text
At z=109/17: mu_(BC)(u)=mu_(CB)(u)=nu_A(u), degree 13.
At z=153/13: mu_(BC)(u)=mu_(CB)(u)=nu_B(u), degree 13.
At both points: mu_Q(t)=nu(t^2), sharp degree 26.
```

证明：分别以有理数精确计算24x24矩阵BC和CB，直接验证nu(BC)=nu(CB)=0。将nu在Q[u]中按不可约因子分解，对于每个因子f，精确计算 (nu/f)(BC) 非零，故不存在可删去的因子，所列13阶是锐的最小多项式。在固定次序 u-8、u-4、u+24、u^2+12u-96、余下8次不可约多项式，五项因子删除后非零矩阵项数为：

```text
A: 576, 16, 128, 248, 576.
B: 128, 16, 576, 248, 576.
```

依据 PREFIX-601 已证的B、C可逆及二分对称性，48维最小多项式次数精确为两倍。对比已证非碰撞点 w=2,z=2 的14/28阶，两正有理点分别降低至13/26阶。

## 完整端口验证与后继

执行源代码 PREFIX601C_R2_positive_collision_exact.py，复用同目录已执行的 PREFIX601_R2_exact_certificate.py 所提供的冻结原生STAR与96端口带标签接口。对每个碰撞点，除24维精确有理数湮灭和锐性见证外，还执行8个不同原生96端口整数输入、6步后续固定有理数门控传播，合计96次完整96端口/尾态精确相等检查。所有断言通过：ALL_ASSERTIONS_PASS。

研究范围是上述两个明确的正有理参数点。下一步研究两条连续正曲线的其他点、交点及z=1处的锐次数/Jordan型，并计入端点转换、系数位长、输出恢复的完整跨步成本。正式CLAIM/Native Result与独立Driver审查未发生。
