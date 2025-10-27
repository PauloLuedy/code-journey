# Conventional Commits

Guia para padronização de mensagens de commit seguindo a especificação Conventional Commits.

## Formato

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

## Tipos

- **feat**: nova funcionalidade
- **fix**: correção de bug
- **docs**: mudanças na documentação
- **style**: formatação, ponto e vírgula, etc (sem mudança de código)
- **refactor**: refatoração de código
- **test**: adição ou correção de testes
- **chore**: tarefas de build, configurações, etc

## Exemplos

### Commit simples
```
feat: adicionar validação de email
```

### Com escopo
```
feat(auth): implementar login com Google
```

### Com corpo e rodapé
```
fix: corrigir erro de validação no formulário

O campo de email não estava validando corretamente
endereços com subdomínios.

Closes #123
```

### Breaking change
```
feat!: alterar estrutura da API de usuários

BREAKING CHANGE: o endpoint /users agora retorna
um objeto com propriedades diferentes
```

## Benefícios

- Histórico de commits mais limpo e organizado
- Geração automática de changelogs
- Facilita identificação de breaking changes
- Melhora comunicação entre desenvolvedores
- Integração com ferramentas de versionamento semântico

## Ferramentas

- **commitizen**: CLI para criar commits padronizados
- **commitlint**: validação de mensagens de commit
- **standard-version**: geração automática de changelog
