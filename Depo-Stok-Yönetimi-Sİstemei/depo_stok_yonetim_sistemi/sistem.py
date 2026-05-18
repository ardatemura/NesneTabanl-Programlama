from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List
from models import Siparis, Urun

@dataclass
class DepoStokSistemi:
    _urunler: Dict[int, Urun] = field(default_factory=dict)
    _siparisler: List[Siparis] = field(default_factory=list)
    _son_siparis_id: int = 0

    def urun_ekle(self, urun: Urun) -> None:
        if urun.urun_id in self._urunler: raise ValueError(f"Bu urun_id zaten var: {urun.urun_id}")
        if urun.stok < 0: raise ValueError("Stok negatif olamaz.")
        self._urunler[urun.urun_id] = urun

    def _sonraki_siparis_id(self) -> int:
        self._son_siparis_id += 1
        return self._son_siparis_id

    def siparis_olustur(self, urun: Urun, adet: int) -> Siparis:
        urun.stok_azalt(adet)
        siparis = Siparis.siparis_olustur(self._sonraki_siparis_id(), urun, adet)
        self._siparisler.append(siparis)
        return siparis

    def gunluk_siparis_listesi(self) -> List[Siparis]:
        return list(self._siparisler)
