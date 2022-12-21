from io import BytesIO
from tempfile import SpooledTemporaryFile
from memory_profiler import profile


input_image = r'C:\Users\Emerson\Pictures\4.jpg'


@profile
def test_tempfile():
    # REALIZANDO A ABERTURA DA IMAGEM
    with open(input_image, 'rb') as file:
        # DEFININDO O PARÂMETRO DE GRANDE DO STF
        um_mb = 1_000_000
        # REALIZANDO A ABERTURA DO
        with SpooledTemporaryFile(max_size=um_mb) as stf:
            em_memoria = stf.write(file.read())
            print(stf.name)
            return em_memoria

@profile
def test_bytesio():
    with open(input_image, 'rb') as file:
        em_memoria = BytesIO(file.read())
        return em_memoria

test_tempfile()
test_bytesio()