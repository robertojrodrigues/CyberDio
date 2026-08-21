from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(nome_arquivo, chave):
    f = Fernet(chave)
    with open(nome_arquivo, "rb") as arquivo:
        conteudo_criptografado = arquivo.read()
    conteudo_original = f.decrypt(conteudo_criptografado)
    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(conteudo_original)

def encontrar_arquivos(caminho):
    lista_arquivos = []
    for root, dirs, files in os.walk(caminho):
        for file in files:
            if file.endswith((".txt", ".docx", ".pdf")):  # Adicione outras extensões conforme necessário
                lista_arquivos.append(os.path.join(root, file))
    return lista_arquivos

def main():
    chave = carregar_chave()
    caminho = r"C:\Users\robertoj\Cyberdio-me\test_files"  # Especificar o diretório neste caso de teste para evitar problemas de permissão e segurança
    arquivos = encontrar_arquivos(caminho)
    
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Arquivos recuperados com sucesso!")

if __name__ == "__main__":
    main()