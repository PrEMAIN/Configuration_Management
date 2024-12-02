from graphviz import Digraph

def build_graph(dependencies):
    """Строим граф зависимостей для коммитов и файлов."""
    dot = Digraph(comment='Dependencies')

    for commit_hash, files in dependencies.items():
        commit_node = f'commit_{commit_hash}'
        dot.node(commit_node, commit_hash)
        for file in files:
            file_node = f'file_{file}'
            dot.node(file_node, file)
            dot.edge(commit_node, file_node)

    return dot
