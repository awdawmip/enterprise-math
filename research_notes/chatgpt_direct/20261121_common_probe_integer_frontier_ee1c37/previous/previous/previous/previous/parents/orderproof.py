"""Recheck the last covering bound by anchoring the least orbit type of a pair of parents."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
from pairtypes import build

def check(work,parents,centers,holes,jobs):
    here=Path(__file__).resolve().parent
    subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',here/'cover_pair.cpp','-o',work/'pairs'],check=True)
    masks=''.join(f'{m%(1<<64)} {m>>64}\n'for m in parents)
    def one(case):
        j,options=case;f=work/f'pair{j}'
        f.write_text(' '.join(map(str,[j,len(options),*options]))+'\n')
        z=subprocess.run([work/'pairs','12',str(holes),f],input=masks,capture_output=True,check=True,text=True)
        rank,n,found=map(int,z.stdout.split())
        assert rank==j and not found
        return [rank,n]
    with ThreadPoolExecutor(jobs) as pool:return list(pool.map(one,build(parents,centers)))
