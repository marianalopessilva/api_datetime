import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verificar_data/<ano>-<mes>-<dia>')
def verificar_data(ano,mes,dia):
    """
    ## Endpoint:
    'GET /dias/<data_str>

    :param ano: ano digitado pelo usuario
    :param mes: mes digitado pelo usuario
    :param dia: dia digitado pelo usuario
    :return: retorna o periodo da data recebida
    (futuro, presente e passado) e a diferença em dias,
     meses e anos entre as datas

    ## Resposta (JSON):
    '''json
    {
        'situacao': passado,
        'dias_diferenca': 90,
        'meses_diferenca': 3,
        'anos_diferenca': 0,
    }
    '''

    ## Erros possiveis:
    - Se data_recebida tiver letra, retorna 'erro': "valor inválido"
       '''json
    """
    try:
        ano = int(ano)
        mes = int(mes)
        dia = int(dia)

        data_recebida = datetime.datetime(ano, mes, dia).date()
        data_atual = datetime.datetime.now().date()

        situacao = ''
        dias_diferenca = data_atual - data_recebida
        meses_diferenca = (data_atual.year - data_recebida.year) * 12
        anos_diferenca = data_atual.year - data_recebida.year

        if data_recebida > data_atual:
            situacao = 'Futuro'
        elif data_recebida < data_atual:
            situacao = 'Passado'
        else:
            situacao = 'Presente'


        return jsonify({
            'situacao': situacao,
            'dias_diferenca': str(dias_diferenca),
            'meses_diferenca': meses_diferenca,
            'anos_diferenca': anos_diferenca,
        })
    except ValueError:
        return jsonify ({
            'erro': "valor inválido"
        })


if __name__ == '__main__':
    app.run(debug=True)
