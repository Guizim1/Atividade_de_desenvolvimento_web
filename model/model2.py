# Importações
from model import model1
import sqlite3

# Classes de associações:

# Classe PersonGrupo
class PersonGrupo:
    def __init__(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Criar a tabela PersonGrupo se ela não existir
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS PersonGrupo(
            id_perso INTEGER,
            id_grup INTEGER,
            PRIMARY KEY (id_perso, id_grup),
            FOREIGN KEY (id_perso) REFERENCES Personagem(id_person) ON DELETE CASCADE,
            FOREIGN KEY (id_grup) REFERENCES Grupo(id_Grupo) ON DELETE CASCADE
        );
        """)
        conn.close()  # Fechar a conexão com o banco de dados

    def add_Person_Grupo(self, id_perso: int, id_grup: int) -> None:
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Inserir uma nova associação na tabela PersonGrupo
        cursor.execute("""
            INSERT INTO PersonGrupo(id_perso, id_grup)
            VALUES(?, ?);
        """, (id_perso, id_grup))
        conn.commit()  # Confirmar as mudanças
        conn.close()  # Fechar a conexão com o banco de dados

    def select_associacao_PersonGrupo(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Selecionar todas as associações da tabela PersonGrupo
        cursor.execute("SELECT * FROM PersonGrupo;")
        anotacoes = []
        # Iterar sobre os resultados da consulta e adicioná-los a uma lista
        for anotacao in cursor.fetchall():
            anotacoes.append({
                'id_perso': anotacao[0],
                'id_grup': anotacao[1]
            })
        conn.close()  # Fechar a conexão com o banco de dados
        return anotacoes  # Retornar a lista de associações

    def select_registro_PersonGrupo(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Selecionar registros combinados das tabelas Personagem e Grupo
        cursor.execute("""
        SELECT P.*, G.*
        FROM Personagem AS P
        INNER JOIN PersonGrupo AS PG ON P.id_person = PG.id_perso
        INNER JOIN Grupo AS G ON G.id_Grupo = PG.id_grup;
        """)
        anotacoes = []
        # Iterar sobre os resultados da consulta e adicioná-los a uma lista
        for anotacao in cursor.fetchall():
            anotacoes.append({
                "id_person": anotacao[0],
                "nome_person": anotacao[1],
                "poder_person": anotacao[2],
                "arma_person": anotacao[3],
                "forca_person": anotacao[4],
                "aligilidade_person": anotacao[5],
                "nivel_person": anotacao[6],
                "id_grup": anotacao[7],
                "nome_Grupo": anotacao[8],
                "quant_membros": anotacao[9]
            })
        conn.close()  # Fechar a conexão com o banco de dados
        return anotacoes  # Retornar a lista de registros combinados

# Classe PersonMiss
class PersonMiss:
    def __init__(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Criar a tabela PersonMiss se ela não existir
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS PersonMiss(
            id_perso INTEGER,
            id_miss INTEGER,
            PRIMARY KEY (id_perso, id_miss),
            FOREIGN KEY (id_perso) REFERENCES Personagem(id_person) ON DELETE CASCADE,
            FOREIGN KEY (id_miss) REFERENCES Missoes(id_miss) ON DELETE CASCADE
        );
        """)
        conn.close()  # Fechar a conexão com o banco de dados

    def add_Person_Miss(self, id_perso: int, id_miss: int):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Inserir uma nova associação na tabela PersonMiss
        cursor.execute("""
            INSERT INTO PersonMiss(id_perso, id_miss)
            VALUES(?, ?);
        """, (id_perso, id_miss))
        conn.commit()  # Confirmar as mudanças
        conn.close()  # Fechar a conexão com o banco de dados

    def select_associacao_PersonMiss(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Selecionar todas as associações da tabela PersonMiss
        cursor.execute("SELECT * FROM PersonMiss;")
        anotacoes = []
        # Iterar sobre os resultados da consulta e adicioná-los a uma lista
        for anotacao in cursor.fetchall():
            anotacoes.append({
                'id_perso': anotacao[0],
                'id_miss': anotacao[1]
            })
        conn.close()  # Fechar a conexão com o banco de dados
        return anotacoes  # Retornar a lista de associações

    def select_registro_PersonMiss(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Selecionar registros combinados das tabelas Personagem e Missoes
        cursor.execute("""
        SELECT P.*, M.*
        FROM Personagem AS P
        INNER JOIN PersonMiss AS PM ON P.id_person = PM.id_perso
        INNER JOIN Missoes AS M ON M.id_miss = PM.id_miss;
        """)
        anotacoes = []
        # Iterar sobre os resultados da consulta e adicioná-los a uma lista
        for anotacao in cursor.fetchall():
            anotacoes.append({
                "id_person": anotacao[0],
                "nome_person": anotacao[1],
                "poder_person": anotacao[2],
                "arma_person": anotacao[3],
                "forca_person": anotacao[4],
                "aligilidade_person": anotacao[5],
                "nivel_person": anotacao[6],
                "id_miss": anotacao[7],
                "objetivo_mis": anotacao[8],
                "descricao_mis": anotacao[9],
                "recompensa": anotacao[10]
            })
        conn.close()  # Fechar a conexão com o banco de dados
        return anotacoes  # Retornar a lista de registros combinados

# Classe PersonGene
class PersonGene:
    def __init__(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Criar a tabela PersonGene se ela não existir
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS PersonGene(
            id_perso INTEGER,
            id_gene INTEGER,
            PRIMARY KEY (id_perso, id_gene),
            FOREIGN KEY (id_perso) REFERENCES Personagem(id_person) ON DELETE CASCADE,
            FOREIGN KEY (id_gene) REFERENCES Genero(id_gene) ON DELETE CASCADE
        );
        """)
        conn.close()  # Fechar a conexão com o banco de dados

    def add_PersonGene(self, id_perso: int, id_gene: int):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Inserir uma nova associação na tabela PersonGene
        cursor.execute("""
            INSERT INTO PersonGene(id_perso, id_gene)
            VALUES(?, ?);
        """, (id_perso, id_gene))
        conn.commit()  # Confirmar as mudanças
        conn.close()  # Fechar a conexão com o banco de dados

    def select_Person_Gene(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Selecionar todas as associações da tabela PersonGene
        cursor.execute("SELECT * FROM PersonGene;")
        anotacoes = []
        # Iterar sobre os resultados da consulta e adicioná-los a uma lista
        for anotacao in cursor.fetchall():
            anotacoes.append({
                'id_perso': anotacao[0],
                'id_gene': anotacao[1]
            })
        conn.close()  # Fechar a conexão com o banco de dados
        return anotacoes  # Retornar a lista de associações

    def select_registro_PersonGene(self):
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        # Selecionar registros combinados das tabelas Personagem e Genero
        cursor.execute("""
        SELECT P.*, G.*
        FROM Personagem AS P
        INNER JOIN PersonGene AS PGen ON P.id_person = PGen.id_perso
        INNER JOIN Genero AS G ON G.id_gene = PGen.id_gene;
        """)
        anotacoes = []
        # Iterar sobre os resultados da consulta e adicioná-los a uma lista
        for anotacao in cursor.fetchall():
            anotacoes.append({
                "id_person": anotacao[0],
                "nome_person": anotacao[1],
                "poder_person": anotacao[2],
                "arma_person": anotacao[3],
                "forca_person": anotacao[4],
                "aligilidade_person": anotacao[5],
                "nivel_person": anotacao[6],
                "id_gene": anotacao[7],
                "tipo_gene": anotacao[8]
            })
        conn.close()  # Fechar a conexão com o banco de dados
        return anotacoes  # Retornar a lista de registros combinados

# Objetos de cada tabela:
Obj_PG = PersonGrupo()
Obj_PM = PersonMiss()
Obj_PGene = PersonGene()
