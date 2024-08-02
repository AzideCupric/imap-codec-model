from imap_codec_model.code import Resource
from imap_codec_model.core import Base, Uint

class QuotaSet(Base):
    resource: Resource
    limit: Uint
