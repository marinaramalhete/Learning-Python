# Projeto Final - Python do Jeito Certo

# Gerar uma Certidão de Quitação Eleitoral (didática)

# Como guia para este projeto, você pode seguir os passos abaixo:

# 1. Abra o site [https://www.tse.jus.br/eleitor/certidoes/certidao-de-quitacao-eleitoral](https://www.tse.jus.br/eleitor/certidoes/certidao-de-quitacao-eleitoral) e verifique os dados solicitados pelo TSE para emissão de uma certidão de quitação eleitoral.
# 2. **[Cadastro]** Crie uma forma de cadastrar um eleitor fictício solicitando seus dados com a função input. Os dados devem ser armazenados em um arquivo de texto no formato CSV*. Além dos dados da certidão, insira um dado extra que represente se a pessoa votou ou não na última eleição.
# 3. **[Validação]** Crie uma forma de solicitar alguns dos dados da pessoa para verificar se é possível emitir sua certidão. Busque a pessoa na sua base de dados (CSV) e verifique se ela está com sua situação eleitoral regular (era obrigada a votar e votou ou não era obrigada a votar). Caso a pessoa não se encontre no cadastro exiba a mensagem *"Eleitor(a) NÃO Cadastado(a)"*. Caso a pessoa não possa votar, informe-a de acordo. Caso a situação esteja regular, proceda com o passo seguinte.
# 4. **[Emissão da Certidão]** Você deve gerar um arquivo que simule a Certidão de Quitação Eleitoral. Você pode gerar uma simples "certidao.txt" sem problemas, o importante é usar os dados cadastrados em uma mensagem que faça sentido. No entanto, existe um arquivo modelo no repositório do curso que pode ser usado para gerar um documento com forma de certidão. Vale a pena tentar usar este modelo e substituir os campos marcados com $ como $CAMPO$ pelo valor cadastrado correspondente.

# No material complementar, você encontrará um arquivo compactado (.zip) com o modelo de certidão (HTML), uma pasta **img** com a imagem de fundo da certidão (é necessária para mostrar direito) e também o arquivo CSV de exemplo, que você pode usar como uma base de dados inicial. Estes arquivos também se encontram na pasta **projeto** no repositório do curso no Github, caso você tenha familiaridade com a plataforma.