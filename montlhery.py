import time
import click
from smspdu.pdu import SMS_GENERIC, SMS_DELIVER


STATUSES = {
    "INBOUND_READ": 0b001,
    "INBOUND_NOT_READ": 0b011,
    "OUTBOUND_SENT": 0b101,
    "OUTBOUND_NOT_SENT": 0b111,
}


@click.command()
@click.option('--message', type=str, required=True)
@click.option('--recipient', type=str, required=True)
@click.option('--sender', type=str, required=True)
@click.option('--date', type=click.DateTime(), default=None)
@click.option('--reference', type=int, default=0)
@click.option('--limit', type=int, default=153)
@click.option('--status', type=click.Choice(STATUSES.keys()))
def montlhery(sender, recipient, message, date, reference, limit, status):
    """
    Create SMS records in the EF.SMS SIM card format.
    """
    length, type, data = SMS_GENERIC.determineAddress(recipient)
    recipient = (chr(length - 4) + chr(type) + data).encode("hex")

    chunks = range(0, len(message), limit)
    for chunk, offset in enumerate(chunks, start=1):
        header = (0, (reference, len(chunks), chunk))
        data = message[offset:offset+limit]

        deliver = SMS_DELIVER.create(
            sender=sender,
            recipient=None,
            user_data=data,
            datestamp=time.mktime(date.timetuple()),
            user_data_headers=[header]
        ).toPDU()

        print("%02X" % STATUSES[status] + recipient.upper() + deliver)


if __name__ == '__main__':
    montlhery()

