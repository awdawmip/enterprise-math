"""Replay the one completed seven-class region and its positive control."""
import argparse,json,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT))
from replay import make_observations
from verify_exchange import evaluate

def run(work):
    work.mkdir(parents=True,exist_ok=True)
    obs=work/'obs';make_observations(obs)
    for exe,src in [('census',ROOT/'regional.cpp'),('cover',HERE/'cover_region.cpp')]:
        subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',src,'-o',work/exe],check=True)
    job=HERE/'job_3050.txt';weights=HERE/'weights_3050.txt'
    values=list(map(int,weights.read_text().split()))
    assert len(values)==127 and 0<values[0]<=10**6
    assert all(abs(v)<10**12 for v in values[1:])
    census=json.loads(subprocess.check_output([work/'census',obs,job,work],text=True))
    assert census['classes']==3661086 and census['enum_nodes']==44727996
    bank=work/'bank_3050'
    negative=work/'negative.json'
    subprocess.run([work/'cover',job,bank,weights,negative],check=True)
    neg=json.loads(negative.read_text())
    assert neg['complete'] and not neg['found'] and neg['search_nodes']==110
    line=job.read_text().split();line[2]='6270'
    equal=work/'equal.txt';equal.write_text(' '.join(line)+'\n')
    positive=work/'positive.json'
    subprocess.run([work/'cover',equal,bank,weights,positive],check=True)
    pos=json.loads(positive.read_text())
    assert pos['complete'] and pos['found'] and pos['cost']==6270
    initial=json.loads((ROOT/'initial.json').read_text())['groups']
    selected=[0,1,2,6,7,8,9]
    assert {tuple(g)for g in pos['groups']}=={tuple(initial[j])for j in selected}
    assert sum(evaluate(tuple(g))for g in pos['groups'])==6270
    result={'old_class_indices':selected,'census':census,'negative':neg,'positive':pos,'direct_menu_positive_control':True,'scope':'one seven-class representative only'}
    (work/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    bank.unlink();print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--work',type=Path);a=p.parse_args()
    if a.work:run(a.work.resolve())
    else:
        with tempfile.TemporaryDirectory()as tmp:run(Path(tmp))
