import flet as ft

def main(page):
    # Personalização da página inicial
    titulo = ft.Text("Chat pessoal")
    chat = ft.Column()
    
    # Função chamada ao receber mensagens
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        page.update()

    # Inscrição no sistema PubSub
    page.pubsub.subscribe(enviar_mensagem_tunel)

    # Enviar mensagem pelo chat
    def enviar_mensagem(evento):
        if campo_enviar_mensagem.value.strip():
            mensagem = f"{nome_usuario.value}: {campo_enviar_mensagem.value}"
            page.pubsub.send_all(mensagem)
            campo_enviar_mensagem.value = ""
            page.update()
        else:
            campo_enviar_mensagem.error_text = "A mensagem não pode estar vazia."
            page.update()

    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_dialogo = ft.Row([campo_enviar_mensagem, botao_enviar])

    # Função para abrir o chat após preencher o nome
    def abrir_chat(evento):
        if not nome_usuario.value.strip():
            nome_usuario.error_text = "Por favor, insira seu nome."
            page.update()
            return
        
        popup.open = False
        page.dialog = None
        page.clean()
        page.add(titulo)
        page.add(chat)
        page.add(linha_dialogo)
        enviar_mensagem_tunel(f"{nome_usuario.value} entrou no chat.")
        page.update()

    # Criando o popup de identificação
    titulo_popup = ft.Text("Bem-vindo ao meu chat personalizado")
    nome_usuario = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Iniciar chat", on_click=abrir_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=nome_usuario, actions=[botao_popup])

    # Botão para abrir o popup
    def abrir_popup(evento):
        page.dialog = popup
        popup.open = True
        page.update()

    botao_iniciar = ft.ElevatedButton("Iniciar aplicação", on_click=abrir_popup)
    page.add(titulo)
    page.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)
