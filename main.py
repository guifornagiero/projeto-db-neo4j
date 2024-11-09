from neo4j import GraphDatabase

URI = "neo4j://localhost"
AUTH = ("neo4j", "faculdadefei")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    with driver.session(database="neo4j") as session:
        
        # Criando Departamentos e Professores
        departamentos = [
            {"id": 1, "nome": "Computação"},
            {"id": 2, "nome": "Medicina"},
            {"id": 3, "nome": "Humanas"}
        ]
        
        professores = [
            {"id": 1, "nome": "João da Silva"},
            {"id": 2, "nome": "Natália Almeida"},
            {"id": 3, "nome": "Carlos Ferreira"}
        ]

        # Criando Cursos
        cursos = [
            {"id": 1, "nome": "Ciência da Computação"},
            {"id": 2, "nome": "Oncologia"},
            {"id": 3, "nome": "Artes"}
        ]

        alunos = [
            {"id": 1, "nome": "Guilherme F.", "ra": "22.122.016-3"},
            {"id": 2, "nome": "Ana L.", "ra": "22.122.017-4"},
            {"id": 3, "nome": "Rafael S.", "ra": "22.122.020-7"},
            {"id": 4, "nome": "Juliana P.", "ra": "22.122.021-8"},
            {"id": 5, "nome": "Fernanda C.", "ra": "22.122.022-9"},
            {"id": 6, "nome": "Lucas M.", "ra": "22.122.023-0"},
        ]

        disciplinasComputacao = [
            { "id": 1, "codigo": "LPG", "nome": "Lógica de Programação", "semestre": 1 },
            { "id": 2, "codigo": "ESD", "nome": "Estruturas de Dados", "semestre": 2 },
            { "id": 3, "codigo": "ALG", "nome": "Algoritmos", "semestre": 3 },
            { "id": 4, "codigo": "ERQ", "nome": "Engenharia de Requisitos", "semestre": 4 },
            { "id": 5, "codigo": "ARS", "nome": "Arquitetura de Software", "semestre": 5 },
            { "id": 6, "codigo": "TSF", "nome": "Testes de Software", "semestre": 6 },
            { "id": 7, "codigo": "MAG", "nome": "Metodologias Ágeis", "semestre": 7 },
            { "id": 8, "codigo": "DWX", "nome": "Desenvolvimento Web", "semestre": 8 },
            { "id": 9, "codigo": "BDB", "nome": "Banco de Dados", "semestre": 9 },
            { "id": 10, "codigo": "GPJ", "nome": "Gerência de Projetos", "semestre": 10 }
        ]

        disciplinasMedicina = [
            { "id": 11, "codigo": "ANH", "nome": "Anatomia Humana", "semestre": 1 },
      { "id": 12, "codigo": "FIS", "nome": "Fisiologia", "semestre": 2 },
      { "id": 13, "codigo": "BQC", "nome": "Bioquímica", "semestre": 3 },
      { "id": 14, "codigo": "FAR", "nome": "Farmacologia", "semestre": 4 },
      { "id": 15, "codigo": "PAT", "nome": "Patologia", "semestre": 5 },
      { "id": 16, "codigo": "CLM", "nome": "Clínica Médica", "semestre": 6 },
      { "id": 17, "codigo": "CIR", "nome": "Cirurgia", "semestre": 7 },
      { "id": 18, "codigo": "PED", "nome": "Pediatria", "semestre": 8 },
      { "id": 19, "codigo": "GOB", "nome": "Ginecologia e Obstetrícia", "semestre": 9 },
      { "id": 20, "codigo": "SPB", "nome": "Saúde Pública", "semestre": 10 }
    ]
        
        disciplinasArtes = [
            {"id": 21, "codigo": "TCB", "nome": "Teoria das Cores", "semestre": 1 },
      { "id": 22, "codigo": "TIP", "nome": "Tipografia", "semestre": 2 },
      { "id": 23, "codigo": "DGD", "nome": "Design Digital", "semestre": 3 },
      { "id": 24, "codigo": "ILS", "nome": "Ilustração", "semestre": 4 },
      { "id": 25, "codigo": "FOT", "nome": "Fotografia", "semestre": 5 },
      { "id": 26, "codigo": "DIH", "nome": "Design de Interface", "semestre": 6 },
      { "id": 27, "codigo": "BRD", "nome": "Branding", "semestre": 7 },
      { "id": 28, "codigo": "ANI", "nome": "Animação", "semestre": 8 },
      { "id": 29, "codigo": "PFN", "nome": "Projeto Final", "semestre": 9 },
      { "id": 30, "codigo": "GPD", "nome": "Gestão de Projetos de Design", "semestre": 10 }
        ]

        # Inserindo Departamentos
        for dep in departamentos:
            session.run(
                """
                MERGE (:Departamento {id: $id, nome: $nome})
                """, dep
            )

        # Inserindo Professores
        for prof in professores:
            session.run(
                """
                MERGE (:Professor {id: $id, nome: $nome})
                """, prof
            )

        # Criando relacionamento PERTENCE_A entre Professores e Departamentos
        for dep, prof in zip(departamentos, professores):
            session.run(
                """
                MATCH (d:Departamento {id: $dep_id}), (p:Professor {id: $prof_id})
                MERGE (p)-[:PERTENCE_A]->(d)
                """, {"dep_id": dep["id"], "prof_id": prof["id"]}
            )

        # Criando relacionamento CHEFE_DE entre Professores e Departamentos
        for dep, prof in zip(departamentos, professores):
            session.run(
                """
                MATCH (d:Departamento {id: $dep_id}), (p:Professor {id: $prof_id})
                MERGE (p)-[:CHEFE_DE]->(d)
                """, {"dep_id": dep["id"], "prof_id": prof["id"]}
            )

        # Inserindo Cursos
        for curso in cursos:
            session.run(
                """
                MERGE (:Curso {id: $id, nome: $nome})
                """, curso
            )

        # Criando relacionamento PERTENCE_A entre Cursos e Departamentos
        for dep, curso in zip(departamentos, cursos):
            session.run(
                """
                MATCH (d:Departamento {id: $dep_id}), (c:Curso {id: $curso_id})
                MERGE (c)-[:PERTENCE_A]->(d)
                """, {"dep_id": dep["id"], "curso_id": curso["id"]}
            )

        for disciplina in disciplinasComputacao:
            session.run(
                """
                MERGE (:Disciplina {id: $id, nome: $nome, semestre: $semestre})
                """, disciplina
            )

        for disciplina in disciplinasMedicina:
            session.run(
                """
                MERGE (:Disciplina {id: $id, nome: $nome, semestre: $semestre})
                """, disciplina
            )
            session.run(
                """
                MERGE (:Disciplina {id: $id, nome: $nome, semestre: $semestre})
                """, disciplina
            )

        for disciplina in disciplinasArtes:
            session.run(
                """
                MERGE (:Disciplina {id: $id, nome: $nome, semestre: $semestre})
                """, disciplina
            )

        

        for disciplina in disciplinasComputacao:
            session.run(
                """
                MATCH (d:Curso {id: 1}), (c:Disciplina {id: $disciplina_id})
                MERGE (c)-[:PERTENCE_A]->(d)
                """, {"disciplina_id": disciplina["id"]}
            )
        for disciplina in disciplinasMedicina:
            session.run(
                """
                MATCH (d:Curso {id: 2}), (c:Disciplina {id: $disciplina_id})
                MERGE (c)-[:PERTENCE_A]->(d)
                """, {"disciplina_id": disciplina["id"]}
            )
        for disciplina in disciplinasArtes:
            session.run(
                """
                MATCH (d:Curso {id: 3}), (c:Disciplina {id: $disciplina_id})
                MERGE (c)-[:PERTENCE_A]->(d)
                """, {"disciplina_id": disciplina["id"]}
            )
        
        for aluno in alunos:
            session.run(
                """
                MERGE (:Aluno {id: $id, nome: $nome, ra: $ra})
                """, aluno
            )

        session.run(
            """
            MATCH (c:Curso {id: 1}), (a:Aluno {id: 1})
            MERGE (a)-[:MATRICULADO_EM]->(c)
            """
        )

        session.run(
            """
            MATCH (c:Curso {id: 1}), (a:Aluno {id: 3})
            MERGE (a)-[:MATRICULADO_EM]->(c)
            """
        )

        session.run(
            """
            MATCH (c:Curso {id: 2}), (a:Aluno {id: 2})
            MERGE (a)-[:MATRICULADO_EM]->(c)
            """
        )

        session.run(
            """
            MATCH (c:Curso {id: 2}), (a:Aluno {id: 4})
            MERGE (a)-[:MATRICULADO_EM]->(c)
            """
        )

        session.run(
            """
            MATCH (c:Curso {id: 3}), (a:Aluno {id: 5})
            MERGE (a)-[:MATRICULADO_EM]->(c)
            """
        )

        session.run(
            """
            MATCH (c:Curso {id: 3}), (a:Aluno {id: 6})
            MERGE (a)-[:MATRICULADO_EM]->(c)
            """
        )
