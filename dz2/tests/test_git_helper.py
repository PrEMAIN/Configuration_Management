import unittest
from unittest.mock import patch, MagicMock
from src.git_helper import get_dependencies

class TestGitHelper(unittest.TestCase):
    @patch('git.Repo')
    def test_get_dependencies(self, MockRepo):
        # Мокаем поведение репозитория
        mock_repo = MagicMock()
        mock_commit = MagicMock()
        mock_commit.hexsha = '123abc'
        mock_commit.stats.files = {'filename.txt': {'lines': 10}}

        mock_repo.iter_commits.return_value = [mock_commit]
        
        dependencies = get_dependencies('/path/to/repo', 'filename.txt')
        
        self.assertIn('123abc', dependencies)
        self.assertIn('filename.txt', dependencies['123abc'])

if __name__ == '__main__':
    unittest.main()
