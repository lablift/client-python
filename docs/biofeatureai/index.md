# BioFeatureAI

Extração de sexo, idade aparente, score de comprometimento da pele e Índice de Massa Corporal a partir de foto de rosto para apoiar operadoras de planos de saúde na gestão digital de saúde populacional.

## Exemplo do processo completo

Um exemplo de código que realiza autenticação, instancia as classes necessárias e realiza uma chamada síncrona para obter a predição de uma imagem qualquer pode ser encontrado abaixo.

<script src="https://emgithub.com/embed.js?target=https://github.com/lablift/client-python/blob/main/examples/biofeature.py&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

O resultado mostrado em tela após a execução desse código contém o resultado da predição como um dicionário Python.

---

## Processo detalhado

Para se autenticar e ter acesso aos nossos produtos é necessário gerar um ***token*** de acesso. Trata-se de uma *string* com validade limitada, obtida fornecendo seus dados de cadastro (usuário e senha). A função generate_token é responsável por gerar os ***tokens*** diretamente no cliente. Ela pode receber como argumentos seu usuário e senha (parâmetros em formato *string* ***username*** e ***password***), caso contrário eles serão solicitados na execução.

Com o ***token*** em mãos, é possível instanciar tanto o cliente quanto o próprio Biofeature e utilizar o método ***call***, que recebe como parâmetro em formato *string* obrigatório **img**, que é o *path* até a imagem que deseja submeter para predição. Esse método se comunica com nosso modelo de inteligência artificial e retorna o resultado da predição como *dict* dentro de alguns segundos.

## Api REST

O BiofeatureAI também pode ser utilizado a partir de uma API REST. Você pode acessar a documentação da API REST <a href="https://api.biofeature.lablift.com.br/docs/" target="_blank">clicando aqui</a>.