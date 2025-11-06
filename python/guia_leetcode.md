# GUIA DE ESTUDO PYTHON PARA LEETCODE

## 🎯 PADRÕES MAIS COMUNS NO LEETCODE

### 1. Two Pointers
```python
# Template básico
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

### 2. Sliding Window
```python
# Template básico
left = 0
for right in range(len(arr)):
    # Expande janela
    while condition:
        # Contrai janela
        left += 1
```

### 3. Hash Map para contagem
```python
from collections import Counter, defaultdict
count = Counter(arr)  # ou defaultdict(int)
```

### 4. BFS/DFS em árvores
```python
# DFS recursivo
def dfs(node):
    if not node:
        return
    # processa node
    dfs(node.left)
    dfs(node.right)

# BFS iterativo
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    # processa node
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
```

## 📚 ESTRUTURAS DE DADOS ESSENCIAIS

### List (Array)
- `append()`, `pop()`, `insert()`, `remove()`
- Slicing: `arr[start:end:step]`
- List comprehension: `[x for x in arr if condition]`

### Dict (Hash Map)
- `get()`, `setdefault()`, `keys()`, `values()`, `items()`
- `collections.defaultdict`, `collections.Counter`

### Set
- `add()`, `remove()`, `discard()`
- Operações: `&` (interseção), `|` (união), `-` (diferença)

### Deque (Queue/Stack)
```python
from collections import deque
dq = deque()
dq.append(x)      # adiciona à direita
dq.appendleft(x)  # adiciona à esquerda
dq.pop()          # remove da direita
dq.popleft()      # remove da esquerda
```

### Heap
```python
import heapq
heap = []
heapq.heappush(heap, item)
min_item = heapq.heappop(heap)
# Para max heap: use valores negativos
```

## 🧠 ESTRATÉGIAS DE RESOLUÇÃO

### 1. Leia o problema 2-3 vezes
- Identifique entrada e saída
- Procure por constraints importantes
- Pense em casos edge

### 2. Identifique o padrão
- Array/String → Two Pointers, Sliding Window
- Árvore/Grafo → DFS/BFS
- Contagem → Hash Map
- Otimização → DP
- Busca → Binary Search

### 3. Comece simples
- Solução bruta força primeiro
- Depois otimize

### 4. Teste com exemplos
- Casos normais
- Casos edge (vazio, um elemento, etc.)

## ⚡ DICAS DE PERFORMANCE

### Time Complexity comum:
- O(1): Hash map lookup
- O(log n): Binary search, heap operations
- O(n): Linear scan
- O(n log n): Sorting
- O(n²): Nested loops

### Space Complexity:
- Prefira O(1) quando possível
- Use hash maps para trade-off tempo vs espaço

## 🔧 FERRAMENTAS ÚTEIS

### Built-ins importantes:
```python
# Matemática
min(), max(), sum(), abs()
divmod(a, b)  # retorna (a//b, a%b)

# Itertools
from itertools import combinations, permutations, product

# Bisect para binary search
import bisect
bisect.bisect_left(arr, target)

# String
s.isalnum(), s.isdigit(), s.isalpha()
s.strip(), s.split(), s.join()
```

## 📈 PLANO DE ESTUDO

### Semana 1-2: Fundamentos
- Exercícios 1-9 (strings, arrays, matemática)
- Pratique 2-3 exercícios por dia

### Semana 3-4: Padrões Intermediários  
- Exercícios 10-19 (two pointers, sliding window, recursão)
- Comece problemas Easy do LeetCode

### Semana 5-8: Conceitos Avançados
- Exercícios 20-32 (DP, árvores, algoritmos)
- Problemas Medium do LeetCode

### Dica: Mantenha um caderno
- Anote padrões que aprender
- Liste erros comuns que comete
- Revise soluções antigas

## 🎯 PROBLEMAS LEETCODE RECOMENDADOS

### Easy (comece aqui):
1. Two Sum
2. Valid Parentheses  
3. Merge Two Sorted Lists
4. Best Time to Buy and Sell Stock
5. Valid Palindrome

### Medium (depois de dominar Easy):
1. Add Two Numbers
2. Longest Substring Without Repeating Characters
3. Container With Most Water
4. 3Sum
5. Group Anagrams

Boa sorte nos estudos! 🚀
