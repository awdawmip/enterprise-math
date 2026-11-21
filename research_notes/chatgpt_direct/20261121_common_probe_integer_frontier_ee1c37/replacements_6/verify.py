"""Audit or rerun the completed radius-five and radius-six replacement proof."""
from hashlib import sha256
from pathlib import Path
import argparse
import importlib.util
import json
import subprocess

HERE=Path(__file__).resolve().parent


def outside_solver(source):
    a=source.index('bool solve(');b=source.index('\nint main(',a)
    return source[:a]+source[b:]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--baseline',type=Path,required=True,
                   help='The C bounded_replacements directory, unchanged in the combined package')
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--mode',choices=['audit','full'],default='audit')
    a=p.parse_args();a.work.mkdir(parents=True,exist_ok=True);baseline=a.baseline.resolve()
    binding=json.loads((HERE/'bindings.json').read_text())
    for name,expected in binding['sha256'].items():
        assert sha256((baseline/name).read_bytes()).hexdigest()==expected
    for name,expected in binding['own_source_sha256'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest()==expected
    old=outside_solver((baseline/'bounded_replacements_color.cpp').read_text())
    assert outside_solver((HERE/'solve_color.cpp').read_text())==old
    assert outside_solver((HERE/'solve.cpp').read_text())==old.replace('radius<=5','radius<=6')
    dual=json.loads((baseline/'point_dual.json').read_text())
    point={int(k):v for k,v in dual['point_weights'].items()}
    expected=[1,0,0]+[dual['class_weight']]*10+[point.get(i,0)for i in range(125)]
    assert list(map(int,(HERE/'global_color_dual.txt').read_text().split()))==expected
    spec=importlib.util.spec_from_file_location('replacement_C_native',baseline/'verify.py')
    native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    rows,costs=native.initial()
    positive=native.check_positive(json.loads((HERE/'positive_control.json').read_text()),rows)
    receipts={}
    for name,radius,nodes,candidates in [
        ('radius5_global.json',5,331464,522700),
        ('radius5_color.json',5,57968,522700),
        ('radius5_color_original.json',5,3513770,522700),
        ('radius6.json',6,35083297,3599794)]:
        r=json.loads((HERE/name).read_text())
        assert r['complete'] and not r['found'] and r['budget']==9995 and r['radius']==radius
        assert r['search_nodes']==nodes and r['legal_candidates_before_price_cap']==candidates
        receipts[name]=r
    result={'source_bindings_checked':True,'candidate_generator_unchanged_except_radius_limit':True,
            'positive_control':positive,'receipts':receipts,'mode':a.mode,
            'searches_reexecuted':False,'review_status':'NOT_REVIEWED'}
    if a.mode=='full':
        result['observations']=native.observations(a.work/'obs')
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'solve.cpp','-o',a.work/'solve'],check=True)
        for radius in (5,6):
            cmd=[str(a.work/'solve'),str(a.work/'obs'),str(baseline/'initial.txt'),str(radius),'9995',str(HERE/'global_color_dual.txt')]
            actual=json.loads(subprocess.check_output(cmd,text=True))
            assert actual==receipts['radius5_global.json'if radius==5 else'radius6.json']
        control=json.loads(subprocess.check_output([str(a.work/'solve'),str(a.work/'obs'),str(baseline/'initial.txt'),
                            '2','9996',str(HERE/'global_color_dual.txt')],text=True))
        result['rerun_positive_control']=native.check_positive(control,rows)
        result['searches_reexecuted']=True
    result['all_checks_passed']=True
    (a.work/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
