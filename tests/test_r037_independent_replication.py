from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=spec_from_file_location("r037_runner",ROOT/"scripts"/"check_r037_independent_replication.py")
R=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(R)


def test_r037_independent_runner_passes():
    out=R.run()
    assert out["status"]=="PASS"
    assert out["fcc_shell_r1_r3"]==[12,42,92]
    assert out["hcp_shell_r1_r3"]==[12,44,96]
    assert out["supports_n0_n12"][2]==[55,57]
    assert out["barlow_returns_equal_through_n"]==12


def test_r037_holdout_growth_formulas():
    r=100
    assert 10*r*r+2==100002
    assert (10*r**3+15*r*r+11*r+3)//3==3383701
    assert (21*r*r+4)//2==105002
    assert (14*r**3+21*r*r+14*r+4)//4==3552851


def test_r037_exposed_face_law_agrees_between_worlds():
    for r in range(1,9):
        _,ff=R.shell_edge_stats(R.fcc_neighbors,R.fcc_distance,r)
        _,fh=R.shell_edge_stats(R.hcp_neighbors,R.hcp_distance,r)
        assert ff==fh==12*(3*r*r+3*r+1)
