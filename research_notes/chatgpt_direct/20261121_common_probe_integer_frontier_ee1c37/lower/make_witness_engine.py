"""Add successful-path recording without changing the search or pruning rules."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
source_name=sys.argv[1] if len(sys.argv)>1 else 'front_orbits.cpp'
output_name=sys.argv[2] if len(sys.argv)>2 else 'front_witness.cpp'
src = (root / source_name).read_text()

def replace(old, new):
    global src
    assert src.count(old) == 1, old
    src = src.replace(old, new)

replace('uint64_t nodes;', 'uint64_t nodes;\nvector<M> solution;')
replace('if(left==1)return choice>=0&&count[choice];',
        'if(left==1){if(choice>=0&&count[choice]){solution.push_back(free);return true;}return false;}')
replace('if(solve(free^all[i],left-1,cnt,options))return true;',
        'if(solve(free^all[i],left-1,cnt,options)){solution.push_back(all[i]);return true;}')
replace('for(M m:all)if((pivot<0||((m>>pivot)&1))&&solve(free^m,left-1,cnt,options))return true;',
        'for(M m:all)if((pivot<0||((m>>pivot)&1))&&solve(free^m,left-1,cnt,options)){solution.push_back(m);return true;}')
replace('if(solve(free^m,left-1,cnt,filtered)){++cnt[j];return true;}',
        'if(solve(free^m,left-1,cnt,filtered)){solution.push_back(m);++cnt[j];return true;}')
replace('if(add_big(free^m,left-1,punct,j+1,cnt,pool,large))return true;',
        'if(add_big(free^m,left-1,punct,j+1,cnt,pool,large)){solution.push_back(m);return true;}')
replace('bool found=false;nodes=0;', 'bool found=false;nodes=0;solution.clear();')
replace('--cnt[a];for(M m:types[ids[a]].reps)if(add_big(FULL^m,left-1,punct,0,cnt,pool,{})){found=true;break;}',
        '--cnt[a];for(M m:types[ids[a]].reps)if(add_big(FULL^m,left-1,punct,0,cnt,pool,{})){solution.push_back(m);found=true;break;}')

helper = r'''
bool finish_witness(M free,vector<int>&rem){
 int chosen=-1,best=2147483647;
 for(int j=0;j<types.size();j++)if(rem[j]){
  int count=0;for(M m:types[j].all)if((m&free)==m)++count;
  if(count<rem[j])return false;
  if(count<best){best=count;chosen=j;}
 }
 if(chosen<0)return !free;
 --rem[chosen];
 for(M m:types[chosen].all)if((m&free)==m&&finish_witness(free^m,rem)){solution.push_back(m);return true;}
 ++rem[chosen];return false;
}
void save_witness(const string&dir,int cost,const vector<int>&orig){
 map<M,int> kind;
 for(int j=0;j<types.size();j++)for(M m:types[j].all)kind[m]=j;
 vector<int>rem=orig;M free=FULL;
 for(M m:solution){
  if(!kind.count(m)||!(rem[kind[m]]--)||(m&free)!=m)throw runtime_error("invalid partial witness");
  free^=m;
 }
 if(!finish_witness(free,rem))throw runtime_error("missing anchored/core decomposition");
 free=FULL;long long check=0;vector<int>verify(types.size());
 for(M m:solution){
  if(!kind.count(m)||(m&free)!=m)throw runtime_error("invalid complete witness");
  free^=m;check+=types[kind[m]].price;++verify[kind[m]];
 }
 if(free||check!=cost||verify!=orig)throw runtime_error("witness verification failure");
 sort(solution.begin(),solution.end());
 ofstream out(dir+"/found_"+to_string(cost)+".json");
 out<<"{\"cost\":"<<cost<<",\"classes\":[";
 for(int i=0;i<solution.size();i++){
  M m=solution[i];int j=kind[m];if(i)out<<",";
  out<<"{\"size\":"<<types[j].sz<<",\"cost\":"<<types[j].price<<",\"points\":[";
  bool sep=false;for(M q=m;q;q&=q-1){if(sep)out<<",";out<<pos(q);sep=true;}out<<"]}";
 }out<<"]}\n";
}
'''
replace('int main(int argc,char**argv){', helper + '\nint main(int argc,char**argv){')
replace('cout<<val<<" "<<geometric_nodes<<" "<<leaf_nodes<<" "<<nodes<<" "<<found<<endl;',
        'if(found)save_witness(argv[3],val,orig);\n  cout<<val<<" "<<geometric_nodes<<" "<<leaf_nodes<<" "<<nodes<<" "<<found<<endl;')
(root / output_name).write_text(src)
print(root / output_name)
