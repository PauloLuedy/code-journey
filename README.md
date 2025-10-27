# Conventional Commits

Guide for standardizing commit messages following the Conventional Commits specification.

## Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

- **feat**: new feature
- **fix**: bug fix
- **docs**: documentation changes
- **style**: formatting, semicolons, etc (no code change)
- **refactor**: code refactoring
- **test**: adding or fixing tests
- **chore**: build tasks, configurations, etc

## Examples

### Simple commit
```
feat: add email validation
```

### With scope
```
feat(auth): implement Google login
```

### With body and footer
```
fix: fix form validation error

The email field was not correctly validating
addresses with subdomains.

Closes #123
```

### Breaking change
```
feat!: change user API structure

BREAKING CHANGE: the /users endpoint now returns
an object with different properties
```

## Benefits

- Cleaner and organized commit history
- Automatic changelog generation
- Easier identification of breaking changes
- Improved communication between developers
- Integration with semantic versioning tools

## Tools

- **commitizen**: CLI for creating standardized commits
- **commitlint**: commit message validation
- **standard-version**: automatic changelog generation
