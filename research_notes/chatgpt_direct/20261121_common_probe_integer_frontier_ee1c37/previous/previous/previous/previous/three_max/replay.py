"""Enumerate low-price covers after fixing the exact number of maximum-size classes."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,subprocess,sys
HERE=Path(__file__).resolve().parent

def test(older,options,jobs):
    src=older/'strata'
    sys.path.insert(0,str(src))
    from orbits import observations,packings,setbits
    bad,pair=observations()
    result={}
    with TemporaryDirectory()as tmp:
        work=Path(tmp)
        for label,target in options.items():
            k=int(label)
            weights=json.loads((src/f'weights{k}.json').read_text())
            _,reps,types=packings(bad,k)
            assert len(weights)==len(types)
            exe=work/f'check{k}'
            subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',f'-DNMAX={k}',str(HERE/'search.cpp'),'-o',str(exe)],check=True)
            def check(arg):
                i,row=arg
                space=(1<<125)-1
                for mask in reps[types[i][0]]:space^=mask
                points=list(setbits(space));ix={v:j for j,v in enumerate(points)}
                assert len(points)==125-13*k
                file=work/f'obs{k}-{i}'
                with file.open('wb')as f:
                    for x in points:
                        for y in points:
                            h=sum(1<<ix[v] for v in setbits(bad[x][y]&space))
                            f.write(h.to_bytes(16,'little'));f.write(pair[x][y].to_bytes(32,'little'))
                values=' '.join(map(str,[1000,row['peak'],*row['point_weights']]))+'\n'
                line=subprocess.check_output([exe,file,str(target)],input=values,text=True)
                allowance,catalog,nodes,found=map(int,line.split());assert not found
                return [allowance,catalog,nodes]
            with ThreadPoolExecutor(max_workers=jobs)as pool:allstats=list(pool.map(check,enumerate(weights)))
            result[label]=dict(budget=target,lower_bound=target+1,types=len(types),checks=allstats,visits=sum(t[2]for t in allstats))
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True);p.add_argument('--jobs',type=int,default=4)
    a=p.parse_args();expect=json.loads((HERE/'result.json').read_text());out=test(a.older.resolve(),{k:v['budget']for k,v in expect.items()},a.jobs)
    assert out==expect;print(json.dumps(out,sort_keys=True))
