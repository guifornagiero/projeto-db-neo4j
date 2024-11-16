from neo4j import GraphDatabase
import pandas as pd

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

        historico_aluno_1 = [
    {
        "id": 1,
        "disciplina": "Lógica de Programação",
        "codigo": "LPG",
        "semestre": 1,
        "ano": 2020,
        "nota": 9.0
    },
    {
        "id": 2,
        "disciplina": "Estruturas de Dados",
        "codigo": "ESD",
        "semestre": 2,
        "ano": 2020,
        "nota": 8.5
    },
    {
        "id": 3,
        "disciplina": "Algoritmos",
        "codigo": "ALG",
        "semestre": 3,
        "ano": 2021,
        "nota": 9.2
    },
    {
        "id": 4,
        "disciplina": "Engenharia de Requisitos",
        "codigo": "ERQ",
        "semestre": 4,
        "ano": 2021,
        "nota": 8.0
    },
    {
        "id": 5,
        "disciplina": "Arquitetura de Software",
        "codigo": "ARS",
        "semestre": 5,
        "ano": 2022,
        "nota": 9.3
    },
    {
        "id": 6,
        "disciplina": "Testes de Software",
        "codigo": "TSF",
        "semestre": 6,
        "ano": 2022,
        "nota": 8.0
    },
    {
        "id": 7,
        "disciplina": "Metodologias Ágeis",
        "codigo": "MAG",
        "semestre": 7,
        "ano": 2023,
        "nota": 9.0
    },
    {
        "id": 8,
        "disciplina": "Desenvolvimento Web",
        "codigo": "DWX",
        "semestre": 8,
        "ano": 2023,
        "nota": 9.5
    },
    {
        "id": 9,
        "disciplina": "Banco de Dados",
        "codigo": "BDB",
        "semestre": 9,
        "ano": 2024,
        "nota": 5.9
    },
    {
        "id": 10,
        "disciplina": "Gerência de Projetos",
        "codigo": "GPJ",
        "semestre": 10,
        "ano": 2024,
        "nota": 6.0
    }
]
        
        historico_aluno_2 = [
            {
                "id": 11,
        "disciplina": "Anatomia Humana",
        "codigo": "ANH",
        "semestre": 1,
        "ano": 2020,
        "nota": 9.0
      },
      {
        "id": 12,
        "disciplina": "Fisiologia",
        "codigo": "FIS",
        "semestre": 2,
        "ano": 2020,
        "nota": 8.5
      },
      {
        "id": 13,
        "disciplina": "Bioquímica",
        "codigo": "BQC",
        "semestre": 3,
        "ano": 2021,
        "nota": 9.2
      },
      {
        "id": 14,
        "disciplina": "Farmacologia",
        "codigo": "FAR",
        "semestre": 4,
        "ano": 2021,
        "nota": 9.0
      },
      {
        "id": 15,
        "disciplina": "Patologia",
        "codigo": "PAT",
        "semestre": 5,
        "ano": 2022,
        "nota": 8.7
      },
      {
        "id": 16,
        "disciplina": "Clínica Médica",
        "codigo": "CLM",
        "semestre": 6,
        "ano": 2022,
        "nota": 8.5
      },
      {
        "id": 17,
        "disciplina": "Cirurgia",
        "codigo": "CIR",
        "semestre": 7,
        "ano": 2023,
        "nota": 9.1
      },
      {
        "id": 18,
        "disciplina": "Pediatria",
        "codigo": "PED",
        "semestre": 8,
        "ano": 2023,
        "nota": 9.2
      },
      {
        "id": 19,
        "disciplina": "Ginecologia e Obstetrícia",
        "codigo": "GOB",
        "semestre": 9,
        "ano": 2024,
        "nota": 8.9
      },
      {
        "id": 20,
        "disciplina": "Saúde Pública",
        "codigo": "SPB",
        "semestre": 10,
        "ano": 2024,
        "nota": 9.4
      }
    ]
        
        historico_aluno_3 = [
      {
          "id": 1,
        "disciplina": "Lógica de Programação",
        "codigo": "LPG",
        "semestre": 1,
        "ano": 2020,
        "nota": 9.0
      },
      {
        "id": 2,
        "disciplina": "Estruturas de Dados",
        "codigo": "ESD",
        "semestre": 2,
        "ano": 2020,
        "nota": 8.5
      },
      {
        "id": 3,
        "disciplina": "Algoritmos",
        "codigo": "ALG",
        "semestre": 3,
        "ano": 2021,
        "nota": 9.2
      },
      {
        "id": 4,
        "disciplina": "Engenharia de Requisitos",
        "codigo": "ERQ",
        "semestre": 4,
        "ano": 2021,
        "nota": 8.0
      },
      {
        "id": 5,
        "disciplina": "Arquitetura de Software",
        "codigo": "ARS",
        "semestre": 5,
        "ano": 2022,
        "nota": 9.3
      },
      {
        "id": 6,
        "disciplina": "Testes de Software",
        "codigo": "TSF",
        "semestre": 6,
        "ano": 2022,
        "nota": 8.0
      },
      {
        "id": 7,
        "disciplina": "Metodologias Ágeis",
        "codigo": "MAG",
        "semestre": 7,
        "ano": 2023,
        "nota": 9.0
      },
      {
        "id": 8,
        "disciplina": "Desenvolvimento Web",
        "codigo": "DWX",
        "semestre": 8,
        "ano": 2023,
        "nota": 9.5
      },
      {
        "id": 9,
        "disciplina": "Banco de Dados",
        "codigo": "BDB",
        "semestre": 9,
        "ano": 2024,
        "nota": 9.1
      },
      {
        "id": 10,
        "disciplina": "Gerência de Projetos",
        "codigo": "GPJ",
        "semestre": 10,
        "ano": 2024,
        "nota": 9.4
      }
    ]
        
        historico_aluno_4 = [
      {
          "id": 11,
        "disciplina": "Anatomia Humana",
        "codigo": "ANH",
        "semestre": 1,
        "ano": 2020,
        "nota": 9.1
      },
      {
        "id": 12,
        "disciplina": "Fisiologia",
        "codigo": "FIS",
        "semestre": 2,
        "ano": 2020,
        "nota": 8.8
      },
      {
        "id": 13,
        "disciplina": "Bioquímica",
        "codigo": "BQC",
        "semestre": 3,
        "ano": 2021,
        "nota": 9.3
      },
      {
        "id": 14,
        "disciplina": "Farmacologia",
        "codigo": "FAR",
        "semestre": 4,
        "ano": 2021,
        "nota": 9.0
      },
      {
        "id": 15,
        "disciplina": "Patologia",
        "codigo": "PAT",
        "semestre": 5,
        "ano": 2022,
        "nota": 8.5
      },
      {
        "id": 16,
        "disciplina": "Clínica Médica",
        "codigo": "CLM",
        "semestre": 6,
        "ano": 2022,
        "nota": 9.2
      },
      {
        "id": 17,
        "disciplina": "Cirurgia",
        "codigo": "CIR",
        "semestre": 7,
        "ano": 2023,
        "nota": 9.4
      },
      {
        "id": 18,
        "disciplina": "Pediatria",
        "codigo": "PED",
        "semestre": 8,
        "ano": 2023,
        "nota": 9.1
      },
      {
        "id": 19,
        "disciplina": "Ginecologia e Obstetrícia",
        "codigo": "GOB",
        "semestre": 9,
        "ano": 2024,
        "nota": 9.0
      },
      {
        "id": 20,
        "disciplina": "Saúde Pública",
        "codigo": "SPB",
        "semestre": 10,
        "ano": 2024,
        "nota": 9.5
      }
    ]
        
        historico_aluno_5 = [
      {
        "id": 21,
        "disciplina": "Teoria das Cores",
        "codigo": "TCB",
        "semestre": 1,
        "ano": 2020,
        "nota": 2.4
      },
      {
        "id": 22,
        "disciplina": "Tipografia",
        "codigo": "TIP",
        "semestre": 2,
        "ano": 2020,
        "nota": 8.5
      },
      {
        "id": 23,
        "disciplina": "Design Digital",
        "codigo": "DGD",
        "semestre": 3,
        "ano": 2021,
        "nota": 9.2
      },
      {
        "id": 24,
        "disciplina": "Ilustração",
        "codigo": "ILS",
        "semestre": 4,
        "ano": 2021,
        "nota": 8.8
      },
      {
        "id": 25,
        "disciplina": "Fotografia",
        "codigo": "FOT",
        "semestre": 5,
        "ano": 2022,
        "nota": 9.1
      },
      {
        "id": 26,
        "disciplina": "Design de Interface",
        "codigo": "DIH",
        "semestre": 6,
        "ano": 2022,
        "nota": 9.3
      },
      {
        "id": 27,
        "disciplina": "Branding",
        "codigo": "BRD",
        "semestre": 7,
        "ano": 2023,
        "nota": 8.9
      },
      {
        "id": 28,
        "disciplina": "Animação",
        "codigo": "ANI",
        "semestre": 8,
        "ano": 2023,
        "nota": 9.4
      },
      {
        "id": 29,
        "disciplina": "Projeto Final",
        "codigo": "PFN",
        "semestre": 9,
        "ano": 2024,
        "nota": 9.5
      },
      {
        "id": 30,
        "disciplina": "Gestão de Projetos de Design",
        "codigo": "GPD",
        "semestre": 10,
        "ano": 2024,
        "nota": 9.2
      }
    ]
        historico_aluno_6 = [
      {
        "id": 21,
        "disciplina": "Teoria das Cores",
        "codigo": "TCB",
        "semestre": 1,
        "ano": 2020,
        "nota": 8.0
      },
      {
        "id": 22,
        "disciplina": "Tipografia",
        "codigo": "TIP",
        "semestre": 2,
        "ano": 2020,
        "nota": 9.3
      },
      {
        "id": 23,
        "disciplina": "Design Digital",
        "codigo": "DGD",
        "semestre": 3,
        "ano": 2021,
        "nota": 8.5
      },
      {
        "id": 24,
        "disciplina": "Ilustração",
        "codigo": "ILS",
        "semestre": 4,
        "ano": 2021,
        "nota": 9.0
      },
      {
        "id": 25,
        "disciplina": "Fotografia",
        "codigo": "FOT",
        "semestre": 5,
        "ano": 2022,
        "nota": 8.7
      },
      {
        "id": 26,
        "disciplina": "Design de Interface",
        "codigo": "DIH",
        "semestre": 6,
        "ano": 2022,
        "nota": 3.2
      },
      {
        "id": 27,
        "disciplina": "Branding",
        "codigo": "BRD",
        "semestre": 7,
        "ano": 2023,
        "nota": 8.4
      },
      {
        "id": 28,
        "disciplina": "Animação",
        "codigo": "ANI",
        "semestre": 8,
        "ano": 2023,
        "nota": 9.2
      },
      {
        "id": 29,
        "disciplina": "Projeto Final",
        "codigo": "PFN",
        "semestre": 9,
        "ano": 2024,
        "nota": 9.0
      },
      {
        "id": 30,
        "disciplina": "Gestão de Projetos de Design",
        "codigo": "GPD",
        "semestre": 10,
        "ano": 2024,
        "nota": 4.6
      }
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

        disciplinasProfessor1 = [
            {"pid": 1, "disciplinaid": 1,"nome": "Lógica de Programação", "codigo": "LPG", "semestre": 1, "ano": 2020},
            {"pid": 1, "disciplinaid": 2, "nome": "Estruturas de Dados", "codigo": "ESD", "semestre": 2, "ano": 2020},
            {"pid": 1, "disciplinaid": 1, "nome": "Lógica de Programação", "codigo": "LPG", "semestre": 1, "ano": 2021},
            {"pid": 1, "disciplinaid": 1, "nome": "Lógica de Programação", "codigo": "LPG", "semestre": 1, "ano": 2022},
            {"pid": 1, "disciplinaid": 6, "nome": "Testes de Software", "codigo": "TSF", "semestre": 6, "ano": 2022},
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
        
        disciplinasProfessor2 = [
            {"pid": 2, "disciplinaid": 13, "nome": "Bioquímica", "codigo": "BQC", "semestre": 3, "ano": 2021},
            {"pid": 2, "disciplinaid": 16, "nome": "Clínica Médica", "codigo": "CLM", "semestre": 6, "ano": 2022},
            {"pid": 2, "disciplinaid": 19, "nome": "Ginecologia e Obstetrícia", "codigo": "GOB", "semestre": 9, "ano": 2024},
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

        disciplinasProfessor3 = [
            {"pid": 3, "disciplinaid": 21, "nome": "Teoria das Cores", "codigo": "TCB", "semestre": 1, "ano": 2020},
            {"pid": 3, "disciplinaid": 30, "nome": "Gestão de Projetos de Design", "codigo": "GPD", "semestre": 10, "ano": 2024},
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
                MATCH (d:Departamento {id: 1}), (c:Disciplina {id: $disciplina_id}), (curso: Curso {id: 1})
                MERGE (c)-[:PERTENCE_A]->(d)
                MERGE (curso)-[:TEM_DISCIPLINA]->(c);
                """, {"disciplina_id": disciplina["id"]}
            )
        
        for relacao in disciplinasProfessor1:
            session.run(
            """
            MATCH (p:Professor {id: $professor_id}), (d:Disciplina {id: $disciplina_id})
            MERGE (p)-[r:PROFESSOR_DE {semestre: $semestre, ano: $ano}]->(d)
            RETURN r
            """,
            {
                "professor_id": relacao["pid"],
                "disciplina_id": relacao["disciplinaid"],
                "semestre": relacao["semestre"],
                "ano": relacao["ano"]
            }
            )


        for disciplina in disciplinasMedicina:
            session.run(
                """
                MATCH (d:Departamento {id: 2}), (c:Disciplina {id: $disciplina_id}), (curso: Curso {id: 2})
                MERGE (c)-[:PERTENCE_A]->(d)
                MERGE (curso)-[:TEM_DISCIPLINA]->(c);
                """, {"disciplina_id": disciplina["id"]}
            )

        for relacao in disciplinasProfessor2:
             session.run(
            """
            MATCH (p:Professor {id: $professor_id}), (d:Disciplina {id: $disciplina_id})
            MERGE (p)-[r:PROFESSOR_DE {semestre: $semestre, ano: $ano}]->(d)
            RETURN r
            """,
            {
                "professor_id": relacao["pid"],
                "disciplina_id": relacao["disciplinaid"],
                "semestre": relacao["semestre"],
                "ano": relacao["ano"]
            }
            )
             
        for disciplina in disciplinasArtes:
            session.run(
                """
                MATCH (d:Departamento {id: 3}), (c:Disciplina {id: $disciplina_id}), (curso: Curso {id: 3})
                MERGE (c)-[:PERTENCE_A]->(d)
                MERGE (curso)-[:TEM_DISCIPLINA]->(c);
                """, {"disciplina_id": disciplina["id"]}
            )
            
        for relacao in disciplinasProfessor3:
             session.run(
            """
            MATCH (p:Professor {id: $professor_id}), (d:Disciplina {id: $disciplina_id})
            MERGE (p)-[r:PROFESSOR_DE {semestre: $semestre, ano: $ano}]->(d)
            RETURN r
            """,
            {
                "professor_id": relacao["pid"],
                "disciplina_id": relacao["disciplinaid"],
                "semestre": relacao["semestre"],
                "ano": relacao["ano"]
            }
            )

        # Inserindo Alunos
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

        for relacao in historico_aluno_1:
            session.run(
                """
                MATCH (a:Aluno {id: 1}), (d:Disciplina {id: $id})
                MERGE (a)-[:CURSOU {semestre: $semestre, ano: $ano, nota: $nota}]->(d)
                """, {
                    "id": relacao["id"],
                    "semestre": relacao["semestre"],
                    "ano": relacao["ano"],
                    "nota": relacao["nota"]
                }
            )
        
        for relacao in historico_aluno_2:
            session.run(
                """
                MATCH (a:Aluno {id: 2}), (d:Disciplina {id: $id})
                MERGE (a)-[:CURSOU {semestre: $semestre, ano: $ano, nota: $nota}]->(d)
                """, {
                    "id": relacao["id"],
                    "semestre": relacao["semestre"],
                    "ano": relacao["ano"],
                    "nota": relacao["nota"]
                }
            )
        
        for relacao in historico_aluno_3:
            session.run(
                """
                MATCH (a:Aluno {id: 3}), (d:Disciplina {id: $id})
                MERGE (a)-[:CURSOU {semestre: $semestre, ano: $ano, nota: $nota}]->(d)
                """, {
                    "id": relacao["id"],
                    "semestre": relacao["semestre"],
                    "ano": relacao["ano"],
                    "nota": relacao["nota"]
                }
            )
        
        for relacao in historico_aluno_4:
            session.run(
                """
                MATCH (a:Aluno {id: 4}), (d:Disciplina {id: $id})
                MERGE (a)-[:CURSOU {semestre: $semestre, ano: $ano, nota: $nota}]->(d)
                """, {
                    "id": relacao["id"],
                    "semestre": relacao["semestre"],
                    "ano": relacao["ano"],
                    "nota": relacao["nota"]
                }
            )
        
        for relacao in historico_aluno_5:
            session.run(
                """
                MATCH (a:Aluno {id: 5}), (d:Disciplina {id: $id})
                MERGE (a)-[:CURSOU {semestre: $semestre, ano: $ano, nota: $nota}]->(d)
                """, {
                    "id": relacao["id"],
                    "semestre": relacao["semestre"],
                    "ano": relacao["ano"],
                    "nota": relacao["nota"]
                }
            )
        
        for relacao in historico_aluno_6:
            session.run(
                """
                MATCH (a:Aluno {id: 6}), (d:Disciplina {id: $id})
                MERGE (a)-[:CURSOU {semestre: $semestre, ano: $ano, nota: $nota}]->(d)
                """, {
                    "id": relacao["id"],
                    "semestre": relacao["semestre"],
                    "ano": relacao["ano"],
                    "nota": relacao["nota"]
                }
            )
        
        session.run(
            """
            MERGE (:TCC {id: 101, nome: 'Estudo de caso: Aplicação de Finanças'});
            """
        )
        
        session.run(
            """
            MATCH (p:Professor {id: 1}), (t:TCC {id: 101})
            MERGE (t)-[:ORIENTADO_POR]->(p);
            """
        )

        session.run(
            """
            MERGE (:TCC {id: 102, nome: 'Impacto da Nutrição na Saúde'});
            """
        )

        session.run(
            """
            MATCH (p:Professor {id: 2}), (t:TCC {id: 102})
            MERGE (t)-[:ORIENTADO_POR]->(p);
            """
        )


        session.run(
            """
            MERGE (:TCC {id: 105, nome: 'Desenvolvimento de Campanha Publicitária'});
            """
        )

        session.run(
            """
            MATCH (p:Professor {id: 3}), (t:TCC {id: 105})
            MERGE (t)-[:ORIENTADO_POR]->(p);
            """
        )

        session.run(
            """
            MERGE (:TCC {id: 106, nome: 'Impacto do Design na Comunicação Visual'});
            """
        )

        session.run(
            """
            MATCH (p:Professor {id: 3}), (t:TCC {id: 106})
            MERGE (t)-[:ORIENTADO_POR]->(p);
            """
        )

        session.run(
            """
            MATCH (a:Aluno {id: 1}), (t:TCC {id: 101})
            MERGE (a)-[:REALIZA]->(t);
            """
        )

        session.run(
            """
            MATCH (a:Aluno {id: 2}), (t:TCC {id: 102})
            MERGE (a)-[:REALIZA]->(t);
            """
        )

        session.run(
            """
            MATCH (a:Aluno {id: 3}), (t:TCC {id: 101})
            MERGE (a)-[:REALIZA]->(t);
            """
        )

        session.run(
            """
            MATCH (a:Aluno {id: 4}), (t:TCC {id: 102})
            MERGE (a)-[:REALIZA]->(t);
            """
        )

        session.run(
            """
            MATCH (a:Aluno {id: 5}), (t:TCC {id: 105})
            MERGE (a)-[:REALIZA]->(t);
            """
        )

        session.run(
            """
            MATCH (a:Aluno {id: 6}), (t:TCC {id: 106})
            MERGE (a)-[:REALIZA]->(t);
            """
        )

        print("Query 1: Histórico escolar de qualquer aluno")

        result = session.run(
    """
    MATCH (a:Aluno)-[r:CURSOU]->(d:Disciplina)
    RETURN a.nome AS aluno, d.id AS id, d.nome AS nomeDisciplina, 
           r.semestre AS semestre, 
           r.ano AS ano, 
           r.nota AS notaFinal
    ORDER BY a.nome, d.id;
    """
)

        
        df = pd.DataFrame(result, columns=["aluno", "id", "disciplina", "semestre", "ano", "nota"])
        print(df)

        print("\nQuery 2: Histórico de disciplinas ministradas por qualquer professor")

        result = session.run(
            """
            MATCH (p:Professor)-[r:PROFESSOR_DE]->(d:Disciplina)
                RETURN p.nome, d.nome AS disciplina, r.semestre AS semestre, r.ano AS ano
            ORDER BY p.nome, r.ano, r.semestre
            """
        )

        df = pd.DataFrame(result, columns=["professor", "disciplina", "semestre", "ano"])
        print(df)

        print("\nQuery 3: Alunos que se formaram em determinado semestre e ano")

        result = session.run(
        """
        MATCH (a:Aluno)-[r:CURSOU]->(d:Disciplina)
WHERE r.nota >= 5
WITH a, collect(DISTINCT d) AS disciplinas_cursadas, max(r.ano) AS ultimo_ano
MATCH (a)-[:MATRICULADO_EM]->(curso:Curso)-[:TEM_DISCIPLINA]->(d:Disciplina)
WITH a, disciplinas_cursadas, ultimo_ano, collect(DISTINCT d) AS disciplinas_curso
WITH a, disciplinas_cursadas, disciplinas_curso, ultimo_ano, size(disciplinas_cursadas) AS qtd_cursadas, size(disciplinas_curso) AS qtd_curso
WHERE ALL(d IN disciplinas_curso WHERE d IN disciplinas_cursadas)
RETURN a.nome AS aluno, a.id AS aluno_id, ultimo_ano AS ano_formacao
        """, 
    )

        df = pd.DataFrame(result, columns=["aluno", "aluno_id", "ano_formacao"])
        print(df)
        

        print("\nQuery 4: Chefes de departamento")

        result = session.run(
            """
            MATCH (p:Professor)-[:CHEFE_DE]->(d:Departamento)
            RETURN p.nome AS professor, d.nome AS departamento
            """
        )

        df = pd.DataFrame(result, columns=["professor", "departamento"])
        print(df)

        
        print("\nQuery 5: Alunos de tcc e orientador")

        result = session.run(
            """
            MATCH (a:Aluno)-[:REALIZA]->(t:TCC)-[:ORIENTADO_POR]->(p:Professor)
            RETURN t.nome AS tcc, collect(a.nome) AS alunos, p.nome AS orientador
            """
        )

        df = pd.DataFrame(result, columns=["tcc", "alunos", "orientador"])
        print(df)

        

       
        


        



