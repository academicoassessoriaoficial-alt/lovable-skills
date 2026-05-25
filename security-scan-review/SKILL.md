---
name: security-scan-review
description: Use when Lovable Security Scan reports findings or a user asks whether reported security issues require a safe fix.
---

# Security Scan Review

## Objetivo

Revisar findings antes de qualquer correcao e produzir somente mudancas pequenas, justificadas e testaveis.

## Fluxo Obrigatorio

1. Solicitar ou ler o finding completo, severidade, recurso afetado, trecho relevante e evidencia reproduzivel.
2. Nao executar `Try to fix all` nem aceitar correcoes em lote.
3. Verificar se o resultado ainda existe no codigo, banco e configuracao atuais.
4. Classificar cada finding como `risco real critico`, `risco real medio`, `falso positivo`, `resultado cacheado/desatualizado` ou `comportamento intencional que precisa confirmacao`.
5. Bloquear alteracao em pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking, credenciais ou dados sensiveis ate existir diagnostico especifico e rollback.
6. Somente depois da aprovacao do diagnostico, propor a menor correcao isolada possivel.

## Tabela De Analise

Entregar antes de corrigir:

| Finding | Recurso/arquivo | Evidencia atual | Classificacao | Impacto | Correcao minima proposta | Teste | Rollback |
| --- | --- | --- | --- | --- | --- | --- | --- |

Se faltarem evidencias, marcar como `precisa investigacao` e nao corrigir.

## Prompt Seguro Para Correcao

Gerar um prompt pronto para colar no Lovable que restrinja a correcao aos findings confirmados, preserve comportamento nao relacionado, proiba ampliacao de acesso sem aprovacao, execute testes focados e entregue reversao.

## Bloqueio Universal

Nao alterar pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking, tokens ou dados sensiveis sem diagnostico previo documentado, teste direcionado e plano de rollback.

## Relatorio Final Obrigatorio

Ao concluir qualquer alteracao, exigir:

- arquivos alterados;
- tabelas alteradas;
- policies/RLS alteradas;
- triggers/functions/RPCs alteradas;
- Edge Functions alteradas;
- riscos restantes;
- como testar;
- plano de rollback.
