import asyncio

from .config import read_config
from stustapay.core.args import Parser

from .signature_processor import SignatureProcessor
from .simulator import Simulator


def main():
    """
    main entry point for launching the administration server
    """
    parser = Parser()

    parser.add_argument("-c", "--config-path", default="tse.conf")

    ### module registration
    parser.add_subcommand("signature_processor", SignatureProcessor)
    parser.add_subcommand("simulator", Simulator)
    ### / module registration

    loop = asyncio.new_event_loop()

    args = parser.parse_args(loop)

    config = read_config(vars(args)["config_path"])

    args.run_subcommand(loop, config=config)


if __name__ == "__main__":
    main()
