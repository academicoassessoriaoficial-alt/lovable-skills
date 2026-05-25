---
name: sied-dev-review
description: Use when reviewing or changing the SIED educational platform built with Lovable, Supabase, React, and TypeScript.
---

# SIED Dev Review

## Contexto

O SIED possui perfis `student`, `admin/professor titular`, `coordinator`, `support_teacher` e `super_admin`. Proteger notas, tokens, ranking, `quiz_attempts.score`, gabaritos, RLS e dados reais.

## Processo Seguro

1. Identificar perfil afetado, tabela/componente, operacao e comportamento atual.
2. Reproduzir ou explicar o problema antes de propor codigo ou SQL.
3. Separar mudanca visual de mudanca de autorizacao, pontuacao ou registro academico.
4. Aplicar a menor correcao e validar com perfis distintos.
5. Nao executar `Try to fix all`.

## Guardrails

- Nao alterar `has_role` sem evidencia forte, justificativa explicita e rollback.
- Nao reintroduzir policies amplas com `has_role(auth.uid(),'admin')` para teachers.
- Nao expor gabaritos ou respostas corretas a alunos.
- Nao recalcular tokens, ranking ou conquistas sem explicar impacto retroativo e criterios.
- Mudancas em notas, ranking e `quiz_attempts` exigem diagnostico, teste por perfil e rollback antes da execucao.
- Bloquear mudanca em pagamento, saldo, webhook, RLS financeira, MFA ou dados sensiveis sem revisao dedicada.

## Validacoes Minimas

Testar aluno, professor titular, coordenador, professor de apoio e super administrador para leitura e escrita autorizadas; verificar que aluno nao altera score, nota, ranking, permissao nem acessa gabarito.

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
- como testar por perfil;
- plano de rollback.
