#include <bits/stdc++.h>
using namespace std;
int Q=7,U=1;
int bits[8][4],lasts[8][4];
vector<pair<int,int>> cutsets[6];
int pairs_[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
int masks[6];
long long total=0, distance_ok=0, stable_ok=0;
int x[7]={};
ofstream* out=nullptr;
void go(int z,int rest){
 if(z==6){x[z]=rest;total++;
  for(int e=0;e<6;e++){int dist=0,mask=masks[e];for(int p=0;p<7;p++) if((mask>>p)&1)dist+=x[p];
   bool adjacent=(e==0||e==2||e==3||e==5);
   if(dist < (adjacent?2*Q+4*U+1:2*(Q+U)+1))return;
  }distance_ok++;
  for(int e=0;e<6;e++) {bool pass=false;for(auto [mask,t]:cutsets[e]){int count=0;for(int p=0;p<7;p++)if((mask>>p)&1)count+=x[p];if(count>=Q*t+2*U+1){pass=true;break;}}if(!pass)return;}
  stable_ok++;for(int p=0;p<7;p++){*out<<x[p]<<(p==6?'\n':' ');}return;
 }
 for(int v=0;v<=rest;v++){x[z]=v;go(z+1,rest-v);}
}
void init(){
 for(int p=1;p<8;p++){for(int i=0;i<4;i++)bits[p][i]=i==0?0:(p>>(i-1))&1;
  for(int i=0;i<4;i++){for(int t=0;t<4;t++){int e=(i-1-t+8)%4;if(bits[p][e]!=bits[p][(e+1)%4]){lasts[p][i]=e;break;}}}}
 for(int k=0;k<6;k++){int i=pairs_[k][0],j=pairs_[k][1];
  vector<tuple<int,int,int>> edges;
  for(int p=1;p<8;p++){if(bits[p][i]!=bits[p][j]){masks[k] |= 1<<(p-1);edges.emplace_back(p,lasts[p][i],4+lasts[p][j]);}}
  set<pair<int,int>> unique;
  for(int s=1;s<256;s++){int mask=0;for(auto [p,a,b]:edges){if((s>>a&1)&&(s>>b&1))mask|=1<<(p-1);}if(mask)unique.insert({mask,__builtin_popcount((unsigned)s)});}
  cutsets[k].assign(unique.begin(),unique.end());
  // Cut with same mask and higher vertex count dominated
  map<int,int> least;for(auto [m,t]:cutsets[k]){if(!least.count(m)||t<least[m])least[m]=t;}
  cutsets[k].clear();for(auto [m,t]:least)cutsets[k].push_back({m,t});
 }
}
int main(int argc,char**argv){if(argc<3){cerr<<"Usage q width\n";return 2;}Q=atoi(argv[1]);int n=atoi(argv[2]);init();string dir=argc>=4?argv[3]:".";string path=dir+"/R284FV_q"+to_string(Q)+"_n"+to_string(n)+"_stable.txt";ofstream f(path);out=&f;go(0,n);cerr<<"q="<<Q<<" n="<<n<<" all="<<total<<" distance="<<distance_ok<<" stable="<<stable_ok<<" file="<<path<<"\n";}
