# X6 的首段负 $e$ 斜率带排除

冻结 Port 10、六对联合 BRC、权重 $(17t,B,22t,D)$、1,935 个方向、严格 $3/2$ 近优集与合法最优项。继承必要支撑墙以及五层纯线性后缀容量上界。假设六深二元树只在根使用一个满秩二次型 $Q=a t^2+b B^2+cD^2+d tB+e tD+fBD$，并把严格芽分支整体定向为 $c>0$。本轮排除
$$
-34c\le e<-68c/3,\qquad e+17f+31c\ge0
$$
的整个斜率带，其内各阈值并列亦保留。与此前结果合并，剩余首步根必须满足 $e<-34c$ 或 $e+17f+31c<0$。总体的 $K_6$ 锐界尚待判定。R273 另行处理 $t=0$ 铅笔自身出现两个零点的情形。本斜率带内该铅笔阈值严格排序。 [此前无界排除域](https://github.com/awdawmip/enterprise-math/blob/863b3c6c096af904e745a9701e3771ee4cb1e2e3/research_notes/portable_direct/2026-11-27_x6_infinity_low_wedge/README.md) · [R273](https://github.com/awdawmip/enterprise-math/blob/9a92a7a6be912cfbad2efeb719db6c117dce1384/research_notes/portable_direct/2026-11-27_r2_x6_r273_infinity_double_pencil_closure.md)

## 一条铅笔的变序

令 $(x,y,z)=(e+17f+31c,-3e-68c,c)$。带内 $x\ge0,\ 0<y\le34z$，逆变换 $e=-(y+68z)/3$、$f=(3x+y-25z)/51$。正比例归一 $x+y+z=1$ 时，闭包的齐次顶点是 $(1,0,0),(0,34,1),(0,0,1)$。铅笔 $(T,U)$ 上纵标 $s$ 的阈值为 $\tau(s)=-cs^2-(eT+fU)s$。$B=0$ 的前三纵标是 $0,68/3,34$，端点编号 10、15、11。第一对已交换，第二和第三个阈值在新顺序上对应 10、11，并在 $y=34z$ 并列。$B=17t$ 的首对 26、19 在 $x=0$ 并列。其余固定排序的邻接差在归一闭包非负，在 $y>0$ 的域内严格。程序逐条核验三顶点差行，非指定并列须在 $(0,34,1)$ 取正。 [冻结 R247](https://github.com/awdawmip/enterprise-math/blob/7e54892a45579bdc497c27e061399339d1fb3512/research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md)

只有铅笔 $(T,U)=(2,5)$ 的排序还会变化。其六个纵标是 $5,47,154/3,158/3,73,112$，斜率量 $\lambda=(2e+5f)/c=(15x-29y-2437z)/(51z)$ 的实际范围是 $[-1141/17,\infty)$。在这个范围，阈值仅在 $\lambda=-52,-169/3,-173/3$ 并列，三处都涉及最低纵标 $5$。每个严格次序有 13 个端点符号词。最低纵标依次跨过三个不同邻居，每次分别增加一个严格词、两个单零词和一个双零词。独立 Fraction 枚举精确覆盖各开区间和并列点，共 25 个词。主搜索用二次式根结构生成全部 73 个一般词，并以局部截距约束验证它们在域内的可行性。

固定排序铅笔的潜在并列对，若符号不同便强制相关墙严格；若两端同时为零便强制等号并共用截距。变序铅笔用前稿的无排序仿射和展开，保留每个阈值行。对任意四铅笔，带号关系的最大可能和是所有选取的仿射和的最小值，逐一施加相应的严格或弱不等式即可。固定铅笔在每个方向只有一个有限上端候选，因此单个四元检验至多展开六行。 [无排序方法](https://github.com/awdawmip/enterprise-math/blob/863b3c6c096af904e745a9701e3771ee4cb1e2e3/research_notes/portable_direct/2026-11-27_x6_infinity_low_wedge/README.md)

## 三阶段精确排除

1. **端点。** 完成 17 条铅笔，执行 17,826,899 次容量分割检查，保留 250 个端点部分分割，无全严格候选。245 个可在带内实现，5 个只能在 $e=-34c$ 边实现。标签分别记录 $x=0$ 与 $e=-34c$ 的可行性，保留重叠。具有 1、2、3、4、5 个零点的候选数为 7、57、115、66、5。
2. **切线。** 允许不同零端点先独立选择切线协向量，保留首阶为零时的二阶符号以及所有零点编号。17,578 次部分选择、7,785,530 次容量分割检查后，留下 13 个不同的完整芽分割，连同零点集是 26 个配对。
3. **共同系数。** 精确行消元以端点零等式生成整数核，以正的 $c$ 选定仿射图。获得 19 个一维和 7 个二维实例。严格保留非零端点的指定符号。从零点 $p$ 向目标端点 $q$ 的芽若要求符号 $\sigma$，对首阶行 $L=2p^\mathsf{T}Aq$ 施加 $\sigma L\ge0$ 当且仅当已知 $Q(q)$ 的符号为 $\sigma$，否则取严格 $>0$。保留三条域侧约束，其中原 $e=-68c/3$ 边仍为排除前提的严格外端。混合严格和弱式的 Fourier–Motzkin 消元排除全部 26 项，记录 23 份两行和 3 份四行正整数组合矛盾证书。每份复算证书消去全部自由坐标，常数负且应非负，或常数零且应严格为正。另用不带证书的有理投影复算得到相同 26 项判定。 [固定切线实现](https://github.com/awdawmip/enterprise-math/blob/a81e850c387f2759776498bcb60245a587624e7f/research_notes/portable_direct/2026-11-27_x6_monotone_chamber_correction/reproduction.json)

紧接的同侧小带 $-153c/4\le e<-34c,\ x\ge0$ 仅再改变 $B=0$ 的一对阈值，并有 $(2e+5f)/c\ge-5057/68$，依然只遇到上述三条 $(2,5)$ 变序线。这条小带和 $x<0$ 的另一个半平面仍待排除。此处只计算冻结 BRC 观测的辅助权重系数。未作 Lean 形式化或正式独立审定。

## 本地复算

取 [本轮固定代码与结果](reproduction.json)，并使用 R247 Markdown `R247.md` 和此前发布的 `replay.cjs`、`tangent_provenance.js`。

```sh
python check_words.py
node replay.cjs R247.md strip.js > /tmp/x6-negative-e-endpoints.json
node replay.cjs R247.md tangent_provenance.js /tmp/x6-negative-e-endpoints.json > /tmp/x6-negative-e-tangents.json
node replay.cjs R247.md coupled.js /tmp/x6-negative-e-tangents.json > /tmp/x6-negative-e-coupled.json
python check_certs.py /tmp/x6-negative-e-coupled.json
```

将精确 JSON 与包内记录逐对象比较。 [固定加载器包](https://github.com/awdawmip/enterprise-math/blob/9eacaaa7040c51c3be61f204a9c5d8e464f95936/research_notes/portable_direct/2026-11-27_x6_c_nonzero_threshold_faces/reproduction.json)
