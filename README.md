# Discord Bot Project

Este é um bot do Discord desenvolvido com a biblioteca [discord.py]. O bot oferece uma variedade de funcionalidades, como comandos personalizados, integração com APIs externas, e outras ferramentas úteis para servidores do Discord.

## Funcionalidades

- **Comandos de Moderador**: Controle de membros, moderação de chat, etc.
- **Comandos Diversos**: Respostas automáticas, diversão, jogos e mais.
- **Integração com APIs**: Conectar-se a APIs externas para trazer informações como clima, notícias, entre outros.
- **Comandos Personalizados**: Criação de comandos conforme a necessidade do servidor.

## Tecnologias

- Python 3.x
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://docs.python-requests.org/en/latest/)

## Pré-requisitos

Antes de começar, você precisará ter os seguintes itens instalados no seu computador:

- Python 3.5 ou superior
- Pip (gerenciador de pacotes do Python)
- Conta no Discord e permissões para adicionar bots ao servidor

## Instalação

1. **Clonar o repositório**:

```bash
git clone https://github.com/seu-usuario/discord-bot.git
cd discord-bot
```

2. Criar e ativar um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

3. Ativar o ambiente virtual:

```bash
./venv/scripts/venv
```

4. Instalar as dependências:

```bash
pip install -r requirements.txt
```

5. Configurar o arquivo .env:

- Crie um arquivo .env na raiz do projeto e adicione sua chave de token do Discord:

```plaintext
DISCORD_TOKEN=seu_token_do_discord
```

## Como rodar

- Com o ambiente configurado, basta rodar o seguinte comando para iniciar o bot:

```bash
python bot.py
```

## Comandos
Comandos de Moderação

- `!ban <usuário>`: Bane um usuário do servidor.
- `!kick <usuário>`: Expulsa um usuário do servidor.
- `!mute <usuário>`: Muta um usuário para impedir que ele envie mensagens.

### Comandos Diversos

- `!ping`: Responde com "Pong!".
- `!hello`: Responde com "Olá, <nome do usuário>!".
- `!roll`: Joga um dado de 6 lados.

## Contribuindo

Se você deseja contribuir para este projeto, siga os seguintes passos:

1. Faça um **fork** do repositório.
2. Crie uma **branch** para a sua feature ou correção (`git checkout -b feature/nome-da-feature`).
3. Realize suas alterações e faça **commit** delas (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça o **push** da sua branch (`git push origin feature/nome-da-feature`).
5. Abra um **pull request**.

## Licença

Este projeto está licenciado sob a licença MIT. O arquivo [LICENSE](LICENSE) será adicionado para mais detalhes.
