"""Certificate for the local Hamming distance of the safe 11-message fallback from a global one-read table."""
import argparse,json,tempfile,subprocess
from pathlib import Path
from translation import forbidden
from hybrid import CODE
def run():
    here=Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory() as tmp:
        w=Path(tmp);src=here/'neighborhood.cpp';p=w/'solve';e=w/'edges';c=w/'color';c.write_text(' '.join(map(str,CODE)));e.write_text('\n'.join(' '.join(map(str,t)) for t in sorted(forbidden())))
        subprocess.run(['c++','-std=c++17','-O3',str(src),'-o',str(p)],check=True)
        radius,nodes,hit=map(int,subprocess.check_output([str(p),str(e),str(c),'15'],text=True).split())
        assert radius==15 and not hit
    return dict(status='PASS',search_nodes=nodes,excluded_hamming_ball_radius=radius,reference_table='hybrid.py/CODE',distance_lower_bound=radius+1,conditional='a valid 11-message common one-read table, should one exist, differs from this particular labeled fallback table in at least 16 input assignments; equally for any relabeling')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('neighborhood_results.json'));args=ap.parse_args();d=run();args.out.write_text(json.dumps(d,indent=2)+'\n');print('PASS',d)
