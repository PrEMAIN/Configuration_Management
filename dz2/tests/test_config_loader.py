import unittest
from src.config_loader import read_config

class TestConfigLoader(unittest.TestCase):
    def test_read_config(self):
        config_data = """
        graphviz_path: /usr/local/bin/dot
        repository_path: /path/to/repo
        target_file: filename.txt
        """
        with open('config.yaml', 'w') as f:
            f.write(config_data)

        config = read_config('config.yaml')
        self.assertEqual(config['graphviz_path'], '/usr/local/bin/dot')
        self.assertEqual(config['repository_path'], '/path/to/repo')
        self.assertEqual(config['target_file'], 'filename.txt')

if __name__ == '__main__':
    unittest.main()
