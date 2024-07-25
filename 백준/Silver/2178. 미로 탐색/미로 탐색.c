#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)
int M, N;
char arr[101][101] = { '0' };	//미로 배열
char visited[101][101] = { '0' };	//0: 방문 아직 안함 1: 방문 이미 함
int check[101][101] = { 0 };
typedef struct point {
	int i;
	int j;
}point;
void enqueue(point* Q, int* f, int* r, int x, int y) {
	*r = (*r + 1) % (M * N);
	Q[*r].i = x;
	Q[*r].j = y;
}
point dequeue(point* Q, int* f, int* r) {
	*f = (*f + 1) % (M * N);
	return Q[*f];
}
void mazeBFS() {
	int cnt = 0;
	int i = 0, j = 0;
	point* Q = (point*)malloc(sizeof(point) * (M * N + 1));
	int f = 0, r = 0;
	enqueue(Q, &f, &r, i, j);
	visited[i][j] = '1';
	check[i][j] = 1;
	while (f != r) {
		point m = dequeue(Q, &f, &r);
		i = m.i;
		j = m.j;
		if (i + 1 < N && (arr[i + 1][j] == '1') && (visited[i + 1][j] == '\0')) {
			visited[i + 1][j] = '1';
			check[i + 1][j] = check[i][j] + 1;
			enqueue(Q, &f, &r, i + 1, j);
		}
		if (j + 1 < M && (arr[i][j + 1] == '1') && (visited[i][j + 1] == '\0')) {
			visited[i][j + 1] = '1';
			check[i][j + 1] = check[i][j] + 1;
			enqueue(Q, &f, &r, i, j + 1);
		}
		if (i - 1 >= 0 && (arr[i - 1][j] == '1') && (visited[i - 1][j] == '\0')) {
			visited[i - 1][j] = '1';
			check[i - 1][j] = check[i][j] + 1;
			enqueue(Q, &f, &r, i - 1, j);
		}
		if (j - 1 >= 0 && (arr[i][j - 1] == '1') && (visited[i][j - 1] == '\0')) {
			visited[i][j - 1] = '1';
			check[i][j - 1] = check[i][j] + 1;
			enqueue(Q, &f, &r, i, j - 1);
		}
		//check[i][j] = check[m.i][m.j] + 1;
	}
	printf("%d\n", check[N-1][M-1]);
}
int main() {
	scanf("%d%d", &N, &M);
	getchar();
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%c", &(arr[i][j]));
		}
		getchar();
	}
	mazeBFS();
}