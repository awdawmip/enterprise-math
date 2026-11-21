"""Canonicalize the minimum *class orbit* at a fixed-core root.

Let G stabilize the already occupied point set, and fix the rarest remaining
class type.  In any feasible partition choose a class whose G-orbit minimum
is least among the selected classes of that type.  Move that class to its
orbit minimum m.  Every other selected class retains orbit minimum >= m and,
being distinct from m, has actual mask > m.  These two conditions therefore
preserve at least one representative of every feasible partition orbit.

The previous solver imposed only the second condition.  The added first
condition removes extra symmetric branches without assuming table symmetry.
"""
from pathlib import Path

root=Path(__file__).resolve().parent
src=(root/'front_orbits.cpp').read_text()

def replace(a,b):
    global src
    assert src.count(a)==1,a
    src=src.replace(a,b)

replace('if(stab.size()<=cnt[j]+1)return solve(free,left,cnt,filtered);',
        'if(stab.size()<=1)return solve(free,left,cnt,filtered);')
replace('vector<M> representatives;\n for(M m:filtered[j]){bool minimum=true;for(const auto*a:stab)if(image(m,*a)<m){minimum=false;break;}if(minimum)representatives.push_back(m);}',
        'vector<M> representatives,orbit_minimum;\n for(M m:filtered[j]){M minimum=m;for(const auto*a:stab)minimum=min(minimum,image(m,*a));orbit_minimum.push_back(minimum);if(minimum==m)representatives.push_back(m);}')
replace('filtered[j].clear();if(cnt[j])for(M row:all)if(row>m)filtered[j].push_back(row);',
        'filtered[j].clear();if(cnt[j])for(int z=0;z<all.size();z++)if(all[z]>m&&orbit_minimum[z]>=m)filtered[j].push_back(all[z]);')
(root/'front_orbit_min.cpp').write_text(src)
print(root/'front_orbit_min.cpp')
