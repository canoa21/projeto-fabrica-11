from flask import Flask, jsonify, request

app = Flask(__name__) 

tarefas = [
    {"id": 1, "titulo": "lavar roupa", "descricao": "lavar roupa", "concluida": False},
    {"id": 2, "titulo": "pasar roupa", "descricao": "passar roupa", "concluida": False}
]

@app.route("/tarefas",methods=["GET"])
def get_tarefas():
    return jsonify({"mensagem": "lista de compras", "itens":tarefas, "total": len (tarefas)})

@app.route("/compras/<int:id>", methods=["GET"])
def get_compra_by_id(id):
    for  tarefa in tarefas:
        if tarefa ["id"] == id:
            return jsonify({"mensagem": "item encontrado", "item": tarefas(id)})
    return jsonify({"mensagem": "item nao encontrado"}), 404

@app.route("/tarefas", methods= ["POST"])
def add_item():
    nova_tarefa = request.json

    nova_tarefa["id"] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify ({"mensagem": "item cadastrado!", "item": nova_tarefa})

@app.route("/tarefas/<int:id>", methods=["PUT"])
def update_item(id):
    dados = request.json

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa.update(dados)
            return jsonify({"mensagem": "item atualizado!"})
       
    return jsonify({"mensagem": "item nao encontrado!"}),404
       
@app.route("/tarefas/<int:id>", methods=["DELETE"])
def delete_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
          tarefas.remove(tarefa)
          
        return jsonify ( {"mensagem": "item deletado"})



if __name__ == '__main__':
    app.run(debug=True)