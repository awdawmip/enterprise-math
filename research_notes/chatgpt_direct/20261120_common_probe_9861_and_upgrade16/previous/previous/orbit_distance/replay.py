"""Evaluate whole-class overlap and optimal label rematching on complete affine orbits."""
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,os,subprocess,sys
HERE=Path(__file__).resolve().parent
def compare(previous):
    fourth=previous/'previous'
    third=fourth/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(third/'previous')
    sys.path.insert(0,str(third/'group'))
    from generate import maps
    linear,tr,_=maps()
    affine=[bytes(t[y] for y in f)for f in linear for t in tr]
    assert len(set(affine))==len(affine)==12000
    def load(path):return json.loads(path.read_text())
    eleven=load(fourth/'eleven_six_counts/groups.json')+[load(previous/'eleven_equal/groups.json')]
    twelve=load(previous/'c3/groups.json')
    thirteen=load(third/'asymmetric8721/groups.json')
    def labels(rows):
        ids={v:j for j,r in enumerate(rows)for v in r}
        assert sorted(sum(rows,[]))==list(range(125))
        return ' '.join(str(ids[i])for i in range(125))
    with TemporaryDirectory()as tmp:
        p=Path(tmp)
        (p/'maps').write_bytes(b''.join(affine))
        subprocess.run(['c++','-O2','-std=c++17',HERE/'distance.cpp','-o',p/'distance'],check=True)
        def run(a,b):
            data=f'{len(a)} {len(b)}\n{labels(a)}\n{labels(b)}\n'
            raw=subprocess.check_output([p/'distance',p/'maps'],input=data,text=True)
            rows=[tuple(map(int,s.split()))for s in raw.splitlines()]
            assert len(rows)==12000
            ma=max(x for _,x,_ in rows);mb=max(h for _,_,h in rows)
            aa=next(i for i,x,h in rows if x==ma)
            bb=next(i for i,x,h in rows if h==mb)
            return dict(maximum_intact_classes=ma,minimum_changed_histories=125-mb,
                        common_class_histogram_by_affine_image=dict(sorted(Counter(x for i,x,h in rows).items())),
                        greatest_history_overlap=mb, sample_maps=[aa,bb],
                        least_changed_histories_at_maximum_intact_classes=125-max(h for i,x,h in rows if x==ma))
        return {'symmetric_11_to_symmetric_12':[run(t,twelve)for t in eleven],
                'symmetric_12_to_global_13':run(twelve,thirteen)}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',required=True,type=Path)
    print(json.dumps(compare(p.parse_args().previous.resolve()),indent=2,sort_keys=True))
