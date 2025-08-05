from pathlib import Path
from typing import Final

MAIN_DIR: Final[Path] = Path(__file__).resolve().parents[1]

PLUGINS_DIR: Final[Path] = MAIN_DIR / "plugins"

PLUGIN_CONFIG: Final[list[tuple[str, str]]] = [
    ("discuz_faqsql", "run"),
    ("activemq_putfile", "run"),
    ("hadoop_yarn_unauth", "run"),
    ("activemq_movefile", "run"),
    ("activemq_putfile", "run"),
    ("activemq_weakpwd", "run"),
    ("discuz_faqsql", "run"),
    ("docker_unauth_api", "run"),
    ("elasticSearch_dir_traversal", "run"),
    ("elasticSearch_dir_traversal2", "run"),
    ("elasticSearch_remote_code_exec", "run"),
    ("elasticSearch_remote_code_exec2", "run"),
    ("hadoop_yarn_unauth", "run"),
    ("redis_unauth", "run"),
    ("struts2_053", "run"),
    ("weblogic_ssrf", "run"),
    ("weblogic_weakpasswd", "run"),
    ("weblogic_xmldecoder", "run"),
]

keywords: Final[list[str]] = [
    "uc_key: n't found...n't found..",
]
