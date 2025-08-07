import os
import glob

def unir_markdown():
    """
    Encontra todos os arquivos .md no diretório atual,
    lê o conteúdo de cada um e os une em um único arquivo de saída.
    """
    # Define o nome do arquivo de saída
    output_filename = "resultado.md"

    # Pega o caminho do diretório onde o script está sendo executado
    # e muda o diretório de trabalho para ele, garantindo que os caminhos funcionem
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Encontra todos os arquivos com a extensão .md no diretório atual
    # e os ordena em ordem alfabética para um resultado consistente.
    md_files = sorted(glob.glob('*.md'))

    # Remove o próprio arquivo de saída da lista para evitar que ele se leia
    if output_filename in md_files:
        md_files.remove(output_filename)

    if not md_files:
        print("Nenhum arquivo .md encontrado para unir.")
        return

    print(f"Encontrados {len(md_files)} arquivos .md para unificar:")
    
    # Lista para armazenar o conteúdo de todos os arquivos
    all_content = []

    # Itera sobre cada arquivo encontrado
    for filename in md_files:
        print(f"  - Lendo '{filename}'")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                all_content.append(f.read())
        except Exception as e:
            print(f"    Erro ao ler o arquivo {filename}: {e}")

    # Une o conteúdo de todos os arquivos, separados por uma linha horizontal
    # para melhor legibilidade.
    consolidated_content = "\n\n---\n\n".join(all_content)

    # Escreve o conteúdo unificado no arquivo de saída
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(consolidated_content)
        print(f"\nSucesso! Arquivos unidos em '{output_filename}'")
    except Exception as e:
        print(f"\nErro ao salvar o arquivo consolidado: {e}")

if __name__ == "__main__":
    unir_markdown()