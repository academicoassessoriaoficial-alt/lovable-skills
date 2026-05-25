---
name: assessoria-dev-review
description: Use when reviewing or changing the Assessoria Academica Brasil platform, including orders, auctions, chat, payment, balance, withdrawal, or admin flows.
---

# Assessoria Dev Review

## Contexto

A plataforma possui cliente, colaborador e admin; pedidos, leilao academico, propostas, chat, Mercado Pago, saldo congelado, garantia, saque PIX e avaliacoes.

## Processo Seguro

1. Diagnosticar fluxo, perfis, registros e operacoes server-side envolvidos.
2. Localizar origem confiavel de preco, pagamento, saldo, garantia e saque.
3. Testar isolamento de dados, autorizacao e transicoes financeiras antes de alterar.
4. Propor alteracao minima com rollback.
5. Nao aplicar `Try to fix all`.

## Regras Criticas

- Nao alterar Mercado Pago, webhook, saldo, saque ou RLS financeira sem diagnostico.
- Cliente nao define preco final do leilao; o valor pago deriva da proposta aceita validada no servidor.
- Dados sensiveis de colaboradores nao podem ser expostos a clientes.
- Colaborador suspenso nao pode se reativar.
- Chat deve bloquear compartilhamento de contato externo conforme a regra do produto.
- Acao administrativa sensivel deve exigir MFA/AAL2.
- Saque deve ser validado no servidor com debito atomico, auditoria e idempotencia apropriada.
- Bloquear alteracoes em valores, webhook, MFA ou dados sensiveis sem testes de abuso e rollback.

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
- como testar cliente, colaborador e admin;
- plano de rollback.
