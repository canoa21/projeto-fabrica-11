
import unittest
from app import app, TASKS

class TodoApiTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # Reset previsível
        TASKS.clear()
        TASKS.extend([
            {"id": 1, "titulo": "Revisar matemática — funções", "descricao": "Listas 1 e 2", "concluida": False, "criada_em": "2025-01-01T10:00:00Z"},
            {"id": 2, "titulo": "Ler capítulo de história", "descricao": "Cap. 3 — Revolução Francesa", "concluida": True, "criada_em": "2025-01-02T14:30:00Z"},
        ])

    def test_health(self):
        r = self.client.get('/health')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["status"], "ok")

    def test_list_tasks(self):
        r = self.client.get('/tasks')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.get_json()), 2)

    def test_filter_concluidas(self):
        r = self.client.get('/tasks?concluida=true')
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(len(data), 1)
        self.assertTrue(data[0]["concluida"])

    def test_get_task_ok(self):
        r = self.client.get('/tasks/1')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["id"], 1)

    def test_get_task_404(self):
        r = self.client.get('/tasks/999')
        self.assertEqual(r.status_code, 404)

    def test_create_task_ok(self):
        r = self.client.post('/tasks', json={"titulo": "Estudar química"})
        self.assertEqual(r.status_code, 201)
        self.assertIn("id", r.get_json())

    def test_create_task_400(self):
        r = self.client.post('/tasks', json={"descricao": "sem titulo"})
        self.assertEqual(r.status_code, 400)

    def test_update_task_ok(self):
        r = self.client.put('/tasks/1', json={"concluida": True})
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.get_json()["concluida"])

    def test_update_task_404(self):
        r = self.client.put('/tasks/999', json={"concluida": False})
        self.assertEqual(r.status_code, 404)

    def test_delete_task_ok(self):
        r = self.client.delete('/tasks/2')
        self.assertEqual(r.status_code, 204)

    def test_delete_task_404(self):
        r = self.client.delete('/tasks/999')
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()
