import os
import yaml
from git import Repo
from graphviz import Digraph

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)
        
def check_repo_exists(repo_path):
    if os.path.exists(repo_path):
        try:
            repo = Repo(repo_path)
            return repo
        except Exception as e:
            print(f"Error: {e}")
            return None
    else:
        print(f"Repository not found at: {repo_path}")
        return None
        
def analyze_commits(repo, target_file):
    if target_file == 'all' or not target_file:
        commits = list(repo.iter_commits())
    else:
        commits = list(repo.iter_commits(paths=target_file))

    return commits
    
def build_dependency_graph(commits, target_file):
    graph = Digraph(comment=f"Dependency Graph for {target_file}")

    for commit in commits:
        graph.node(commit.hexsha, commit.hexsha[:7])  # Добавляем узел для каждого коммита
        if target_file != 'all' and target_file in commit.stats.files:
            graph.edge(commit.hexsha, f'{target_file}', label='modified')

    return graph
    
def main():
    # Загружаем конфигурацию
    config = load_config()
    repo_path = config['repo_path']
    target_file = config['target_file']
    graph_tool_path = config['graph_tool_path']

    # Проверяем, что репозиторий существует
    repo = check_repo_exists(repo_path)
    if repo is None:
        return

    # Анализируем коммиты
    commits = analyze_commits(repo, target_file)

    # Строим граф зависимостей
    graph = build_dependency_graph(commits, target_file)

    # Сохраняем граф в файл
    output_file = f"{target_file}_dependency_graph.pdf"
    graph.render(output_file, format='pdf', cleanup=True)
    print(f"Dependency graph saved to {output_file}")
    
if __name__ == "__main__":
    main()
