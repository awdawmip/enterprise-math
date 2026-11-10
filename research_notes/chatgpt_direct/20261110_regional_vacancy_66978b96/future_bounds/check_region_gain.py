"""Targeted exact control family for region recycling versus monotone shrinking."""
from __future__ import annotations

from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'regional'))
from region import RegionEvidence
from check_prefix_controls import PrefixControl, compare
from check_future_controls import target


class RegionControl(PrefixControl):
    def __init__(self,residues):
        super().__init__(residues,'region')
        self.region=RegionEvidence(self.r,self.width)
        self.witness=None

    def reserve(self,phase):
        legal=target(self.r,phase)
        color=self.region.select(legal[0],self.r+1,preferred=self.witness)
        if color is None:
            chosen=self.search.query(legal)
            level,prefix,_,labels=self.search.query_trace[-1]['visits'][-1]
            assert labels==0
            self.region.acquire(level,prefix)
            self.misses+=1
        else:
            chosen=legal[color]
            self.hits+=1
        assert chosen not in self.residues
        self.selected=self.witness=chosen
        return chosen

    def bind(self,slot):
        value=self.selected
        self.residues[slot]=value
        self.search.tree.known_write(slot,value)
        # Every bind in this experiment is nonempty; residue zero uses code B.
        self.region.bind(slot,value or self.B)
        if self.witness==value:
            self.witness=None

    def result(self):
        result=super().result()
        result.update(region_metrics=self.region.metrics(),region_events=self.region.events)
        return result


def run_region(residues,operations):
    controller=RegionControl(residues)
    for op in operations:controller.step(op)
    return controller.result()


def general_family():
    rows=[]
    for b in (3,4,5,7):
        B=1<<b;r=B-2;k=r//2;rounds=max(8,b+1)
        residues=(2,)*k+(3,)*k
        operations=tuple(op for _ in range(rounds) for op in [('reserve',0),('bind',0)])
        row=compare(residues,operations)
        row['region']=run_region(residues,operations)
        assert row['region']['reads']==3*r//2
        assert row['point']['reads']==row['prefix']['reads']==3*r//2+k-1
        assert row['region']['searches']==1
        assert row['region']['region_metrics']['prefix']==[2,1]
        assert row['region']['region_metrics']['occupied_residues']==1
        assert row['region']['region_events']['last_releases']==rounds-1
        if b>=4:assert 1<(B-1)//4
        rows.append(dict(b=b,r=r,rounds=rounds,mu=(B-1)//4,
                         point={k:v for k,v in row['point'].items() if k!='trace'},
                         prefix={k:v for k,v in row['prefix'].items() if k!='trace'},
                         region={k:v for k,v in row['region'].items() if k!='trace'}))
    return rows


def main():
    rows=general_family()
    prior=json.loads((ROOT/'prefix_mixed_regressions.json').read_text())
    regressions={name:run_region(row['residues'],row['operations'])
                 for name,row in prior['examples'].items()}
    result=dict(status='PASS',scope='Exact controller feedback; no BRC commands inferred',
                general_family=rows,previous_mixed_cases=regressions)
    (ROOT/'region_gain_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
