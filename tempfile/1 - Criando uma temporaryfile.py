from tempfile import TemporaryFile

# CRIANDO UM TEMPORARYFILE EM MODO DE ESCRITA
with TemporaryFile(mode='w+') as temp_file:

    # OBTENDO O NOME DO ARQUIVO TEMP
    print(temp_file.name)

    # ESCREVENDO NO ARQUIVO TEMP
    temp_file.write('batatinhas')

    # INDO ATÉ A PRIMEIRA LINHA DO ARQUIVO
    temp_file.seek(0)

    # REALIZANDO A LEITURA DESSA PRIMEIRA LINHA
    print(temp_file.read())