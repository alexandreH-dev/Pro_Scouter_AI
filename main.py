from crud import GenericCRUD
from users import Users  # Suponha que a classe User esteja em user.py

# Criar uma instância para manipular a tabela "users"
users_crud = GenericCRUD(Users)

# # 1️⃣ Inserir um novo usuário
# novo_usuario = User(nome="Carlos Mendes", email="carlos@email.com")
# usuario_inserido = users_crud.insert(novo_usuario)
# print(f"Usuário inserido com ID: {usuario_inserido.user_id}")

# # 2️⃣ Atualizar o usuário
# usuario_inserido.nome = "Carlos M."
# usuario_inserido.email = "carlos.m@email.com"
# users_crud.update(usuario_inserido)
# print("Usuário atualizado!")

# 3️⃣ Listar todos os usuários
usuarios = users_crud.list_all()
print("Lista de usuários:")
print(usuarios)
for usuario in usuarios:
    print(f"ID: {usuario.user_id}, Nome: {usuario.nome}, Email: {usuario.email}")

# # 4️⃣ Deletar o usuário
# users_crud.delete(usuario_inserido)
# print("Usuário deletado!")

# 5️⃣ Fechar conexão
users_crud.close()
