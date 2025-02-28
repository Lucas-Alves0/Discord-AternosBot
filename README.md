# Discord-AternosBot

Este é um bot do Discord que interage com o serviço de hospedagem de servidores Aternos. Ele permite que você inicie, pare e verifique o status do seu servidor Aternos diretamente do Discord.

## Funcionalidades

- Iniciar o servidor Aternos
- Parar o servidor Aternos
- Verificar o status do servidor
- Listar jogadores online
- Mostrar informações do servidor (endereço e porta)
- Mensagens de boas-vindas para novos membros

## Pré-requisitos

- Python 3.7+
- Conta no Aternos
- Token do bot do Discord

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/Discord-AternosBot.git
    cd Discord-AternosBot
    ```

2. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

3. Configure suas credenciais do Aternos e o token do bot do Discord no arquivo `:

`Discord_Aternos_Bot.py    ```python
    atclient.login(str('User123'),str('Password123'))
    dcbot.run('Your discord bot TOKEN here')
    ```

4. Execute o bot:

    ```sh
    python [Discord_Aternos_Bot.py](http://_vscodecontentref_/1)
    ```

## Comandos do Bot

- `!iniciar` - Inicia o servidor
- `!parar` - Para o servidor
- `!status` - Mostra o status do servidor
- `!jogadores` - Mostra os jogadores online
- `!infoserver` - Mostra o endereço e porta do servidor
- `!ajuda` - Mostra os comandos disponíveis

## Arquivos

- `Discord_Aternos_Bot.py`: Código principal do bot
- `keep_alive.py`: Mantém o bot ativo usando Flask
- `README.md`: Este arquivo
