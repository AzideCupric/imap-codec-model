from collections.abc import Sequence

from msgspec import field
from .core import NString, Base

class Address(Base):
    class AddressVal(Base):
        name: NString
        adl: NString
        mailbox: NString
        host: NString

    codec_data: AddressVal

class EnvelopeStuct(Base):
    class EnvelopeVal(Base):
        date: NString
        subject: NString
        from_: Sequence[Address] = field(name="from")
        sender: Sequence[Address]
        reply_to: Sequence[Address]
        to: Sequence[Address]
        cc: Sequence[Address]
        bcc: Sequence[Address]
        in_reply_to: NString
        message_id: NString

    codec_data: EnvelopeVal
