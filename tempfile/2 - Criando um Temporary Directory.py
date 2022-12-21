from pathlib import Path
from tempfile import TemporaryDirectory

# CRIANDO UM TEMPORARYDIRECTORY - SEM DEFINIR O SEU NOME
with TemporaryDirectory() as temp_dir:

    # OBTENDO O NOME DO DIRETÓRIO TEMPORÁRIO
    print(temp_dir)

    # DEFININDO O NOME DO ARQUIVO DENTRO DA TEMPDIR
    arquivo = Path(temp_dir) / 'batatinhas.txt'

    arquivo.write_text('Paulo Braga')

print("TEMPDIRECTORY FINISH")