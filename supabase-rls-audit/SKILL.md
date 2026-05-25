---
name: supabase-rls-audit
description: Use when a task involves Supabase Auth, Database, RLS, policies, RPCs, triggers, Edge Functions, Storage, or Realtime authorization.
---

# Supabase RLS Audit

## Objetivo

Diagnosticar exposicao ou escalada de privilegio antes de propor a menor alteracao de autorizacao possivel.

## Auditoria

1. Mapear tabelas, operacoes, perfis, policies, RPCs, triggers, funcoes, buckets e canais Realtime afetados.
2. Confirmar RLS ativa em tabelas com dados de usuario ou operacionais.
3. Revisar policies amplas, ausencia de `WITH CHECK`, acesso entre usuarios e escrita de campos administrativos por usuario comum.
4. Inspecionar funcoes `SECURITY DEFINER`, `search_path`, autorizacao interna e chamadas expostas.
5. Verificar vazamento de PII e impacto em tabelas financeiras, notas, ranking, credenciais ou permissoes.
6. Tratar Edge Functions, Storage e Realtime como superficies de autorizacao.

## Validacao Obrigatoria

| Perfil | Pode ler | Pode gravar | Deve ser bloqueado |
| --- | --- | --- | --- |
| Usuario proprietario | Dados proprios permitidos | Operacoes proprias permitidas | Campos administrativos |
| Outro usuario autenticado | Somente dados autorizados | Nada de terceiros | Dados privados de terceiros |
| Administrador autorizado | Escopo previsto | Acoes previstas | Elevacao indevida |
| Nao autenticado | Conteudo realmente publico | Nenhuma gravacao sensivel | Dados protegidos |

Nao aplicar `Try to fix all`. Bloquear alteracao de RLS financeira, MFA, notas, ranking ou dados sensiveis sem diagnostico e rollback aprovados.

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
- como testar com perfis diferentes;
- plano de rollback.
