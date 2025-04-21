from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lista_contatos import contatos_destino
import time
import random

# Nome do grupo de origem
nome_do_grupo = "Automation"

# Configurações do navegador
chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=C:/zap")  # Descomente se usar perfil específico
# chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_experimental_option("detach", True)

# Inicia o navegador
driver = webdriver.Chrome(service=Service(), options=chrome_options)
driver.get("https://web.whatsapp.com/")

print("🔒 WhatsApp Web aberto. Aguarde o carregamento completo manualmente.")
input("✅ Quando o WhatsApp Web estiver 100% carregado e com o grupo visível, pressione ENTER para continuar...")

# PAUSAS REDUZIDAS MAS AINDA ALEATÓRIAS
def pausa_aleatoria(minimo=0.6, maximo=1.5):
    tempo = random.uniform(minimo, maximo)
    print(f"⏳ Pausando por {tempo:.2f} segundos...")
    time.sleep(tempo)

def abrir_grupo(grupo_nome):
    try:
        print(f"Aguardando o grupo '{grupo_nome}' aparecer...")
        grupo = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//span[@title='{grupo_nome}']"))
        )
        grupo.click()
        print(f"✅ Grupo '{grupo_nome}' aberto com sucesso!")
        pausa_aleatoria()
    except Exception as e:
        print(f"❌ Erro ao localizar o grupo: {e}")

def clicar_botao_encaminhar():
    try:
        print("Clicando no botão de encaminhar...")
        encaminhar_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "x17t9dm2"))
        )
        encaminhar_btn.click()
        print("✅ Botão de encaminhar clicado!")
        pausa_aleatoria()
    except Exception as e:
        print(f"❌ Erro ao clicar no botão de encaminhar: {e}")

def selecionar_contatos(contatos):
    for contato in contatos:
        try:
            print(f"🔍 Buscando contato '{contato}'...")
            campo_pesquisa = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
            )

            campo_pesquisa.clear()
            for _ in range(30):  # Pressiona backspace várias vezes só pra garantir
                campo_pesquisa.send_keys(Keys.BACKSPACE)

            campo_pesquisa.send_keys(contato)
            pausa_aleatoria(0.5, 1.0)

            # Verifica se o contato apareceu
            try:
                contato_elemento = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, f"//span[@title='{contato}']"))
                )
                contato_elemento.click()
                print(f"✅ Contato '{contato}' selecionado.")
                pausa_aleatoria(0.5, 1.0)
            except:
                print(f"⚠️ Contato '{contato}' não encontrado. Pulando...")
                campo_pesquisa.clear()
                for _ in range(30):
                    campo_pesquisa.send_keys(Keys.BACKSPACE)
                continue

        except Exception as e:
            print(f"⚠️ Erro inesperado ao buscar o contato '{contato}': {e}")

def enviar_mensagem():
    try:
        print("📤 Navegando com TAB até o botão de envio...")
        actions = ActionChains(driver)
        for i in range(6):
            actions.send_keys(Keys.TAB).perform()
            print(f"TAB {i+1} pressionado")
            time.sleep(0.3)  # Tempo de resposta entre TABs reduzido
        actions.send_keys(Keys.ENTER).perform()
        print("✅ Mensagem enviada com sucesso!")
        pausa_aleatoria(1.0, 2.0)

        # Pressiona ESC para garantir que tela volte ao normal
        actions.send_keys(Keys.ESCAPE).perform()
        print("🧹 Tecla ESC pressionada para limpar a tela.")
        pausa_aleatoria(0.6, 1.2)

    except Exception as e:
        print(f"❌ Erro ao finalizar envio com TAB + ENTER: {e}")

# Loop por lotes de 5 contatos
tamanho_lote = 5
for i in range(0, len(contatos_destino), tamanho_lote):
    lote = contatos_destino[i:i + tamanho_lote]
    print(f"\n🔁 Enviando para lote {i//tamanho_lote + 1}: {lote}")
    abrir_grupo(nome_do_grupo)
    clicar_botao_encaminhar()
    selecionar_contatos(lote)
    enviar_mensagem()

print("\n🎉✅ Todos os contatos foram processados com sucesso!")
