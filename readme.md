# CRUD DE FUNDAMENTOS DE PROGRAMAÇÃO


Nesse projeto foi desenvolvido o CRUD onde foram feitas as etapas de armazenamento de treinos e competições de um determinado atleta, podendo criar novos trenos, atalizar informações sobre eles e também deletalos. Além de tudo isso, foi implementada uma função de tempo para que possa cronometrar seus treinos.


## 🚀 C.R.U.D - CREATE | READ | UPDATE | DELETE


USAMOS DE *VETORES* PARA ARMAZENAR AS INFORMAÇOES, ORGANIZA-LAS E IMLEMENTALAS NO **'ARQUIVO.TXT"**


Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.


### 📋 Funcionamento






```python
Menu:
1. Adicionar Treino ou Competição
2. Visualizar Treinos ou Competição
3. Atualizar Treino ou Competição
4. filtrar Treino
5. Excluir Treino ou Competição
6. contar tempo de treino
7. Sair
```


### 🔧 manutenção de treinos:


após adicionar um treino, ele vai ser separado e implementado no arquivo'.txt', dessa forma:




```txt
treino;11/11/11;11.0;11.0;climafrio
competição;11/11/11;11.0;11.0;climaquente
```


quando ele é solicitado para sustituir/deletar, aparece no terminal dessa forma:


```python
1.treino;11/11/11;11.0;11.0;climafrio
2.competição;11/11/11;11.0;11.0;climaquente


##assim você seleciona o arquivo que quer alterar colocando sua numeração no input do terminal
```


## ⚙️ COM OS TREINOS ADICIOADOS


Com os treinos adicioados, ten-se as opções de visualização e também de substituir datasets


### 🔩 Substituindo as datasets


Os seguinte código serve para modificar os itens do arquivo individualmente, dessa forma, coseguindo alterar no formato correto, caso erre o formato, será exibido **ERRO DE TIPAGEM**:.


```python
try:
        index = int(input("Qual o dataset a modificar?: ")) - 1


        arquivo = arquivoHandler("treinos.txt", "r")
        data = arquivo.readlines()


        arquivo.close()


        data[index] = verificaTreino()


        arquivo = arquivoHandler("treinos.txt", "w")


        for i in data:
            arquivo.write(i)
       
        print("Dataset modificado com sucesso!")
        arquivo.close()


    except ValueError:
        print("Erro de tipagem")
    except IndexError:
        print("Dataset inexistente")
```


### ⌨️ E testes de estilo de codificação


Explique que eles verificam esses testes e porquê.


```
Dar exemplos
```


## 📦 Implantação


Adicione notas adicionais sobre como implantar isso em um sistema ativo


## 🛠️ Construído com


Mencione as ferramentas que você usou para criar seu projeto


* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - O framework web usado
* [Maven](https://maven.apache.org/) - Gerente de Dependência
* [ROME](https://rometools.github.io/rome/) - Usada para gerar RSS


## 🖇️ Colaborando


Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.


## 📌 Versão


Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto).


## ✒️ Autores


Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início


* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)


Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.


## 📄 Licença


Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.


## 🎁 Expressões de gratidão


* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.




---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊

