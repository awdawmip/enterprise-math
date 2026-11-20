"""Enumerate the seven-parent branch of the eleven-message feasibility problem."""
import subprocess
def verify(tmp):
    from seven import seven
    counts=seven(tmp)
    assert counts==(36,10430,300,283)
    raw=subprocess.check_output([str(tmp/'core_completions'),'7','11','31250','0',str(tmp/'obs'),str(tmp/'seven_spaces.txt'),'regions'],text=True)
    rows=[list(map(int,l.split()))for l in raw.splitlines()]
    assert len(rows)==counts[-1] and all(r[3]==0 for r in rows)
    twelve=subprocess.check_output([str(tmp/'core_completions'),'7','12','10146','0',str(tmp/'obs'),str(tmp/'seven_spaces.txt'),'regions'],text=True)
    trows=[list(map(int,l.split()))for l in twelve.splitlines()]
    assert len(trows)==counts[-1] and all(r[3]==0 for r in trows)
    return dict(twelve_excluded_through=10146,pointed=counts[1],orbits=counts[0],residual_cost_pairs=counts[2],
                distinct_residuals=counts[3],completions=0,nodes=sum(r[2]for r in rows))
