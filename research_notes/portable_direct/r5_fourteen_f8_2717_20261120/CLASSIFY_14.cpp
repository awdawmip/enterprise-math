#define main solver14_unused
#include "SOLVE_F8_14.cpp"
#undef main
static string key(Sig const &a){
 string s;
 for(auto const &p:a){s+=to_string(p.cost);s+=':';for(auto m:p.masks){s+=to_string(m);s+=',';}s+=';';}
 return s;
}
int main(int argc,char**argv){
 if(argc<2)return 2;
 ifstream fd(argv[1],ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 fd.read((char*)adj.data(),adj.size());if(fd.gcount()!=(streamsize)adj.size())return 3;
 bool used[N]={};for(int i:W)used[i]=true;
 vector<int> names;for(int i=0;i<N;i++)if(!used[i])names.push_back(i);
 map<string,vector<pair<int,int>>> groups;
 for(size_t i=0;i<names.size();i++)for(size_t j=i+1;j<names.size();j++){
  auto a=signature(adj,names[i],names[j]);
  groups[key(a)].push_back({names[i],names[j]});
 }
 vector<pair<int,pair<int,int>>> sizes;
 for(auto const&[s,v]:groups)sizes.push_back({(int)v.size(),v[0]});
 sort(sizes.begin(),sizes.end(),greater<>());
 cout<<"PAIRS="<<names.size()*(names.size()-1)/2<<" CLASSES="<<groups.size()<<"\n";
 for(int i=0;i<min(15,(int)sizes.size());i++)
  cout<<"TOP="<<sizes[i].first<<" REPRESENTATIVE="<<sizes[i].second.first<<","<<sizes[i].second.second<<"\n";
 ofstream out("CLASSES_14.csv");
 out<<"u,v,class_size,representative_u,representative_v\n";
 for(auto const&[s,v]:groups)for(auto [u,w]:v)
  out<<u<<","<<w<<","<<v.size()<<","<<v[0].first<<","<<v[0].second<<"\n";
}
