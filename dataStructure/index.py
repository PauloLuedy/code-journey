def groupAnagrams(strs):
    anagrams = {}  # dicionário normal

    for word in strs:
        # Cria a chave ordenando as letras
        key = ''.join(sorted(word))

        # Se a chave ainda não existir, cria uma nova lista
        if key not in anagrams:
            anagrams[key] = []

        # Adiciona a palavra original no grupo
        anagrams[key].append(word)

    # Retorna apenas os grupos (listas)
    return list(anagrams.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))