class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque

        # 큐에 있는 유전자의 문자를 하나씩 acgt로 바꿈
        # bank에 있다면 변이횟수++ 하고 큐에 넣음
        # 큐에서 꺼낼 때 endGene과 검사
        q = deque([[startGene, 0]])
        visited = {startGene}
        while q:
            gene, mutationCnt = q.popleft()
            if gene == endGene: 
                return mutationCnt

            for idx, c in enumerate(gene):
                for nuc in 'ATCG':
                    mutation = gene[:idx] + nuc + gene[idx+1:]
                    if mutation not in visited and mutation in bank:
                        q.append([mutation, mutationCnt+1])
                        visited.add(mutation)
        else:
            return -1
