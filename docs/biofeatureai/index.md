# BioFeatureAI

O LabLift BioFeature AI é uma solução de inteligência artificial que extrai fatores de risco de saúde a partir de foto de rosto. Com esta solução, nossos clientes conseguem ser mais eficientes na gestão preventiva de saúde. 

A interface Python do BioFeature AI provê padronização para integração com outros sistemas, aumentando a produtividade e reduzindo *bugs* durante a implantação e manutenção do produto. 

## Autenticação

Para se autenticar e ter acesso aos nossos produtos é necessário gerar um ***token*** de acesso. Trata-se de uma *string* com validade limitada, obtida fornecendo seus dados de cadastro (usuário e senha). Caso você não possua um cadastro, contate o administrador da conta LabLift da sua empresa. 

A função generate_token é responsável por gerar os ***tokens*** diretamente no cliente. Ela pode receber como argumentos seu usuário e senha (parâmetros em formato *string* ***username*** e ***password***), caso contrário eles serão solicitados na execução. O exemplo abaixo mostra como utilizar a função.

<script src="https://emgithub.com/embed.js?target=https://github.com/lablift/client-python/blob/main/examples/create_token.py&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>


## Requisição

Com o ***token*** em mãos, é possível instanciar tanto o cliente quanto o próprio Biofeature e utilizar o método ***call***, que recebe o argumento **`img`** (*string* obrigatório), que é o *path* até a imagem que se deseja submeter para predição, e, **opcionalmente**, o argumento *string* **`cpf`**, correspondente ao Cadastro de Pessoa Física, para identificação pessoal. Esse método se comunica com nosso modelo de inteligência artificial e retorna o resultado da predição como *dict* dentro de alguns segundos.

Um exemplo de código que realiza autenticação, instancia as classes necessárias e realiza uma chamada síncrona para obter a predição de uma imagem qualquer pode ser encontrado abaixo.

<script src="https://emgithub.com/embed.js?target=https://github.com/lablift/client-python/blob/main/examples/biofeature.py&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

O resultado mostrado em tela após a execução desse código contém o resultado da predição como um dicionário Python.

Você também pode **realizar requisições em lote** utilizando o método **`.multiple_calls()`**, que recebe como argumento uma lista de dicionários. Cada dicionário nesta lista representa uma única imagem, e precisa conter obrigatoriamente o atributo **`img`** (*path* até a imagem) e opcionalmente o atributo **`cpf`**. O código abaixo exemplifica o envio de imagens em lote.

<script src="https://emgithub.com/embed.js?target=https://github.com/lablift/client-python/blob/main/examples/biofeature_multiplecall.py&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Resultado

Uma resposta típica do BioFeature AI contém os seguintes campos:

* **`age`**: Idade aparente da pessoa na foto, em anos. Geralmente este valor é próximo à idade cronológica, porém fatores como envelhecimento precoce da pele podem produzir diferenças significativas.

* **`age_margin_error`**: Margem de erro da idade inferida.

* **`bmi`**: Índice de Massa Corporal inferido, em kg/m². 

* **`bmi_class`**: Classificação do Índice de Massa Corporal inferido para população ocidental, conforme tabela abaixo:

| Classe IMC  | Faixa de IMC (kg/m²) |
|-------------|----------------------|
| **`underweight`** | < 18.5               |
| **`normal`**      | 18.5 <= IMC < 25     |
| **`overweight`**  | 25 <= IMC < 30       |
| **`obese`**       | >= 30                 |

* **`cpf`**: O mesmo valor do campo **`cpf`**, caso tenha sido enviado, ou **`None`**. Este campo confirma a atribuição do documento à imagem. 

* **`ethnicity`**: Provável etnia da pessoa na foto. 

* **`ethnicity_probability`**: Probabilidade atribuída pelo modelo com relação à etnia inferida.

* **`face`**: String base64 contendo o rosto detectado na foto.

* **`gender`**: Gênero inferido. **`M`** para masculino e **`F`** para feminino.

* **`gender_probability`**: Probabilidade atribuída pelo modelo com relação ao gênero inferido.

* **`id`**: Código identificador da imagem na LabLift.

* **`prevalent_emotion`**: Emoção prevalente esboçada pelo rosto na foto. Esta informação deriva dos processos de validação da imagem.

* **`prevalent_emotion_probability`**: Probabilidade atribuída pelo modelo com relação à emoção inferida.

* **`responsible`**: *Username* que solicitou a avaliação da imagem.

* **`roll`**: Rolagem do rosto (uma das medidas de posicionamento avaliadas). Esta informação deriva dos processos de validação da imagem.

* **`submitted_image_name`**: Nome do arquivo da imagem salva no servidor da LabLift.

* **`skin_lesion_score`**: Score de Manchas Faciais. Quanto maior, pior. Veja o campo **`skin_lesion_score_interpretation`** para mais informações.

* **`skin_lesion_score_interpretation`**: Classificação de comprometimento da pele por manchas faciais, de acordo com o Score de Manchas Faciais. As classes são, em ordem crescente de comprometimento: **`low`**, **`medium-low`**, **`medium-high`**, **`high`**.

* **`time_taken`**: Tempo de processamento, em segundos. 

* **`wearing_eyeglasses`**: Indica se foi detectado o uso de óculos durante a coleta ou análise da foto de rosto.

* **`wearing_eyeglasses_probability`**: Probabilidade atribuída pelo modelo com relação ao uso de óculos.

* **`yaw`**: Guinada do rosto (uma das medidas de posicionamento avaliadas). Esta informação deriva dos processos de validação da imagem.

## Mensagens de erro

Quando o BioFeature AI retorna um **`status_code`** diferente de OK, o campo **`error`** da resposta frequentemente contém informações mais detalhadas sobre a causa do erro. Geralmente, as causas de erro estão relacionadas à validação da imagem. As imagens enviadas são validadas quanto à sua qualidade e o posicionamento da pessoa antes de serem analisadas pelos modelos. Esta validação busca garantir que as inferências pelos modelos ocorram no maior nível de confiabilidade possível. 

Os principais erros na etapa de validação são:

* **`unable to read file as image`**: O arquivo recebido não é suportado pela solução. Envie imagens JPEG ou PNG.

* **`unable to detect frontal face on image`**: Este erro indica que a solução não conseguiu localizar um rosto completo na imagem. Possíveis causas para isso incluem: não há um rosto na foto; a proporção entre o rosto da pessoa e o tamanho da foto é muito pequena; rosto parcialmente oculto; baixa qualidade da imagem.

* **`unacceptable pose`**: Este erro ocorre quando é detectada inclinação do rosto acima da tolerância da solução, ou quando a pessoa aparenta emoção prevalente não-neutra (ex: a pessoa está sorrindo).

* **`unable to apply model to image`**: Este erro indica que houve uma falha durante a etapa de aplicação dos modelos. Tente enviar a imagem novamente. Caso o erro persista entre em contato com nosso suporte e informe este erro.

* **`unable to process image`**: Este erro indica que houve uma falha inesperada durante o pré-processamento da imagem. Tente enviar a imagem novamente. Caso o erro persista entre em contato com nosso suporte e informe este erro.

> **Nota:** Imagens não aceitas na etapa de validação não são analisadas pelos modelos, por isso os campos gerados pelos modelos não estarão presentes.

---

## Api REST

O BiofeatureAI também pode ser utilizado a partir de uma API REST. Você pode acessar a documentação da API REST <a href="https://api.biofeature.lablift.com.br/docs/" target="_blank">clicando aqui</a>.