# 用相邻两次舍入读数作逐渐加长的线性外推

在相邻临界窗口令 $L_c=2^p/c^{9/4}\to L\in(0,\infty)$，$r=r_c$ 为趋于无穷且 $r=o(c)$ 的整数。从 $c,c+1$ 两次格编号外推至 $c+r$。容许各次用任意独立的已知格偏移 $\alpha_j$，定义
$$Y_j=2^p g(c+j;v,w),\quad K_j=\lfloor Y_j+\alpha_j\rfloor,\quad \widehat Y_j=K_j-\alpha_j,$$
$$ E_{r,c}=\widehat Y_r-r\widehat Y_1+(r-1)\widehat Y_0. $$
这是用格下端点（已减去已知的格平移）给出的三读数差，各格同平移时为整数。令 $X=(v/c,w/c)$，$B_2(X)=\partial_s^2G_{s^{-15/4}}|_{s=1}$。以全部模板等权，有下列可直接检验的规律，联合于宏观源点。

* 若 $r/\sqrt c\to d\in[0,\infty)$，则
$$ (X,E_{r,c}/r)\Longrightarrow (X,\Theta_1-\Theta_0+LdB_2(X)/2). $$
其中 $\Theta_0,\Theta_1$ 彼此独立均匀并且独立于 $X$。特别在 $r=o(\sqrt c)$，归一外推误差的密度是 $1-|t|$，$-1\le t\le1$，与源点无关。
* 若 $\sqrt c=o(r)$ 且 $r=o(c)$，则
$$ (X,\sqrt c\,E_{r,c}/r^2)\Longrightarrow(X,LB_2(X)/2). $$
在各个正规内紧区域，后一分量与 $L_c B_2(X)/2$ 的差一致趋零。因此使用三个普通舍入读数，可以在此范围反演相应模板的极限谱曲率 $B_2$，无需实际的准确有理读数。

证明写偏移后相位 $\Theta_{j,c}=Y_j+\alpha_j-K_j\in[0,1)$。三格端点外推误差准确等于
$$ E_{r,c}=Y_r-rY_1+(r-1)Y_0 +r(\Theta_{1,c}-\Theta_{0,c})+\Theta_{0,c}-\Theta_{r,c}. $$
前两相位在临界窗口联合 Haar，保持与源独立，见 CRITICAL_PHASES.md。第三相位只用其有界性，不要求远库存与相邻二库存的相位独立。在正规内紧集对实际的有限 $U_c(s,X)$ 函数展开，两次线性项完全消去。其二阶偏导在 $1\le s\le1+r/c$ 齐近 $B_2(X)$，因此一致有
$$ Y_r-rY_1+(r-1)Y_0
=\frac{L_c}{2\sqrt c}\big((r^2-r)B_2(X)+o(r^2)\big). $$
这里用 $r/c\to0$ 与有限谱定阶导数紧收敛；未将有限梯度替换成极限梯度。除以两种指定尺度即得，其余源区域可用任意小面积控制。若几何偏移使用绝对格编号而各自不同，直接将已知偏移差补回即可。
