#include <bits/stdc++.h>
using namespace std;
struct Node {int ch[6];uint8_t ec,mask;Node(){fill(ch,ch+6,-1);ec=1;mask=0;}};
vector<string> split(const string&s,char sep){vector<string>a; string v;stringstream f(s);while(getline(f,v,sep))a.push_back(v);return a;}
string decode(const string &hex){string s;for(size_t i=0;i+1<hex.size();i+=2)s.push_back((char)stoi(hex.substr(i,2),nullptr,16));return s;}
const int steps[6][4]={{-1,-1,0,0},{1,2,-1,-2},{2,1,-2,-1},{3,1,1,-3},{1,-1,0,0},{2,-2,0,0}};
const int lengths[6]={2,4,4,4,2,2};
int idx(char c){switch(c){case 'a':return 0;case 'c':return 1;case 'd':return 2;case 'e':return 3;case 'f':return 4;case 'g':return 5;}throw runtime_error("bad word");}
string key(int h,int s,const string&k){return to_string(h)+":"+to_string(s)+":"+k;}
int main(int argc,char**argv){
 if(argc!=4){cerr<<"usage: solver catalog cases results\n";return 2;}
 ifstream f(argv[1]); string line; unordered_map<string,vector<string>> word_map;int n=0;
 while(getline(f,line)){auto v=split(line,'\t');if(v.size()!=6)throw runtime_error("bad catalog");word_map[key(stoi(v[0]),stoi(v[1]),v[2]+","+v[3]+","+v[4])].push_back(v[5]);n++;}
 if(n!=178850)throw runtime_error("not frozen catalog");
 ifstream cas(argv[2]);ofstream out(argv[3]);int cases=0,solved=0,skipped=0,ok=0;string prev="",totalinfo="";
 while(getline(cas,line)){
  auto v=split(line,'\t');if(v.size()!=6)throw runtime_error("bad case");
  string group=v[0]+":"+v[1];if(group!=prev){prev=group;solved++;ok=0;}
  if(ok){skipped++;continue;}
  auto labels=split(v[3],';');auto keys=split(v[4],';');auto fp=split(v[5],';');
  if(labels.size()!=4||keys.size()!=7||fp.size()!=78)throw runtime_error("bad input dimensions");
  unordered_set<string>zero;for(const auto &p:fp)zero.insert(decode(p));
  vector<Node>tr(1); string prefix;
  for(int j=0;j<4;j++){
   auto hs=split(labels[j],',');int h=stoi(hs[0]),s=stoi(hs[1]);
   for(const auto &k:keys){auto wlist=word_map.find(key(h,s,k));if(wlist==word_map.end())continue;
    for(const auto &w:wlist->second){int u=0;prefix.clear();for(char c:w){int op=idx(c);for(int z=0;z<lengths[op];z++){
     int d=steps[op][z];prefix.push_back(char(d+4));int dir=d<0?d+3:d+2;
     int t=tr[u].ch[dir];if(t<0){t=(int)tr.size();tr[u].ch[dir]=t;tr.emplace_back();tr[t].ec=zero.count(prefix)?0:1;}u=t;
    }}tr[u].mask |=uint8_t(1u<<j);
   }
  }
  } // close four-label loop
  constexpr uint8_t CAP=16;
  vector<array<uint8_t,16>>dp(tr.size());
  for(int u=(int)tr.size()-1;u>=0;--u){auto &a=dp[u];a.fill(CAP);int em=tr[u].mask;
   for(int sub=em;;sub=(sub-1)&em){a[sub]=0;if(!sub)break;}
   for(int dir=0;dir<6;dir++){int ch=tr[u].ch[dir];if(ch<0)continue;const auto &b=dp[ch];int ec=tr[ch].ec;
    array<uint8_t,16>nx=a;
    for(int S=0;S<16;S++)if(a[S]<CAP){int rest=(~S)&15;for(int T=rest;T;T=(T-1)&rest){if(b[T]>=CAP)continue;
      int cost=int(a[S])+int(b[T])+ec;if(cost<nx[S|T])nx[S|T]=(uint8_t)cost;
    }}a=nx;
   }
  }
  int value=dp[0][15]; cases++;
  if(value>=16){ok=1;out<<v[0]<<'\t'<<v[1]<<'\t'<<v[2]<<'\t'<<v[3]<<'\t'<<value<<'\t'<<tr.size()<<'\n';}
  if(cases%100==0)cerr<<"CHECKED "<<cases<<" group "<<group<<" found "<<bool(ok)<<" nodes "<<tr.size()<<'\n';
 }
 cerr<<"FINISHED candidates "<<cases<<" groups "<<solved<<" skipped "<<skipped<<'\n';
}
