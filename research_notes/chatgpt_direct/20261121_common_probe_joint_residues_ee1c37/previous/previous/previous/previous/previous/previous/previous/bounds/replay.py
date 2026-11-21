"""Replay the parent packing, global minimum-read bounds and the twelve-label witness."""
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import subprocess
import tempfile

import geometry
import prior_bounds as prior
from verify_twelve import verify as audit_table

HERE=Path(__file__).resolve().parent
CUTOFF={8:435,9:620,10:807,11:994,12:1179,13:1354}
# The inherited exact-cover proof covers the preceding ranges.
PREVIOUS={11:10926,12:9816}
BUDGET={11: 10958, 12: 9822}

def verify(budgets=None):
    budgets = BUDGET if budgets is None else budgets
    with tempfile.TemporaryDirectory() as location:
        tmp=Path(location)
        for name in ("parent_packing","class_enumeration","search"):
            subprocess.run([os.environ.get("CXX","c++"),"-std=c++17","-O3","-mpopcnt",str(HERE/(name+'.cpp')),"-o",str(tmp/name)],check=True)
        packing=geometry.verify(tmp)
        prior.observation_file(tmp/"observations.bin")
        output=subprocess.check_output([str(tmp/"class_enumeration"),str(tmp/"observations.bin"),str(tmp/"seeds.txt")],text=True)
        minima={1:0}
        for row in output.splitlines():
            size,visits,cost,*rest=map(int,row.split())
            minima[size]=cost
        bank=prior.families(tmp/"seeds.txt",tmp/"db.txt")
        assert len(bank[12,1104])==250 and len(bank[12,1116])==3000 and len(bank[13,1296])==250
        assert all(c in (1104,1116)for s,c in bank if s==12)
        assert [(c,len(bank[11,c])) for c in (936,944,960)]==[(936,4500),(944,12000),(960,3000)]
        assert prior.core_packing(bank)==6
        prior.CEILINGS=CUTOFF
        keys=sorted(bank)

        def one(labels):
            candidates=prior.profiles(labels,budgets[labels],minima,bank,6)
            profiles=[]
            for value, counts in candidates:
                if value<PREVIOUS[labels]:continue
                large=sum(cnt for (s,c),cnt in zip(keys,counts) if s>=12)
                thirteens=counts[keys.index((13,1296))]
                peripheral=counts[keys.index((12,1116))]
                if labels==11 and thirteens>=5:continue   # prior complete five/six-13 classification
                if large>=9:continue
                if large==8 and peripheral!=8:continue
                if large==7 and (thirteens>1 or peripheral<5+thirteens):continue
                profiles.append((value,counts))
            request=''.join(' '.join(map(str,[value,*counts]))+'\n' for value,counts in profiles)
            transcript=subprocess.check_output([str(tmp/"search"),str(tmp/"db.txt")],text=True,input=request)
            searched=[tuple(map(int,l.split()))for l in transcript.splitlines()]
            assert [v for v,_,found in searched]==[v for v,_ in profiles]
            assert all(found==0 for _,_,found in searched)
            return dict(tested_through=budgets[labels],lower_bound=budgets[labels]+1,
                        new_profiles=len(profiles),search_nodes=sum(nodes for _,nodes,_ in searched))
        with ThreadPoolExecutor(max_workers=2) as pool:
            low=dict(zip((11,12),pool.map(one,(11,12))))
    code=list(map(int,(HERE/"twelve_10147.txt").read_text().split()))
    table=audit_table(code)
    assert table['one_read']==10147
    return dict(geometry=packing,bounds=low,twelve=table)

if __name__=='__main__':print(json.dumps(verify(),sort_keys=True,indent=2))
