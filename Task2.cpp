#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <sstream>

using namespace std;

int mode_print_prim = 0;

void makeCombiUtil(vector<vector<int> >& ans,
	vector<int>& tmp, int n, int left, int k){
	
	if (k == 0) {
		ans.push_back(tmp);
		return;
	}

	for (int i = left; i <= n; ++i){
		tmp.push_back(i);
		makeCombiUtil(ans, tmp, n, i + 1, k - 1);
		tmp.pop_back();
	}
}


vector<vector<int> > makeCombi(int n, int k){
	vector<vector<int> > ans;
	vector<int> tmp;
	makeCombiUtil(ans, tmp, n, 1, k);
	return ans;
}

void print(vector<vector<int> > &myvec){
	for (int i = 0; i < myvec.size(); i++) {
		for (int j = 0; j < myvec[i].size(); j++) {
			cout << myvec[i][j] << " ";
		}
		cout << endl;
	}
}


int minKey(vector<int> &key, vector<bool> &mstSet,int n){  
	int min = INT_MAX, min_index=0;

	for (int v = 0; v < n; v++) {
		if (mstSet[v] == false && key[v] < min){
			min = key[v], min_index = v;
		}
	}

	return min_index;
}


int prim(vector<vector<int> > &graph,int &n) {
	vector <int> parent;
	vector <int> key;
	vector<bool> mstSet;

	int cost = 0;

	parent.resize(n);
	key.resize(n);
	mstSet.resize(n);

	for (int i = 0; i < n; i++){
		key[i] = INT_MAX,
		mstSet[i] = false;
	}
 
	key[0] = 0;
	parent[0] = -1; 

	for (int count = 0; count < n - 1; count++) {
		int u = minKey(key, mstSet,n);
		mstSet[u] = true;
		for (int v = 0; v < n; v++) {
			if (graph[u][v] && mstSet[v] == false && graph[u][v] < key[v]){
				parent[v] = u, key[v] = graph[u][v];
		}
	  }
	}
	
	for (int i = 1; i < n; i++) {
		cost = cost + graph[i][parent[i]];
	}

	if (mode_print_prim == 1) {
		for (int i = 1; i < n; i++) {
			cout << i << "-" << parent[i] << endl;
		}
	}

	return cost;
}

int create_matrix(string &a, int n,int mode, vector<vector<int> > &myvec) {
	vector<int> coord_x;
	vector<int> coord_y;
	vector<int> coord;
	
	for (int i = 0; i < a.length(); i++) {
		if (string(1, a[i]) != " ") {
			coord.push_back(a[i] - '0');
		}
	}

	for (int i = 0; i < coord.size(); i++) {
		if (i % 2) {
			coord_y.push_back(coord[i]);
		}
		else {
			coord_x.push_back(coord[i]);
		}
	}

	if (mode == 0){
		for (int i = 0; i < n; i++) {
			vector<int> v;
			for (int j = 0; j < n; j++) {
				v.push_back(0);
			}

			myvec.push_back(v);
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				myvec[i][j] = fabs(coord_x[i] - coord_x[j]) + fabs(coord_y[i] - coord_y[j]);
				myvec[j][i] = myvec[i][j];
			}
		}

		return prim(myvec, n);
	} 

	if (mode == 1) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i != j) {
					vector<int> v;
					v.push_back(coord_x[i]);
					v.push_back(coord_y[j]);
					myvec.push_back(v);
				}
			}
		}
	}

	return 0;
}

int main() {
	string coords="0 3 1 1 3 0 4 2 2 4";
	
	vector<vector<int> > myvec;
	vector<vector<int> > vector_of_coord;

	int n=5;
	int weight=create_matrix(coords, n, 0, myvec); 
	
	create_matrix(coords, n, 1, vector_of_coord); 
	
	int k = 0;
	int num = 0;
	int res = 0;
	string temp_string = "";
	string temp_string2 = "";
	string save_coord = coords;
	int c = 0;
	int d = 0;
	
	for (int k = 1; k < n; k++) {
		vector<vector<int> > ans = makeCombi(vector_of_coord.size(), k);
		cout << "Add point " << ans[0].size() << endl; 
		for (int i = 0; i < ans.size(); i++) {
			for (int j = 0; j < ans[i].size(); j++) {
				num = ans[i][j]; 
				stringstream c1,c2;
				c1 << vector_of_coord[num - 1][0];
				c2 << vector_of_coord[num - 1][1];
				
				temp_string = temp_string + " " + c1.str() + " " + c2.str();
			}

			temp_string2 = coords + temp_string; 
			res=create_matrix(temp_string2, n+k, 0, myvec); 
			myvec.clear();

			if (res < weight) { 
				weight = res;
				save_coord = temp_string2;
				d = n + k;
			}

			temp_string = "";
		}
	}

	cout << endl << "Weight:" << weight << endl;
	mode_print_prim = 1;
	create_matrix(save_coord, d, 0, myvec);
	cout << "Coord: " << save_coord << endl;
	system("pause");
	return 0;
}
