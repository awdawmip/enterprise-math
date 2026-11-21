#include <unordered_map>
#include <unordered_set>
using Vec=std::array<int,5>;
using Triple=std::array<int,3>;
using VKey=unsigned;
using JKey=uint64_t;
VKey encode_shape(Vec v){
 sort(v.begin(),v.end());unsigned ans=0;for(int i=1;i<5;i++){ans|=unsigned(v[i]-v[0])<<(6*(i-1));}
 return ans;
}
Vec decode_shape(VKey key){Vec a{};for(int i=1;i<5;i++){a[i]=key&63;key>>=6;}return a;}
map<VKey,int> primitive_ids;
vector<vector<Vec>> permutations_by_shape;
int primitive(VKey k){
 auto it=primitive_ids.find(k);if(it!=primitive_ids.end())return it->second;
 int id=primitive_ids.size();primitive_ids[k]=id;
 vector<Vec> p;Vec a=decode_shape(k);do{p.push_back(a);}while(next_permutation(a.begin(),a.end()));permutations_by_shape.push_back(p);
 return id;
}
vector<vector<Triple>> orient;
void init_shapes(){
 primitive(0);
 for(const auto&t:types){
  set<Triple> shapes;for(M r:t.reps){Shape h=shape(r);Triple z;
   for(int d=0;d<3;d++)z[d]=primitive(encode_shape(h[d]));
   sort(z.begin(),z.end());do{shapes.insert(z);}while(next_permutation(z.begin(),z.end()));
  }
  orient.emplace_back(shapes.begin(),shapes.end());
 }
}
using List=std::vector<int>;
map<List,int> multi_id;
vector<List> multis;
vector<unordered_set<VKey>> reachable;
unordered_map<uint64_t,int> plus_cache;
int plus_one(int old,int shape){
 if(!shape)return old;
 uint64_t k=(uint64_t(old)<<32)|shape;
 auto cache=plus_cache.find(k);if(cache!=plus_cache.end())return cache->second;
 List n=multis[old];n.insert(lower_bound(n.begin(),n.end(),shape),shape);
 auto iter=multi_id.find(n);int idx;
 if(iter!=multi_id.end())idx=iter->second;
 else{
  idx=multis.size();multi_id[n]=idx;multis.push_back(n);
  unordered_set<VKey> output;
  for(VKey id:reachable[old]){
   Vec base=decode_shape(id);
   for(const auto& extra:permutations_by_shape[shape]){
    Vec val;for(int i=0;i<5;i++)val[i]=base[i]+extra[i];
    output.insert(encode_shape(val));
   }}
  reachable.push_back(move(output));
 }
 plus_cache[k]=idx;return idx;
}
struct Joint{
 vector<Triple> combinations;
 map<array<VKey,3>,bool> ok;
};
map<List,Joint> table;
vector<int> actual_ids;
Joint& group(const List&cnt){
 auto it=table.find(cnt);if(it!=table.end())return it->second;
 int j=0;while(j<cnt.size()&&!cnt[j])j++;
 Joint result;
 if(j==cnt.size())result.combinations.push_back({0,0,0});
 else{List next=cnt;next[j]--;set<Triple> variants;
  for(auto old:group(next).combinations){
   for(auto t:orient[actual_ids[j]]){
    Triple p;for(int i=0;i<3;i++)p[i]=plus_one(old[i],t[i]);sort(p.begin(),p.end());variants.insert(p);
   }}
  result.combinations.assign(variants.begin(),variants.end());
 }
 return table.emplace(cnt,move(result)).first->second;
}
bool exact_margins(M f,const List&cnt){
 auto &state=group(cnt);
 Shape h=shape(f);array<VKey,3> target;for(int i=0;i<3;i++)target[i]=encode_shape(h[i]);
 sort(target.begin(),target.end());
 auto it=state.ok.find(target);if(it!=state.ok.end())return it->second;const auto key=target;
 do{
  for(auto t:state.combinations)if(reachable[t[0]].count(target[0])&&reachable[t[1]].count(target[1])&&reachable[t[2]].count(target[2])){state.ok[key]=true;return true;}
 }while(next_permutation(target.begin(),target.end()));
 state.ok[key]=false;return false;
}
