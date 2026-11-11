#include <bits/stdc++.h>
using namespace std;
struct Word {int h,s; string key,word;};
struct Node {int ch[6]; unsigned char ec; unsigned char endmask; Node():ch{-1,-1,-1,-1,-1,-1},ec(1),endmask(0) {}};
vector<string> split(const string&s,char sep){vector<string>v; string a; stringstream f(s); while(getline(f,a,sep))v.push_back(a); return v;}
string decode(const string &h){string s;for(size_t i=0;i+1<h.size();i+=2) s.push_back((char)stoi(h.substr(i,2),nullptr,16));return s;}
string ident(int h,int s,const string&k){return to_string(h)+":"+to_string(s)+":"+k;}
vector<int> ste(char c){switch(c){case 'a':return {-1,-1};case 'c':return {1,2,-1,-2};case 'd':return {2,1,-2,-1};case 'e':return {3,1,1,-3};case 'f':return {1,-1};case 'g':return {2,-2};}throw runtime_error("op");}
int main(int argc,char**argv){
 if(argc<4){cerr<<"args catalog cases output [profile] [start_Q_index]\n";return 2;}
 ifstream src(argv[1]); string row;unordered_map<string,vector<string>> catalogue;
 int nw=0;
 while(getline(src,row)){
  auto v=split(row,'\t');if(v.size()!=6)throw runtime_error("bad catalog");
  catalogue[ident(stoi(v[0]),stoi(v[1]),v[2]+","+v[3]+","+v[4])].push_back(v[5]);nw++;
 }
 if(nw!=178850)throw runtime_error("wrong catalog");
 ofstream out(argv[3]);
 ifstream cases(argv[2]); int case_i=0;int remaining=0;int solved=0;
 while(getline(cases,row)){
  auto v=split(row,'\t');if(v.size()!=6)throw runtime_error("bad case");
  case_i++;
  if(argc>4&&v[0]!=argv[4])continue;
  if(argc>5&&case_i<stoi(argv[5]))continue;
  auto labels=split(v[2],';'); if(labels.size()!=6)throw runtime_error("not 6 labels");
  auto fixed=split(v[3],';'),candidate=split(v[4],';'),fpre=split(v[5],';');
  unordered_set<string> zero;for(auto &p:fpre)zero.insert(decode(p));
  if(fixed.size()!=6 || zero.size()!=70)throw runtime_error("fixed input mismatch");
  int success=0,best=255;int states=0;int maxi=0;
  for(int z=0;z<(int)candidate.size();z++){
   unordered_set<string> allowed(fixed.begin(),fixed.end());allowed.insert(candidate[z]);
   vector<Node> tr(1);
   string prefix;
   for(int j=0;j<6;j++){
    auto parts=split(labels[j],',');
    int h=stoi(parts.at(0)), sig=stoi(parts.at(1));
    for(const auto&k:allowed){
     auto itr=catalogue.find(ident(h,sig,k));if(itr==catalogue.end())continue;
     for(const auto&w:itr->second){
      int u=0;prefix.clear();
      for(char op:w){
       for(int d:ste(op)){
        prefix.push_back(char(d+4));int ix=d<0?d+3:d+2;
        int c=tr[u].ch[ix];
        if(c<0){c=tr.size();tr[u].ch[ix]=c;tr.emplace_back();tr[c].ec=(zero.count(prefix)?0:1);}
        u=c;
       }
      }
      tr[u].endmask|=1<<j;
     }
    }
   }
   maxi=max(maxi,(int)tr.size());
   vector<array<uint8_t,64>> dp(tr.size());
   const int CAP=24;
   for(int u=(int)tr.size()-1;u>=0;u--){
    auto &a=dp[u];a.fill(CAP);
    int em=tr[u].endmask;
    for(int sub=em;;sub=(sub-1)&em){a[sub]=0;if(sub==0)break;}
    for(int i=0;i<6;i++){
     int v=tr[u].ch[i];if(v<0)continue;
     auto &b=dp[v];int ec=tr[v].ec;
     array<uint8_t,64> n;n.fill(CAP);
     for(int sm=0;sm<64;sm++) if(a[sm]<CAP){
      // Ignore empty child at no cost; choose disjoint assigned demands otherwise.
      if(a[sm]<n[sm])n[sm]=a[sm];
      for(int tm=1;tm<64;tm++) if((sm&tm)==0&&b[tm]<CAP){
       int cost=a[sm]+b[tm]+ec;
       if(cost<n[sm|tm])n[sm|tm]=cost;
      }
     }
     a=n;
    }
   }
   int opt=dp[0][63];best=min(best,opt);states++;
   if(opt<=23){success++;cerr<<"POSSIBLE "<<v[0]<<" Q="<<v[1]<<" key="<<candidate[z]<<" opt="<<opt<<"\n";}
  }
  string line="{\"profile\":\""+v[0]+"\",\"Q\":\""+v[1]+"\",\"candidate_count\":"+to_string(candidate.size())+",\"checked\":"+to_string(states)+",\"best_clipped_cost\":"+to_string(best)+",\"feasible_93\":"+to_string(success)+",\"max_trie_nodes\":"+to_string(maxi)+"}";
  out<<line<<"\n";out.flush();solved++;
  cerr<<"CASE "<<v[0]<<" Q="<<v[1]<<" options="<<states<<" best_clipped="<<best<<" feasible="<<success<<" trie="<<maxi<<"\n";
 }
 cerr<<"ALL_CASES_FINISHED "<<solved<<"\n";
}
