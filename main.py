import instaloader
from win10toast import ToastNotifier
import time

# Criar uma instância do Instaloader
L = instaloader.Instaloader()

# Fazer login na sua conta (substitua 'seu_usuario' e 'sua_senha' pelas suas credenciais)
L.load_session_from_file('lou_is.gg')

# Obter o perfil do usuário (substitua 'seu_usuario' pelo seu nome de usuário)
profile = instaloader.Profile.from_username(L.context, 'lou_is.gg')

# Inicializar o objeto para exibir notificações
toaster = ToastNotifier()

# Obter a lista de seguidores atual
followers_before = set(profile.get_followers())

# Loop infinito para verificar se há mudanças nos seguidores
while True:
    # Obter a lista de seguidores atual
    followers_now = set(profile.get_followers())
    
    # Verificar se algum seguidor deixou de seguir
    unfollowed = followers_before - followers_now
    
    # Notificar se houver seguidores que deixaram de seguir
    if unfollowed:
        notification_text = "Os seguintes usuários deixaram de seguir:\n" + "\n".join([user.username for user in unfollowed])
        toaster.show_toast("Instagram", notification_text, duration=10)
    
    # Atualizar a lista de seguidores
    followers_before = followers_now
    
    # Esperar um tempo antes de verificar novamente (evitar sobrecarga)
    time.sleep(60)  # Aguardar 1 minuto antes de verificar novamente
