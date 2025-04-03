from database import get_connection

class GenericCRUD:
    def __init__(self, object_class=None):
        self.table_name = object_class.table_name
        self.object_class = object_class
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def insert(self, obj):
        """Insere um novo registro na tabela utilizando um objeto"""
        data = obj.to_dict()  # Convertendo o objeto para dicionário
        columns = ', '.join(data.keys())  # Gera "coluna1, coluna2"
        values_placeholder = ', '.join(['%s'] * len(data))  # Gera "%s, %s"
        sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values_placeholder}) RETURNING id;"
        
        self.cur.execute(sql, tuple(data.values()))
        record_id = self.cur.fetchone()[0]
        self.conn.commit()
        
        # Se for um objeto, atribuímos o id gerado
        if self.object_class:
            obj.user_id = record_id
        return obj

    def update(self, obj):
        """Atualiza um registro pelo ID utilizando um objeto"""
        data = obj.to_dict()  # Convertendo o objeto para dicionário
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE id = %s;"
        
        self.cur.execute(sql, tuple(data.values()) + (obj.user_id,))
        self.conn.commit()

    def delete(self, obj):
        """Exclui um registro pelo ID utilizando um objeto"""
        sql = f"DELETE FROM {self.table_name} WHERE id = %s;"
        self.cur.execute(sql, (obj.user_id,))
        self.conn.commit()

    def list_all(self):
        """Lista todos os registros da tabela, retornando objetos"""
        sql = f"SELECT * FROM {self.table_name};"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        
        # Retorna uma lista de objetos, se a classe do objeto for fornecida
        if self.object_class:
            return [self.object_class.from_db_row(row) for row in rows]
        return rows

    def close(self):
        """Fecha a conexão com o banco"""
        self.cur.close()
        self.conn.close()
