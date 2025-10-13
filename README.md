# ✅ Flask To‑Do API — organizando tarefas com estilo (CRUD)

Você foi convidado(a) por uma **escola** para criar uma **API de Lista de Tarefas** que ajude estudantes a organizar **trabalhos, provas e estudos**.  
A missão é direta e útil: **cadastrar**, **listar**, **atualizar** e **excluir** tarefas — tudo via HTTP e respostas em **JSON**.

Projeto pensado para **ensino médio**: linguagem técnica, mas acessível, e um toque de design para ficar gostoso de ler. ✨

---

## 🎬 Enunciado — A missão do dev
A coordenação pedagógica quer incentivar **organização e autonomia**. Para isso, você vai construir uma **API** que gerencie tarefas (to‑dos).

Cada **tarefa** possui:
- `id` *(int)* — gerado pela API
- `titulo` *(str, obrigatório)* — ex.: “Revisar matemática — funções”
- `descricao` *(str, opcional)* — detalhes úteis
- `concluida` *(bool)* — `false` por padrão
- `criada_em` *(str ISO8601)* — timestamp gerado pelo servidor

### O que o sistema deve permitir
1) **Listar** todas as tarefas (`GET /tasks`)  
   - Bônus: filtrar por `?concluida=true|false`  
2) **Criar** nova tarefa (`POST /tasks`)  
3) **Atualizar** uma tarefa (`PUT /tasks/<id>`) — atualização **parcial** permitida  
4) **Excluir** uma tarefa (`DELETE /tasks/<id>`)  
5) **Saúde da API** (`GET /health`)  

> **Obs. didática:** Persistência em **memória** (dicionário/lista). Em projetos reais, troque por um BD.

---

## 🚦 Rotas (CRUD)
| Método | Rota            | Descrição                                     | Corpo (JSON)                                                             | Códigos |
|------:|------------------|-----------------------------------------------|--------------------------------------------------------------------------|--------:|
| GET   | `/tasks`         | Lista tarefas. Aceita filtro `?concluida=`    | –                                                                        | 200     |
| GET   | `/tasks/<id>`    | Retorna uma tarefa por `id`                   | –                                                                        | 200/404 |
| POST  | `/tasks`         | Cria tarefa                                   | `{ "titulo", "descricao?", "concluida?" }`                               | 201/400 |
| PUT   | `/tasks/<id>`    | Atualiza **parcialmente** campos da tarefa    | Subconjunto de `{ "titulo","descricao","concluida" }`                    | 200/400/404 |
| DELETE| `/tasks/<id>`    | Apaga tarefa                                  | –                                                                        | 204/404 |
| GET   | `/health`        | Verifica se a API está ativa                  | –                                                                        | 200     |

---

## 🔎 Exemplos rápidos com `curl`
Listar tarefas:
```bash
curl -s http://127.0.0.1:5000/tasks | jq
```

Listar **concluídas**:
```bash
curl -s "http://127.0.0.1:5000/tasks?concluida=true" | jq
```

Criar tarefa:
```bash
curl -s -X POST http://127.0.0.1:5000/tasks   -H "Content-Type: application/json"   -d '{"titulo":"Estudar literatura", "descricao":"Cap. 3 e 4 do livro"}' | jq
```

Concluir tarefa (atualização parcial):
```bash
curl -s -X PUT http://127.0.0.1:5000/tasks/1   -H "Content-Type: application/json"   -d '{"concluida": true}' | jq
```

Excluir tarefa:
```bash
curl -i -X DELETE http://127.0.0.1:5000/tasks/1
```

---

## 💻 Como rodar

**Pré‑requisito:** Python **3.10+**

```bash
# 1) (opcional) ambiente virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) dependências
pip install -r requirements.txt

# 3) iniciar API
python app.py
# ou:
# flask --app app:app run --reload

# teste rápido
curl -s http://127.0.0.1:5000/health
```

---

## 🧠 Conceitos trabalhados
- **CRUD** completo
- **Dicionário/lista em memória** como “mini‑banco”
- **Validação simples** de payload e **códigos HTTP**
- **Filtros** via query string (`?concluida=`)
- Testes com **Flask test client**

---

## 🚀 Próximos passos
- Persistência real (SQLite) e **camada de repositório**
- Campo `prazo` (deadline) e filtro por vencidas
- Ordenação por `criada_em` / `concluida`
- Autenticação (token simples) para usuários
- CORS + frontend simples consumindo a API

---

## 📂 Estrutura
```
flask-todo-api/
├─ app.py
├─ requirements.txt
├─ README.md
├─ tests/
│  └─ test_app.py
├─ .gitignore
└─ LICENSE
```

---

## 📝 Licença
Projeto sob **MIT** — use, adapte e compartilhe. ✅
