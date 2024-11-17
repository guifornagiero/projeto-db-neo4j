// Query 1: Histórico escolar de qualquer aluno
// A consulta retorna o histórico escolar de todos os alunos, incluindo seu RA, nome, disciplinas cursadas, semestre, ano e nota final.
MATCH (a:Aluno)-[r:CURSOU]->(d:Disciplina)
RETURN a.ra AS ra, a.nome AS aluno, d.id AS id, d.nome AS nomeDisciplina, 
       r.semestre AS semestre, 
       r.ano AS ano, 
       r.nota AS notaFinal
ORDER BY a.ra, a.nome, d.id;

// Query 2: Histórico de disciplinas ministradas por qualquer professor
// A consulta retorna o histórico de disciplinas ministradas por qualquer professor, incluindo o nome do professor, o nome da disciplina, semestre e ano.
MATCH (p:Professor)-[r:PROFESSOR_DE]->(d:Disciplina)
    RETURN p.nome, d.nome AS disciplina, r.semestre AS semestre, r.ano AS ano
ORDER BY p.nome, r.ano, r.semestre

// Query 3: Alunos que se formaram em determinado semestre e ano
// A consulta retorna os alunos que se formaram, considerando aqueles que cursaram todas as disciplinas obrigatórias do curso e obtiveram nota maior ou igual a 5. Ela retorna o RA, nome, ID do aluno e o ano de formação.
MATCH (a:Aluno)-[r:CURSOU]->(d:Disciplina)
WHERE r.nota >= 5
WITH a, collect(DISTINCT d) AS disciplinas_cursadas, max(r.ano) AS ultimo_ano
MATCH (a)-[:MATRICULADO_EM]->(curso:Curso)-[:TEM_DISCIPLINA]->(d:Disciplina)
WITH a, disciplinas_cursadas, ultimo_ano, collect(DISTINCT d) AS disciplinas_curso
WITH a, disciplinas_cursadas, disciplinas_curso, ultimo_ano, size(disciplinas_cursadas) AS qtd_cursadas, size(disciplinas_curso) AS qtd_curso
WHERE ALL(d IN disciplinas_curso WHERE d IN disciplinas_cursadas)
RETURN a.ra AS ra, a.nome AS aluno, a.id AS aluno_id, ultimo_ano AS ano_formacao

// Query 4: Chefes de departamento
// A consulta retorna os professores que são chefes de departamentos, incluindo o nome do professor e o nome do departamento.
MATCH (p:Professor)-[:CHEFE_DE]->(d:Departamento)
RETURN p.nome AS professor, d.nome AS departamento

// Query 5: Alunos de tcc e orientador
// A consulta retorna os alunos que estão realizando TCC, juntamente com o nome do TCC e o nome do orientador.
MATCH (a:Aluno)-[:REALIZA]->(t:TCC)-[:ORIENTADO_POR]->(p:Professor)
RETURN t.nome AS tcc, collect(a.nome) AS alunos, p.nome AS orientador
