from fastapi import APIRouter
from crud import GenericCRUD
from users import Users
from typing import List

router = APIRouter()

# Criar uma instância para manipular a tabela "users"
users_crud = GenericCRUD(Users)

@router.get("/users", response_model=List[Users])
def get_all_users():
    """Retorna a lista de todos os usuários."""
    return users_crud.list_all()

# Listar todos os usuários
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
