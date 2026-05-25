---
name: release-checklist
description: Use when preparing to publish, launch, share, deploy, or test a Lovable project with real users.
---

# Release Checklist

## Objetivo

Emitir uma decisao `GO` ou `NO-GO` baseada em evidencias, sem introduzir correcoes amplas durante a revisao.

## Checklist

Marcar cada item como `passou`, `falhou` ou `validacao manual pendente`:

| Area | Verificacao |
| --- | --- |
| Acesso | Login, logout, recuperacao relevante e rotas protegidas |
| Dados | RLS ativa e isolamento entre usuarios |
| Mobile | Fluxos principais funcionam em largura mobile |
| Conteudo | Ausencia de placeholders e links quebrados |
| Ambiente | Variaveis necessarias sem exposicao no cliente |
| Legal | Politica de privacidade, termos e consentimentos |
| Negocio | Fluxos principais e estados de erro testados |
| Qualidade | Sem erros criticos no console |
| Recuperacao | Rollback definido e executavel |

## Decisao

- Emitir `NO-GO` para falha critica, autorizacao nao validada ou risco sensivel sem diagnostico.
- Emitir `GO` somente quando itens criticos passarem ou tiverem aceite humano registrado.
- Nao usar `Try to fix all`; criar tarefas pequenas para falhas encontradas.
- Bloquear alteracoes improvisadas em pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking ou dados sensiveis.

## Bloqueio Universal

Nao alterar pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking, tokens ou dados sensiveis sem diagnostico previo documentado, teste direcionado e plano de rollback.

## Relatorio Final Obrigatorio

Se houver correcao antes da liberacao, exigir:

- arquivos alterados;
- tabelas alteradas;
- policies/RLS alteradas;
- triggers/functions/RPCs alteradas;
- Edge Functions alteradas;
- riscos restantes;
- como testar;
- plano de rollback.

Encerrar com a decisao `GO` ou `NO-GO` e seus bloqueadores.
