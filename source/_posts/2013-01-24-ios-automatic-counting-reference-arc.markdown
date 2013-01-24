---
layout: post
title: "iOS : Automatic Counting Reference - ARC"
date: 2013-01-24 14:58
comments: true
categories: 
---

Introdução
=============

A grande mudança no iOS 5 foi o novo recurso adicionado  chamado de contador automático de referência (ARC - Automatic Counting Reference).ARC é uma característica do novo compilador LLVM 3.0 que acaba completamente com  o gerenciamento  de memória manual.Usar o ARC em seus projetos é extremamente simples.Você mantém o mesmo código, como de costume, exceto que você não precisa realizar chamadas a release , retain ou ao autorelease.O ARC realiza todas essas tarefas pra você :).  
Com o ARC habilitado , o compilador irá inserir automaticamente retain,release e autorelease nos lugares corretos em seu programa.Mas se você ainda está cético  sobre o ARC - talvez você não confia  que ele vai fazer sempre a coisa certa, ou você acha que isso de alguma formar vai ser mais lento do que fazendo o gerenciamento de memória manual, se você acha isso , continue a ler.