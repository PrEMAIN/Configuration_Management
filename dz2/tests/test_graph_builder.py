import unittest
from graphviz import Digraph
from src.graph_builder import build_graph

class TestGraphBuilder(unittest.TestCase):
    def test_build_graph(self):
        dependencies = {
            '123abc': ['file1.txt', 'file2.txt'],
            '456def': ['file3.txt']
        }
        
        dot = build_graph(dependencies)
        
        self.assertIn('commit_123abc', dot.source)
        self.assertIn('file1.txt', dot.source)
        self.assertIn('file2.txt', dot.source)
        self.assertIn('commit_456def', dot.source)
        self.assertIn('file3.txt', dot.source)

if __name__ == '__main__':
    unittest.main()
