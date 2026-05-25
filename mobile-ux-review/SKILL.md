---
name: mobile-ux-review
description: Use when a task involves mobile layout, topbar, sidebar, drawer, menu, overlay, responsive behavior, or navigation usability.
---

# Mobile UX Review

## Objetivo

Diagnosticar problemas de uso em telas pequenas e propor ajustes pontuais sem redesenhar a aplicacao inteira.

## Matriz De Teste

| Viewport/zoom | Conferir |
| --- | --- |
| Mobile `375px` | Navegacao, CTA, teclado, overlay e scroll horizontal |
| Tablet | Transicao de menu/sidebar e largura de conteudo |
| Desktop | Ausencia de regressao e hierarquia preservada |
| Zoom `100%`, `90%`, `80%`, `75%`, `67%` | Cortes, colisoes, botoes e menus acessiveis |

## Criterios

- Nao permitir scroll horizontal involuntario.
- Manter botoes principais visiveis e acionaveis.
- Evitar texto cortado, sobreposicao, drawer preso ou modal inacessivel.
- Usar menu `Mais` quando a topbar nao comportar acoes secundarias.
- Preservar acessibilidade basica, foco e alvos de toque.

## Forma De Correcao

1. Registrar defeito, viewport, zoom, rota e passos de reproducao.
2. Identificar o componente e a regra de layout responsavel.
3. Propor a menor mudanca CSS/componente que resolva o defeito.
4. Repetir a matriz de teste e registrar o resultado.
5. Nao executar `Try to fix all` nem combinar ajuste visual com mudanca sensivel de dados.

Bloquear qualquer alteracao incidental em pagamento, saldo, saque, webhook, RLS financeira, MFA, notas, ranking ou dados sensiveis.

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
- como testar nos viewports e zooms indicados;
- plano de rollback.
