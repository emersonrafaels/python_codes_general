from datetime import datetime

def medidor_de_tempo(func):

    def aninhada(*args, **kwargs):

        # OBTENDO O TEMPO INICIAL
        initial_time = datetime.now()

        # EXECUTANDO A FUNÇÃO DECORADA
        function_result = func(*args, **kwargs)

        # OBTENDO O TEMPO FINAL
        final_time = datetime.now()

        # CALCULANDO O TIMEDELTA
        delta_time = final_time - initial_time

        # REALIZANDO O PRINT
        print(f'A função {func.__name__} demorou {delta_time.total_seconds()} segundos.')

        # RETORNANDO O RESULTADO DA FUNÇÃO DECORADA
        return function_result

    return aninhada