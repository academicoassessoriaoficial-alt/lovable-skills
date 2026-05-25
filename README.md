# Lovable Skills

Colecao local de skills para revisoes seguras em projetos desenvolvidos no Lovable. Cada pasta contem um `SKILL.md` independente, com gatilho claro e instrucoes para diagnosticar antes de alterar codigo, banco ou integracoes.

## Conteudo

| Skill | Finalidade | Uso recomendado |
| --- | --- | --- |
| `security-scan-review` | Revisar findings do Security Scan e propor correcao minima | Automatico |
| `lovable-plan-approval` | Aprovar, ajustar ou recusar planos antes da execucao | Manual |
| `supabase-rls-audit` | Auditar Auth, RLS, policies, RPCs, triggers, Storage e Realtime | Automatico |
| `financial-flow-review` | Proteger pagamentos, saldo, saque e webhooks | Automatico |
| `release-checklist` | Emitir decisao go/no-go antes de release | Manual |
| `mobile-ux-review` | Revisar navegacao e responsividade mobile | Manual |
| `sied-dev-review` | Proteger regras criticas do SIED | Automatico no projeto SIED |
| `assessoria-dev-review` | Proteger operacoes da Assessoria Academica Brasil | Automatico nesse projeto |
| `scriptum-dev-review` | Proteger dados academicos privados do Scriptum | Automatico nesse projeto |
| `autoded-dev-review` | Proteger automacoes locais do AutoDED | Automatico nesse projeto |

`Automatico` significa manter a skill habilitada no projeto relevante para que o Lovable possa seleciona-la quando a descricao corresponder ao pedido. `Manual` significa preferir invoca-la explicitamente pelo menu `/` quando voce quiser a revisao.

## Limite Atual Do Import Pelo GitHub

A documentacao oficial do Lovable, consultada em 25 de maio de 2026, informa que cada repositorio GitHub importado representa **uma unica skill**. O repositorio precisa conter `SKILL.md` na raiz ou dentro de uma unica pasta superior. Portanto, este repositorio `lovable-skills` funciona como catalogo e fonte versionada, mas nao pode ser importado de uma vez como dez skills.

Fonte: [Define reusable instructions with skills - Lovable Documentation](https://docs.lovable.dev/features/skills)

## Subir Este Catalogo Para O GitHub

Abra um terminal na pasta `lovable-skills` e execute:

```powershell
git init
git add .
git commit -m "add lovable workspace skills"
git branch -M main
git remote add origin https://github.com/academicoassessoriaoficial-alt/lovable-skills.git
git push -u origin main
```

O repositorio publico principal e `https://github.com/academicoassessoriaoficial-alt/lovable-skills`. O login e a autorizacao do GitHub devem ser feitos manualmente por voce.

## Importar No Lovable Pelo GitHub

Para usar a importacao GitHub, publique uma copia independente de cada skill, deixando seu `SKILL.md` na raiz do repositorio individual. Exemplo para `security-scan-review`:

```powershell
mkdir lovable-skill-security-scan-review
Copy-Item .\security-scan-review\SKILL.md .\lovable-skill-security-scan-review\SKILL.md
cd .\lovable-skill-security-scan-review
git init
git add .
git commit -m "add security scan review skill"
git branch -M main
git remote add origin https://github.com/academicoassessoriaoficial-alt/lovable-skill-security-scan-review.git
git push -u origin main
```

Repita o fluxo para cada pasta, trocando o nome do repositorio. No Lovable:

1. Acesse `Settings` > `Skills`.
2. Clique em `Import` e escolha a aba `GitHub`.
3. Cole a URL publica do repositorio individual da skill.
4. Revise o nome, a descricao e as instrucoes importadas.
5. Habilite a skill apenas nos projetos em que ela se aplica.

## URLs Para Importacao Individual

Depois que cada repositorio individual existir publicamente, use:

| Skill | URL a colar no Lovable |
| --- | --- |
| `security-scan-review` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-security-scan-review` |
| `lovable-plan-approval` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-lovable-plan-approval` |
| `supabase-rls-audit` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-supabase-rls-audit` |
| `financial-flow-review` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-financial-flow-review` |
| `release-checklist` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-release-checklist` |
| `mobile-ux-review` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-mobile-ux-review` |
| `sied-dev-review` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-sied-dev-review` |
| `assessoria-dev-review` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-assessoria-dev-review` |
| `scriptum-dev-review` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-scriptum-dev-review` |
| `autoded-dev-review` | `https://github.com/academicoassessoriaoficial-alt/lovable-skill-autoded-dev-review` |

Como alternativa sem repositorios separados, compacte uma pasta de skill por vez em `.zip` e use a aba `ZIP` do importador. O arquivo compactado deve conter somente a pasta da skill com seu `SKILL.md`.

## Validacao Local

```powershell
python .\validate_skills.py
```

O validador verifica as dez pastas, o frontmatter obrigatorio, o formato dos nomes, o inicio de cada descricao e padroes suspeitos de credenciais nos arquivos `SKILL.md`.

## Uso Seguro

Estas skills orientam o Lovable a diagnosticar antes de corrigir, evitar alteracoes amplas, nunca aplicar `Try to fix all` automaticamente e produzir relatorio final com alteracoes, riscos, testes e rollback. Elas nao substituem testes manuais, revisao humana ou controles de acesso do projeto.
