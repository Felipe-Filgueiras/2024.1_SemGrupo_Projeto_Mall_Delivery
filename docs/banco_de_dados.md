# Modelo de Banco de Dados do Projeto

Este documento fornece uma visão geral do modelo de banco de dados para o nosso projeto Django, que inclui entidades para gerenciar produtos e perfis de usuário. O modelo é projetado para lidar com listagens de produtos e informações adicionais específicas do usuário.

## Entidades e Campos

### Produto
Esta tabela armazena informações sobre cada produto que os usuários podem visualizar, adicionar ou gerenciar no sistema.

- **Campos**:
  - **id**: Chave primária, gerada automaticamente pelo Django.
  - **nome**: O nome do produto.
  - **descricao**: Uma descrição detalhada do produto.
  - **preco**: O preço do produto.
  - **categoria**: A categoria à qual o produto pertence.
  - **imagem**: Uma imagem do produto.
  - **criado_em**: A data e hora em que o produto foi adicionado ao sistema.

### PerfilUsuario
Esta tabela armazena informações adicionais sobre os usuários. Ela está vinculada ao modelo User incorporado do Django por um relacionamento um-para-um.

- **Campos**:
  - **usuario_id**: Uma chave estrangeira vinculando ao modelo User padrão do Django (relacionamento um-para-um).
  - **nome**: O primeiro nome do usuário.
  - **sobrenome**: O sobrenome do usuário.
  - **cnpj**: Um identificador fiscal brasileiro semelhante a um CNPJ.
  - **foto_perfil**: Uma imagem para o perfil do usuário.
  - **conta_bancaria**: O número da conta bancária do usuário.
  - **agencia_bancaria**: O número da agência bancária.

## Relacionamentos
- **User para PerfilUsuario**: Um-para-Um (Cada usuário tem um perfil. Cada perfil está associado a um usuário).

