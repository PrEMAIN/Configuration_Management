import git

def get_dependencies(repo_path, target_file):
    """Получаем зависимости для коммитов, где встречается target_file."""
    repo = git.Repo(repo_path)
    dependencies = {}

    for commit in repo.iter_commits():
        if target_file in commit.stats.files:
            # Добавляем коммит и затронутые файлы
            dependencies[commit.hexsha] = commit.stats.files.keys()

    return dependencies
