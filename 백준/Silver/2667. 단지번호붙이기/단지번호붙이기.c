#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)
int N;
char arr[26][26] = { '0' };
int cnt = 0;
int visited[26][26] = { 0 };

int size[625];
int size_i = 0;

void DFS(int i, int j) {
	visited[i][j] = 1;
	cnt++;
	if (i + 1 < N && (arr[i + 1][j]=='1') && visited[i + 1][j] == 0) {
		DFS(i + 1, j);
	}
	if (j + 1 < N && (arr[i][j + 1]=='1') && visited[i][j + 1] == 0) {
		DFS(i, j + 1);
	}
	if (i - 1 >= 0 && (arr[i - 1][j]=='1') && visited[i - 1][j] == 0) {
		DFS(i - 1, j);
	}
	if (j - 1 >= 0 && (arr[i][j - 1]=='1') && visited[i][j - 1] == 0) {
		DFS(i, j - 1);
	}
	else return;
}

int main() {
	scanf("%d", &N);	//5~25
	getchar();
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%c", &arr[i][j]);
		}
		getchar();
	}
	int dcnt = 0;
	//getchar();
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if ((arr[i][j]=='1') && visited[i][j] == 0) {
				DFS(i, j);
				size[size_i++] = cnt;
				dcnt++;
				cnt = 0;
			}
		}
	}
	for (int i = 1; i < size_i; i++) {
		int temp = size[i];
		int j = i;
		while (j > 0 && size[j - 1] > temp) {
			size[j] = size[j - 1];
			j--;
		}
		size[j] = temp;
	}
	printf("%d\n", dcnt);
	for (int i = 0; i < size_i; i++) printf("%d\n", size[i]);
}