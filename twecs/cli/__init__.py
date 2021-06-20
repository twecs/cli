import importlib
import logging

import twecs.cli.argparsing
import twecs.cli.config
import twecs.cli.logs
import twecs.wise

default_logging_level = 'INFO'
logger = logging.getLogger(
    __name__,
)


def entry_point(
    ):
    argparser = twecs.cli.argparsing.set_up_argparser(
        default_logging_level=default_logging_level,
    )

    args = argparser.parse_args(
    )

    twecs.cli.logs.set_up(
        level=args.logging_level,
    )

    logger.debug(
        'logging level: %s',
        args.logging_level,
    )

    profiles = twecs.cli.config.load_profiles(
    )
    profile = profiles[args.profile]

    wise_configuration = profile['wise']

    if args.source_amount:
        amount = args.source_amount
        amount_side = 'source'
    else:
        assert args.target_amount
        amount = args.target_amount
        amount_side = 'target'

    transfer = twecs.wise.set_up_transfer(
        **wise_configuration,
        amount=amount,
        amount_side=amount_side,
        reference=args.reference,
        source_currency=args.source_currency,
        target_currency=args.target_currency,
    )

    for notifier_name in args.notifiers:
        logger.debug(
            'will try to execute notifier %s',
            notifier_name,
        )

        notifier_module = importlib.import_module(
            name=f'twecs.notifiers.{notifier_name}',
        )

        notifier_module.execute(
            parameters=profile['notifiers'][notifier_name],
            transfer=transfer,
        )
