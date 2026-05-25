---
name: financial-flow-review
description: Use when a task changes Mercado Pago, payments, webhooks, balances, withdrawals, escrow, commission, cashback, orders, auctions, or monetary values.
---

# Financial Flow Review

## Objetivo

Impedir manipulacao indevida de valores e mudancas financeiras sem evidencias, controles server-side e reversao segura.

## Superficies Protegidas

Tratar como criticos: `payment_status`, `total_value`, `final_price`, `commission_value`, `saldo_disponivel`, `saldo_congelado`, `withdrawal_requests`, dados bancarios e webhooks.

## Diagnostico Primeiro

1. Mapear a origem confiavel de cada valor, estados de pagamento e transicoes permitidas.
2. Identificar endpoints, Edge Functions, tabelas, RLS, RPCs, triggers e eventos externos envolvidos.
3. Verificar autenticacao do webhook, idempotencia, repeticao, concorrencia, trilha de auditoria e tratamento de falhas.
4. Confirmar que cliente/browser nao calcula, autoriza nem grava valores finais, creditos, saques ou status de pagamento.
5. Bloquear qualquer correcao ate o fluxo atual, a falha reproduzida e o rollback estarem documentados.

## Regras De Implementacao

- Executar calculo e validacao financeira somente no servidor.
- Processar webhooks com idempotencia e logs de auditoria sem dados sensiveis desnecessarios.
- Efetuar debito, congelamento, liberacao e saque em operacao atomica ou transacao equivalente.
- Nao aplicar `Try to fix all` nem combinar ajuste visual com alteracao financeira.
- Validar cenarios aprovado, pendente, rejeitado, duplicado, reenvio de webhook e falha de atualizacao.

## Bloqueio Universal

Nao alterar pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking, tokens ou dados sensiveis sem diagnostico previo documentado, teste direcionado e plano de rollback.

## Relatorio Final Obrigatorio

Exigir:

- arquivos alterados;
- tabelas alteradas;
- policies/RLS alteradas;
- triggers/functions/RPCs alteradas;
- Edge Functions alteradas;
- riscos restantes;
- como testar, incluindo repeticao de webhook;
- plano de rollback.
