#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)
typedef struct incidence {
	int opn;
	struct incidence* next;
}IC;
typedef struct vertex {
	int n;
	struct incidence* link;
}VX;
void enqueue(int* Q, int* f, int* r, int N, int x) {
	*r = (*r + 1) % N;
	Q[*r] = x;
}
int dequeue(int* Q, int* f, int* r, int N) {
	*f = (*f + 1) % N;
	return Q[*f];
}
IC* getinc() {
	IC* newinc = (IC*)malloc(sizeof(IC));
	newinc->next = NULL;
	int n1 = 0;
	int n2 = 0;
	return newinc;
}
VX* makeVertexList(VX* LV, int N, int M) {
	LV = (VX*)malloc(sizeof(VX) * N);
	for (int i = 0; i < N; i++) {
		LV[i].n = i + 1;
		LV[i].link = getinc();
	}

	int v1, v2;
	for (int i = 0; i < M; i++) {
		scanf("%d%d", &v1, &v2);
		//v1->v2
		IC* p = LV[(v1 - 1)].link;
		while ((p->next != NULL) && (p->next->opn < v2)) {
			p = p->next;
		}
		IC* new12 = getinc();
		new12->opn = v2;
		new12->next = p->next;
		p->next = new12;
		//v2->v1
		p = LV[(v2 - 1)].link;
		while ((p->next != NULL) && (p->next->opn < v1)) {
			p = p->next;
		}
		IC* new21 = getinc();
		new21->opn = v1;
		new21->next = p->next;
		p->next = new21;
	}
	return LV;
}
void DFS(VX* LV, int V, int* visited) {
	visited[V] = 1;
	printf("%d ", V);
	IC* p = LV[V - 1].link->next;
	while (p) {
		if (visited[p->opn] == 0) DFS(LV, p->opn, visited);
		else p = p->next;
	}
}
void BFS(VX* LV, int N, int V, int* visited) {
	int* Q = (int*)malloc(sizeof(int) * (N + 1));
	int f = 0, r = 0;
	visited[V] = 1;
	printf("%d ", V);
	enqueue(Q, &f, &r, N, V);
	while (f != r) {
		int w = dequeue(Q, &f, &r, N);
		IC* p = LV[w - 1].link->next;
		while (p) {
			if (visited[p->opn] == 0) {
				visited[p->opn] = 1;
				printf("%d ", p->opn);
				enqueue(Q, &f, &r, N, p->opn);
			}
			p = p->next;
		}
	}
}
int main() {
	int N, M, V;
	scanf("%d%d%d", &N, &M, &V);
	VX* LV = NULL;
	LV = makeVertexList(LV, N, M);
	
	int* visited = (int*)malloc(sizeof(int) * (N + 1));
	for (int i = 1; i <= N; i++) visited[i] = 0;
	DFS(LV, V, visited);
	
	printf("\n");
	for (int i = 1; i <= N; i++) visited[i] = 0;
	BFS(LV, N, V, visited);
}