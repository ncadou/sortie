""" Test connecting to the configured in IMAP4 server. """

from argparse import ArgumentParser

import transaction

from pyramid.paster import bootstrap

from ..api.person import import_csv


def main():
    args = parse_args()
    env = bootstrap(args.config_uri)

    with open(args.filepath, 'r') as f:
        import_csv(f)

    transaction.commit()


def parse_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('config_uri', help='configuration to use')
    parser.add_argument('filepath', help='file to import')
    return parser.parse_args()


if __name__ == '__main__':
    main()
