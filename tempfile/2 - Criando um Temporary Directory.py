from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:

    # OBTENDO O NOME DO DIRETÓRIO TEMPORÁRIO
    print(temp_dir)

    # DEFININDO O NOME DO ARQUIVO DENTRO DA TEMPDIR
    arquivo = Path(temp_dir) / 'batatinhas.txt'

    arquivo.write_text('Paulo Braga')