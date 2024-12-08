from git import Repo
import pygraphviz as pgv

def build_dependency_graph(repo_path, target_file):
    repo = Repo(repo_path)
    graph = pgv.AGraph(strict=True, directed=True)

    for commit in repo.iter_commits('main'):  # или используйте нужную ветку
        commit_hash = commit.hexsha[:7]  # Используем первые 7 символов хэша
        commit_message = commit.message.strip()
        commit_author = commit.author.name
        commit_date = commit.committed_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Формируем метку для коммита, которая будет отображаться в графе
        label = f"Hash: {commit_hash}\nMessage: {commit_message}\nAuthor: {commit_author}\nDate: {commit_date}"

        # Добавляем узел с меткой
        graph.add_node(commit_hash, label=label)

        # Добавляем зависимости между родительским и текущим коммитом
        if commit.parents:
            for parent in commit.parents:
                graph.add_edge(parent.hexsha[:7], commit_hash)

        # Также можно добавить информацию о том, какие файлы изменены в этом коммите
        for diff in commit.diff(commit.parents or NULL_TREE):
            file_name = diff.a_path  # или diff.b_path, если это изменение файла
            if diff.change_type == 'M':  # Если файл был изменен
                graph.add_edge(commit_hash, file_name, label="modified")

    # Генерируем и сохраняем граф в PDF
    graph.layout(prog='dot')
    graph.draw(target_file, format='pdf')

# Пример вызова функции
build_dependency_graph('/Users/romanagarkov/VUZ/CU', 'dependency_graph.pdf')
