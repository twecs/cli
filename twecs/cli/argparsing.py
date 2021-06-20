import argparse
import logging

logger = logging.getLogger(
    __name__,
)


def set_up_argparser(
            default_logging_level,
        ):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-l',
        '--logging-level',
        choices=[
            'DEBUG',
            'INFO',
            'WARNING',
            'ERROR',
            'CRITICAL',
        ],
        default=default_logging_level,
        dest='logging_level',
        help='logging level',
        metavar='LEVEL',
    )

    parser.add_argument(
        '-N',
        '--notifiers',
        action='extend',
        default=[
        ],
        dest='notifiers',
        help='notification plug-ins to execute',
        metavar='NOTIFIER',
        nargs='+',
    )

    parser.add_argument(
        '-p',
        '--profile',
        dest='profile',
        help='configuration group to apply',
        metavar='PROFILE',
        required=True,
    )

    parser.add_argument(
        '-r',
        '--reference',
        dest='reference',
        help='transfer reference line',
        metavar='REFERENCE',
        required=True,
    )

    parser.add_argument(
        '--source-currency',
        dest='source_currency',
        help='currency to exchange from',
        metavar='CURRENCY',
        required=True,
    )

    parser.add_argument(
        '--target-currency',
        dest='target_currency',
        help='currency to exchange into',
        metavar='CURRENCY',
        required=True,
    )

    amount_group = parser.add_mutually_exclusive_group(
        required=True,
    )

    amount_group.add_argument(
        '--source-amount',
        dest='source_amount',
        help='available amount to exchange',
        metavar='AMOUNT',
    )

    amount_group.add_argument(
        '--target-amount',
        dest='target_amount',
        help='desired amount in foreign currency',
        metavar='AMOUNT',
    )

    return parser
