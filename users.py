class Users:
    table_name = 'users'
  
    def __init__(self, name_user, email_user, id_user=None):
        self.id_user = id_user
        self.name_user = name_user
        self.email_user = email_user

    def to_dict(self):
        """Converte o objeto User para um dicionário"""
        return {
            'nome': self.nome,
            'email': self.email
        }

    @classmethod
    def from_db_row(cls, row):
        """Cria um objeto User a partir de uma linha de resultado do banco"""
        return cls(user_id=row[0], nome=row[1], email=row[2])
