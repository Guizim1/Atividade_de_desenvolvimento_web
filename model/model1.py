# Importando o módulo que fornece uma DB-API para SQLite
import sqlite3

# Classe Table (superclasse):
class Table:
    def __init__(self):
        # Inicializa a conexão com o banco de dados e cria um cursor
        self.module = sqlite3
        self.conn = self.module.connect("myDB.db")
        self.cursor = self.conn.cursor()

    def close(self):
        # Fecha o cursor e a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()

# Classe Personagem:
class Personagem(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Personagem se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Personagem(
            id_person INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_person VARCHAR(30) NOT NULL,
            poder_person VARCHAR(30) NOT NULL,
            arma_person VARCHAR(30) NOT NULL,
            forca_person INTEGER NOT NULL,
            agilidade_person INTEGER NOT NULL,
            nivel_person INTEGER NOT NULL
        );""")
        self.conn.commit()
    def add_person(self, nome_person: str, poder_person: str, arma_person: str, forca_person: int, agilidade_person: int, nivel_person: int):
        # Insere um novo personagem na tabela Personagem
        self.cursor.execute("""
        INSERT INTO Personagem (nome_person, poder_person, arma_person, forca_person, agilidade_person, nivel_person)
        VALUES (?, ?, ?, ?, ?, ?);
        """, (nome_person, poder_person, arma_person, forca_person, agilidade_person, nivel_person))
        self.conn.commit()
    def select_person(self):
        # Seleciona todos os personagens da tabela Personagem
        self.cursor.execute("SELECT * FROM Personagem;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_person': registro[1],
                'poder_person': registro[2],
                'arma_person': registro[3],
                'forca_person': registro[4],
                'agilidade_person': registro[5],
                'nivel_person': registro[6]})
            return registros

    def del_person(self, id: int):
        # Ativa chaves estrangeiras e deleta um personagem pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Personagem WHERE id_person = ?;", (id,))
        self.conn.commit()
    def update_person(self, id_person: int, nome_person: str, poder_person: str, arma_person: str, forca_person: int, agilidade_person: int, nivel_person: int):
        # Atualiza os dados de um personagem existente pelo id
        self.cursor.execute("""
            UPDATE Personagem SET nome_person = ?, poder_person = ?, arma_person = ?, forca_person = ?, agilidade_person = ?, nivel_person = ?
            WHERE id_person = ?;
            """, (nome_person, poder_person, arma_person, forca_person, agilidade_person, nivel_person, id_person))
        self.conn.commit()
# Classe Grupo:
class Grupo(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Grupo se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Grupo(
            id_Grupo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_Grupo VARCHAR(30) NOT NULL,
            quant_membros INTEGER NOT NULL
        );""")
        self.conn.commit()
    def add_Grupo(self, nome_Grupo: str, quant_membros: int):
        # Insere um novo grupo na tabela Grupo
        self.cursor.execute("""
        INSERT INTO Grupo (nome_Grupo, quant_membros)
        VALUES (?, ?);
        """, (nome_Grupo, quant_membros))
        self.conn.commit()
    def select_Grupo(self):
        # Seleciona todos os grupos da tabela Grupo
        self.cursor.execute("SELECT * FROM Grupo;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_Grupo': registro[1],
                'quant_membros': registro[2]})
        return registros

    def del_Grupo(self, id: int):
        # Ativa chaves estrangeiras e deleta um grupo pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Grupo WHERE id_Grupo = ?;", (id,))
        self.conn.commit()
    def update_Grupo(self, id_Grupo: int, nome_Grupo: str, quant_membros: int):
        # Atualiza os dados de um grupo existente pelo id
        self.cursor.execute("""
            UPDATE Grupo SET nome_Grupo = ?, quant_membros = ?
            WHERE id_Grupo = ?;
            """, (nome_Grupo, quant_membros, id_Grupo))
        self.conn.commit()

# Classe Missoes:
class Missoes(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Missoes se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Missoes(
            id_mis INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            objetivo_mis VARCHAR(30) NOT NULL,
            descricao_mis VARCHAR(30) NOT NULL,
            recompensa INTEGER NOT NULL
        );""")
        self.conn.commit()

    def add_mis(self, objetivo: str, descricao: str, recompensa: int):
        # Insere uma nova missão na tabela Missoes
        self.cursor.execute("""
        INSERT INTO Missoes (objetivo_mis, descricao_mis, recompensa)
        VALUES (?, ?, ?);
        """, (objetivo, descricao, recompensa))
        self.conn.commit()
    def select_mis(self):
        # Seleciona todas as missões da tabela Missoes
        self.cursor.execute("SELECT * FROM Missoes;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_mis': registro[0],
                'objetivo_mis': registro[1],
                'descricao_mis': registro[2],
                'recompensa': registro[3]})
        return registros

    def del_mis(self, id: int):
        # Ativa chaves estrangeiras e deleta uma missão pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Missoes WHERE id_mis = ?;", (id,))
        self.conn.commit()
    def update_mis(self, id_mis: int, objetivo: str, descricao: str, recompensa: int):
        # Atualiza os dados de uma missão existente pelo id
        self.cursor.execute("""
            UPDATE Missoes SET objetivo_mis = ?, descricao_mis = ?, recompensa = ?
            WHERE id_mis = ?;
            """, (objetivo, descricao, recompensa, id_mis))
        self.conn.commit()
# Classe Genero:
class Genero(Table):
    def __init__(self):
        super().__init__()
        # Cria a tabela Genero se ela não existir
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Genero(
            id_gene INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            tipo_gene VARCHAR(30) NOT NULL
        );""")
        self.conn.commit()

    def add_gene(self, tipo: str):
        # Insere um novo gênero na tabela Genero
        self.cursor.execute("""
        INSERT INTO Genero (tipo_gene)
        VALUES (?);
        """, (tipo,))
        self.conn.commit()
    def select_gene(self):
        # Seleciona todos os gêneros da tabela Genero
        self.cursor.execute("SELECT * FROM Genero;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_gene': registro[0],
                'tipo_gene': registro[1]})
        return registros

    def del_gen(self, id: int):
        # Ativa chaves estrangeiras e deleta um gênero pelo id
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("DELETE FROM Genero WHERE id_gene = ?;", (id,))
        self.conn.commit()
    def update_gen(self, id_gene: int, tipo: str):
        # Atualiza os dados de um gênero existente pelo id
        self.cursor.execute("""
            UPDATE Genero SET tipo_gene = ?
            WHERE id_gene = ?;
            """, (tipo, id_gene))
        self.conn.commit()
# Objetos de cada tabela:
# Cria instâncias de cada classe para interação com o banco de dados
Obj_Person = Personagem()
Obj_grupo = Grupo()
Obj_Mis = Missoes()
Obj_Genero = Genero()
