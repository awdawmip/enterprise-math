#!/usr/bin/env python3
"""PREFIX-745-R6: check 70 whole closed Gamma grid cells and their transposes.
FROZEN SCIENTIFIC INPUT: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Dependency: PREFIX741_R6_INNER_STRIP_194.py at its published, compatible source.
Usage: python PREFIX745_R6_GAMMA_140_EXACT.py [first_j last_j_exclusive].
Running 40 50 checks all 70 cells. Python 3 standard library exact fractions.
"""
import sys
from fractions import Fraction as F
from PREFIX741_R6_INNER_STRIP_194 import (
    lower_cell, emu, eW, oldmu, oldW, pair, tails
)
EXPECTED = [[4,40,44489051,-94176368],[5,40,48300576,-90626804],[6,40,52342167,-86872994],[7,40,56607993,-82923046],[8,40,61090122,-78787522],[9,40,65778469,-74479429],[10,40,70660784,-70014190],[11,40,75722627,-65409586],[12,40,80947383,-60685693],[13,40,86316275,-55864790],[4,41,32835167,-109452622],[5,41,36565677,-105956298],[6,41,40530407,-102249085],[7,41,44725094,-98337414],[8,41,49143475,-94230064],[9,41,53777240,-89938160],[10,41,58615995,-85475157],[11,41,63647237,-80856804],[12,41,68856341,-76101099],[13,41,74226561,-71228222],[4,42,21827030,-124072338],[5,42,25469151,-120638456],[6,42,29348173,-116988623],[7,42,33461290,-113127696],[8,42,37803810,-109062766],[9,42,42369100,-104803158],[10,42,47148544,-100360431],[11,42,52131504,-95748357],[12,42,57305293,-90982897],[13,42,62655161,-86082150],[7,43,22846919,-127256008],[8,43,27102748,-123246442],[9,43,31587037,-119033867],[10,43,36292855,-114628027],[11,43,41211349,-110040789],[12,43,46331702,-105286130],[13,43,51641105,-100380110],[8,44,17067345,-136746685],[9,44,21459456,-132594511],[10,44,26078764,-128240733],[11,44,30918110,-123695393],[12,44,35968467,-118970552],[8,45,7720059,-149533929],[9,45,12010137,-145454175],[10,45,16531466,-141166199],[11,45,21278478,-136678312],[12,45,26243845,-132000744],[13,45,31418425,-127145655],[9,46,3258261,-157586798],[10,46,7671523,-153376947],[11,46,12314491,-148960570],[12,46,17181435,-144346159],[13,46,22264915,-139544039],[14,46,27555716,-134566388],[11,47,4043611,-160518021],[12,47,8800234,-155981086],[13,47,13778985,-151248092],[14,47,18972353,-146329384],[12,48,1114756,-166884548],[13,48,5976746,-162235209],[14,48,11058910,-157391818],[15,48,16353704,-152364675],[16,48,21851875,-147165800],[17,48,27542420,-141808934],[18,48,33412550,-136309533],[19,48,39447674,-130684733],[14,49,3828802,-167733984],[15,49,9005793,-162788536],[16,49,14393378,-157661232],[17,49,19982325,-152363941]]
RANGES = [[40,4,14],[41,4,14],[42,4,14],[43,7,14],[44,8,13],[45,8,14],[46,9,15],[47,11,15],[48,12,20],[49,14,18]]
def microfloor(value):
    x = value * 1000000
    return x.numerator // x.denominator
def main():
    if len(sys.argv) == 1:
        start, end = 40, 50
    elif len(sys.argv) == 3:
        start, end = int(sys.argv[1]), int(sys.argv[2])
    else:
        raise SystemExit("usage: checker.py [first_j last_j_exclusive]")
    assert 40 <= start < end <= 50
    checked = []
    for i,j,new_expected,old_expected in EXPECTED:
        if not (start <= j < end):
            continue
        new = lower_cell(i,j,4,emu,eW)
        old = lower_cell(i,j,1,oldmu,oldW)
        assert microfloor(new) == new_expected, (i,j,"new")
        assert microfloor(old) == old_expected, (i,j,"old")
        assert new > F(1), (i,j,"uniform gap")
        assert old < F(0), (i,j,"PREFIX712 old sufficient predicate")
        checked.append((i,j,new_expected,old_expected))
        print("PASS",i,j,new_expected,old_expected,flush=True)
        pair.cache_clear()
        tails.cache_clear()
    assert len(checked) == sum(1 for x in EXPECTED if start <= x[1] < end)
    assert len(set((i,j) for i,j,_,_ in checked)) == len(checked)
    if (start,end) == (40,50):
        assert len(checked) == 70
        cells = {(i,j) for i,j,_,_ in checked}
        both = cells | {(j,i) for i,j in cells}
        assert len(both) == 140
        assert min(v[2] for v in checked) == 1114756
        assert max(v[3] for v in checked) == -55864790
        assert 141802+len(both) == 141942
    print("ALL_CHECKS_PASS PREFIX745-R6",len(checked),"original cells",flush=True)
if __name__ == "__main__":
    main()
