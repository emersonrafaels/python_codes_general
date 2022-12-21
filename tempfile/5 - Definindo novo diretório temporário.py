import tempfile
from pathlib import Path

# DEFININDO O NOVO DIRETÓRIO TEMPORÁRIO
tempfile.tempdir = 'cache_dir'

# OBTENDO O LOCAL DO DIRETÓRIO TEMPORÁRIO
print(tempfile.gettempdir())

with tempfile.TemporaryDirectory() as temp_dir:

    # OBTENDO O NOME DO DIRETÓRIO TEMPORÁRIO
    print(temp_dir)

    # DEFININDO O NOME DO ARQUIVO DENTRO DA TEMPDIR
    arquivo = Path(temp_dir) / 'batatinhas.txt'

    arquivo.write_text('Paulo Braga')