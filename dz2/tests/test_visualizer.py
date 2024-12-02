import unittest
from unittest.mock import patch
from src.visualizer import visualize_graph

class TestVisualizer(unittest.TestCase):
    @patch('src.visualizer.build_graph')
    @patch('src.visualizer.get_dependencies')
    @patch('src.visualizer.read_config')
    def test_visualize_graph(self, mock_read_config, mock_get_dependencies, mock_build_graph):
        # Мокаем функции
        mock_read_config.return_value = {
            'graphviz_path': '/usr/local/bin/dot',
            'repository_path': '/path/to/repo',
            'target_file': 'filename.txt'
        }
        mock_get_dependencies.return_value = {'123abc': ['file1.txt']}
        mock_build_graph.return_value = "graph"

        visualize_graph('config.yaml')

        mock_read_config.assert_called_once_with('config.yaml')
        mock_get_dependencies.assert_called_once_with('/path/to/repo', 'filename.txt')
        mock_build_graph.assert_called_once_with({'123abc': ['file1.txt']})

if __name__ == '__main__':
    unittest.main()
