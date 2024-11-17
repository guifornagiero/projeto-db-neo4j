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

## Estrutura do projeto
- docker-compose.yml: arquivo de configuração dos containers Docker para o Neo4j
- main.py: arquivo de execução do projeto, onde é criada toda a estrutura do banco, onde é populado, e onde são selecionadas as queries
- data/: arquivo de volumes do Docker

## Descrição das coleções
Para criar as coleções foi usado como base o diagrama relacional, no qual as entidades são nós e as relações são arestas, rodando uma query em Neo4J, chegou-se na seguinte descrição:

### Rótulos
- Departamento
- Professor
- Curso
- Disciplina
- Aluno
- TCC

### Tipos de Relacionamento
- PERTENCE_A
- CHEFE_DE
- TEM_DISCIPLINA
- PROFESSOR_DE
- MATRICULADO_EM
- CURSOU
- ORIENTADO_POR
- REALIZA

### Property Keys
- nome
- id
- semestre
- ano
- ra
- nota

### Node Type Properties
- :Professor.nome
- :Professor.id
- :Curso.nome
- :Curso.id
- :Disciplina.nome
- :Disciplina.id
- :Disciplina.semestre
- :Aluno.nome
- :Aluno.id
- :Aluno.ra
- :TCC.nome
- :TCC.id
- :Departamento.nome
- :Departamento.id

### Relation Type Properties
- :PROFESSOR_DE.semestre
- :PROFESSOR_DE.ano
- :CURSOU.semestre
- :CURSOU.ano
- :CURSOU.nota

## Como rodar o projeto?
1. Clone o projeto com o seguinte comando ```git clone https://github.com/guifornagiero/projeto-db-neo4j.git``` <br>
2. Entre na pasta do projeto com o comando ```cd projeto-db-neo4j```
3. Instale o Docker <br>
4. Instale o interpretador do Python <br>
5. Instale o driver do Neo4j e do Pandas com o comando ```pip install neo4j && pip install pandas``` <br>
6. Suba o container Docker com o comando ```docker-compose up -d``` <br>
7. Execute o arquivo main.py com o comando ```python main.py``` <br>

## Problemas comuns
- Pode ser que, na primeira vez que o comando ```python main.py``` for executado, mostre uma mensagem de erro.
- Basta executar novamente, que o código funcionará de forma correta, trazendo os selects das queries.
