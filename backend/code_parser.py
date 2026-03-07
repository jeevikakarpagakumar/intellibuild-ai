import os
import tempfile
import git
import ast
from collections import defaultdict

def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()
    git.Repo.clone_from(repo_url, temp_dir)
    return temp_dir


def parse_python_repo(repo_path):
    file_data = {}
    module_sizes = defaultdict(int)
    directory_map = defaultdict(int)

    total_functions = 0
    total_classes = 0

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, repo_path)

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read())

                        functions = []
                        classes = []

                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                functions.append(node.name)
                                total_functions += 1
                            if isinstance(node, ast.ClassDef):
                                classes.append(node.name)
                                total_classes += 1

                        file_data[rel_path] = {
                            "functions": functions,
                            "classes": classes
                        }

                        module_sizes[rel_path] = len(functions) + len(classes)

                        top_dir = rel_path.split(os.sep)[0]
                        directory_map[top_dir] += 1

                except:
                    continue

    top_modules = sorted(
        module_sizes.items(),
        key=lambda x: x[1],
        reverse=True
    )[:15]

    entry_points = [
        f for f in file_data.keys()
        if f.endswith("app.py") or f.endswith("__init__.py")
    ]

    core_directory = max(directory_map.items(), key=lambda x: x[1])[0] if directory_map else None

    architectural_signals = {
        "has_app_file": any("app.py" in f for f in file_data.keys()),
        "has_context_module": any("ctx.py" in f for f in file_data.keys()),
        "has_json_module": any("json" in f for f in file_data.keys()),
    }

    return {
        "total_functions": total_functions,
        "total_classes": total_classes,
        "top_modules": top_modules,
        "entry_points": entry_points,
        "directory_density": dict(directory_map),
        "core_directory": core_directory,
        "architectural_signals": architectural_signals
    }