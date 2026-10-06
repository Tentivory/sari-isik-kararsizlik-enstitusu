# Sari Isik Kararsizlik Enstitusu

Resmi adi: **Ulusal Sari Faz Kararsizlik ve Ani Gaz Enstitusu** (USKAE).

Bu kurum, trafik lambasi sariya dondugu anda vatandasin frene mi basacagini yoksa "yetisirim" diyerek gaza mi yuklenecegini bilimsel, hukuki ve biraz da mahcup bir sekilde cozer.

Ciddiyet derecesi: yuksek.
Komiklik derecesi: resmi olarak sifir. Fiilen tartisilir.

## Problem

Sari isik 3 saniye surer. Insan beyni bu 3 saniyede su kurumlarla eszamanli toplanti yapar:

- Icisleri Bakanligi (korku)
- Maliye (ceza ihtimali)
- Ulastirma (yetisir mi)
- Aile (arkadaki araba korna calarsa ne olacak)
- Vicdan (bugun erken donmek istiyor mu)

Enstitu bu toplantiyi tek dosyada bitirir.

## Kurulum

```bash
python3 sari_isik.py
```

Bagimlilik yoktur. Devlet kadar yalniz, cay kadar hazirdir.

## Kullanim

```bash
python3 sari_isik.py --hiz 54 --mesafe 28 --vicdan 0.4 --arkadaki-korna 2
```

Parametreler:

| Parametre | Anlam |
| --- | --- |
| `--hiz` | km/saat. 0 ile 180 arasi. 180 ustu zaten sariyi gormez. |
| `--mesafe` | lambaya kalan metre |
| `--vicdan` | 0 ile 1. 0 = "yetisirim abi", 1 = "durayim, belki izlerler" |
| `--arkadaki-korna` | son 10 saniyedeki korna sayisi |

Cikti bir **karar tutanagi**dir. Itiraz mercii yoktur. Itiraz ederseniz sari tekrar yanar.

## Metodoloji

Karar skoru su kutsal formul ile hesaplanir:

```
S = (hiz / 12) + (40 - mesafe) / 10 + korna * 0.7 - vicdan * 5
```

- S > 4 ise GAZ. Gerekce: fizik.
- S < 1 ise FREN. Gerekce: toren.
- Arasi KARARSIZ. Gerekce: insan.

Formul peer-review'dan gecmemistir. Peer'lar sari da yakalanmistir.

## Yasal uyari

Bu yazilim gercek trafikte kullanilamaz. Kullanirsaniz enstitu sizi tanimaz. Tanimasa da plakanizi ezberler, sonra unutur, sonra yine ezberler.

## Katki

Pull request'ler once sari faz komisyonuna gelir. Komisyon 3 saniye icinde karar veremezse dosya bir sonraki yesile kalir.

---

DAMGA: Grok Kayyum Muhru, seri no SK-2026-SARI
TARIH: 6 Ekim 2026, saat 17:06, +03
ISIM: Kayyum Grok, Tentivory adina
CIDDIYET: resmi evrak kagidi kadar ciddi, sari isik kadar degil
