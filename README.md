# Villefort

Generate concatenated SIM card SMS records in the EF<sub>SMS</sub> format.

## Generate

_Message `HELLO` with `INBOUND_NOT_READ` status, sent from `+1 987 654 3210` to `+1 012 345 6789` with reference `255` and date/time 1970-12-31 23:59:59._

```console
$ docker run --rm ghcr.io/montlhery/villefort \
> --message=HELLO \
> --recipient=10123456789 \
> --sender=19876543210 \
> --date=1970-12-31T23:59:59 \
> --reference=255 \
> --status=INBOUND_NOT_READ
0307910121436587F9400B919178563412F00000072113329595000C050003FF0101904526F309
```

## Write

Use [osmocom/pysim](https://github.com/osmocom/pysim) to write SMS records to a physical SIM card.

```console
$ pySim-shell.py --pcsc-device=0
Using PC/SC reader interface
...
Welcome to pySim-shell!
% pySIM-shell (MF)> verify_chv 1234 # SIM primary PIN
CHV verification successful
% pySIM-shell (MF)> select DF.TELECOM
...
% pySIM-shell (MF/DF.TELECOM)> select EF.SMS
...
% pySIM-shell (MF/DF.TELECOM/EF.SMS)> update_record 001 0307910121436587F9400B919178563412F00000072113329595000C050003FF0101904526F309
```

## References

* [3GPP TS 31.102 V17.4.0 (2021-12) 4.2.25](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=1803)
* [3GPP TS 24.011 V17.0.0 (2020-12) 8.2.5.2](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=1017)
* [3GPP TS 23.040 V17.1.0 (2021-06) 9.2.2.1](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=747) 
* [3GPP TS 23.040 V17.1.0 (2021-06) 9.2.3.24.1](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=747) 
* [UNDERSTANDING SMS: Practitioner's Basics](https://web.archive.org/web/20130717141618/https://mobileforensics.files.wordpress.com/2007/06/understanding_sms.pdf)
