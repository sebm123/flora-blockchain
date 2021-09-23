from dataclasses import dataclass
from typing import Optional

from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.blockchain_format.program import Program
from chia.util.ints import uint64
from chia.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class LineageProof(Streamable):
    parent_name: bytes32
    inner_puzzle_hash: Optional[bytes32]
    amount: uint64

    def to_program(self):
        final_list = [self.parent_name]
        if self.inner_puzzle_hash:
            final_list.append(self.inner_puzzle_hash)
        final_list.append(self.amount)
        return Program.to(final_list)
