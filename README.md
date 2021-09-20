# nlp-demo-sentiment

## Como implementar

### Pré-requisitos:
- Tenha um email cadastrado no facebook e uma página pública que exista há pelo menos 1 hora
- Tenha uma conta no OCI

### Passo 1: Facebook e configurações

Entre no link `https://developers.facebook.com/?locale=pt_BR`. Você deve observar uma página assim:

![alt text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-16%2012-04-34.png)

Clique em Primeiros Passos. Você será redirecionado para essa página:

![alt text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-16%2012-05-48.png)
Concorde com os termos e clique em "Continuar". 

Nessa página, digite seu número de telefone e clique em "Enviar SMS para verificação"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-16%2012-05-53.png)

Insira o código que chegou por SMS no seu celular e clique em "Continuar"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-16%2012-06-03.png)

Clique em "Confirmar email"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-16%2012-11-06.png)

Selecione "Desenvolvedor" e clique em "Registro concluído"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-16%2012-11-10.png)

Clique em "Criar aplicativo"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-29-11.png)

Selecione "Empresa"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-29-17.png)

Dê um nome ao seu app, selecione "Sua empresa ou você" em Finalidade do aplicativo e clique em "Criar aplicativo"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-29-32.png)

Vá em Ferramentas > Explorador de Graph API
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-33-07.png)

Clique em Obter token > Obter token de acesso da Página
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-33-16.png)

Clique em "Continuar como <nome do seu usuário>"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-33-21.png)

Selecione a página que deseja usar e clique em "Avançar"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-33-25.png)

Habilite as duas opções e clique em "Concluir"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-33-28.png)

Clique em "OK"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-33-35.png)

Clique em "Copy token"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-38-08.png)

Clique em "2 opções selecionadas" e selecione todos os acessos que você deseja dar ao aplicativo
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-41-02.png)

Clique em "Token de usuário" > "<nome da sua página>" e clique em gerar "Copy token"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-38-08.png)

Vá em Ferramentas > Depurador de token de acesso
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-38-18.png)

Cole o token que você copiou e clique em "Depurar"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-38-24.png)

Clique em "Estender token de acesso". Isso fará com que o token de acesso fique válido por 3 meses. A cada 3 meses será necessário refazer esse processo para gerar um novo token substituir no código.
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-38-29.png)

Copie esse token de acesso e guarde!!
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-38-38.png)

Entre na sua página do Facebook e copie o id que está no URL. Guarde esse id!!
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-17%2015-48-18.png)

### Passo 2: OCI 

Primeiro, entre no link https://cloud.oracle.com e esteja logado
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-23-19.png)

Clique no ícone de menu > Identity and Security > Compartments
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-23-34.png)

Clique em "Create Compartment"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-23-43.png)

Preencha o nome do compartment (recomendamos: "nlp-demo"), a descrição e o Parent Compartment (neste caso deixamos dentro do root). Depois clique em "Create Compartment"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-24-08.png)

Clique em "Groups" no canto esquerdo
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-24-44.png)

Clique em "Create Group"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-26-52.png)

Chame o grupo de "RepoAccess" e adicione uma descrição
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-27-20.png)

Clique em "Add User to Group" e adicione o seu email ao grupo
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-27-26.png)

Clique no ícone de menu > Developer Services > Kubernetes Clusters (OKE)
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-28-44.png)

Selecione o compartimento que você criou para esse projeto 
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-29-05.png)

Clique em "Create Cluster"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-29-10.png)

Seleciona "Quick Create" e clique em "Launch Workflow"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-29-13.png)

Dê um nome ao seu cluster, escolha o shape desejado e clique em "Next"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-29-25.png)

Clique em "Create Cluster"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-29-35.png)

Clique em "Container Registry" no canto esquerdo e clique em "Create Repository".
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-30-10.png)

Crie 4 repositórios (públicos):
- facebook-job
- nlp-translation
- stream-trigger-job
- predict-sentiment
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-30-35.png)

Clique no ícone de menu > Oracle Database > Autonomous Transaction Processing
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-31-00.png)

Certifique-se que está no compartimento correto e clique em "Create Autonomous Database"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-31-09.png)

Preencha o "Display Name" e "Database Name". Selecione "Transaction Processing" e "Shared Infrastructure"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-31-20.png)

Nessa demo, nós habilitamos o "Always Free". Crie uma senha forte.
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-31-27.png)

Selecione "Allow secure access from everywhere" e "License Included". Clique em "Create Autonomous Database"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-31-30.png)

Clique no ícone de menu > Analytics & AI > Streaming
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-32-52.png)

Certifique-se que está no compartimento correto e clique em "Create Stream"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-33-03.png)

Configure como está na imagem
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2021-33-26.png)

### Passo 3: Alterando um pouco do repositorio para adicionar suas credenciais

Rode o comando em seu terminal:

`git clone https://github.com/Anatamais-oracle/nlp-demo-sentiment`

Clique no ícone de Profile no canto superior direito > User Settings
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-02-31.png)

Clique em "API Keys"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-02-44.png)

Clique em "Add API Key"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-02-54.png)

Selecione "Generate API Key Pair" e clique em "Download Private Key"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-02-58.png)
Salve esse arquivo dentro de `nlp-demo-sentiment/facebook-job/.oci`, `nlp-demo-sentiment/predict-sentiment-api/.oci` e `nlp-demo-sentiment/stream-trigger-job/.oci` com o nome `oracleidentitycloudservice.pem`
Clique em "Add"

Clique em "Copy", e crie um arquivo config em todas as pastas .oci dentro do repositório. Cole o que você copiou nos arquivos `config` e substitua `<path to your private keyfile> #TODO` por `.oci/oracleidentitycloudservice.pem`

Clique em "Close"

Clique em "Auth Tokens" > Generate Token
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-28-54.png)

Adicione uma descrição e clique em "Generate Token"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-29-10.png)

Clique em "Copy" e guarde esse token muito bem!!
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-29-16.png)

Clique no ícone de menu > Analytics & AI > Streaming > nome do seu serviço de streaming
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-05-23.png)

Abra o arquivo `nlp-demo-sentiment/facebook-job/.env` e substitua:
- `ACCESS_TOKEN_FB`: por aquele token que guardamos no Passo 1 deste tutorial
- `PAGE_ID`: pelo id da página do Facebook que guardamos no Passo 1 deste tutorial
- `OCI_MESSAGE_ENDPOINT`: pelo `Messages Endpoint`, mostrado como exemplo na imagem
- `OCI_STREAM_OCID`: pelo `OCID`, mostrado como exemplo na imagem
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-05-36.png)

Clique no ícone de menu > Oracle Database > Autonomous Transaction Processing
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-31-55.png)

Clique no banco de dados que será usado neste projeto, que você criou no Passo 2
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-32-04.png)

Clique em "Service Console"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-32-10.png)

Clique em "Desenvolvimento" ao lado esquerdo
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-32-18.png)

Clique em "Oracle APEX"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-32-20.png)

Faça o login no Oracle APEX com o workspace, username e password
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-32-36.png)

Clique em "SQL Workshop"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-32-43.png)

Clique em "Table" no menu direito (dentro do escopo "Create Object")
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-33-22.png)

Dê o nome "FACEBOOK_COMMENTS" à table, e insira as colunas como na imagem:
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-36-54.png)

Selecione "No Primary Key" e clique "Next" > clique "Next" > clique "Next" > clique em "Create Table"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-37-46.png)

Volte ao "SQL Workshop" e clique em "RESTful Services"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-52-06.png)

Clique em "Modules" e "Create Module"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-53-09.png)

Dê um nome ao módulo e coloque o base path (no meu caso, /NLPDB/). Clique em "Create Module"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-53-52.png)

Clique no seu módulo no canto esquerdo e clique em "Create Template"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-58-08.png)

Crie 2 templates com os seguintes nomes (preencher no campo `URI Template`):
- `INSERTCOMMENTS`
- `CHECKIFEXIST`
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-58-18.png)

Clique no template `INSERTCOMMENTS`
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-59-03.png)

Clique em "Create Handler"
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2022-59-09.png)

Selecione o método "POST" e insira isso como source:
```
INSERT INTO NLPDB.FACEBOOK_COMMENTS (
    ID_,
    POST_ID,
    MESSAGE,
    CREATED_TIME,
    UPDATED_TIME,
    TEXT_ELEMENT_EN,
    TEXT_ELEMENT_PT,
    SENTIMENT
) VALUES (
    :ID_,
    :POST_ID,
    :MESSAGE,
    :CREATED_TIME,
    :UPDATED_TIME,
    :TEXT_ELEMENT_EN,
    :TEXT_ELEMENT_PT,
    :SENTIMENT
)
```
E salve este handler
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-03-38.png)

Agora selecione o template `CHECKIFEXIST`, clique em "Create Handler".
Selecione o método "GET", `Source Type` "Collection Query Item" e insira isso como source:
```
SELECT COUNT(*) AS count_ FROM NLPDB.FACEBOOK_COMMENTS WHERE ID_ = :ID_
```
E salve este handler
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-07-04.png)

Abra o arquivo `nlp-demo-sentiment/predict-sentiment-api/.env` e substitua:
- `ACCESS_TOKEN`: por um ACCESS_TOKEN aleatório que você deve criar (só usar gerados aleatório de senha na internet - eu recomendo: https://passwordsgenerator.net/)
- `ADB_URL_CHECKIFEXIST`: pela URL do handler que chamamos do template `CHECKIFEXIST` (campo `FULL URL`, que está selecionado na imagem)
![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-09-54.png)
- `AUTH_TOKEN_TRANSLATIONAPI`: por um outro ACCESS_TOKEN aleatório que você deve criar
- `ADB_URL_INSERTCOMMENTS`: pela URL do handler que chamamos do template `INSERTCOMMENTS` (campo `FULL URL`)

Abra o arquivo `nlp-demo-sentiment/stream-trigger-job/.env` e substitua:
- `OCI_MESSAGE_ENDPOINT`: igual ao `OCI_MESSAGE_ENDPOINT` do `nlp-demo-sentiment/facebook-job/.env`
- `OCI_STREAM_OCID`: igual ao `OCI_STREAM_OCID` do `nlp-demo-sentiment/facebook-job/.env`
- `AUTH_TOKEN_PREDICTSENTIMENT`: igual ao `ACCESS_TOKEN` do `nlp-demo-sentiment/predict-sentiment-api/.env`

Abra o arquivo `nlp-demo-sentiment/translation-api/.env` e substitua:
- `ACCESS_TOKEN`: igual ao `AUTH_TOKEN_TRANSLATIONAPI` do `nlp-demo-sentiment/predict-sentiment-api/.env`

Substitua nos arquivos `image-to-registry.sh` (dentro das pastas `facebook-job`, `predict-sentiment-api`, `stream-trigger-job`, `translation-api`):
- `<Object Storage Namespace>`: 
  - clique no ícone de menu > Governance & Administration > Tenancy Details
    ![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-19-10.png)
  - Substitua `<Object Storage Namespace>` pelo ítem que está selecionado na imagem
    ![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-19-24.png)
- `<user>`: pelo o email da sua conta no OCI
- `<Auth Token>`: pelo Auth Token que guardamos no início do Passo 3
- `<region>`: pelo id da região que está utilizando (no caso desta demo, selecionei sa-saopaulo-1)
    
Substitua nos arquivos `run-on-k8s.sh` (dentro das pastas `facebook-job`, `predict-sentiment-api`, `stream-trigger-job`, `translation-api`):
- `<access cluster>`:
  - Clique no ícone de menu > Developer Services > Kubernetes Clusters (OKE)
    ![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-28-29.png)
  - Clique no cluster que você vai usar para esse projeto
    ![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-28-41.png)
  - Clique em "Access Cluster"
    ![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-28-47.png)
  - Clique em "Copy"
    ![alt_text](https://github.com/Anatamais-oracle/nlp-demo-sentiment/blob/master/images/Screenshot%20from%202021-09-19%2023-28-51.png)
  Substitua o `<access cluster>` pelo que você acabou de copiar
- `<region>`: pelo id da região que está utilizando (no caso desta demo, selecionei sa-saopaulo-1)
- `<Object Storage Namespace>`: igual ao `<Object Storage Namespace>` do arquivo `image-to-registry.sh`
- `<user>`: pelo o email da sua conta no OCI
- `<Auth Token>`: pelo Auth Token que guardamos no início do Passo 3

Substitua nos arquivos `k8s-deployment.yaml` (dentro das pastas `facebook-job`, `predict-sentiment-api`, `stream-trigger-job`, `translation-api`):
- `<region>`: pelo id da região que está utilizando (no caso desta demo, selecionei sa-saopaulo-1)
- `<Object Storage Namespace>`: igual ao `<Object Storage Namespace>` do arquivo `image-to-registry.sh`
- `<SUBNET_LB_OCID>`: OCID da subnet privada da VCN do seu cluster de Kubernetes
