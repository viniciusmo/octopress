---
layout: post
title: "iOS : Automatic Counting Reference - ARC"
date: 2013-01-24 14:58
comments: true
categories: iOS
---

Introdução
=============

A grande mudança no ***iOS 5*** foi o novo recurso adicionado  chamado de contador automático de referência (ARC - Automatic Counting Reference).ARC é uma característica do novo compilador LLVM 3.0 que acaba completamente com  o gerenciamento  de memória manual.Usar o ARC em seus projetos é extremamente simples.Você mantém o mesmo código, como de costume, exceto que você não precisa realizar chamadas a ***release*** , ***retain*** ou ao ***autorelease***.O ARC realiza todas essas tarefas pra você :).  
Com o ARC habilitado , o compilador irá inserir automaticamente ***retain***,***release*** e ***autorelease*** nos lugares corretos em seu programa.

Como o ARC funciona?
=============

Você provavelmente já está familiarizado com o gerenciamento de memória manual, que funciona basicamente assim:  

   *   Se você precisa manter um objeto , você deve retê-lo (***retain***), a menos que já foi retido para você.
   *   Se você quiser parar de usar um objeto , você precisa para liberá-lo (***release***), a menos que já foi liberado para você ( com o ***autorelease***).

Acho que para todos no começo , essa tarefa de entender o gerenciamento de memória manual é algo difícil,mas com o tempo se torna natural  manter o balanceamento dos ***retains*** e ***releases*** .Exceto quando você esquece de realizar essa tarefa rs  
Os princípios de gerenciamento de memória manual não são difíceis, mas é muito fácil cometer um erro. E esses pequenos erros podem ter consequências terríveis. O seu aplicativo irá falhar em algum ponto, porque você lançou um objeto muitas vezes e suas variáveis ​​estão apontando para dados que já não é válido, ou você vai ficar sem memória, porque se você não liberar os objetos  acontecem os famosos ***leaks***.  
O ***Static Analyzer*** do Xcode é uma grande ajuda para encontrar esses problemas , mas o ARC vai um passo além.O ARC evita problemas de gerenciamento de memória completamente ,inserindo o ***retain*** e o ***release*** pra você.  
É importante perceber que a ARC é uma característica do compilador do Objective-C e, portanto, todo o trabalho do ARC é feito na compilação do seu programa. O ARC não é uma característica de tempo de execução (com exceção de uma pequena parte, o sistema de ***weak pointer***), nem é  um  ***garbage collector***.  

Ponteiros mantém os objetos em memória
=============
As novas regras que você tem que aprender para o ARC são bastante simples. Com o gerenciamento de memória manual você precisava dar um ***retain*** no objeto para mantê-lo em memória. Isso já não é necessário, tudo que você precisa é fazer um ponteiro para o objeto.  
Enquanto há uma variável que aponta para um objeto, esse objeto permanece na memória. Quando o ponteiro chega um novo valor ou deixa de existir, o objeto associado é liberado (***release***). Isto é válido para todas as variáveis​​:***variáveis ​​de instância***, ***propriedades***, e até  mesmo,***variáveis ​​locais***.  
Veja o seguinte exemplo :
{% codeblock lang:objc %}
     NSString * firstName = self.textField.text;  
{% endcodeblock %}
 A variável ***firstName*** é um ponteiro para o objeto string "Ray"  que  guarda o valor do campo de texto.Essa variável agora também é proprietário do objeto string "Ray".

{% img center https://raw.github.com/viniciusmo/octopress/master/source/images/blog/ios/arc-introduction/image05.png%}

Um objeto pode ter mais de um dono. Até que o usuário não mude o conteúdo do UITextField,a propriedade self.textField.text também  é um proprietário do objeto string "Ray". Existem dois ponteiros para manter esse objeto em memória :  
{% img center https://raw.github.com/viniciusmo/octopress/master/source/images/blog/ios/arc-introduction/image00.png%}
Momentos depois, o usuário vai digitar algo novo no campo de texto e sua propriedade de texto agora aponta para um novo objeto string. Mas o objeto string original ainda tem um proprietário (a variável firstName) e, portanto, permanece na memória.  
{% img center https://raw.github.com/viniciusmo/octopress/master/source/images/blog/ios/arc-introduction/image04.png%}

Somente quando firstName recebe um novo valor também, ou sai do escopo - porque é uma variável local e o método termina, ou porque é uma variável de instância e o objeto a que  ela pertence é desalocado .O objeto string não tem mais proprietários, o seu retain count é 0 e ele é desalocado.

{% img center https://raw.github.com/viniciusmo/octopress/master/source/images/blog/ios/arc-introduction/image06.png%}
Chamamos ponteiros como firstName e textField.text  de ***strong*** porque mantém os objetos vivos (em memória). Por padrão, todas as variáveis ​​de instância e variáveis ​​locais são ponteiros ***strong***.  
Há também um ponteiro chamado de ***weak***. Variáveis ​​que são ***weak*** ainda pode apontar para objetos, mas eles não se tornam proprietários.  
Veja o seguinte exemplo :  
{% codeblock lang:objc %}
__weak NSString * weakName = self.textField.text;
{% endcodeblock %}

{% img center https://raw.github.com/viniciusmo/octopress/master/source/images/blog/ios/arc-introduction/image02.png%}

A variável ***weakName*** aponta para o mesmo objeto  string "Rayman" que a propriedade self.textField.text aponta , mas ela não é proprietária do objeto.  
Se o campo de texto alterar o conteúdo, então o objeto string "Rayman" não tem mais donos e é desalocado.  

{% img center https://raw.github.com/viniciusmo/octopress/master/source/images/blog/ios/arc-introduction/image03.png%}

Quando isso acontece, o valor de ***weakName*** torna-se automaticamente nulo.Note que este é extremamente conveniente, pois impede ponteiros ***weak*** de apontar para a memória liberada.  
Você provavelmente não vai usar muito os  ponteiros ***weaks***. Eles são principalmente úteis quando dois objetos têm uma relação parent-child. O parent vai ter um ponteiro strong para seu child - e, portanto, é o "dono" - mas, a fim de evitar ciclos de propriedade, o child só tem um ponteiro ***weak*** de volta para seu parent.  
Um exemplo disto é o padrão delegate. Seu UIControllerView pode possuir um UITableView através de um ponteiro ***strong***. Já o data source e o delegate  apontam para o UIControllerView mas são ***weaks*** ponteiros.  

{% img center https://raw.github.com/viniciusmo/octopress/master/source/images/blog/ios/arc-introduction/image01.png%}


Veja o seguinte exemplo :  

{% codeblock lang:objc %}
__weak NSString *str = [[NSString alloc] initWithFormat:...];
NSLog(@"%@", str);  // a saída será "(null)"
{% endcodeblock %}



Não existe um dono para o objeto string (porque str é fraco) e o objeto será desalocado imediatamente após ele ser criado. O Xcode vai dar o  seguinte aviso quando você faz isso ,porque provavelmente não é o que você quer fazer.
{% codeblock lang:objc %}

(“Warning: assigning retained object to weak variable; object will be released after assignment”).
{% endcodeblock %}

Você pode usar a palavra-chave __***strong*** para falar que uma variável é um ponteiro ***strong***:
{% codeblock lang:objc %}
__strong NSString *firstName = self.textField.text;
{% endcodeblock %}

As variáveis ​​são ***strong*** por default e o ***__strong*** pode ser omitido. Propriedades também podem ser ***strong*** e ***weak***. A notação para propriedades é:  
{% codeblock lang:objc %}
@property (nonatomic, strong) NSString *firstName;
@property (nonatomic, weak) id <MyDelegate> delegate;
{% endcodeblock %}

O ARC vai remover um monte de lixo do seu código. Você não tem que pensar sobre quando usar o release ou quando usar o retain, apenas sobre como os objetos se relacionam entre si.  

***Traduzido de ***: [http://www.raywenderlich.com/5677/beginning-arc-in-ios-5-part-1](http://www.raywenderlich.com/5677/beginning-arc-in-ios-5-part-1).
