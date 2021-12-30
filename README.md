# Montlhéry

Tool to generate concatenated SIM card SMS records in the EF<sub>SMS</sub> format. Named after the telegraph of Montlhéry from [Le Comte de Monte-Cristo](https://fr.wikisource.org/wiki/Le_Comte_de_Monte-Cristo/Chapitre_61).

## Example

Message `HELLO` with `INBOUND_NOT_READ` status, sent from `+1 987 654 3210` to `+1 012 345 6789` with reference `255` and date/time 1970-12-31 23:59:59.

```console
$ montlhery \
> --message=HELLO \
> --recipient=10123456789 \
> --sender=19876543210 \
> --date=1970-12-31T23:59:59 \
> --reference=255 \
> --status=INBOUND_NOT_READ
0307910121436587F9400B919178563412F00000072113329595000C050003FF0101904526F309
```

## Installation

This project only supports Python 2 [(obsolete)](https://www.python.org/doc/sunset-python-2) because of the [`smspdu`](https://pypi.org/project/smspdu) package. Use the provided container images to avoid [XKCD 1987](https://xkcd.com/1987).

```console
$ docker run --rm ghcr.io/0x2b3bfa0/montlhery --help
```

## References

* [3GPP TS 31.102 V17.4.0 (2021-12) 4.2.25](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=1803)
* [3GPP TS 24.011 V17.0.0 (2020-12) 8.2.5.2](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=1017)
* [3GPP TS 23.040 V17.1.0 (2021-06) 9.2.2.1](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=747) 
* [3GPP TS 23.040 V17.1.0 (2021-06) 9.2.3.24.1](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=747) 
* [UNDERSTANDING SMS: Practitioner's Basics](https://mobileforensics.files.wordpress.com/2007/06/understanding_sms.pdf)
