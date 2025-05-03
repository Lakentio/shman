import argparse
from .config import ensure_directories
from .manager import create_script, edit_script, list_versions, restore_version, commit_script
from .logger import run_script, list_logs, view_log

def main():
    parser = argparse.ArgumentParser(prog="shman", description="Shell Script Manager")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init", help="Initializes the shman environment")

    new = sub.add_parser("new", help="Creates a new script")
    new.add_argument("name")
    new.add_argument("--category", default="uncategorized")
    new.add_argument("--tags", nargs="*", default=[])

    edit = sub.add_parser("edit", help="Edits a script")
    edit.add_argument("name")

    versions = sub.add_parser("versions", help="Lists the versions of a script")
    versions.add_argument("name")

    restore = sub.add_parser("restore", help="Restores a previous version of a script")
    restore.add_argument("name")
    restore.add_argument("version", type=int)

    commit = sub.add_parser("commit", help="Saves a new version of a script")
    commit.add_argument("name")
    commit.add_argument("version")
    commit.add_argument("message", help="Commit message in quotes")

    run = sub.add_parser("run", help="Executes a script and saves the logs")
    run.add_argument("name")

    log = sub.add_parser("log", help="Lists the execution logs of a script")
    log.add_argument("name")

    view_log_cmd = sub.add_parser("view-log", help="Displays the content of an execution log")
    view_log_cmd.add_argument("name")
    view_log_cmd.add_argument("log_number", type=int)

    args = parser.parse_args()

    if args.command == "init":
        ensure_directories()
        print("shman environment initialized in ~/.shman")
    elif args.command == "new":
        create_script(args.name, args.category, args.tags)
    elif args.command == "edit":
        edit_script(args.name)
    elif args.command == "versions":
        list_versions(args.name)
    elif args.command == "restore":
        restore_version(args.name, args.version)
    elif args.command == "commit":
        commit_script(args.name, args.version, args.message)
    elif args.command == "run":
        run_script(args.name)
    elif args.command == "log":
        list_logs(args.name)
    elif args.command == "view-log":
        view_log(args.name, args.log_number)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()