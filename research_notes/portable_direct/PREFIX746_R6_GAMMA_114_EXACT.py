#!/usr/bin/env python3
"""PREFIX-746 exact 57+57 Gamma cell exclusion replay (Python 3 standard library).
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Dependency: published PREFIX741_R6_INNER_STRIP_194.py from this same directory.
Usage: python PREFIX746_R6_GAMMA_114_EXACT.py
"""
from PREFIX741_R6_INNER_STRIP_194 import lower_cell, pair, tails, emu, eW, oldmu, oldW

# [i, j, subdivision k, floor(1e6 * new lower bound), floor(1e6 * PREFIX-712 old sufficient bound)]
EXPECTED = [[15,46,4,33042798,-129427234],[16,46,4,38713265,-124142450],[10,47,8,27002790,-164850312],[15,47,4,24371089,-141237086],[16,47,4,29964158,-135985109],[17,47,4,35738705,-130589136],[18,47,4,41680036,-125066592],[20,47,4,53995183,-113719823],[11,48,8,24535826,-171331230],[20,48,4,45631417,-124953298],[21,48,4,51945649,-119135545],[12,49,8,22747775,-177040130],[13,49,8,27509360,-172487371],[18,49,4,25761685,-146910199],[19,49,4,31718752,-141315204],[20,49,4,37839055,-135595783],[21,49,4,44106374,-129770346],[22,49,4,50502771,-123858811],[23,49,4,57008651,-117882524],[13,50,8,21620243,-181990942],[14,50,8,26470862,-177340583],[15,50,4,2338297,-172491620],[16,50,4,7601398,-167452537],[17,50,4,13073020,-162233404],[18,50,4,18743973,-156845907],[19,50,4,24603375,-151303350],[20,50,4,30638617,-145620656],[21,50,4,36835360,-139814333],[22,50,4,43177540,-133902437],[23,50,4,49647411,-127904507],[24,50,4,56225600,-121841480],[15,51,8,26063219,-181461078],[16,51,4,1484642,-176525059],[17,51,4,6825055,-171400790],[18,51,4,12371887,-166098179],[19,51,4,18116002,-160628703],[20,51,4,24046595,-155005422],[21,51,4,30151162,-149242976],[22,51,4,36415495,-143357561],[23,51,4,42823689,-137366895],[24,51,4,49358182,-131290157],[25,51,4,55999809,-125147920],[16,52,8,26263252,-184868118],[17,52,4,1245155,-179853558],[18,52,4,6654046,-174652540],[19,52,4,12267224,-169274788],[20,52,4,18075614,-163731561],[21,52,4,24068494,-158035673],[22,52,4,30233465,-152201484],[23,52,4,36556446,-146244896],[24,52,4,43021685,-140183311],[25,52,4,49611790,-134035592],[26,52,4,56307786,-127821987],[27,52,4,63089192,-121564044],[28,52,4,69934125,-115284508],[29,52,4,76819417,-109007188],[30,52,4,83720768,-102756816]]

def floor_micro(value):
    v = value * 1000000
    return v.numerator // v.denominator

def main():
    confirmed = []
    for i, j, split, newfloor, oldfloor in EXPECTED:
        actual = lower_cell(i, j, split, emu, eW)
        historical = lower_cell(i, j, 1, oldmu, oldW)
        assert floor_micro(actual) == newfloor, (i,j,"new")
        assert floor_micro(historical) == oldfloor, (i,j,"old")
        assert actual > 6/5 and historical < 0, (i,j,"strict comparison")
        confirmed.append((i,j))
        print("PASS",i,j,split,newfloor,oldfloor,flush=True)
        pair.cache_clear()
        tails.cache_clear()
    assert len(confirmed) == len(set(confirmed)) == 57
    assert len({(i,j) for i,j in confirmed} | {(j,i) for i,j in confirmed}) == 114
    assert min(row[3] for row in EXPECTED) == 1245155
    assert max(row[4] for row in EXPECTED) == -102756816
    assert 141942 + 114 == 142056
    print("ALL_CHECKS_PASS PREFIX746-R6 57+57=114",flush=True)

if __name__ == "__main__":
    main()
