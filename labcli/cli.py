import argparse
import os
import runpy
import sys

HERE = os.path.dirname(__file__)
PROGRAMS_DIR = os.path.normpath(os.path.join(HERE, os.pardir, 'programs'))


def list_programs():
    if not os.path.isdir(PROGRAMS_DIR):
        print("No programs directory found.")
        return
    files = sorted(f for f in os.listdir(PROGRAMS_DIR) if f.endswith('.py'))
    if not files:
        print("No programs found in programs/.")
        return
    print("Available programs:")
    for f in files:
        print('  ' + os.path.splitext(f)[0])


def run_program(name):
    module_path = os.path.join(PROGRAMS_DIR, name + '.py')
    if not os.path.isfile(module_path):
        print(f"Program '{name}' not found in programs/.")
        sys.exit(2)
    # Execute the file in a fresh namespace
    try:
        runpy.run_path(module_path, run_name='__main__')
    except SystemExit as e:
        # Propagate exit codes from executed program
        raise
    except Exception as e:
        print(f"Error while running program '{name}': {e}")
        sys.exit(1)


def show_program(name):
    """Print the source of a program to the terminal with line numbers."""
    module_path = os.path.join(PROGRAMS_DIR, name + '.py')
    if not os.path.isfile(module_path):
        print(f"Program '{name}' not found in programs/.")
        sys.exit(2)
    try:
        with open(module_path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
    except Exception as e:
        print(f"Could not read '{name}': {e}")
        sys.exit(1)

    print(f"--- {name}.py ---")
    width = len(str(len(lines)))
    for i, line in enumerate(lines, start=1):
        print(f"{str(i).rjust(width)}: {line.rstrip()}")


def main(argv=None):
    parser = argparse.ArgumentParser(prog='lab', description='List and run lab programs')
    sub = parser.add_subparsers(dest='command')

    sub.add_parser('list', help='List available programs')

    run_parser = sub.add_parser('run', help='Run a program')
    run_parser.add_argument('program', help='Program name (without .py)')
    show_parser = sub.add_parser('show', help='Show source of a program')
    show_parser.add_argument('program', help='Program name (without .py)')

    args = parser.parse_args(argv)

    if args.command == 'list':
        list_programs()
    elif args.command == 'run':
        run_program(args.program)
    elif args.command == 'show':
        show_program(args.program)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
