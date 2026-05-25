---
name: scriptum-dev-review
description: Use when reviewing or changing Scriptum features for academic notes, references, citations, chapters, tags, or researcher data.
---

# Scriptum Dev Review

## Contexto

Scriptum atende pesquisadores, TCC, mestrado e doutorado. Proteger fichamentos, referencias, citacoes, capitulos, tags, notas e demais dados privados de pesquisa.

## Processo Seguro

1. Identificar entidade, proprietario dos dados, operacao e regras de compartilhamento existentes.
2. Diagnosticar o problema e mapear tabelas, RLS e componentes atingidos.
3. Propor a menor correcao sem ampliar acesso entre contas.
4. Validar leitura, escrita, exportacao e exclusao com usuarios distintos.
5. Nao executar `Try to fix all`.

## Regras Criticas

- Nao misturar dados entre usuarios nem tornar fichamentos privados publicos por conveniencia.
- Validar ABNT ou APA quando houver geracao ou formatacao de referencia, explicitando norma escolhida.
- Nao apagar fichamentos sem confirmacao clara e possibilidade de recuperacao ou rollback.
- Nao alterar estrutura de dados sem plano de migracao, preservacao e reversao.
- Bloquear mudancas incidentais em pagamento, saldo, webhook, RLS sensivel, MFA ou dados pessoais sem diagnostico previo.

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
- como testar isolamento, referencias e exclusao;
- plano de rollback.
