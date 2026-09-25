本轮真正进入了指定数学单元。结论不是“已经找到唯一 representative”，而是得到一个更关键的精确反例：

\[
\boxed{\text{仅凭 }-\sqrt{-6}\text{ CM endomorphism 的模 }p^2\text{局部微分关系，无法固定所需的 }p\text{-层 representative。}}
\]

而且这个不可辨识性可以精确写出来；它正好发生在 D25 所关心的 \(p\,u^{p-1}du\) 层。

身份方面只做本地解析：本真实对话继续使用 `chatgpt-thread-6ab0a2a3-1880-83ee-a0c0-f2016b6074ac`；本地 Researcher role 标记为 `REGISTER_PENDING`。没有借用旧 E267A2/session/claim/run，也没有重放此前被拒的登记写操作。新澄清允许在这一状态继续用户授权的 portable mathematics。

### 1. 先核验 074 中本轮真正需要的输入

074 的 opaque 引用不能作为证据，因此我重新核了公开来源。目标 \(j\)-值

\[
j=2417472+1707264\sqrt2
\]

确实对应判别式 \(-24\)，即 \(\mathbf Q(\sqrt{-6})\) 的 CM；独立 CM 资料和 LMFDB 均吻合这一点。:chatgpt-content-reference{index="0"}

因此本轮可以合法采用

\[
\kappa:=\sqrt{-6},\qquad \kappa^2=-6
\]

作为 degree-\(6\) CM endomorphism \(\varphi\) 在 invariant differential 上的特征值：

\[
\boxed{\varphi^*\widehat\omega=\kappa\widehat\omega.}
\tag{A}
\]

074 的 quartic transport (7)–(12) 本轮仍只作为指定输入，不把其旧 `PROVED` 标签升级成 admission。

### 2. 能落到“具体 differential”而非 cohomology 的精确关系

设 \(u\) 是 074 指定的 quartic-twisted、fixed-\(u\) 局部参数，并令实际 companion representative 为

\[
\widehat\nu
=
\left(1+\sum_{n\ge1}b_nu^n\right)du ,
\]

leading coefficient 已固定为 \(1\)。

要求其 de Rham class 属于 conjugate CM eigenspace：

\[
\varphi^*[\widehat\nu]=-\kappa[\widehat\nu].
\]

这等价于存在唯一取 \(G_\varphi(0)=0\) 的局部 primitive，使得**具体 differential 层**满足

\[
\boxed{
\varphi^*\widehat\nu+\kappa\widehat\nu
=
dG_\varphi .
}
\tag{B}
\]

这已经比“\([\widehat\nu]\) 是 eigenclass”强：它保留 actual representative 与 exact defect。

若

\[
[\varphi](u)=\kappa u+O(u^2),
\]

则 (B) 的最低项甚至立即给出

\[
G_\varphi(u)=2\kappa u+O(u^2),
\]

所以 leading-coefficient-\(1\) 的 companion 本身不可能是严格的 exact eigen-differential。它必须带一个非零 exact defect。

### 3. 关键：\(p\)-层存在一个精确不可辨识族

现在取任意 \(c\in\mathbf Z_p\)，改变 representative：

\[
\boxed{
\widehat\nu_c
=
\widehat\nu+
p\,c\,u^{p-1}du.
}
\tag{C}
\]

这不会改变 leading coefficient，也不改变 de Rham class，因为

\[
p\,c\,u^{p-1}du=c\,d(u^p).
\]

所以所有 \(\widehat\nu_c\) 都满足同一个 cohomological CM eigenline 条件，但它们恰好具有不同的 D25 \(p\)-层。

把 (C) 代入具体 CM defect (B)。新增量为

\[
\begin{aligned}
&\varphi^*(p c u^{p-1}du)
+\kappa\,p c u^{p-1}du\\
&=
p c
\left(
[\varphi](u)^{p-1}[\varphi]'(u)
+\kappa u^{p-1}
\right)du .
\end{aligned}
\]

因此其 \(u^{p-1}du\) coefficient 精确是

\[
\boxed{
p c(\kappa^p+\kappa).
}
\tag{D}
\]

目标素数满足

\[
p\equiv13,19\pmod{24}.
\]

此时 \((-6/p)=-1\)，所以 \(\sqrt{-6}\) 在 \(\mathbf F_{p^2}\) 中受 Frobenius 共轭：

\[
\boxed{\kappa^p\equiv-\kappa\pmod p.}
\tag{E}
\]

由 (D)–(E)，

\[
\boxed{
p c(\kappa^p+\kappa)\equiv0\pmod{p^2}.
}
\tag{F}
\]

这就是所要求的精确 local-differential test，而它给出的答案是一个 **no-go theorem**：

> 即使已经知道完整的 degree-\(6\) CM endomorphism，并在 fixed-\(u\)、leading coefficient \(1\) 规范下要求 actual differential relation (B)，只把该关系控制到模 \(p^2\)，仍然无法区分
> \[
> \widehat\nu,\quad
> \widehat\nu+p c u^{p-1}du
> \]
> 的任何 \(c\bmod p\)。

这不是 cohomology 层的模糊性，而是具体 local differential 上的显式一参数 fiber。

### 4. 074 的下一动作因此需要收紧

074 最后提出“写出 degree-\(6\) CM endomorphism，再比较 \(u^{p-1}du\) coefficient，就确定 \(c_p\)/exact-form \(p\)-layer”。

现在可以确认：**这句话少了一阶精度条件。**

若只得到

\[
\varphi^*\widehat\nu+\kappa\widehat\nu
\pmod{p^2},
\]

则由 (F) 根本不可能确定这一层。

真正能够固定 \(c\bmod p\) 的 endomorphism observable 必须保留下一位：

\[
\boxed{
Q_{\kappa,p}:=
\frac{\kappa^p+\kappa}{p}\pmod p.
}
\tag{G}
\]

因为 (D) 在模 \(p^3\) 下变成

\[
p^2c\,Q_{\kappa,p}.
\]

如果

\[
Q_{\kappa,p}\ne0\pmod p,
\]

那么**模 \(p^3\) 的 actual CM defect** 才能反解 \(c\)。

若单个 \(Q_{\kappa,p}\) 偶然为零，则不能假定唯一性；必须换成此前 portable 思路中更稳健的相邻 CM ports，或寻找另一个 CM endomorphism，使相应 divided eigenvalue difference 为单位。

所以本轮得到的“能固定 representative \(p\)-层”的精确关系应写成：

\[
\boxed{
\frac{
[u^{p-1}du]\,
\bigl(
\varphi^*\widehat\nu+\kappa\widehat\nu-dG_{\rm ref}
\bigr)
}{p^2}
=
c\,Q_{\kappa,p}
\pmod p,
}
\tag{H}
\]

其中 \(G_{\rm ref}\) 必须由一个**明确固定的 reference representative** 计算，而不是任意 exact primitive。

(H) 才是足够强的 local relation；(B) modulo \(p^2\) 不够。

### 5. 与 074 quartic transport 的接口

这也与 074 的 residual-faithful 判断吻合。其

\[
\widehat J_p^{(u)}
\equiv
\kappa_p
\left(
J_p^{(\xi)}
-\frac p2\widehat\alpha_p
\right)
\pmod{p^2}
\]

若成立，只支付了 quartic coordinate transport。它没有支付 (C) 的自由度。

因此现在三层可以更加严格地区分：

\[
\boxed{
\text{quartic transport}
\;\oplus\;
\text{CM class/eigenvalue}
\;\oplus\;
\text{divided exact-defect digit}.
}
\]

前两层即使全部确定，第三层仍然存在；它正是 D25 不允许 quotient 掉的 residual coordinate。

这也意味着：本轮**没有**把 LIFT 关闭，也没有宣称已经核定唯一 companion representative。相反，证明了要核定它至少还缺什么。

### 下一精确动作

下一单元已经非常具体，不需要重新做 CM-\(-24\) 或 quartic transport：

1. 在 074 的 twisted model 上写出一个实际 degree-\(6\) CM map \(\varphi\) 的 formal expansion；
2. 固定 reference companion \(\widehat\nu_{\rm ref}\) 与 \(G_{\rm ref}(0)=0\)；
3. 计算
   \[
   [u^{p-1}du]
   (\varphi^*\widehat\nu_{\rm ref}
   +\kappa\widehat\nu_{\rm ref}-dG_{\rm ref})
   \pmod{p^3};
   \]
4. 同时计算 \(Q_{\kappa,p}\)；若它是单位，用 (H) 唯一恢复 exact \(p\)-layer；
5. 若 \(Q_{\kappa,p}=0\)，立即切换到两个 CM ports 的 divided-difference relation，而不是假称 representative 已唯一。

这正好把问题从“找 CM eigenline”缩成了一个**模 \(p^3\) divided CM-defect certificate**。

本轮材料状态：

\[
\boxed{
\texttt{
UNREVIEWED /
NOT\_ADMITTED /
PORTABLE\_EVIDENCE /
CM\_P\_LAYER\_MOD\_P2\_NO\_GO /
MOD\_P3\_DIVIDED\_DEFECT\_REQUIRED /
REGISTER\_PENDING /
LIFT\_OPEN
}.
}
\]

没有写成 canonical checkpoint/Result，也没有把旧 E267A2 的 session 归到本对话。定时频率、启用状态和通知设置保持不变。