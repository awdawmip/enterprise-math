"""Standalone replay: direct menus -> full regional census -> integer duals.

The final package puts dual_*.json under duals/. During development it also
accepts the identical files under lp6/. No LP or floating-point package is used.
"""
import argparse,json,subprocess,tempfile
from itertools import combinations,product
from pathlib import Path
from verify_exchange import MENUS,main as verify_small
HERE=Path(__file__).resolve().parent

def coverage():
    initial=json.loads((HERE/'initial.json').read_text());rows=initial['groups'];prices=initial['costs']
    symmetry=json.loads((HERE/'neighborhood_symmetry.json').read_text())
    g=symmetry['point_permutation'];perm=symmetry['class_permutation']
    assert g==[25*(p//5%5)+5*(p%5)+p//25 for p in range(125)]
    assert all(set(g[p]for p in row)==set(rows[perm[i]])for i,row in enumerate(rows))
    # Coordinate permutation transports each complete native observation menu.
    for t,menu in enumerate(MENUS):
        target_menu=MENUS[(t//125)*125+g[t%125]]
        for p,(active,target)in enumerate(menu):
            rotated_active=(active>>1)|((active&1)<<2)
            rotated_target=(target//5%5)+5*(target//25)+25*(target%5)
            assert target_menu[g[p]]==(rotated_active,rotated_target)
    jobs=json.loads((HERE/'jobs6_reps.json').read_text())
    actual={tuple(job['selected']):job for job in jobs};assert len(actual)==len(jobs)==312
    expected=set()
    for selected in combinations(range(12),6):
        once=tuple(sorted(perm[p]for p in selected));twice=tuple(sorted(perm[p]for p in once))
        expected.add(min(selected,once,twice))
    assert set(actual)==expected
    for selected,job in actual.items():
        assert job['points']==sorted(sum((rows[i]for i in selected),[]))
        assert job['budget']==sum(prices[i]for i in selected)-1 and job['k']==6
    return {'all_six_class_choices':924,'representatives':312,'cost_preserving_order_three_action':True}

def make_observations(path):
    pair=[[0]*125 for _ in range(125)];triples=set()
    for t,menu in enumerate(MENUS):
        cells={}
        for p,(active,target)in enumerate(menu):cells.setdefault(active,{}).setdefault(target,[]).append(p)
        for targets in cells.values():
            groups=list(targets.values())
            for a,b in combinations(groups,2):
                for x,y in product(a,b):pair[x][y]|=1<<t;pair[y][x]|=1<<t
            for a,b,c in combinations(groups,3):
                for x,y,z in product(a,b,c):triples.add(tuple(sorted((x,y,z))))
    assert len(triples)==47000
    with path.open('wb')as f:
        for row in pair:
            for value in row:f.write(value.to_bytes(32,'little'))
        for triple in sorted(triples):f.write(bytes(triple))
    return {'menus':250,'forbidden_triples':47000}

def replay(work):
    work.mkdir(parents=True,exist_ok=True)
    summary={'coverage':coverage()}
    obs=work/'obs';summary['observations']=make_observations(obs)
    for name,source in [('census','regional.cpp'),('check_dual','verify_dual.cpp')]:
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/source,'-o',work/name],check=True)
    duals=HERE/'duals'
    if not duals.exists():duals=HERE/'lp6'
    combined=HERE/'duals.json'
    certificates={c['job']:c for c in json.loads(combined.read_text())} if combined.exists() else None
    jobs=json.loads((HERE/'jobs6_reps.json').read_text());verified=[]
    if certificates is not None:assert set(certificates)=={j['job']for j in jobs}
    for spec in jobs:
        jid=spec['job'];certificate=certificates[jid] if certificates is not None else json.loads((duals/f'dual_{jid}.json').read_text())
        assert certificate['job']==jid and certificate['exclusion']
        assert set(map(int,certificate['point_weights']))==set(spec['points'])
        job=work/'job.txt';job.write_text(f"{jid} 6 {spec['budget']} {len(spec['points'])} "+' '.join(map(str,spec['points']))+'\n')
        weights=[0]*125
        for p,value in certificate['point_weights'].items():weights[int(p)]=value
        weight_file=work/'weights.txt';weight_file.write_text(f"{certificate['scale']} {certificate['class_weight']}\n"+' '.join(map(str,weights))+'\n')
        generated=json.loads(subprocess.check_output([work/'census',obs,job,work],text=True))
        bank=work/f'bank_{jid}'
        checked=json.loads(subprocess.check_output([work/'check_dual',job,bank,weight_file],text=True))
        assert checked['columns_checked']==generated['classes']
        assert checked['lower_numerator']==certificate['scaled_lower_bound']
        assert checked['budget_numerator']==certificate['scaled_budget']
        assert checked['minimum_slack']==certificate['minimum_column_slack']
        checked['census_nodes']=generated['enum_nodes'];verified.append(checked);bank.unlink()
        with (work/'checked.jsonl').open('a')as f:f.write(json.dumps(checked,sort_keys=True)+'\n')
        if len(verified)%20==0:print(json.dumps({'verified':len(verified),'total':len(jobs)}),flush=True)
    summary['regional']={'verified':len(verified),'all_excluded':True,'columns':sum(r['columns_checked']for r in verified),'census_nodes':sum(r['census_nodes']for r in verified),'minimum_margin_numerator':min(r['lower_numerator']-r['budget_numerator']for r in verified),'denominator':1000000}
    verify_small(work/'exchange_verification.json');summary['exchange']=json.loads((work/'exchange_verification.json').read_text())
    (work/'replay_result.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--work',type=Path);a=p.parse_args()
    if a.work:replay(a.work.resolve())
    else:
        with tempfile.TemporaryDirectory()as tmp:replay(Path(tmp))
