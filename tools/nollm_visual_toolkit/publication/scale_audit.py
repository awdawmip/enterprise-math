"""Fixed-phase scale audit: collision reduction is not free uniformity.

Integer IDs and phase ticks are retained. Trigonometric placement and cell rounding
are inherited floating observers, not certified native geometry.
"""
from __future__ import annotations
import argparse, hashlib, html, json, math, sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from nollm_visual_toolkit import multiplication_lab as lab

SCALES=(Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(5,4),Fraction(3,2),Fraction(2),Fraction(3))

def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def convex_hull(points):
    pts=sorted(set(points))
    if len(pts)<=1:return pts
    lower=[];upper=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def lattice_count(hull):
    """Count integer sites by exact half-plane row intersections, no float hull."""
    if len(hull)<2:return len(hull)
    if len(hull)==2:return math.gcd(abs(hull[1][0]-hull[0][0]),abs(hull[1][1]-hull[0][1]))+1
    total=0;lo_r=min(y for x,y in hull);hi_r=max(y for x,y in hull)
    for q in range(min(x for x,y in hull),max(x for x,y in hull)+1):
        lo,hi=lo_r,hi_r
        for a,b in zip(hull,hull[1:]+hull[:1]):
            dx,dy=b[0]-a[0],b[1]-a[1];rhs=dy*q+dx*a[1]-dy*a[0]
            if dx>0:lo=max(lo,-((-rhs)//dx))
            elif dx<0:hi=min(hi,rhs//dx)
            elif rhs>0:hi=-1;lo=0;break
        total+=max(0,hi-lo+1)
    return total

def quantized_cells(phi, scale):
    cells=defaultdict(list)
    for n,tick in enumerate(phi):
        if n:
            theta=2*math.pi*tick/lab.MODULUS;radius=float(scale)*math.sqrt(n)
            cell=lab.rounded_hex(radius*math.cos(theta),radius*math.sin(theta))
        else:cell=(0,0)
        cells[cell].append(n)
    return dict(cells)

def statistics(phi,scale):
    cells=quantized_cells(phi,scale);hull=convex_hull(cells);capacity=lattice_count(hull)
    count=len(phi);unique=len(cells)
    buckets=[0]*64
    for p in phi[1:]:buckets[p*64//lab.MODULUS]+=1
    mean=(count-1)/64
    out={'scale':[scale.numerator,scale.denominator],'scale_label':str(scale),
         'population':count,'unique_cells':unique,'collision_excess':count-unique,
         'collision_groups':sum(len(v)>1 for v in cells.values()),'max_cell_load':max(map(len,cells.values())),
         'hull_vertices':[list(p) for p in hull],'hull_lattice_sites':capacity,
         'empty_hull_sites':capacity-unique,'hull_fill_ratio':unique/capacity,
         'identity_per_hull_site':count/capacity,'angular_counts':buckets,
         'angular_cv':math.sqrt(sum((x-mean)**2 for x in buckets)/64)/mean,
         'retained_identity_count':sum(map(len,cells.values()))}
    assert out['retained_identity_count']==count and capacity>=unique
    return out,cells

def self_tests():
    fixtures=[[(0,0)],[(0,0),(6,4)],[(0,0),(4,0),(4,4),(0,4)],
              [(-3,-1),(0,-3),(4,0),(1,4)],[(0,0),(5,0),(0,5)]]
    for pts in fixtures:
        h=convex_hull(pts)
        if len(h)>=3:
            brute=sum(all(cross(a,b,(q,r))>=0 for a,b in zip(h,h[1:]+h[:1]))
                      for q in range(-6,7) for r in range(-6,7))
            assert lattice_count(h)==brute
    assert lattice_count(convex_hull(fixtures[0]))==1
    assert lattice_count(convex_hull(fixtures[1]))==3
    assert lattice_count(convex_hull(fixtures[2]))==25
    assert lattice_count(convex_hull(fixtures[4]))==21
    return 7

def write(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')

def run(out,count=65536):
    tests=self_tests();out=Path(out);out.mkdir(parents=True,exist_ok=True)
    spf=lab.smallest_factors(count);rows=[];tables={}
    for mode in ('golden','rank','zero'):
        phi=lab.phases(spf,lab.prime_phases(spf,mode));tables[mode]=phi
        invariant=None
        for scale in SCALES:
            row,cells=statistics(phi,scale);row['mode']=mode;rows.append(row)
            if invariant is None:invariant=row['angular_counts']
            assert invariant==row['angular_counts']
            if scale==1:
                write(out/f'cells_{mode}_scale1.json',{'schema':'LAB_INTEGER_ID_FIBERS_V1','mode':mode,'scale':[1,1],
                      'cells':[{'coord':list(p),'ids':ids} for p,ids in sorted(cells.items())]})
            print(mode,str(scale),row['unique_cells'],row['hull_lattice_sites'],round(row['hull_fill_ratio'],6),flush=True)
    write(out/'phase_ticks.json',{'modulus':lab.MODULUS,'zero_phase':None,'tables':tables})
    result={'schema':'NOLLM_SCALE_AUDIT_V1','population':count,'modes':['golden','rank','zero'],'rows':rows,
       'self_tests':tests,'scale_invariant_histograms_checked':len(rows),
       'integer_fiber_identity_counts_checked':len(rows),
       'source':'Unmodified multiplication_lab phases and rounded_hex; fixed 16-bit definitions',
       'limits':['Finite 0..65535 benchmark by default, not optimality or semantic quality.',
                 'Lattice hull counts exact for computed integer cells; trig placement/quantization remains floating.',
                 'High hull fill can occur for a one-dimensional line; compare angular CV and footprint.',
                 'No new mathematical foundation, native geometry or Nollm runtime changes.']}
    write(out/'results.json',result)
    table=''.join(f'<tr data-mode="{r["mode"]}"><td>{r["mode"]}</td><td>{r["scale_label"]}</td><td>{r["unique_cells"]:,}</td><td>{r["collision_excess"]:,}</td><td>{r["hull_lattice_sites"]:,}</td><td>{r["hull_fill_ratio"]:.2%}</td><td>{r["angular_cv"]:.5f}</td></tr>' for r in rows)
    page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>数场尺度审计</title><style>body{font:15px/1.7 system-ui;max-width:1100px;margin:auto;padding:24px}h1{font-size:27px}table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}th,td{padding:9px;border-bottom:1px solid #ddd;text-align:right}th:first-child,td:first-child{text-align:left}.scroll{overflow:auto}button,a{margin:5px;padding:7px}aside{padding:14px;border:1px solid #bbb;border-radius:8px}</style><h1>数场尺度审计 / 不再把放大当成均匀化</h1><p>同一批整数、同一组精确相位，只改变相对于固定六角 Cell 的布局尺度 C。全部计算，不抽样。</p><aside><b>同时看三项：</b>重复占格、占地大小、方向分布。全零相位即使凸包填充率 100%，仍然只是一条线。相机缩放没有参与此计算。</aside><p><button data-mode="all">全部</button><button data-mode="golden">黄金角</button><button data-mode="rank">质数序号等分</button><button data-mode="zero">全零反例</button></p><div class="scroll"><table><thead><tr><th>相位规则</th><th>C</th><th>占用格</th><th>重复标签</th><th>凸包格容量</th><th>格点填充率</th><th>角向 CV</th></tr></thead><tbody>__ROWS__</tbody></table></div><p><a href="../site/index.html">进入完整交互数场</a><a href="results.json">全量统计 JSON</a><a href="phase_ticks.json">全部精确相位</a><a href="cells_golden_scale1.json">逐格反查全部身份</a></p><p>这里的六角坐标仍是 A2 兼容观察，不是原生 X6。取整后的整数凸包计数精确，三角函数与落格仍是浮点观察。结果不证明无限均匀分布。</p><script>for(const b of document.querySelectorAll('button'))b.onclick=()=>{for(const r of document.querySelectorAll('tbody tr'))r.hidden=b.dataset.mode!=='all'&&r.dataset.mode!==b.dataset.mode};</script></html>'''
    (out/'index.html').write_text(page.replace('__ROWS__',table),encoding='utf-8')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--count',type=int,default=65536);a=p.parse_args();run(a.out,a.count)
