import os
import sys
from pathlib import Path
from tempfile import TemporaryFile

sys.path.append(str(Path(os.path.dirname(__file__))))

try:
    from UTILS.base64_encode_decode import image_to_base64
except Exception as ex:
   raise Exception(ex)

input_image = r'C:\Users\Emerson\Desktop\Analytics\MATERIAIS POR TEMA\OCR\IMAGENS\A-comparative-study-of-the-OCR-systems-using-color-and-gray-scale-images-with-or-without.png'

image_base64 = image_to_base64(input_image)

# CRIANDO UM TEMPORARYFILE EM MODO DE ESCRITA
with TemporaryFile() as temp_file:

    # OBTENDO O NOME DO ARQUIVO TEMP
    print(temp_file.name)

    # ESCREVENDO NO ARQUIVO TEMP
    temp_file.write(image_base64)

    # INDO ATÉ A PRIMEIRA LINHA DO ARQUIVO
    temp_file.seek(0)

    # REALIZANDO A LEITURA DESSA PRIMEIRA LINHA
    print(temp_file.read())