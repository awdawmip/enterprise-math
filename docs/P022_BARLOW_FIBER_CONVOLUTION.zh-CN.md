# P022 — 检查点 Fiber 的乘法卷积代数

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE RE-ENCODING / PRIOR-ART SENSITIVE`  
归属：`program/p022-geometry-v2`  
依赖：P011 完整 fiber/collision spectrum；Barlow selected-layer fiber 因子化

## 1. 完整 fiber state

对有限 observation quotient `O` 定义

\[
c_s(O)=\#\{y:|O^{-1}(y)|=s\}.
\]

有限 profile

\[
\boxed{C_O=(c_1,c_2,\ldots)}
\]

是完整 fiber-size multiset。P011 已证明该 profile 与完整 collision spectrum

\[
(J_1,J_2,\ldots)
\]

通过有限 binomial inversion 互相恢复。

## 2. Segment profile 与乘法卷积

长度 `ell` 的 prefix-imbalance segment 定义

\[
\boxed{
B_\ell(s)=\#\left\{j:\binom{\ell}{j}=s\right\}.
}
\]

对正整数上的有限函数定义

\[
\boxed{
(f\star_\times g)(n)=\sum_{ab=n}f(a)g(b).
}
\]

独立 segments 的 fiber sizes 相乘，因此最终层被观察时

\[
\boxed{
C_O=B_{\ell_1}\star_\times\cdots\star_\times B_{\ell_m}.
}
\]

若末尾还有完全未观察 tail `u`，所有 fiber sizes 再统一乘

\[
2^u.
\]

## 3. P022-FC02 — power moments 是卷积 characters

定义

\[
\Phi_r(f)=\sum_s f(s)s^r.
\]

则

\[
\boxed{
\Phi_r(f\star_\times g)=\Phi_r(f)\Phi_r(g).
}
\]

单 segment 上

\[
\Phi_r(B_\ell)=\sum_j\binom{\ell}{j}^r=F_r(\ell),
\]

立即得到

\[
\boxed{M_r=2^{ru}\prod_jF_r(\ell_j).}
\]

所以 higher-collision note 的 moment 因子化，本质是完整 fiber convolution 的 character evaluation。

## 4. P022-FC03 — 完整 P011 spectrum 是等价编码

P011 有

\[
J_k=\sum_s c_s\binom{s}{k},
\]

并可整数反演回全部 `c_s`。故

\[
\boxed{
C_O\longleftrightarrow(J_1,J_2,\ldots)
}
\]

以及 collision polynomial

\[
K_O(t)=\sum_{k\ge1}J_k t^k
\]

都完整编码本 quotient 的 fiber-size profile。

## 5. P022-FC04 — 最终层已观察时，profile 唯一恢复 segment-length multiset

每个正长度 segment 都有：

1. 恰好两个 singleton fibers，故 `B_ell(1)=2`；
2. `ell>=2` 时最小 non-singleton fiber size 恰好为
   \[
   \binom{\ell}{1}=\ell;
   \]
3. 该最小 nontrivial size 的 multiplicity 为
   \[
   \beta_2=1,\qquad \beta_\ell=2\ (\ell\ge3).
   \]

这些事实让 convolution 在 fiber size 递增方向呈三角结构。

### Segment 数与总长度

若有 `m` 个 segments，则只有全部 segment 都选 singleton 才得到总 fiber size 1，因此

\[
\boxed{c_1=2^m.}
\]

故 `m` 可恢复。

同时

\[
\sum_s sc_s=2^N
\]

恢复 microscopic 总长度 `N`。

### 逐长度剥离

假设所有 `<n` 的 segment counts 已知，其 convolution 为 `P_<n`，数量为 `m_<n`。

完整 profile 的 `c_n` 中：

- 未知长度 `>n` 的 segment 只能选 singleton；
- 已知短 segments 的贡献为
  \[
  2^{m-m_{<n}}P_{<n}(n);
  \]
- 长度 `n` 的 segment 贡献 residual
  \[
  t_n\beta_n2^{m-1}.
  \]

所以

\[
\boxed{
t_n=
\frac{c_n-2^{m-m_{<n}}P_{<n}(n)}{\beta_n2^{m-1}}.
}
\]

从 `n=2` 递推到 `N` 后，再由

\[
t_1=m-\sum_{n\ge2}t_n
\]

恢复长度 1 的个数。

因此

\[
\boxed{
C_O\Longleftrightarrow\{\ell_1,\ldots,\ell_m\}.
}
\]

右侧是 multiset，不含顺序。

## 6. P022-FC05 — 未观察 tail 也可恢复

若末尾 tail 长度为 `u`，所有 constrained fibers 都乘 `2^u`。normalized constrained profile 本来有 singleton fibers，因此完整 profile 的最小 fiber size 恰为

\[
\boxed{2^u.}
\]

故

\[
\boxed{u=v_2(\min\operatorname{supp}C_O).}
\]

除去该因子后用 FC04 恢复 observed segment multiset。

所以一般 selected-layer quotient 满足

\[
\boxed{
C_O
\Longleftrightarrow
(\{\ell_1,\ldots,\ell_m\},u).
}
\]

结合 P011：

\[
\boxed{
K_O(t)
\Longleftrightarrow
(\text{无序 observed segment geometry},\text{hidden tail}).
}
\]

## 7. 精确边界：顺序仍然丢失

乘法卷积可交换，所以完整 profile 与 collision polynomial 不能恢复 segment order。

例如

\[
(1,2,3)
\]

和

\[
(3,2,1)
\]

得到相同完整 collision data，却对应不同 checkpoint locations

\[
(1,3,6)
\]

与

\[
(3,5,6).
\]

所以完整 P011 statistics 恢复的是**无序 observation geometry**，不是时间/空间有序排布。

## 8. 低阶统计不足

完整 spectrum 的要求是真实的：`J_2` 存在固定 `N,m` 的精确 alias，不同 segment multisets 可具有相同 pair collision。相关反例见 `P022_BARLOW_PAIR_COLLISION_ALIAS.*`。

## 9. Prior-art 边界

Dirichlet/multiplicative convolution、binomial rows、power moments、Stirling/binomial inversion 都是经典数学。本项目的特定内容是：Barlow checkpoint quotient 的 fiber state 恰由这一卷积构成，并且其完整 P011 statistics 可三角反演回无序 checkpoint geometry。

## 10. 可执行资产

- `src/enterprise_math/p022_barlow_fiber_convolution.py`；
- `tests/test_p022_barlow_fiber_convolution.py`；
- `src/enterprise_math/p022_barlow_collision_geometry.py`；
- `tests/test_p022_barlow_collision_geometry.py`。