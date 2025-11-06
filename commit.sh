#!/bin/bash

# Conventional Commit Script
# Usage: ./commit.sh

echo "🚀 Conventional Commit Generator"
echo "================================"

# Tipos de commit
echo "Selecione o tipo de commit:"
echo "1) feat     - Nova funcionalidade"
echo "2) fix      - Correção de bug"
echo "3) docs     - Documentação"
echo "4) style    - Formatação/estilo"
echo "5) refactor - Refatoração"
echo "6) test     - Testes"
echo "7) chore    - Tarefas/manutenção"

read -p "Digite o número (1-7): " tipo_num

case $tipo_num in
    1) tipo="feat" ;;
    2) tipo="fix" ;;
    3) tipo="docs" ;;
    4) tipo="style" ;;
    5) tipo="refactor" ;;
    6) tipo="test" ;;
    7) tipo="chore" ;;
    *) echo "❌ Opção inválida"; exit 1 ;;
esac

# Escopo (opcional)
read -p "Escopo (opcional, ex: api, ui, auth): " escopo

# Descrição
read -p "Descrição curta: " descricao

if [ -z "$descricao" ]; then
    echo "❌ Descrição é obrigatória"
    exit 1
fi

# Corpo (opcional)
read -p "Descrição detalhada (opcional): " corpo

# Breaking change
read -p "É uma breaking change? (y/n): " breaking

# Monta a mensagem
if [ -n "$escopo" ]; then
    mensagem="$tipo($escopo): $descricao"
else
    mensagem="$tipo: $descricao"
fi

if [ "$breaking" = "y" ]; then
    mensagem="$mensagem

BREAKING CHANGE: $corpo"
elif [ -n "$corpo" ]; then
    mensagem="$mensagem

$corpo"
fi

# Mostra preview
echo ""
echo "📝 Preview do commit:"
echo "===================="
echo "$mensagem"
echo ""

# Confirma
read -p "Confirmar commit? (y/n): " confirma

if [ "$confirma" = "y" ]; then
    git add .
    git commit -m "$mensagem"
    echo "✅ Commit realizado com sucesso!"
else
    echo "❌ Commit cancelado"
fi
