# Six-axis derived foundation V2 closure addenda

本目录的 V1 文件保持原验证字节；V2 只增加闭合层文件。

运行：

```bash
python check_six_axis.py
python check_ports.py
python check_mutations.py
python check_closure_addenda.py
python check_independent_reference.py
```

`closure_addenda.py` 提供：
- `triangle_products` / `is_fcc_orientation_connection` / `gauge_to_all_negative`；
- `quadratic_components` / `quadratic_spectral_extension` / `metric_eigenvalues`。

`check_independent_reference.py` 不 import `six_axis.py` 或 `vendor.atlas_brc.py`，从 K4/S4、tetrahedral carrier、gluing equations 与 metric symmetry 独立重建核心结果。

此目录是派生共同层，不声明 native X6、唯一 native global metric 或完整 native rotation group。
