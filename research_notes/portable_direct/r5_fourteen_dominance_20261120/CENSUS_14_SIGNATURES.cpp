// Deterministic all-pairs exact priced-joint-support signature census.
#define main previous_solver_main
#include "R5_FOURTEEN_F8_ONE.cpp"
#undef main
int main(){
 ifstream fi("window_adj.bin",ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 fi.read((char*)adj.data(),adj.size());if(fi.gcount()!=(streamsize)adj.size())return 2;
 bool used[N]={};for(int x:seed)used[x]=true;
 unordered_map<string,int>seen;vector<pair<int,int>> reps;vector<int> members;
 ofstream pairs("R5_14_29646_TO_CLASS.csv");pairs<<"u,v,signature_class\n";
 for(int u=0;u<N;u++)if(!used[u])for(int v=u+1;v<N;v++)if(!used[v]){
  auto actions=signature(adj,u,v);string key;
  for(auto&a:actions){key+=to_string(a.cost)+":";
   for(int m:a.masks)key+=to_string(m)+",";
   key+=";";}
  int id;auto it=seen.find(key);
  if(it==seen.end()){id=reps.size();seen.emplace(move(key),id);reps.push_back({u,v});members.push_back(0);}
  else id=it->second;
  members[id]++;pairs<<u<<","<<v<<","<<id<<"\n";
 }
 ofstream out("R5_14_CLASS_REPS.csv");out<<"class,u,v,count\n";
 for(int id=0;id<reps.size();id++)out<<id<<","<<reps[id].first<<","<<reps[id].second<<","<<members[id]<<"\n";
 cout<<"PAIRS=29646 CLASSES="<<reps.size()<<" MAX="<<*max_element(members.begin(),members.end())<<"\n";
 return reps.size()==1906?0:1;
}
