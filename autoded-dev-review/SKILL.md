---
name: autoded-dev-review
description: Use when reviewing or changing AutoDED Windows desktop automation for DED+, SIED, lessons, attendance, grades, or migration routines.
---

# AutoDED Dev Review

## Contexto

AutoDED e um programa Windows em Python, Tkinter/ttk e Playwright. O arquivo principal e `ded_central.py`; a configuracao local fica em `C:\Users\pheli\Documents\DED Central\config.json` e evidencias de debug em `C:\Users\pheli\Documents\DED Central\debug`.

## Processo Seguro

1. Diagnosticar a falha com fluxo, tela, turma, disciplina e operacao pretendida.
2. Inspecionar o trecho minimo necessario antes de editar.
3. Preservar o fluxo seguro de notas, aulas, chamadas e migracao SIED para DED+.
4. Fazer mudanca pequena, validar sintaxe com `py_compile` e testar em cenario controlado.
5. Nao executar `Try to fix all`.

## Regras Criticas

- Nao incluir senha, credencial, chave privilegiada ou acesso fixo no codigo.
- Nao enviar dados sensiveis para servidor externo.
- Nao lancar aula, chamada ou nota sem conferir turma e disciplina.
- Nao duplicar aula ou atividade; validar existencia antes da criacao.
- Nao apagar dados sem regra explicita, confirmacao e rollback.
- Em falha, gerar relatorio `.txt`, HTML e screenshot na pasta de debug.
- Bloquear mudancas em notas, credenciais, dados sensiveis ou integracoes sem diagnostico previo.

## Bloqueio Universal

Nao alterar pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking, tokens ou dados sensiveis sem diagnostico previo documentado, teste direcionado e plano de rollback.

## Relatorio Final Obrigatorio

Exigir:

- arquivos alterados;
- tabelas alteradas, se aplicavel;
- policies/RLS alteradas, se aplicavel;
- triggers/functions/RPCs alteradas, se aplicavel;
- Edge Functions alteradas, se aplicavel;
- riscos restantes;
- como testar, incluindo `py_compile`;
- plano de rollback.
