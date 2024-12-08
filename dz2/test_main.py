import unittest
from unittest.mock import patch, MagicMock
import os
from git import Repo
from graphviz import Digraph
from main import load_config, check_repo_exists, analyze_commits, build_dependency_graph

class TestMainFunctions(unittest.TestCase):

    # Тест для load_config
    @patch("builtins.open", new_callable=MagicMock)
    def test_load_config(self, mock_open):
        mock_open.return_value.read.return_value = """
        graph_tool_path: /usr/local/bin/dot
        repo_path: /path/to/repo
        target_file: dz2_graph.py
        """
        config = load_config()
        self.assertEqual(config['graph_tool_path'], "/usr/local/bin/dot")
        self.assertEqual(config['repo_path'], "/path/to/repo")
        self.assertEqual(config['target_file'], "dz2_graph.py")

    # Тест для check_repo_exists
    @patch("git.Repo")
    def test_check_repo_exists(self, mock_repo):
        # Мокируем успешное создание репозитория
        mock_repo.return_value = MagicMock(spec=Repo)
        repo = check_repo_exists("/path/to/repo")
        self.assertIsNotNone(repo)

    @patch("git.Repo")
    def test_check_repo_not_exists(self, mock_repo):
        mock_repo.side_effect = Exception("Repository not found")
        repo = check_repo_exists("/path/to/nonexistent/repo")
        self.assertIsNone(repo)

    # Тест для analyze_commits
    @patch("git.Repo.iter_commits")
    def test_analyze_commits(self, mock_iter_commits):
        mock_iter_commits.return_value = ["commit1", "commit2"]
        repo_mock = MagicMock()
        commits = analyze_commits(repo_mock, "dz2_graph.py")
        self.assertEqual(len(commits), 2)
        mock_iter_commits.assert_called_with(paths="dz2_graph.py")

    @patch("git.Repo.iter_commits")
    def test_analyze_all_commits(self, mock_iter_commits):
        mock_iter_commits.return_value = ["commit1", "commit2"]
        repo_mock = MagicMock()
        commits = analyze_commits(repo_mock, 'all')
        self.assertEqual(len(commits), 2)
        mock_iter_commits.assert_called_with()

    # Тест для build_dependency_graph
    @patch("graphviz.Digraph.render")
    def test_build_dependency_graph(self, mock_render):
        mock_commits = ["commit1", "commit2"]
        graph = build_dependency_graph(mock_commits, "dz2_graph.py")
        self.assertEqual(len(graph.body), 4)  # Мы ожидаем 4 строки в графе
        mock_render.assert_called()

if __name__ == "__main__":
    unittest.main()
