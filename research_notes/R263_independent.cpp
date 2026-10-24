// Standalone independent exact finite check of the R263 toy-model claim.
// NOT an Enterprise Math native module or native heartbeat validation.
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stdexcept>
#include <algorithm>
using namespace std;
struct State {int q=0,r=0,e=1,k=0;};
const int target_q[3][2]={{2,2},{0,0},{1,2}};
const int sign[3][2]={{-1,1},{-1,1},{1,1}};
const int tr[3][2]={{-1,-1},{-1,-1},{1,-1}};
int delta(int r,int a) { if(r==2)return 2; if(a==1)return 0;return r==0?1:2; }
State step(State s,int a) {int q=s.q;return {target_q[q][a],delta(s.r,a),sign[q][a]*s.e,sign[q][a]*s.k+tr[q][a]};}
State eval(const string& s) {State v;for(char c:s){if(c!='0'&&c!='1')throw runtime_error("non binary input");v=step(v,c-'0');}return v;}
using pair_t=pair<int,int>; using fiber_t=map<pair<int,int>,set<pair_t>>;
void require(bool flag,const string& msg){if(!flag)throw runtime_error(msg);}
int main(){
  const set<pair_t> all={{0,0},{0,2},{1,1},{1,2},{2,0},{2,1},{2,2}};
  const int expected_max[]={1,1,1,3,4,4,5,6,7,7,7};
  for(int m=0;m<=10;m++){
     fiber_t fibers;const unsigned end=1u<<m;
     for(unsigned mask=0;mask<end;mask++){
         State s;for(int b=m-1;b>=0;b--)s=step(s,(mask>>b)&1);
         fibers[{s.e,s.k}].insert({s.q,s.r});
     }
     int mx=0;for(auto &it:fibers)mx=max(mx,(int)it.second.size());
     require(mx==expected_max[m],"wrong max joint states at depth "+to_string(m));
     if(m==8)require(fibers[{1,0}]==all,"missing 7-states at depth 8 effect (+1,0)");
     if(m==9)require(fibers[{-1,-1}]==all,"missing 7-states at depth 9 effect (-1,-1)");
     if(m==10)require(fibers[{-1,0}]==all,"missing 7-states at depth 10 effect (-1,0)");
  }
  State reset=eval("101");require(reset.q==0&&reset.r==0&&reset.e==1&&reset.k==-1,"reset mismatch");
  const pair<int,int> base_effect[3]={{1,0},{-1,-1},{-1,0}};
  const string W[3][7]={
    {"01010101","00001100","01010110","00000100","01101011","10101010","00001010"},
    {"110101101","000001000","101010110","000001110","101101011","010101010","000000011"},
    {"1011010101","0000000101","1011010110","0000000110","1011101011","0101011010","0000000011"}
  };
  vector<pair_t> states(all.begin(),all.end());
  for(int j=0;j<3;j++)for(int i=0;i<7;i++){
    State s=eval(W[j][i]);require(make_pair(s.q,s.r)==states[i],"witness control mismatch");
    require(make_pair(s.e,s.k)==base_effect[j],"witness affine mismatch");
  }
  for(int m=8;m<=180;m++){
    int idx=(m-8)%3, j=8+idx, h=(m-j)/3;
    string prefix;for(int z=0;z<h;z++)prefix+="101";
    for(int i=0;i<7;i++){
      State s=eval(prefix+W[idx][i]);
      require(make_pair(s.q,s.r)==states[i],"lifted control mismatch");
      require(s.e==base_effect[idx].first&&s.k==base_effect[idx].second-s.e*h,"lifted affine mismatch");
    }
  }
  cout<<"PASS: independent C++17 exact enumeration m=0..10, first full fiber m=8, 21 independent witnesses, prefix lifting through m=180\n";
}
