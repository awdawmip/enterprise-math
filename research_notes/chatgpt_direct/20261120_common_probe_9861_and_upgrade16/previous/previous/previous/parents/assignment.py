"""Verify an exact integer dual for the thirteen selected parents' least read cost."""
import json
from pathlib import Path

def check(parents,indices,menus,class_cost):
    here=Path(__file__).resolve().parent
    cert=json.loads((here/'assignment.json').read_text())
    selected=[parents[j]for j in indices]
    degree=[sum((r>>i)&1 for r in selected)for i in range(125)]
    assert all(degree)
    shared=[i for i in range(125)if degree[i]>1]
    w=cert['weights'];scale=cert['scale'];assert len(w)==len(shared)+13
    tests=0
    for j,r in enumerate(selected):
        fixed=[i for i in range(125)if degree[i]==1 and r>>i&1]
        optional=[i for i in shared if r>>i&1]
        for mask in range(1<<len(optional)):
            take=[i for k,i in enumerate(optional)if mask>>k&1]
            cost=class_cost(fixed+take,menus)
            assert w[len(shared)+j]+sum(w[shared.index(i)]for i in take)<=scale*cost
            tests+=1
    table=cert['partition']
    assert len(table)==13 and sorted(sum(table,[]))==list(range(125))
    assert all(all(r>>i&1 for i in row)for r,row in zip(selected,table))
    minimum=sum(class_cost(row,menus)for row in table)
    assert sum(w)==scale*minimum
    return dict(minimum=minimum,locally_checked_rows=tests,shared=len(shared),private=125-len(shared))
