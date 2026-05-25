---
name: lovable-plan-approval
description: Use when Lovable presents an implementation plan for review before making code, database, integration, or UX changes.
---

# Lovable Plan Approval

## Objetivo

Avaliar um plano antes de sua execucao e devolver decisao clara com um prompt corrigido quando necessario.

## Metodo

1. Resumir objetivo, superficies atingidas e alteracoes pretendidas.
2. Pedir diagnostico ou evidencia quando o plano partir de suposicao nao comprovada.
3. Avaliar riscos tecnico, financeiro, juridico/LGPD, RLS/permissoes, UX e rollback.
4. Escolher uma decisao: `aprovado`, `aprovado com ajustes`, `recusado` ou `dividido em fases`.
5. Recusar plano que inclua `Try to fix all`, mudanca ampla sem evidencias ou alteracao sensivel sem validacao previa.

## Bloqueios

Nao aprovar mudancas em pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking, credenciais ou dados sensiveis sem diagnostico, teste dirigido e rollback. Preferir fase de investigacao separada da implementacao.

## Saida Obrigatoria

| Area | Risco | Evidencia necessaria | Ajuste exigido | Decisao |
| --- | --- | --- | --- | --- |

Depois, escrever um `Prompt corrigido para o Lovable` que limite escopo, estabeleca testes, proiba correcoes em lote e solicite reversao verificavel.

## Bloqueio Universal

Nao alterar pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking, tokens ou dados sensiveis sem diagnostico previo documentado, teste direcionado e plano de rollback.

## Relatorio Final Obrigatorio

Se o plano resultar em alteracao, exigir:

- arquivos alterados;
- tabelas alteradas;
- policies/RLS alteradas;
- triggers/functions/RPCs alteradas;
- Edge Functions alteradas;
- riscos restantes;
- como testar;
- plano de rollback.
