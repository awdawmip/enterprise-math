# 同作者交叉核对：锚定障碍稿引理 1

Date: 2026-11-21  
Context: EM-DIRECT-B5750A 原母任务内 unshared 作者交叉核对。  
Scope: rh_joint_anchor/ANCHORED_ENVELOPE_OBSTRUCTION.md §1 的解析推导。  
Status: NO_GAP_FOUND_IN_THIS_LEMMA；不是独立 Project Review，不包括全稿或全部实现审查。

## 被核对的命题

对任意整数 \(n\ge2,d\ge2\)，
\[
\left|P_d(n)-\frac{B_d(n)}n\right|\le\frac{d^2}{8n^2}.
\]
前提是此前已证明的两个精确 Fourier/积分表示，采用原稿的相位与端点约定。
本核对没有重新运行旧证书全集。

## 常数与统一性

令 \(u=e^{2\pi i\ell/d}\ne1\)，
\(f_u(t)=t/(1-tu)^2\)。直接求导：
\[
f'_u(t)=\frac{1+tu}{(1-tu)^3}.
\]
对 \(0<t\le1\)，
\[
|1-tu|^2=(1-t)^2+t|1-u|^2\ge t|1-u|^2,
\]
故
\[
|f'_u(t)|\le2t^{-3/2}|1-u|^{-3}.
\]
从 \(t\) 积到 1 得
\[
|f_u(t)-f_u(1)|
\le4(t^{-1/2}-1)|1-u|^{-3}.
\]
乘 \(t^{n-1}\) 后积分，常数恰为
\[
4\left(\frac1{n-1/2}-\frac1n\right)
=\frac2{n(n-1/2)}.
\]
对 \(n\ge2\) 此积分收敛；在 \(t=0\) 的点态粗界发散不会破坏积分步骤。

若 \(k=\min(\ell,d-\ell)\)，弦界给出
\[
|1-u|=2\sin(\pi k/d)\ge4k/d.
\]
每个 \(k\) 最多对应两个 \(\ell\)，故即使 \(d\) 为偶数，也有正确方向的上界
\[
\sum_{\ell=1}^{d-1}|1-u|^{-3}
\le2(d/4)^3\sum_{k\ge1}k^{-3}
\le2(d/4)^3(3/2)=3d^3/64.
\]
加上 Fourier 外因子 \(1/d\) 后，总误差至多
\[
\frac{3d^2}{32n(n-1/2)}.
\]
末步
\[
\frac3{32n(n-1/2)}\le\frac1{8n^2}
\]
等价于 \(n\ge2\)，在 \(n=2\) 的比较处达到相等。

因此该推导没有隐含 \(d\le n\)、固定 \(d\) 或极限与求和交换要求。
它确实给出同时关于 \(n,d\) 的统一误差界。
本核对未发现引理 1 的符号、常数或积分可积性缺口。
