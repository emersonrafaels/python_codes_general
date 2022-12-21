from tempfile import NamedTemporaryFile


# CRIANDO UM TEMPORARYFILE - DEFININDO O SEU NOME
"""
    suffix: Sufixo do nome do arquivo
    prefix: Prefixo do nome do arquivo
    delete: Se o arquivo deve ser deletado ao fim do script
"""
with NamedTemporaryFile(
    suffix='.mp3',
    prefix='ldp_',
    delete=False
) as file:
    print(file.name)

print("TEMPDIRECTORY FINISH")