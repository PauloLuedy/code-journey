"""1️⃣ r = 0 → s[r] = 'a'

counter = {'a': 1}

Nenhuma repetição → while não roda

max_len = max(0, 0 - 0 + 1) = 1

🪟 janela = "a"

2️⃣ r = 1 → s[r] = 'b'

counter = {'a': 1, 'b': 1}

Sem repetição

max_len = max(1, 1 - 0 + 1) = 2

🪟 janela = "ab"

3️⃣ r = 2 → s[r] = 'c'

counter = {'a': 1, 'b': 1, 'c': 1}

Sem repetição

max_len = 3

🪟 janela = "abc"

4️⃣ r = 3 → s[r] = 'a'`

Agora 'a' já existe → counter = {'a': 2, 'b': 1, 'c': 1}

Entra no while counter['a'] > 1

Diminui counter[s[l]] → counter['a'] -= 1

l = 1

Agora counter = {'a': 1, 'b': 1, 'c': 1}

Repetição resolvida

max_len = max(3, 3 - 1 + 1) = 3

🪟 janela = "bca"

5️⃣ r = 4 → s[r] = 'b'`

counter = {'a': 1, 'b': 2, 'c': 1}

Repetição de 'b'

counter['a'] -= 1 → {'a': 0, 'b': 2, 'c': 1}

l = 2

ainda counter['b'] > 1

counter['b'] -= 1 → {'a': 0, 'b': 1, 'c': 1}

l = 3

max_len = max(3, 4 - 3 + 1) = 3

🪟 janela = "cab"

6️⃣ r = 5 → s[r] = 'c'`

Repetição novamente: 'c'

counter['c'] += 1 → {'a': 0, 'b': 1, 'c': 2}

move l:

counter['c'] -= 1 e l = 4

counter = {'a': 0, 'b': 1, 'c': 1}

max_len = max(3, 5 - 4 + 1) = 3

🪟 janela = "abc"

7️⃣ r = 6 → s[r] = 'b'`

counter = {'a': 0, 'b': 2, 'c': 1}

Repetição → move l

counter['b'] -= 1 e l = 5

max_len = 3

🪟 janela = "cb"

8️⃣ r = 7 → s[r] = 'b'`

counter = {'a': 0, 'b': 2, 'c': 0}

repete 'b' de novo → move l

counter['c'] já é 0, ignora

counter['b'] -= 1 → l = 7

max_len = 3

🪟 janela final = "b

def longestSubstring(s: str) -> int:
    l = 0
    counter = {}
    max_len = 0

    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r], 0) + 1
        while counter[s[r]] > 1:
            counter[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len
print(longestSubstring("abcabcbb"))  # 3
"""


"""
Entrada: nums = [2, 1, 5, 1, 3, 2], k = 3
Saída: 9
Explicação: subarray [5, 1, 3] tem soma = 9, que é a maior.



[2, 1, 5, 1, 3, 2]

l = 0
r = 0
k =3
max_sum = 0
counter = {}
max_sum = 8
[1, 5, 1, 3, 2]
max_sum = 7
[5, 1, 3, 2]
max_sum = 9
[1, 3, 2]
max_sum = 6
repetir
   add counter 
   max_sum = 2 + 1 + 5
   se len(counter) > 3:
         diminuir counter
         l += 1

   max_sum =max(max_sum, l - r + 1) 
"""


def maxSubArraySum(nums, k):
    window_sum = sum(nums[:k])   # soma inicial da janela
    print("Initial window sum:", window_sum)
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # entra nums[i], sai nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


print(maxSubArraySum([2, 1, 5, 1, 3, 2], 2))  # 9
