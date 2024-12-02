from src.config_loader import read_config
from src.git_helper import get_dependencies
from src.graph_builder import build_graph

def visualize_graph(config_path):
    """Основная функция для визуализации зависимостей."""
    # Чтение конфигурации
    config = read_config(config_path)
    repo_path = config['repository_path']
    target_file = config['target_file']

    # Получение зависимостей
    dependencies = get_dependencies(repo_path, target_file)

    # Построение графа
    dot = build_graph(dependencies)

    # Вывод графа
    dot.render('/tmp/dependencies_graph', format='png', view=True)
