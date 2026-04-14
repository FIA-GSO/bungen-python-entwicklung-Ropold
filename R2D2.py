
def zyklus(junge, erwachsene, alt):
    neue_junge = (erwachsene * 4) + (alt * 2)
    neue_erwachsene = junge // 2
    neue_alt = erwachsene // 3
    print(f"Vorher  -> Junge: {junge}, Erwachsene: {erwachsene}, Alte: {alt}")
    print(f"Nachher -> Junge: {neue_junge}, Erwachsene: {neue_erwachsene}, Alte: {neue_alt}")
    return neue_junge, neue_erwachsene, neue_alt

#zyklus(60, 5, 3)
zyklus(26, 30, 1)