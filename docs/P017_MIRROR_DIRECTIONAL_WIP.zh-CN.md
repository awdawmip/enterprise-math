# P017 Mirror Certificate — 方向化细化 WIP

状态：`ACTIVE PROGRAM RESEARCH / NOT CANONICAL`  
Owner：P017 program layer  
依赖：canonical mirror MC01–MC06  
创新性：`NOVELTY_UNVERIFIED`

## MC07 候选 — 保留 first moment 的两个方向

对每个 surviving radius `r`，令

\[
a_r=|\mathcal P_-(r)|,
\qquad
b_r=|\mathcal P_+(r)|.
\]

旧证书会立刻把它们压成

\[
J=\sum_r(a_r+b_r).
\]

这里先保留方向：

\[
J_-:=\sum_r a_r,
\qquad
J_+:=\sum_r b_r.
\]

令 `S=|S_k|`，定义 directional excess slacks

\[
U_-:=J_--S,
\qquad
U_+:=J_+-S.
\]

已有 cross-side slack 为

\[
V=E-J_- -J_+ +S
 =\sum_r(a_r-1)(b_r-1).
\]

若假设整个 basin prime-free，则每个 surviving mirror side 都必须 composite，因此

\[
a_r\ge1,
\qquad
b_r\ge1.
\]

令

\[
x_r=a_r-1,
\qquad
y_r=b_r-1,
\]

则

\[
U_- =\sum_r x_r\ge0,
\qquad
U_+ =\sum_r y_r\ge0,
\qquad
V=\sum_r x_ry_r\ge0.
\]

由于所有项非负，

\[
\boxed{
V=\sum_r x_ry_r
\le
\left(\sum_r x_r\right)
\left(\sum_r y_r\right)
=U_-U_+.
}
\]

因此 prime-free basin 必须满足

\[
\boxed{
U_-\ge0,
\quad
U_+\ge0,
\quad
V\ge0,
\quad
V\le U_-U_+.
}
\]

任何违反都构成 sufficient prime certificate。

## MC07 严格包含 MC06

旧 slack 为

\[
U=U_-+U_+.
\]

若 `U<0`，至少一个 directional slack 为负。

若 `V<0`，MC07 同样直接检测。

若旧 quadratic certificate 触发

\[
4V>U^2,
\]

而两个 directional slacks 均非负，则

\[
U_-U_+\le\frac{(U_-+U_+)^2}{4}=\frac{U^2}{4}<V.
\]

所以每个 MC06 certificate 都自动是 MC07 certificate。

## 有限压力测试

直接 bounded check `3<=k<=1000` 得到：

- MC06 certificates：`733`；
- MC07 directional certificates：`740`；
- 新增的 MC07-only roots：

`137, 171, 233, 293, 336, 470, 570`。

其中除 `233` 外的 6 个 root 已经违反某一侧 first-moment 条件。`k=233` 时

\[
U_-=0,
\qquad
U_+=4,
\qquad
V=1,
\]

旧 total certificate 无法得出矛盾，但 directional product envelope 直接给出

\[
1>0\cdot4.
\]

该计算只是压力测试证据，不是全体 `k` 的证明。

## 负面测试：不重新开启无结构 moment 扩张

我们还测试了最自然的下一扩张：加入左右 same-side second moments，再用 Cauchy bound 控制 `V`。在 `k<=1000` 上，它**没有增加任何一个** MC07 之外的 certificate。

因此这条 moment-expansion 路线在这里停止。下一步必须引入结构上不同的信息，例如 bounded least-factor gate、exact support closure，或者与 quotient/root windows 的非循环耦合。

## 实现

Program branch 资产：

- `src/enterprise_math/p017_mirror_directional.py`；
- `tests/test_p017_mirror_directional.py`。

方向化计数完全复用 MC01 的 anchor Möbius / CRT machinery，不引入新的外部 theorem。
