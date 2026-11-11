#include <bits/stdc++.h>
using namespace std;

struct Node { int ch[6]; uint8_t ec,endmask; Node(){fill(ch,ch+6,-1);ec=1;endmask=0;} };
vector<string> split(const string &s,char sep){vector<string>v;string a;stringstream f(s);while(getline(f,a,sep))v.push_back(a);return v;}
string decode(const string &h){string s;for(size_t i=0;i+1<h.size();i+=2)s.push_back((char)stoi(h.substr(i,2),nullptr,16));return s;}
string id(int h,int s,const string&k){return to_string(h)+":"+to_string(s)+":"+k;}
const int axis[6][4]={{-1,-1,0,0},{1,2,-1,-2},{2,1,-2,-1},{3,1,1,-3},{1,-1,0,0},{2,-2,0,0}};
const int alen[6]={2,4,4,4,2,2};
int opindex(char c){switch(c){case 'a':return 0;case 'c':return 1;case 'd':return 2;case 'e':return 3;case 'f':return 4;case 'g':return 5;}throw runtime_error("bad op");}
int main(int argc,char**argv){
 if(argc!=4){cerr<<"args catalog cases output\n";return 2;}
 ifstream src(argv[1]);string row;unordered_map<string,vector<string>> catalog;int nw=0;
 while(getline(src,row)){auto v=split(row,'\t');if(v.size()!=6)throw runtime_error("bad catalog");catalog[id(stoi(v[0]),stoi(v[1]),v[2]+","+v[3]+","+v[4])].push_back(v[5]);nw++;}
 if(nw!=178850)throw runtime_error("catalog mismatch");
 ifstream cas(argv[2]);ofstream out(argv[3]);int lineno=0;int solved=0;
 while(getline(cas,row)){
  ++lineno;auto v=split(row,'\t');if(v.size()!=5)throw runtime_error("bad case");
  auto labels=split(v[2],';');if(labels.size()!=6)throw runtime_error("bad 6 labels");
  auto opts=split(v[3],'|');auto fp=split(v[4],';');unordered_set<string>zero;
  for(auto &p:fp)zero.insert(decode(p));int CAP=94-(int)zero.size();if(CAP!=11 && CAP!=13 && CAP!=14 && CAP!=15 && CAP!=16)throw runtime_error("unexpected B class");
  int minopt=CAP,maxnodes=0,feasible=0,noptions=0;
  for(const string&allow:opts){
   auto keys=split(allow,';');if(keys.size()!=7)throw runtime_error("expected 7 keys");
   vector<Node>tr(1);string prefix;
   for(int j=0;j<6;j++){
    auto hs=split(labels[j],',');int h=stoi(hs[0]),sig=stoi(hs[1]);
    for(auto &key:keys){auto p=catalog.find(id(h,sig,key));if(p==catalog.end())continue;
     for(const auto &w:p->second){int u=0;prefix.clear();for(char c:w){int oi=opindex(c);for(int k=0;k<alen[oi];k++){
      int d=axis[oi][k];prefix.push_back(char(d+4));int ai=d<0?d+3:d+2;
      int t=tr[u].ch[ai];if(t<0){t=tr.size();tr[u].ch[ai]=t;tr.emplace_back();tr[t].ec=zero.count(prefix)?0:1;}u=t;
     }}tr[u].endmask |= uint8_t(1<<j);}
    }
   }
   maxnodes=max(maxnodes,(int)tr.size());vector<array<uint8_t,64>>dp(tr.size());
   for(int u=(int)tr.size()-1;u>=0;u--){auto&a=dp[u];a.fill(CAP);int em=tr[u].endmask;
    for(int sub=em;;sub=(sub-1)&em){a[sub]=0;if(sub==0)break;}
    for(int dir=0;dir<6;dir++){int child=tr[u].ch[dir];if(child<0)continue;const auto&b=dp[child];int ec=tr[child].ec;
     array<uint8_t,64> nx=a;
     for(int s=0;s<64;s++)if(a[s]<CAP){int remaining=(~s)&63;
      for(int t=remaining;t;t=(t-1)&remaining){if(b[t]>=CAP)continue;int cost=a[s]+b[t]+ec;if(cost<nx[s|t])nx[s|t]=uint8_t(cost);}
     }a=nx;
    }
   }
   int o=dp[0][63];minopt=min(minopt,o);noptions++;if(o<CAP){feasible++;cerr<<"POSSIBLE "<<v[0]<<" Q="<<v[1]<<" opt="<<o<<" keyset="<<allow<<"\n";}
  }
  out<<"{\"profile\":\""<<v[0]<<"\",\"Q\":\""<<v[1]<<"\",\"options\":"<<noptions<<",\"best_clipped\":"<<minopt<<",\"feasible_93\":"<<feasible<<",\"max_nodes\":"<<maxnodes<<"}\n";
  solved++;if(solved%200==0)cerr<<"CASE "<<solved<<" "<<v[0]<<" Q="<<v[1]<<" options="<<noptions<<" best="<<minopt<<" trie="<<maxnodes<<"\n";
 }
 cerr<<"SOLVED "<<solved<<"\n";
}
