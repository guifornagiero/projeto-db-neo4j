# projeto-db-neo4j
Projeto criado para a disciplina de Tópicos Avançados de Banco de Dados - FEI 6 semestre

## Sobre
Este projeto cria e popula um banco de dados de uma universidade utilizando Neo4j. O banco de dados atua no modelo de grafos, e o arquivo executável traz os dados das seguintes queries: <br>
1. Histórico escolar dos alunos <br>
2. Histórico de disciplinas ministradas pelos professores <br>
3. Alunos formados <br>
4. Chefes de departamento <br>
5. Grupos de TCC e orientador

## Grupo
Gianluca Mariano Sobreiro - 22.122.011-4<br>
Guilherme Fornagiero de Carvalho - 22.122.016-3<br>
Paulo Vinícius Bessa de Brito - 22.122.005-6<br>
Pedro Augusto Bento Rocha - 22.122.028-8<br>

## Como rodar o projeto?
1. Instale o Docker <br>
2. Instale o interpretador do Python <br>
3. Instale o driver do Neo4j com o comando ```pip install neo4j``` <br>
4. Suba o container Docker com o comando ```docker-compose up -d``` <br>
5. Execute o arquivo main.py com o comando ```python main.py``` <br>

## Estrutura do projeto
- docker-compose.yml: arquivo de configuração dos containers Docker para o Neo4j
- main.py: arquivo de execução do projeto, onde é criada toda a estrutura do banco, onde é populado, e onde são selecionadas as queries
- data/: arquivo de volumes do Docker

## Problemas comuns
- Pode ser que, na primeira vez que o comando ```python main.py``` for executado, mostre uma mensagem de erro.
- Basta executar novamente, que o código funcionará de forma correta, trazendo os selects das queries.
