"""Expose unchanged top-level prefix ranges as resumable exact-cover units."""
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
original = HERE.parent/'front_orbit_min_witness.cpp'
text = original.read_text()
old_dispatch = '''  if(pre){
   auto &sub=frames(k,h,pre);cnt[punct]-=pre;
   for(const auto&r:sub)if(add_big(r.f,left-pre,punct,0,cnt,pool,r.rows)){found=true;break;}
  }else if(k){for(M f:spaces[{k,h}])if(add_big(f,left,punct,0,cnt,pool,{})){found=true;break;}}
  else{int a=0;for(int j=1;j<ids.size();j++)if(types[ids[j]].all.size()<types[ids[a]].all.size())a=j;
   --cnt[a];for(M m:types[ids[a]].reps)if(add_big(FULL^m,left-1,punct,0,cnt,pool,{})){solution.push_back(m);found=true;break;}
  }'''
new_dispatch = '''  int total_frames=0;
  if(pre){
   auto &sub=frames(k,h,pre);cnt[punct]-=pre;total_frames=sub.size();
   for(int index=begin_frame;index<end_frame&&index<total_frames;index++){
    const auto&r=sub[index];
    if(add_big(r.f,left-pre,punct,0,cnt,pool,r.rows)){found=true;break;}
   }
  }else if(k){
   const auto&sub=spaces[{k,h}];total_frames=sub.size();
   for(int index=begin_frame;index<end_frame&&index<total_frames;index++)
    if(add_big(sub[index],left,punct,0,cnt,pool,{})){found=true;break;}
  }else{
   int a=0;for(int j=1;j<ids.size();j++)if(types[ids[j]].all.size()<types[ids[a]].all.size())a=j;
   --cnt[a];const auto&sub=types[ids[a]].reps;total_frames=sub.size();
   for(int index=begin_frame;index<end_frame&&index<total_frames;index++){
    M m=sub[index];
    if(add_big(FULL^m,left-1,punct,0,cnt,pool,{})){solution.push_back(m);found=true;break;}
   }
  }'''
replacements = {
    ' int val;while(cin>>val){': ' int val,begin_frame,end_frame;while(cin>>val>>begin_frame>>end_frame){\n  if(begin_frame<0||end_frame<begin_frame)throw runtime_error("bad prefix interval");',
    old_dispatch: new_dispatch,
    'cout<<val<<" "<<geometric_nodes<<" "<<leaf_nodes<<" "<<nodes<<" "<<found<<endl;':
        'cout<<val<<" "<<geometric_nodes<<" "<<leaf_nodes<<" "<<nodes<<" "<<found<<" "<<total_frames<<endl;'
}
for old, new in replacements.items():
    assert text.count(old) == 1, old
    text = text.replace(old, new)
target = HERE/'front_sharded.cpp'
target.write_text(text)
(HERE/'generation.json').write_text(json.dumps({'original_source_sha256': sha256(original.read_bytes()).hexdigest(),
    'derived_source_sha256': sha256(target.read_bytes()).hexdigest(), 'replacements': replacements}, indent=2)+'\n')
print(target)
