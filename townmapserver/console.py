"""Handles the console interface for the Town Map Server application"""
import sys
import argparse
import townmapserver.database as database
import townmapserver.server as server


def build_run_parser(subparsers):
    run_parser = subparsers.add_parser(
        'run', help='Run the server.'
    )
    run_parser.add_argument(
        '-a', '--address', type=str, default='localhost',
        help='Host address for running the server'
    )
    run_parser.add_argument(
        '-p', '--port', type=int, default=5000,
        help='Port for running the server'
    )
    run_parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Runs server in debug mode.'
    )
    return run_parser


def build_database_parser(subparsers):
    db_parser = subparsers.add_parser(
        'database', help='Manage the database.'
    )
    db_subparser = db_parser.add_subparsers(dest='subcommand')
    db_subparser.required = True

    # Create database subcommand
    db_create_parser = db_subparser.add_parser(
        'create', help='Create the database schema from the defined models.'
    )
    db_create_parser.add_argument(
        'username', type=str,
        help='Name of Postgres login role with create permissions.'
    )
    db_create_parser.add_argument(
        'password', type=str,
        help='Password of Postgres login role with create permissions.'
    )
    db_connection_uri_parser = db_subparser.add_parser(
        'uri', help='Display the connection URI'
    )

    return db_parser


def parse_arguments(args):
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Manages the backend server API for the Town Map app'
    )
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    # Build command parsers
    build_run_parser(subparsers)
    build_database_parser(subparsers)

    return parser.parse_args(args)


def handle_command_database(args):
    if args.subcommand == 'create':
        database.create_schema(server.flaskApp, args.username, args.password)
    if args.subcommand == 'uri':
        print(database.build_connection_uri())


def handle_command_run(args):
    server.launch_server(args.address, args.port, args.debug)


def handle_command(args):
    globals()['handle_command_{}'.format(args.command)](args)
    # launch_server(args.address, args.port)


def main():
    args = parse_arguments(sys.argv[1:])
    handle_command(args)
