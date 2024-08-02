from .ccr import CommandContinuationRequest
from .data import Data
from .status import Status

Response = Data | Status | CommandContinuationRequest
